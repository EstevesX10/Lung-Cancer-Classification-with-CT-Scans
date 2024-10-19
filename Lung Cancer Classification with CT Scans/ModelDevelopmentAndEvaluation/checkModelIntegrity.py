from sklearn.base import (BaseEstimator, ClassifierMixin)
import xgboost as xgb

def isValidAlgorithm(algorithm:object=None, bestParams:dict=None) -> bool:
    """
    # Description
        -> Check if a given algorithm can be instanciated.
    ------------------------------------------------------
    := param: algorithm - A machine learning model class (e.g., XGBoost or any classifier implementing fit/predict).
    := param: bestParams - Best parameters to use when instanciating the model.
    := return: Boolean value describing if the algorithm can be instanciated with the given parameters.
    """
    # Check if it's callable (can be instantiated)
    if callable(algorithm):
        try:
            # Try to instantiate it
            _ = algorithm(**bestParams)
            return True
        except:
            return False
    else:
        return False
    
def isMachineLearningModel(model:object=None) -> bool:
    """
    # Description
        -> This function checks if a given instance
        corresponds to a scikit-learn or xgb machine learning model.
    ----------------------------------------------------------------
    := return: boolean value regarding the possible machine learning model object.
    """

    # Defining a constraint for the model existence
    if model is None:
        raise ValueError("Missing a model!")

    return isinstance(model, (BaseEstimator, xgb.XGBModel))

def isModelTrained(model:BaseEstimator=None) -> bool:
    """
    # Description
        -> Checks if a scikit-learn model has been trained.
    -------------------------------------------------------
    := param: model - The scikit-learn model instance.
    := return: bool - True if the model has been trained, False otherwise.
    """

    # Defining a constraint for the model existence
    if model is None:
        raise ValueError("Missing a scikit-learn Model!")

    # Making sure that the model is a instance of both BaseEstimator and ClassifierMixin
    if not isinstance(model, (BaseEstimator, ClassifierMixin)):
        raise ValueError("The model must be an instance of both BaseEstimator and ClassifierMixin.")

    # Most scikit-learn models will have these attributes after training
    trainedAttributes = ['coef_', 'intercept_', 'n_features_in_', 'classes_']
    
    # Check if any of the common trained attributes exist in the model
    for attr in trainedAttributes:
        if hasattr(model, attr):
            return True
    return False