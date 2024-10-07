def loadConfig() -> dict:
    """
    # Description
        -> This function aims to store all the configuration related parameters used inside the project
    """
    return {
        'pylidcFeaturesFilename':'./Datasets/pylidc_features.csv',
        'pyradiomicsFeaturesFilename':'./Datasets/pyradiomics_features.csv',
        'pyradiomicsRefactoredFeaturesFilename':'./Datasets/refactored_pyradiomics_features.csv',
        'finalFeaturesDatasetFilename':'./Datasets/final_features_dataset.csv'
    }