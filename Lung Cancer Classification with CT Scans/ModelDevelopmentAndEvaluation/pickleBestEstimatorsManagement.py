import pickle

def saveBestEstimator(bestEstimator:object=None, filePath:str=None) -> None:
    """
    # Description
        -> Saves the best estimator found (passed onto the function).
    -----------------------------------------------------------------    
    Parameters:
    := param: bestEstimator - Best estimator found after performing Grid Search.
    := param: filePath - File path to the estimator.
    := return: None, since we are only saving an estimator.
    """

    # Check if a estimator was provided
    if bestEstimator is None:
        raise ValueError("Missing a best estimator to save!")
    
    # Check if the path is valid
    if filePath is None:
        raise ValueError("Invalid Path provided!")

    # Save the best estimator
    with open(filePath, 'wb') as f:
        pickle.dump(bestEstimator, f)

def loadBestEstimator(filePath:str=None) -> object:
    """
    # Description
        -> Loads a previously saved best estimator.
    ----------------------------------------------
    := param: filePath - File path to the estimator.
    := return: Best Estimator.
    """

    # Check if the path is valid
    if filePath is None:
        raise ValueError("Invalid Path provided!")

    # Load the best estimator
    with open(filePath, 'rb') as f:
        bestEstimator = pickle.load(f)

    # Return the best estimator
    return bestEstimator