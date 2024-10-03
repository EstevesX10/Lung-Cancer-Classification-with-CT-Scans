import numpy as np
import pandas as pd

def removeHighlyCorrelatedFeatures(df:pd.DataFrame, correlationThreshold:float=0.9, verbose:bool=False) -> pd.DataFrame:
    """
    # Description
        -> Removes highly correlated features from a DataFrame 
        based on the specified correlation threshold.
        
    := param: df - The input DataFrame
    := param: correlation_threshold - The threshold above which features will be considered highly correlated
    := param: verbose - Whether to print verbose output showing the features being dropped
    := return: A DataFrame with highly correlated features removed
    """
    
    # Compute the correlation matrix
    correlationMatrix = df.corr().abs()  # Get absolute values of correlations

    # Select the upper triangle of the correlation matrix
    upperTriangleCorrelationMatrix = correlationMatrix.where(np.triu(np.ones(correlationMatrix.shape), k=1).astype(bool))

    # Find features with correlation greater than the threshold
    columnsToDrop = [column for column in upperTriangleCorrelationMatrix.columns if any(upperTriangleCorrelationMatrix[column] > correlationThreshold)]
    
    if verbose:
        print(f"Columns to drop (correlation > {correlationThreshold}): {columnsToDrop}")
    
    # Drop the highly correlated features
    reducedDataFrame = df.drop(columns=columnsToDrop)

    # Return the reduced dataset
    return reducedDataFrame