import pandas as pd
from sklearn.base import (BaseEstimator)
from sklearn.model_selection import (GridSearchCV)
import xgboost as xgb
from .checkModelIntegrity import (isMachineLearningModel)
from .jsonFileManagement import (dictToJsonFile)
from .pickleBestEstimatorsManagement import (saveBestEstimator)

def computeModelBestParameters(algorithm:object, parameterGrid:dict, X:pd.DataFrame, y:pd.DataFrame, scoring:str, modelPathsConfig:dict, saveBestModel:bool) -> dict:
    """
    # Description
        -> This funtion aims to calculate the best parameters of a given model using a Grid Search approach.
    ----------------------------------------------------------------
    := param: algorithm - Class type of a Machine Learning Algorithm which supports a BaseEstimator from Scikit-learn.
    := param: parameterGrid - Hyperparameter values to consider when performing Grid Search.
    := param: X - Features from the dataset.
    := param: y - Target label from the dataset.
    := param: scoring - Evaluation metric to take into consideration when performing Grid Search.
    := param: modelPathsConfig - Dictionary with the file paths to save the model best parameters.
    := param: saveBestModel - Boolean value that determined whether or not to save the best model and its parameters.
    """

    # Check if the given scoring method is valid
    if scoring not in ['accuracy', 'balanced_accuracy', 'recall'] and scoring is not None:
        raise ValueError("Got Invalid Scoring!")

    # Instanciate the classifier
    classifier = algorithm(random_state=42)

    # Check if the given model is an instance of a Machine Learning Model
    if not isMachineLearningModel(classifier):
        raise ValueError("The given model does not match a Machine Learning Model!")

    # Initialize a instance of the grid search
    gridSearch = GridSearchCV(estimator=classifier, param_grid=parameterGrid[type(classifier).__name__], scoring=scoring, refit=True, cv=3, n_jobs=-1, verbose=3)

    # Perform grid search
    gridSearch.fit(X, y)

    # Retrive the best parameters
    bestParameters = gridSearch.best_params_

    # Save if the model is to be saved
    if saveBestModel:
        # Save the best parameters
        dictToJsonFile(bestParameters, filePath=modelPathsConfig[type(classifier).__name__][scoring]['bestParamsPath'])

        # Save the best estimator
        saveBestEstimator(bestEstimator=gridSearch.best_estimator_, filePath=modelPathsConfig[type(classifier).__name__][scoring]['bestEstimatorPath'])

    # Return the dictionary with the best parameters
    return bestParameters

