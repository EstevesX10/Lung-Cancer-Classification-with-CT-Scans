import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

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

def plot_feature_distribution(df:pd.DataFrame=None, feature:str=None, forceCategorical:bool=None) -> None:
    """
    # Description
        -> This function plots the distribution of a feature (column) in a dataset.

    := param: df - Pandas DataFrame containing the dataset
    := param: feature - Feature of the dataset to plot
    := param: forceCategorical - Forces a categorical analysis on a numerical feature
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
            value_counts = df[feature].value_counts().sort_index()
            
            # Create a color map from green to red
            cmap = plt.get_cmap('RdYlGn_r')  # Reversed 'Red-Yellow-Green' colormap (green to red)
            colors = [pastelize_color(cmap(i / (len(value_counts) - 1))) for i in range(len(value_counts))]

            # Plot the bars with gradient colors
            bars = plt.bar(value_counts.index.astype(str), value_counts.values, color=colors, edgecolor='lightgrey', alpha=1.0, width=0.8, zorder=2)
            
            # Plot the grid behind the bars
            plt.grid(True, zorder=1)

            # Add text (value counts) to each bar at the center with a background color
            for i, bar in enumerate(bars):
                yval = bar.get_height()
                # Use a lighter color as the background for the text
                lighter_color = pastelize_color(colors[i], weight=0.2)
                plt.text(bar.get_x() + bar.get_width() / 2,
                         yval / 2,
                         int(yval),
                         ha='center',
                         va='center',
                         fontsize=10,
                         color='black',
                         bbox=dict(facecolor=lighter_color, edgecolor='none', boxstyle='round,pad=0.3'))

            # Add title and labels
            plt.title(f'Distribution of {feature}')
            plt.xlabel(f'{feature} Labels')
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
            
            # Plot the grid behind the bars
            plt.grid(True, zorder=1)
            
            # Display the plot
            plt.show()

    # For categorical features, use a bar plot
    elif pd.api.types.is_categorical_dtype(df[feature]) or df[feature].dtype == object:
            # Create a figure
            plt.figure(figsize=(8, 5))

            # Get unique values and their counts
            value_counts = df[feature].value_counts().sort_index()
            
            # Create a color map from green to red
            cmap = plt.get_cmap('viridis')  # Reversed 'Red-Yellow-Green' colormap (green to red)
            colors = [pastelize_color(cmap(i / (len(value_counts) - 1))) for i in range(len(value_counts))]

            # Plot the bars with gradient colors
            plt.bar(value_counts.index.astype(str), value_counts.values, color=colors, edgecolor='lightgrey', alpha=1.0, width=0.8, zorder=2)
            
            # Plot the grid behind the bars
            plt.grid(True, zorder=1)

            # Add text (value counts) to each bar at the center with a background color
            for i, bar in enumerate(bars):
                yval = bar.get_height()
                # Use a lighter color as the background for the text
                lighter_color = pastelize_color(colors[i], weight=0.2)
                plt.text(bar.get_x() + bar.get_width() / 2,
                         yval / 2,
                         int(yval),
                         ha='center',
                         va='center',
                         fontsize=10,
                         color='black',
                         bbox=dict(facecolor=lighter_color, edgecolor='none', boxstyle='round,pad=0.3'))

            # Add title and labels
            plt.title(f'Distribution of {feature}')
            plt.xlabel(f'{feature} Labels')
            plt.ylabel('Number of Samples')
            
            # Display the plot
            plt.show()
    else:
        print(f"The feature '{feature}' is not supported for plotting.")