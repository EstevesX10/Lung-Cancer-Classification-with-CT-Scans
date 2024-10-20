def loadConfig() -> dict:
    """
    # Description
        -> This function aims to store all the configuration related parameters used inside the project.
    ----------------------------------------------------------------------------------------------------
    := return: Dictionary with some of the important file paths of the project.
    """
    return {
        'pylidcFeaturesFilename':'./Datasets/pylidc_features.csv',
        'multiClassPylidcFeaturesFilename':'./Datasets/multi_class_pylidc_features.csv',
        'binaryPylidcFeaturesFilename':'./Datasets/binary_pylidc_features.csv',
        'pyradiomicsFeaturesFilename':'./Datasets/pyradiomics_features.csv',
        'pyradiomicsRefactoredFeaturesFilename':'./Datasets/refactored_pyradiomics_features.csv',
        'finalFeaturesDatasetFilename':'./Datasets/final_features_dataset.csv',
        'metricsDatasetFilename':'./Datasets/metrics_collected.csv',
    }

def loadModelsPaths() -> dict:
    """
    # Description
        -> Loads a dictionary with important paths when analysing a model's performance.
    ------------------------------------------------------------------------------------
    := return: Dictionary with all the paths used to stored model related data.
    """
    return {
        'SVC':{
            'accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/SVM/accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/SVM/accuracy/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/SVM/accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/SVM/accuracy/evaluationPlot.png'
            },
            'balanced_accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/SVM/balanced_accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/SVM/balanced_accuracy/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/SVM/balanced_accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/SVM/balanced_accuracy/evaluationPlot.png'
            },
            'recall':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/SVM/recall/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/SVM/recall/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/SVM/recall/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/SVM/recall/evaluationPlot.png'
            }
        },

        'RandomForestClassifier':{
            'accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/RandomForest/accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/RandomForest/accuracy/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/RandomForest/accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/RandomForest/accuracy/evaluationPlot.png'
            },
            'balanced_accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/RandomForest/balanced_accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/RandomForest/balanced_accuracy/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/RandomForest/balanced_accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/RandomForest/balanced_accuracy/evaluationPlot.png'
            },
            'recall':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/RandomForest/recall/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/RandomForest/recall/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/RandomForest/recall/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/RandomForest/recall/evaluationPlot.png',
            }
        },

        'XGBClassifier':{
            'accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/XGBoost/accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/XGBoost/accuracy/bestEstimator.pkl',
                
                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/XGBoost/accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/XGBoost/accuracy/evaluationPlot.png'
            },
            'balanced_accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/XGBoost/balanced_accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/XGBoost/balanced_accuracy/bestEstimator.pkl',
                
                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/XGBoost/balanced_accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/XGBoost/balanced_accuracy/evaluationPlot.png'
            },
            'recall':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/XGBoost/recall/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/XGBoost/recall/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/XGBoost/recall/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/XGBoost/recall/evaluationPlot.png'
            }
        },

        'VotingClassifier':{
            'accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/VotingClassifier/accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/VotingClassifier/accuracy/bestEstimator.pkl',
                
                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/VotingClassifier/accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/VotingClassifier/accuracy/evaluationPlot.png'
            },
            'balanced_accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/VotingClassifier/balanced_accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/VotingClassifier/balanced_accuracy/bestEstimator.pkl',
                
                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/VotingClassifier/balanced_accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/VotingClassifier/balanced_accuracy/evaluationPlot.png'
            },
            'recall':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/VotingClassifier/recall/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/VotingClassifier/recall/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/VotingClassifier/recall/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/VotingClassifier/recall/evaluationPlot.png'
            }
        }
    }

def loadModelsParameterGrids() -> dict:
    """
    # Description
        -> This function focuses on storing the possible paramaters configurations of
        some machine learning algorithms to be used alongside GridSearch.
    ---------------------------------------------------------------------------------
    := return: Dictionary with all the parameter grids used on each model Grid Search.
    """
    return {
        'XGBClassifier':{
            'max_depth': [4, 6],
            'n_estimators': [50, 100],
            'learning_rate': [0.05, 0.1],
            'subsample': [0.7, 0.8], 
            'colsample_bytree': [0.7, 0.8], 
            'gamma': [0, 0.1, 0.2],  
            'min_child_weight': [1, 3]
        },

        'SVC':{
            'C': [0.1, 1, 10, 100],
            'kernel': ['linear', 'rbf', 'poly'],
            'gamma': ['scale', 'auto'],
            'degree': [2, 3, 4],
            'coef0': [0.0, 0.1, 0.5],
            'probability': [True]
        },

        'RandomForestClassifier':{
            'n_estimators': [100, 200, 500],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'oob_score':[True],
            'bootstrap':[True]
        }
    }