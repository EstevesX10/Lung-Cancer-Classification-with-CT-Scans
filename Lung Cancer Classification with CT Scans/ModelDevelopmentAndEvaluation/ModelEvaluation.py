from typing import (Tuple)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, f1_score, log_loss, hamming_loss, confusion_matrix, precision_recall_curve, average_precision_score, roc_curve, roc_auc_score)
from .jsonFileManagement import (dictToJsonFile, jsonFileToDict)
from .pickleBestEstimatorsManagement import (loadBestEstimator)

def evaluateModel(algorithm:object=None, scoring:str=None, folds:list[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]]=None, modelPaths:dict=None, targetLabels:list[str]=None, title:str=None) -> dict:
    """
    # Description
        -> Evaluate a machine learning model using a list of cross-validation 
        folds and plot the evaluation metrics.
    ---------------------------------------------------------------------------
    := param: algorithm - A machine learning model class (e.g., XGBoost or any classifier implementing fit/predict).
    := param: scoring - Evaluation metric to take into consideration when performing Grid Search.
    := param: folds - A list of tuples where each tuple contains (X_train, X_test, y_train, y_test) for each fold.
    := param: modelPaths - Dictionary with the paths to save the metrics associated with the model.
    := param: targetLabels - Target labels associated with the classification problem.
    := param: title -The title of the plot. Default is "Model Performance Evaluation".
    := return: A dictionary with some metrics.
    """
    
    # Check if a model was provided
    if algorithm is None:
        raise ValueError("Missing a model to evaluate!")

    # Check if the given scoring is valid
    if scoring not in ['accuracy', 'balanced_accuracy', 'recall'] and scoring is not None:
        raise ValueError("Got Invalid Scoring!")

    # Check if a folds list was provided
    if folds is None:
        raise ValueError("Missing the data folds in which to evaluate the model in!")

    # Check if the folds list is empty
    if len(folds) == 0:
        raise ValueError("The folds list does not contain any fold!")

    # Check if the modelPaths dictionary was provided
    if modelPaths is None:
        raise ValueError("Missing dictionary with the model paths")

    # Check if the target labels were given
    if targetLabels is None:
        raise ValueError("Missing target labels for the confusion matrix!")

    # Check if the target labels list is empty
    if len(targetLabels) == 0:
        raise ValueError("The target labels list is Empty!")

    # Get the possible metrics dictionary
    if not os.path.exists(modelPaths[algorithm.__name__][scoring]['modelEvaluationMetrics']):
        calculatedMetrics = {}
    else:
        calculatedMetrics = jsonFileToDict(modelPaths[algorithm.__name__][scoring]['modelEvaluationMetrics'])

    # Check if the metrics have already been computed and can be imported
    if calculatedMetrics == {}:
        # Initialize auxiliar variables where we are going to store intermidiate results from each fold
        conf_matrices = []
        y_pred_proba_list = []
        y_test_list = []
        log_losses = []
        accuracies = []
        balanced_accuracies = []
        f1_scores = []
        hamming_losses = []

        # Defining auxiliar lists to store the amount of malignant / benign cases per fold
        malignantCases = []
        benignCases = []

        # Check if we are to create a voting classifier with the SVM, Random Forest and XGBoost with the same scoring method
        if algorithm.__name__ == "VotingClassifier":
            model = algorithm(estimators=[(
                'SVC',
                loadBestEstimator(modelPaths['SVC'][scoring]['bestEstimatorPath'])
            ),(
                'RandomForestClassifier',
                loadBestEstimator(modelPaths['RandomForestClassifier'][scoring]['bestEstimatorPath'])
            ),(
                'XGBClassifier',
                loadBestEstimator(modelPaths['XGBClassifier'][scoring]['bestEstimatorPath'])
            )], voting='soft')
        else:
            # Load the best estimator obtained from Grid Search
            model = loadBestEstimator(modelPaths[algorithm.__name__][scoring]['bestEstimatorPath'])

        # Iterate through each fold
        for (X_train_fold, X_test_fold, y_train_fold, y_test_fold) in folds:
            # Train the model on the training fold
            model.fit(X_train_fold, y_train_fold)
            
            # Make predictions on the test fold
            y_pred_fold = model.predict(X_test_fold)
            y_pred_proba_fold = model.predict_proba(X_test_fold)[:, 1]

            # Calculate and append results
            conf_matrices.append(confusion_matrix(y_test_fold, y_pred_fold))
            y_pred_proba_list.append(y_pred_proba_fold)
            y_test_list.append(y_test_fold)
            accuracies.append(accuracy_score(y_test_fold, y_pred_fold))
            balanced_accuracies.append(balanced_accuracy_score(y_test_fold, y_pred_fold))
            f1_scores.append(f1_score(y_test_fold, y_pred_fold))
            log_losses.append(log_loss(y_test_fold, y_pred_proba_fold))
            hamming_losses.append(hamming_loss(y_test_fold, y_pred_fold))

            # Add the amount of bening and malignant cases
            benignCases.append(np.sum(y_test_fold == 0))
            malignantCases.append(np.sum(y_test_fold == 1))

        # Calculate average confusion matrix across all folds
        conf_matrix = np.average(conf_matrices, axis=0)

        # Concatenate results for ROC curve and Precision-Recall Curve
        y_test_combined = np.concatenate(y_test_list)
        y_pred_proba_combined = np.concatenate(y_pred_proba_list)

        # Scale the confusion matrix to percentages (%)
        totalBenignCases = np.sum(benignCases)/len(folds)
        totalMalignantCases = np.sum(malignantCases)/len(folds)
        
        # Since it is a binary classification problem we can do this
        conf_matrix[0,:] = np.round(conf_matrix[0,:]/totalBenignCases*100, 3)
        conf_matrix[1,:] = np.round(conf_matrix[1,:]/totalMalignantCases*100, 3)

        # Calculate Precision-Recall curve
        precisionScores, recallScores, _ = precision_recall_curve(y_test_combined, y_pred_proba_combined)
        avg_precision = average_precision_score(y_test_combined, y_pred_proba_combined)

        # Calculate ROC curve and AUC
        fpr, tpr, _ = roc_curve(y_test_combined, y_pred_proba_combined)
        auc_score = roc_auc_score(y_test_combined, y_pred_proba_combined)

        # Calculate the average accuracy
        avg_accuracy = np.mean(accuracies)
        
        # Calculate the average balanced accuracy
        avg_balanced_accuracy = np.mean(balanced_accuracies)
        
        # Calculate the average f1 scores
        avg_f1_score = np.mean(f1_scores)

        # Calculate average log loss
        avg_log_loss = np.mean(log_losses)

        # Calculate the average hamming loss
        avg_hamming_loss = np.mean(hamming_losses)

        # Update the calculated metrics dictionary
        calculatedMetrics.update({
            # (Average) Accuracy
            'avg_accuracy':avg_accuracy,
            'accuracy_scores':accuracies,

            # (Average) Balanced Accuracy
            'avg_balanced_accuracy':avg_balanced_accuracy,
            'balanced_accuracy_scores':balanced_accuracies,

            # (Average) F1 Score
            'avg_f1_score':avg_f1_score,
            'f1_scores':f1_scores,

            # (Average) log loss
            'avg_log_loss':avg_log_loss,
            'log_loss_scores':log_losses,
            
            # (Average) Hamming loss
            'avg_hamming_loss':avg_hamming_loss,
            'hamming_loss_scores':hamming_losses,

            # Average confusion matrix across all folds
            'conf_matrix':conf_matrix.tolist(),

            # From the Precision-Recall curve
            'precision_scores':precisionScores.tolist(),
            'recall_scores':recallScores.tolist(),
            'avg_precision':avg_precision,

            # From the ROC Curve
            'fpr':fpr.tolist(),
            'tpr':tpr.tolist(),
            'auc_score':auc_score
        })

        # Save the calculated metrics into a json file
        dictToJsonFile(calculatedMetrics, modelPaths[algorithm.__name__][scoring]['modelEvaluationMetrics'])

    else:
        # Get the average confusion matrix across all folds
        conf_matrix = np.array(calculatedMetrics['conf_matrix'])

        # Get the Precision-Recall curve
        precisionScores = np.array(calculatedMetrics['precision_scores'])
        recallScores = np.array(calculatedMetrics['recall_scores'])
        avg_precision = float(calculatedMetrics['avg_precision'])

        # Calculate ROC curve and AUC
        fpr = np.array(calculatedMetrics['fpr'])
        tpr = np.array(calculatedMetrics['tpr'])
        auc_score = float(calculatedMetrics['auc_score'])

    # Create a larger figure to accommodate the plots
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

    # Plot the Precision-Recall curve
    axs[0].plot(recallScores, precisionScores, label=f'Precision-Recall curve (AP = {avg_precision:.2f})', color='darkblue')
    axs[0].set_xlabel('Recall')
    axs[0].set_ylabel('Precision')
    axs[0].set_title('Precision-Recall Curve')
    axs[0].legend(loc='lower left')

    # Plot ROC Curve
    axs[1].plot(fpr, tpr, label=f"ROC curve (AUC = {auc_score:.2f})", color="darkblue", linestyle='-', linewidth=1.4)
    axs[1].plot([0, 1], [0, 1], color="darkred", linestyle='--', label="Chance level (AUC = 0.5)")
    axs[1].set_title('ROC Curve')
    axs[1].set_xlabel('False Positive Rate')
    axs[1].set_ylabel('True Positive Rate')
    axs[1].legend()

    # Plot Confusion Matrix
    df_conf_matrix = pd.DataFrame(conf_matrix, index=targetLabels, columns=targetLabels)
    sns.heatmap(df_conf_matrix, annot=True, cmap='Blues', fmt='.2f', ax=axs[2])
    axs[2].set_title('Confusion Matrix (%)')
    axs[2].set_xlabel('Predicted Labels')
    axs[2].set_ylabel('True Labels')

    # Set the super title for all subplots
    title = f"{algorithm.__name__} Model Evaluation" if title is None else title
    fig.suptitle(title)

    # Tighten up the layout
    plt.tight_layout()

    # Save the plot as a PNG file if it has not been already saved
    if not os.path.exists(modelPaths[algorithm.__name__][scoring]['modelEvaluationPlot']):
        plt.savefig(modelPaths[algorithm.__name__][scoring]['modelEvaluationPlot'], format="png", dpi=600)

    # Display the plot
    plt.show()

    # Return the model metrics
    return calculatedMetrics

