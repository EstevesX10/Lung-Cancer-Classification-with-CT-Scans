import pandas as pd
from sklearn.model_selection import (GridSearchCV)
from sklearn.base import (BaseEstimator)
import xgboost as xgb
import json

def dictToJsonFile(dictionary:dict, filePath:str) -> None:
    """
    # Description
        -> Converts a Python dictionary to a JSON file.
    ----------------------------------------------------------------
    := param: dictionary - The dictionary to convert into a JSON file.
    := param: filePath - The path (including filename) where the JSON file will be saved.
    := return: None, since we are only creating a json file.
    """

    # Check if a dictionary was passed
    if dictionary is None:
        raise ValueError("No dictionary was provided!")
    
    # Check if a save path was provided
    if filePath is None:
        raise ValueError("No file path was provided!")

    # Dump the dictionary into a json file
    try:
        with open(filePath, 'w') as json_file:
            json.dump(dictionary, json_file, indent=4)
    except Exception as e:
        return e

def jsonFileToDict(filePath:str) -> dict:
    """
    # Description
        -> Loads a JSON file and converts it to a Python dictionary.
    ----------------------------------------------------------------
    := param: filePath - The path (including filename) where the JSON file will be saved.
    := return: The dictionary loaded from the JSON file.
    """

    # Check if a save path was provided
    if filePath is None:
        raise ValueError("No json file path was provided!")

    # Load the dictionary from the json file
    try:
        with open(filePath, 'r') as json_file:
            dictionary = json.load(json_file)
        return dictionary
    except Exception as e:
        return None

def isMachineLearningModel(model:any) -> bool:
    """
    # Description
        -> This function checks if a given instance
        corresponds to a scikit-learn or xgb machine learning model.
    ----------------------------------------------------------------
    := return: boolean value regarding the possible machine learning model object.
    """
    return isinstance(model, (BaseEstimator, xgb.XGBModel))

def computeModelBestParameters(model:any, parameterGrid:dict, X_train:pd.DataFrame, y_train:pd.DataFrame, modelPathsConfig:dict, saveBestParams:bool) -> dict:
    """
    # Description
        -> This funtion aims to calculate the best parameters of a given model using a Grid Search approach.
    ----------------------------------------------------------------
    := param: model - Class type of a Machine Learning Algorithm which supports a BaseEstimator from Scikit-learn
    := param: parameterGrid - Hyperparameter values to consider when performing Grid Search.
    := param: X_train - Features from the training set
    := param: y_train - Target label from the trainin set.
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
    gridSearch.fit(X_train, y_train)

    # Retrive the best parameters
    bestParameters = gridSearch.best_params_

    # Save the best parameters
    if saveBestParams:
        dictToJsonFile(bestParameters, filePath=modelPathsConfig[type(classifier).__name__]['bestParamsPath'])

    # Return the dictionary with the best parameters
    return bestParameters

