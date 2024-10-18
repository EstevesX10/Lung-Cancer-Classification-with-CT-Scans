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
    plt.plot(pcValues, explainedVariance, 'o-', linewidth=2, color='blue')
    plt.title('Scree Graph')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    for x in (50, 100, 150, 200):
        plt.axvline(x=x, color='red', linestyle='--')
    # plt.figure(figsize=(8,4))
    plt.grid(True)
    plt.show()