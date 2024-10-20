from typing import (Tuple)
import numpy as np
import pandas as pd
from sklearn.decomposition import (PCA)

def computePCA(numberComponents:int, X:pd.DataFrame) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    # Description
        -> This function focuses on performing the principal component analysis
        of a dataframe composed of features.
    ---------------------------------------------------------------------------
    := param: numberComponents - Number of components to be considered.
    := param: X - Features Dataset.
    := return:  mostImportantFeatures - Features indices to maintain from the original dataframe.
                explainedVariance - Array with each feature variance contribution on the dataset.
                pcValues - Principal Component Values [In a Array].
    """
    # Setting a default value for the number of components
    numberComponents = X.shape[1] - 1 if numberComponents is None or numberComponents >= X.shape[1] else numberComponents
    
    # Initialize a PCA object instance
    pca = PCA(n_components=numberComponents)

    # Get the most important features
    X_pca = pca.fit_transform(X)
    
    # Compute the explained variance
    explainedVariance = np.cumsum(pca.explained_variance_ratio_)

    # Get the principal Component Values
    pcValues = np.arange(pca.n_components_) + 1

    # number of components
    numberPrinciapalComponents = pca.components_.shape[0]

    # Get the indices of the most important features on each component
    mostImportantFeaturesIdxs = [np.abs(pca.components_[i]).argmax() for i in range(numberPrinciapalComponents)]

    # Return the indices of the most important features, the explained variance as well as the principal component values
    return (mostImportantFeaturesIdxs, explainedVariance, pcValues)