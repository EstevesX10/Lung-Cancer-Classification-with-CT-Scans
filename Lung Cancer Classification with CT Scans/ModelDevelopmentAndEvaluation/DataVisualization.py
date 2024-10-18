import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plotScreeGraph(pcValues:np.ndarray, explainedVariance:np.ndarray) -> None:
    """
    # Description
        -> The plotScreeGraph function simply creates a plot
        showcasing the influence of Features in the datasets variance
    -----------------------------------------------------------------
    := param: pcValues - Principal Component Values
    := param: explainedVariance - Array with each feature variance contribution on the dataset
    := return: None, since we are merely plotting a graph
    """

    # Create figure with specific size
    plt.figure(figsize=(10, 6))

    # Plot with improved styling
    plt.plot(pcValues, explainedVariance, '.-', linewidth=2, color='#fcb9b2', markersize=8, label='Explained Variance')

    # Add title and labels with larger font sizes for clarity
    plt.title('[Scree Plot] Principal Component Analysis', fontsize=16)
    plt.xlabel('Number of Components', fontsize=14)
    plt.ylabel('Cumulative Explained Variance (%)', fontsize=14)

    # Add vertical dashed lines at key points with annotations in the middle height
    middleHeight = 0.5
    for x in (50, 100, 150, 200):
        if x < len(pcValues):
            plt.axvline(x=x, color='#780000', linestyle='--', alpha=0.7, linewidth=3)
            plt.text(x, middleHeight, f'{x}', color='white', fontsize=12, fontweight='bold',
                    ha='center', va='center', bbox=dict(facecolor='#ba181b', edgecolor='#9d0208', alpha=1.0, boxstyle='round,pad=0.5'))

    # Add grid with subtle styling for better visual separation
    plt.grid(True, linestyle=':', alpha=0.6)

    # Display legend
    plt.legend(loc='lower right', fontsize=12)

    # Improve axis ticks and limits for clearer presentation
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlim([min(pcValues), max(pcValues)])
    plt.ylim([0, max(explainedVariance) * 1.05])

    # Show plot
    plt.tight_layout()
    plt.show()