import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
from sklearn.base import (BaseEstimator, ClassifierMixin)
from sklearn.metrics import (confusion_matrix, precision_recall_curve, average_precision_score, roc_curve, roc_auc_score)

def pastelize_color(c:tuple, weight:float=None) -> np.ndarray:
    """
    # Description
        -> Lightens the input color by mixing it with white, producing a pastel effect.
    
    := param: c - Original color.
    := param: weight - Amount of white to mix (0 = full color, 1 = full white).
    """

    # Set a default weight
    weight = 0.5 if weight is None else weight

    # Initialize a array with the white color values to help create the pastel version of the given color
    white = np.array([1, 1, 1])

    # Returns a tuple with the values for the pastel version of the color provided
    return mcolors.to_rgba((np.array(mcolors.to_rgb(c)) * (1 - weight) + white * weight))

def plot_feature_distribution(df:pd.DataFrame=None, feature:str=None, forceCategorical:bool=None, featureDecoder:dict=None) -> None:
    """
    # Description
        -> This function plots the distribution of a feature (column) in a dataset.

    := param: df - Pandas DataFrame containing the dataset
    := param: feature - Feature of the dataset to plot
    := param: forceCategorical - Forces a categorical analysis on a numerical feature
    := param: featureDecoder - Dictionary with the conversion between the column value and its label [From Integer to String]
    """

    # Check if a dataframe was provided
    if df is None:
        print('The dataframe was not provided.')
        return
    
    # Check if a feature was given
    if feature is None:
        print('Missing a feature to Analyse.')
        return

    # Check if the feature exists on the dataset
    if feature not in df.columns:
        print(f"The feature '{feature}' is not present in the dataset.")
        return

    # Set default value
    forceCategorical = False if forceCategorical is None else forceCategorical

    # Check the feature type
    if pd.api.types.is_numeric_dtype(df[feature]):
        # For numerical class-like features, we can treat them as categories
        if forceCategorical:
            # Create a figure
            plt.figure(figsize=(8, 5))

            # Get unique values and their counts
            valueCounts = df[feature].value_counts().sort_index()
            
            # Check if a feature Decoder was given and map the values if possible
            if featureDecoder is not None:
                # Map the integer values to string labels
                labels = valueCounts.index.map(lambda x: featureDecoder.get(x, x))
                
                # Tilt x-axis labels by 0 degrees and adjust the fontsize
                plt.xticks(rotation=0, ha='center', fontsize=8)
            
            # Use numerical values as the class labels
            else:
                labels = valueCounts.index

            # Create a color map from green to red
            cmap = plt.get_cmap('RdYlGn_r')  # Reversed 'Red-Yellow-Green' colormap (green to red)
            colors = [pastelize_color(cmap(i / (len(valueCounts) - 1))) for i in range(len(valueCounts))]

            # Plot the bars with gradient colors
            bars = plt.bar(labels.astype(str), valueCounts.values, color=colors, edgecolor='lightgrey', alpha=1.0, width=0.8, zorder=2)
            
            # Plot the grid behind the bars
            plt.grid(True, zorder=1)

            # Add text (value counts) to each bar at the center with a background color
            for i, bar in enumerate(bars):
                yval = bar.get_height()
                # Use a lighter color as the background for the text
                lighterColor = pastelize_color(colors[i], weight=0.2)
                plt.text(bar.get_x() + bar.get_width() / 2,
                         yval / 2,
                         int(yval),
                         ha='center',
                         va='center',
                         fontsize=10,
                         color='black',
                         bbox=dict(facecolor=lighterColor, edgecolor='none', boxstyle='round,pad=0.3'))

            # Add title and labels
            plt.title(f'Distribution of {feature}')
            plt.xlabel(f'{feature} Labels', labelpad=20)
            plt.ylabel('Number of Samples')
            
            # Display the plot
            plt.show()
        
        # For numerical features, use a histogram
        else:
            # Create a figure
            plt.figure(figsize=(8, 5))

            # Plot the histogram with gradient colors
            plt.hist(df[feature], bins=30, color='lightgreen', edgecolor='lightgrey', alpha=1.0, zorder=2)
            
            # Add title and labels
            plt.title(f'Distribution of {feature}')
            plt.xlabel(feature)
            plt.ylabel('Frequency')
            
            # Tilt x-axis labels by 0 degrees and adjust the fontsize
            plt.xticks(rotation=0, ha='center', fontsize=10)

            # Plot the grid behind the bars
            plt.grid(True, zorder=1)
            
            # Display the plot
            plt.show()

    # For categorical features, use a bar plot
    elif pd.api.types.is_categorical_dtype(df[feature]) or df[feature].dtype == object:
            # Create a figure
            plt.figure(figsize=(8, 5))

            # Get unique values and their counts
            valueCounts = df[feature].value_counts().sort_index()
            
            # Create a color map from green to red
            cmap = plt.get_cmap('viridis')  # Reversed 'Red-Yellow-Green' colormap (green to red)
            colors = [pastelize_color(cmap(i / (len(valueCounts) - 1))) for i in range(len(valueCounts))]

            # Plot the bars with gradient colors
            plt.bar(valueCounts.index.astype(str), valueCounts.values, color=colors, edgecolor='lightgrey', alpha=1.0, width=0.8, zorder=2)
            
            # Plot the grid behind the bars
            plt.grid(True, zorder=1)

            # Add text (value counts) to each bar at the center with a background color
            for i, bar in enumerate(bars):
                yval = bar.get_height()
                # Use a lighter color as the background for the text
                lighterColor = pastelize_color(colors[i], weight=0.2)
                plt.text(bar.get_x() + bar.get_width() / 2,
                         yval / 2,
                         int(yval),
                         ha='center',
                         va='center',
                         fontsize=10,
                         color='black',
                         bbox=dict(facecolor=lighterColor, edgecolor='none', boxstyle='round,pad=0.3'))

            # Add title and labels
            plt.title(f'Distribution of {feature}')
            plt.xlabel(f'{feature} Labels', labelpad=20)
            plt.ylabel('Number of Samples')
            
            # Tilt x-axis labels by 0 degrees and adjust the fontsize
            plt.xticks(rotation=0, ha='center', fontsize=8)

            # Display the plot
            plt.show()
    else:
        print(f"The feature '{feature}' is not supported for plotting.")

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
