def loadConfig() -> dict:
    """
    # Description
        -> This function aims to store all the configuration related parameters used inside the project.
    """
    return {
        'pylidcFeaturesFilename':'./Datasets/pylidc_features.csv',
        'multiClassPylidcFeaturesFilename':'./Datasets/multi_class_pylidc_features.csv',
        'binaryPylidcFeaturesFilename':'./Datasets/binary_pylidc_features.csv',
        'pyradiomicsFeaturesFilename':'./Datasets/pyradiomics_features.csv',
        'pyradiomicsRefactoredFeaturesFilename':'./Datasets/refactored_pyradiomics_features.csv',
        'finalFeaturesDatasetFilename':'./Datasets/final_features_dataset.csv'
    }

def loadModelsPaths() -> dict:
    """
    # Description
        -> Loads a dictionary with important paths when analysing a model's performance.
    """
    return {
        'XGBClassifier':{
            'bestParamsPath':'./ExperimentalResults/XGBoost/bestParams.json',
            'modelMetrics':'./ExperimentalResults/XGBoost/metrics.json',
            'modelPath':'./ExperimentalResults/XBGBoost/'
        },

        'SVC':{
            'bestParamsPath':'./ExperimentalResults/SVM/bestParams.json',
            'modelMetrics':'./ExperimentalResults/SVM/metrics.json',
            'modelPath':'./ExperimentalResults/SVM/'
        },

        'RandomForestClassifier':{
            'bestParamsPath':'./ExperimentalResults/RandomForest/bestParams.json',
            'modelMetrics':'./ExperimentalResults/RandomForest/metrics.json',
            'modelPath':'./ExperimentalResults/RandomForest/'
        }
    }

def loadModelsParameterGrids() -> dict:
    """
    # Description
        -> This function focuses on storing the possible paramaters configurations of
        some machine learning algorithms to be used alongside GridSearch.
    """
    return {
        'XGBClassifier':{
            'max_depth': [4, 6, 8],
            'n_estimators': [50, 100, 150],
            'learning_rate': [0.01, 0.05, 0.1, 0.2],
            'subsample': [0.6, 0.8, 1.0],
            'colsample_bytree': [0.6, 0.8,1.0],
            'gamma': [0, 0.2, 0.4],
            'min_child_weight': [2, 3, 4]
        },

        'SVC':{
            'C': [0.1, 1, 10, 100],
            'gamma': [1, 0.1, 0.01, 0.001],
            'kernel': ['rbf', 'sigmoid']
        },

        'RandomForestClassifier':{
            'n_estimators': [100, 300, 500, 700, 900, 1100, 1300, 1500],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'min_samples_leaf': [1, 2, 3, 4, 5, 6]
        }
    }