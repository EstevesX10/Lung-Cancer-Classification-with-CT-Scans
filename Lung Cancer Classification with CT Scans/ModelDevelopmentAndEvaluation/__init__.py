# This Python Package contains the code used to define, train and assess machine learning models

# Defining which submodules to import when using from <package> import *
__all__ = []
__all__ = [
    "dictToJsonFile", "jsonFileToDict",
    "computeModelBestParameters",
    "computePCA",
    "stratifiedGroupSplit", "stratifiedGroupKFoldSplit",
    "isValidAlgorithm", "isMachineLearningModel", "isModelTrained",
    "saveBestEstimator", "loadBestEstimator",
    "evaluateModel", "convertMetricsToDataFrame",
    "plotScreeGraph", "plotCritialDifferenceDiagram"
]


from .jsonFileManagement import (dictToJsonFile, jsonFileToDict)
from .GridSearch import (computeModelBestParameters)
from .PCA import (computePCA)
from .DataPartitioning import (stratifiedGroupSplit, stratifiedGroupKFoldSplit)
from .checkModelIntegrity import (isValidAlgorithm, isMachineLearningModel, isModelTrained)
from .pickleBestEstimatorsManagement import (saveBestEstimator, loadBestEstimator)
from .ModelEvaluation import (evaluateModel, convertMetricsToDataFrame)
from .DataVisualization import (plotScreeGraph, plotCritialDifferenceDiagram)