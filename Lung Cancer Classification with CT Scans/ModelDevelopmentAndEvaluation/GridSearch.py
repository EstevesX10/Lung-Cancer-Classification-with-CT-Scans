import pandas as pd
from sklearn.model_selection import (GridSearchCV)
from sklearn.base import (BaseEstimator)
import xgboost as xgb
from .jsonFileManipulation import (dictToJsonFile, jsonFileToDict)

def isMachineLearningModel(model:any) -> bool:
    """
    # Description
        -> This function checks if a given instance
        corresponds to a scikit-learn or xgb machine learning model.
    ----------------------------------------------------------------
    := return: boolean value regarding the possible machine learning model object.
    """
    return isinstance(model, (BaseEstimator, xgb.XGBModel))

def computeModelBestParameters(model:any, parameterGrid:dict, X:pd.DataFrame, y:pd.DataFrame, modelPathsConfig:dict, saveBestParams:bool) -> dict:
    """
    # Description
        -> This funtion aims to calculate the best parameters of a given model using a Grid Search approach.
    ----------------------------------------------------------------
    := param: model - Class type of a Machine Learning Algorithm which supports a BaseEstimator from Scikit-learn
    := param: parameterGrid - Hyperparameter values to consider when performing Grid Search.
    := param: X - Features from the dataset.
    := param: y - Target label from the dataset.
    := param: modelPathsConfig - Dictionary with the file paths to save the model best parameters.
    := param: saveBestParams - Boolean value that determined whether or not to save the best parameters of the model.
    """

    # Instanciate the classifier
    classifier = model(random_state=42)

    # Check if the given model is an instance of a Machine Learning Model
    if not isMachineLearningModel(classifier):
        raise ValueError("The given model does not match a Machine Learning Model!")

    # Initialize a instance of the grid search
    gridSearch = GridSearchCV(estimator=classifier, param_grid=parameterGrid[type(classifier).__name__], refit=True, cv=3, n_jobs=-1, verbose=3)

    # Perform grid search
    gridSearch.fit(X, y)

    # Retrive the best parameters
    bestParameters = gridSearch.best_params_

    # Save the best parameters
    if saveBestParams:
        dictToJsonFile(bestParameters, filePath=modelPathsConfig[type(classifier).__name__]['bestParamsPath'])

    # Return the dictionary with the best parameters
    return bestParameters