def convertMetricsToDataFrame(metricsList:list[list[str, dict]]=None, filePath:str=None) -> pd.DataFrame:
    """
    # Description
        -> Converts a list of [algorithm, collectedMetrics] into a dataframe to 
        better visualize the whole performance of the models.
    ----------------------------------------------------------------------------
    := param: metricsList - List with all the previously collected data.
    := param: filePath - Path to where the metrics dataframe should be saved.
    := return: pandas Dataframe with all the collected data properly organized.
    """

    def toCamelCase(text:str) -> str:
        """
        # Description
            -> This function converts a given text to camelCase
        -------------------------------------------------------
        := param: text - String to convert .
        := return: Formated string in camel case
        """
        s = text.replace("-", " ").replace("_", " ")
        s = s.split()
        if len(text) == 0:
            return text
        return s[0] + ''.join(i.capitalize() for i in s[1:])

    # Check if a metrics List was provided
    if metricsList is None:
        raise ValueError("Missing a Proper List with all the metrics!")
    
    # Check if the metrics list is empty
    if len(metricsList) == 0:
        raise ValueError("Empty Metrics List!")

    # Check if a file path for the final dataframe was provided
    if filePath is None:
        raise ValueError("Missing path to save the final metrics dataframe!")

    # Get the firt dictionary to occur [To get all the keys since all dicts are going to have the same]
    firstDictionary = metricsList[0][1]

    # Hardcode the columns to later remove
    columnsToRemove = ['accuracy_scores', 'balanced_accuracy_scores', 'f1_scores', 'log_loss_scores', 'hamming_loss_scores', 'fpr', 'tpr', 'precision_scores', 'recall_scores', 'conf_matrix']
    
    # Fetch all the columns to use in the dataframe
    df_columns = ['Algorithm'] + [columnName \
                  for columnName in sorted(list(firstDictionary.keys()))]

    # Initialize a dataframe to store the results in
    df_metrics = pd.DataFrame(columns=df_columns)

    # Iterate over the collected metrics
    for algorithm, metricsDict in metricsList:
        # Create a new line for the dataframe
        newLine = pd.DataFrame(columns=df_columns)
        newLine = pd.DataFrame.from_dict([metricsDict])
        newLine['Algorithm'] = algorithm

        # Concatenate the new line to the previously created dataframe
        df_metrics = pd.concat([df_metrics, newLine], ignore_index=True)

    # Drop unnecessary columns
    df_metrics = df_metrics.drop(columns=columnsToRemove)

    # Format the columns names to camel case
    df_metrics.columns = list(toCamelCase(col.replace('avg_', '')) for col in df_metrics.columns)
    
    # Save the final dataframe if it does not exist
    if not os.path.exists(filePath):
        df_metrics.to_csv(filePath, sep=',', index=False)

    # Return dataframe
    return df_metrics