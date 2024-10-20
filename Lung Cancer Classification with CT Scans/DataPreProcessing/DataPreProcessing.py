import numpy as np
import pandas as pd
from sklearn.preprocessing import (MinMaxScaler, StandardScaler)

def performDataNormalization(df:pd.DataFrame, method:str=None, verbose:bool=False) -> pd.DataFrame:
    """
    # Description
        -> This function aims to normalize float64 features from the extracted datasets
        Since we are working with already encoded categorical features we must
        take them into consideration during normalization, therefore the need to 
        indicate the columns to normalize.
    -----------------------------------------------------------------------------------
    := param: df - DataFrame to be normalized.
    := param: method - Which data preprocessing technique to utilize [Either Normalization (Min-Max Scaling) or Standardization (Z-Score Scaling)].
    := param: verbose - Flag that determines whether ot not to include additional information regarding the function execution.
    := return: A new dataframe with the proper data normalized.
    """

    # Add a default value to the method to use
    method = 'min-max' if method is None else method

    # Check for a valid method
    if method not in ['min-max', 'z-score']:
        raise ValueError(f"Invalid \'{method}\' Method introduced! Please pick between (min-max or z-score)")

    # Perform a copy of the dataframe
    df_normalized = df.copy()

    # Filter only columns with dtype of np.float64 [We do not want integer values since they are encoded categorical features and also not the nodule_id]
    float64_cols = df_normalized.select_dtypes(include=['float64']).columns
 
    # Perform Min-Max scaling
    if method == "min-max":
        scaler = MinMaxScaler()
        df_normalized[float64_cols] = scaler.fit_transform(df_normalized[float64_cols])

    # Apply Z-score scaling (Standardization) to the float64 columns
    elif method == "z-score":
        scaler = StandardScaler()
        df_normalized[float64_cols] = scaler.fit_transform(df_normalized[float64_cols])

    return df_normalized

def removeHighlyCorrelatedFeatures(df:pd.DataFrame, correlationThreshold:float=0.9, verbose:bool=False) -> pd.DataFrame:
    """
    # Description
        -> Removes highly correlated features from a DataFrame 
        based on the specified correlation threshold.
    ----------------------------------------------------------
    := param: df - The input DataFrame.
    := param: correlation_threshold - The threshold above which features will be considered highly correlated.
    := param: verbose - Whether to print verbose output showing the features being dropped.
    := return: A DataFrame with highly correlated features removed.
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