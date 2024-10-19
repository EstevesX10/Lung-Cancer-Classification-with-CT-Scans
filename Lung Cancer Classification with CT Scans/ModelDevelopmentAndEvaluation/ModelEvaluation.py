from typing import (Tuple)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import (confusion_matrix, precision_recall_curve, average_precision_score, roc_curve, roc_auc_score, log_loss, balanced_accuracy_score, f1_score, hamming_loss)
from .checkModelIntegrity import (isValidAlgorithm)
from .jsonFileManagement import (dictToJsonFile, jsonFileToDict)
from .pickleBestEstimatorsManagement import (loadBestEstimator)

def evaluateModel(algorithm:object=None, bestParams:dict=None, scoring:str=None, folds:list[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]]=None, modelPaths:dict=None, targetLabels:list[str]=None, title:str=None) -> dict:
    """
    # Description
        -> Evaluate a machine learning model using a list of cross-validation 
        folds and plot the evaluation metrics.
    ---------------------------------------------------------------------------
    := param: algorithm - A machine learning model class (e.g., XGBoost or any classifier implementing fit/predict).
    := param: bestParams - Best parameters to use when instanciating the model.
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
    
    # Check if the algorithm is valid
    if not isValidAlgorithm(algorithm, bestParams):
        raise ValueError("Got an Invalid Algorithm!")

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
        balanced_accuracies = []
        f1_scores = []
        hamming_losses = []
        
        # # Check for algorithms that do not support predict_proba natively
        # if algorithm.__name__ in ['SVC']:
        #     # Create a new instance of the machine learning model, enabling the calculation of y_pred_proba
        #     model = algorithm(**bestParams, probability=True)
        # else:
        #     # Create a new instance of the machine learning model
        #     model = algorithm(**bestParams)

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
            balanced_accuracies.append(balanced_accuracy_score(y_test_fold, y_pred_fold))
            f1_scores.append(f1_score(y_test_fold, y_pred_fold))
            log_losses.append(log_loss(y_test_fold, y_pred_proba_fold))
            hamming_losses.append(hamming_loss(y_test_fold, y_pred_fold))

        # Calculate average confusion matrix across all folds
        conf_matrix = np.average(conf_matrices, axis=0)

        # Concatenate results for ROC curve and Precision-Recall Curve
        y_test_combined = np.concatenate(y_test_list)
        y_pred_proba_combined = np.concatenate(y_pred_proba_list)

        # Calculate Precision-Recall curve
        precision, recall, _ = precision_recall_curve(y_test_combined, y_pred_proba_combined)
        avg_precision = average_precision_score(y_test_combined, y_pred_proba_combined)

        # Calculate ROC curve and AUC
        fpr, tpr, _ = roc_curve(y_test_combined, y_pred_proba_combined)
        auc_score = roc_auc_score(y_test_combined, y_pred_proba_combined)

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
            # Average confusion matrix across all folds
            'conf_matrix':conf_matrix.tolist(),

            # From the Precision-Recall curve
            'precision':precision.tolist(),
            'recall':recall.tolist(),
            'avg_precision':avg_precision,

            # From the ROC Curve
            'fpr':fpr.tolist(),
            'tpr':tpr.tolist(),
            'auc_score':auc_score,

            # Average Balanced Accuracy
            'avg_balanced_accuracy':avg_balanced_accuracy,

            # Average F1 Score
            'avg_f1_score':avg_f1_score,

            # Average log loss
            'avg_log_loss':avg_log_loss,
            
            # Average Hamming loss
            'avg_hamming_loss':avg_hamming_loss,
        })

        # Save the calculated metrics into a json file
        dictToJsonFile(calculatedMetrics, modelPaths[algorithm.__name__][scoring]['modelEvaluationMetrics'])

    else:
        # Get the average confusion matrix across all folds
        conf_matrix = np.array(calculatedMetrics['conf_matrix'])

        # Get the Precision-Recall curve
        precision = np.array(calculatedMetrics['precision'])
        recall = np.array(calculatedMetrics['recall'])
        avg_precision = float(calculatedMetrics['avg_precision'])

        # Calculate ROC curve and AUC
        fpr = np.array(calculatedMetrics['fpr'])
        tpr = np.array(calculatedMetrics['tpr'])
        auc_score = float(calculatedMetrics['auc_score'])

    # Create a larger figure to accommodate the plots
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

    # Plot the Precision-Recall curve
    axs[0].plot(recall, precision, label=f'Precision-Recall curve (AP = {avg_precision:.2f})', color='darkblue')
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
    sns.heatmap(df_conf_matrix, annot=True, cmap='Blues', fmt='g', ax=axs[2])
    axs[2].set_title('Confusion Matrix')
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