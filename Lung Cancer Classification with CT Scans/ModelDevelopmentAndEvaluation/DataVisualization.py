import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.base import (BaseEstimator, ClassifierMixin)
from sklearn.metrics import (confusion_matrix, precision_recall_curve, average_precision_score, roc_curve, roc_auc_score)

def is_model_trained(model:BaseEstimator=None) -> bool:
    """
    # Description
        -> Checks if a scikit-learn model has been trained.

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

# [NEEDS TESTING]
def plot_model_stats(fitModel:BaseEstimator=None, x_test:np.ndarray=None, y_test:np.ndarray=None, title:str=None) -> None:
    """
    # Description
        -> Plots the model's precision-recall curve, ROC Curve and the Confusion Matrix
    
    := param: fitModel - Trained Classifier 
    := param: x_test - Array with the Features Test set
    := param: y_test - Array with the Labels Test set
    """

    # -> Defining some constraints on the function usage
    # Check if a model was given
    if fitModel is None:
        print("Missing a Trained Model!")
        return
    
    # Check if the features test set was given
    if x_test is None:
        print("Missing the Features test set!")
        return

    # Check if the labels test set was given
    if y_test is None:
        print("Missing the Labels test set!")
        return

    # Check if the Model was trained
    if not is_model_trained(fitModel):
        print("The given model has yet to be trainned!")
        return

    # Making sure that the model is a instance of both BaseEstimator and ClassifierMixin
    if not isinstance(fitModel, (BaseEstimator, ClassifierMixin)):
        raise ValueError("The model must be an instance of both BaseEstimator and ClassifierMixin.")

    # Set Default Value to the title
    title = "Model Performance Evaluation" if title is None else title

    # Predict Probability of belonging to a certain class
    Y_Pred_Proba = fitModel.predict_proba(x_test)[:,1]

    # Create a larger figure to accommodate the plots
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(16, 4))

    # Calculate precision, recall, and thresholds
    precision, recall, _ = precision_recall_curve(y_test, Y_Pred_Proba)
    
    # Calculate average precision score
    avg_precision = average_precision_score(y_test, Y_Pred_Proba)
    
    # Plot the precision-recall curve
    axs[0].plot(recall, precision, label=f'Precision-Recall curve (AP = {avg_precision:.2f})')
    axs[0].xlabel('Recall')
    axs[0].ylabel('Precision')
    axs[0].title('Precision-Recall Curve')
    axs[0].legend(loc='lower left')

    # Getting the ROC Curve
    false_positive_rate, true_positive_rate, _ = roc_curve(y_test, Y_Pred_Proba)

    # Calculating the Area Under Curve
    AUC = roc_auc_score(y_test, Y_Pred_Proba)

    # Creating a Confusion Matrix
    cm = confusion_matrix(y_test, fitModel.predict(x_test))

    # Creating a HeatMap
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', ax=axs[2])

    # Plot Confusion Matrix
    axs[1].set_title('Confusion Matrix')
    axs[1].set_xlabel('Predicted Labels')
    axs[1].set_ylabel('True Labels')
    axs[1].xaxis.set_ticklabels(np.unique(y_test))
    axs[1].yaxis.set_ticklabels(np.unique(y_test))

    # Plot ROC Curve
    axs[2].plot(false_positive_rate, true_positive_rate, label=f"AUC = {round(AUC, 4)}", color="darkblue", linestyle='-', linewidth=1.4)
    axs[2].plot([0, 1], [0, 1], label="Chance level (AUC = 0.5)", color="darkred", linestyle='--')
    axs[2].set_title('ROC Curve')
    axs[2].set_xlabel('False Positive Rate')
    axs[2].set_ylabel('True Positive Rate')
    axs[2].legend()

    # Set the super title for all subplots
    fig.suptitle(title)

    plt.tight_layout()
    plt.show()
