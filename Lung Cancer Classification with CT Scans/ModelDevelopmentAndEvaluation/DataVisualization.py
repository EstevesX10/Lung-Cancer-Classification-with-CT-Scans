from typing import (Tuple)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.base import (BaseEstimator, ClassifierMixin)
from sklearn.metrics import (confusion_matrix, precision_recall_curve, average_precision_score, roc_curve, roc_auc_score, log_loss)
from .jsonFileManipulation import (dictToJsonFile, jsonFileToDict)

def isModelTrained(model:BaseEstimator=None) -> bool:
    """
    # Description
        -> Checks if a scikit-learn model has been trained.
    -------------------------------------------------------
    := param: model - The scikit-learn model instance.
    := return: bool - True if the model has been trained, False otherwise.
    """

    # Defining a constraint for the model existence
    if model is None:
        raise ValueError("Missing a scikit-learn Model!")

    # Making sure that the model is a instance of both BaseEstimator and ClassifierMixin
    if not isinstance(model, (BaseEstimator, ClassifierMixin)):
        raise ValueError("The model must be an instance of both BaseEstimator and ClassifierMixin.")

    # Most scikit-learn models will have these attributes after training
    trainedAttributes = ['coef_', 'intercept_', 'n_features_in_', 'classes_']
    
    # Check if any of the common trained attributes exist in the model
    for attr in trainedAttributes:
        if hasattr(model, attr):
            return True
    return False

def evaluateModel(model:object=None, folds:list[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]]=None, modelPaths:dict=None, targetLabels:list[str]=None, title:str=None) -> dict:
    """
    # Description
        -> Evaluate a machine learning model using a list of cross-validation 
        folds and plot the evaluation metrics.
    ---------------------------------------------------------------------------
    := param: model - A non-trained machine learning model (e.g., XGBoost or any classifier implementing fit/predict).
    := param: folds - A list of tuples where each tuple contains (X_train, X_test, y_train, y_test) for each fold.
    := param: modelPaths - Dictionary with the paths to save the metrics associated with the model.
    := param: targetLabels - Target labels associated with the classification problem.
    := param: title -The title of the plot. Default is "Model Performance Evaluation".
    := return: A dictionary with some metrics.
    """
    
    # Check if a model was provided
    if model is None:
        raise ValueError("Missing a model to evaluate!")

    # Check if the given model has been previously trained
    if isModelTrained(model):
        raise ValueError("The model provided has already been trained!")

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
    if not os.path.exists(modelPaths[type(model).__name__]['modelEvaluationMetrics']):
        calculatedMetrics = {}
    else:
        calculatedMetrics = jsonFileToDict(modelPaths[type(model).__name__]['modelEvaluationMetrics'])

    # Check if the metrics have already been computed and can be imported
    if calculatedMetrics == {}:
        # Initialize auxiliar variables
        conf_matrices = []
        y_pred_proba_list = []
        y_test_list = []
        log_losses = []
        
        # Iterate through each fold
        for (X_train_fold, X_test_fold, y_train_fold, y_test_fold) in folds:
            # Train the model on the training fold
            model.fit(X_train_fold, y_train_fold)
            
            # Make predictions on the test fold
            y_pred_fold = model.predict(X_test_fold)
            y_pred_proba_fold = model.predict_proba(X_test_fold)[:, 1]
            
            # Append results
            conf_matrices.append(confusion_matrix(y_test_fold, y_pred_fold))
            y_pred_proba_list.append(y_pred_proba_fold)
            y_test_list.append(y_test_fold)
            log_losses.append(log_loss(y_test_fold, y_pred_proba_fold))

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

        # Calculate average log loss
        avg_log_loss = np.mean(log_losses)

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

            # Average log loss
            'avg_log_loss':avg_log_loss
        })

        # Save the calculated metrics into a json file
        dictToJsonFile(calculatedMetrics, modelPaths[type(model).__name__]['modelEvaluationMetrics'])

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
    title = f"{type(model).__name__} Model Evaluation" if title is None else title
    fig.suptitle(title)

    # Tighten up the layout
    plt.tight_layout()

    # Save the plot as a PNG file if it has not been already saved
    if not os.path.exists(modelPaths[type(model).__name__]['modelEvaluationPlot']):
        plt.savefig(modelPaths[type(model).__name__]['modelEvaluationPlot'], format="png", dpi=600)

    # Display the plot
    plt.show()

    # Return the model metrics
    return calculatedMetrics