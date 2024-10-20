import pandas as pd
from sklearn.model_selection import (StratifiedGroupKFold)
from imblearn.over_sampling import (SMOTE)

def stratifiedGroupSplit(preProcessedDataFrame:pd.DataFrame, useSMOTE:bool=None, test_size:float=None, randomState:int=None, verbose:bool=None) -> tuple:
    """
    # Description
        -> Perform Stratified Group Split on a dataset.
        This function ensures that the target variable's class distribution is 
        preserved across train and test sets while ensuring that groups are not split between them.
    -----------------------------------------------------------------------------------------------
    := param: preProcessedDataFrame - Pre-processed dataframe.
    := param: useSMOTE - Perform synthetic oversampling on each fold's training set.
    := param: test_size - Proportion of the test size to be considered.
    := param: randomState - Integer value used to guarantee the reproducibility of the results.
    := param: verbose - Boolean value which decides whether or not to provide additional information during the function execution.
    := return: A tuple of 4 elements containing the train and test sets for features and labels in the format (X_train, X_test, y_train, y_test).
    """
    
    # Check if a dataframe was provided
    if preProcessedDataFrame is None:
        raise ValueError("A dataframe was not passed to the function!")

    # Define default values for the arguments
    useSMOTE = False if useSMOTE is None else useSMOTE
    test_size = 0.3 if test_size is None else test_size
    randomState = 123 if randomState is None else randomState
    verbose = False if verbose is None else verbose

    # Make a copy of the dataframe
    df = preProcessedDataFrame.copy()

    # Create a 'group' column (Column containing the patient-ID) from the 'nodule_id'
    df['group'] = df['nodule_id'].str[10:14]
    groups = df['group']

    # Define the features (X) and the target variable (y)
    X = df.drop(['malignancy', 'nodule_id', 'group'], axis=1)
    y = df['malignancy']

    # Initialize StratifiedGroupKFold
    sgkf = StratifiedGroupKFold(n_splits=2, shuffle=True, random_state=randomState)

    # Perform the split
    for train_idx, test_idx in sgkf.split(X, y, groups=groups):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
        
        # Apply SMOTE to the training data only [if necessary]
        if useSMOTE:
            smote = SMOTE(random_state=randomState)
            X_train, y_train = smote.fit_resample(X_train, y_train)

        # Optionally, print the training and testing sizes or check the stratification
        if verbose:
            print(f"Training set size: {X_train.shape[0]}, Test set size: {X_test.shape[0]}")
            print(f"Training malignancy distribution:\n{y_train.value_counts()}")
            print(f"Test malignancy distribution:\n{y_test.value_counts()}")
        
        # Add the current fold to the list
        return (X_train, X_test, y_train, y_test)

def stratifiedGroupKFoldSplit(preProcessedDataFrame:pd.DataFrame, useSMOTE:bool=None, n_splits:int=None, randomState:int=None, verbose:bool=None) -> list[tuple]:
    """
    # Description
        -> Perform Stratified Group K-Fold cross-validation on a dataset.
        This function ensures that the target variable's class distribution is preserved across folds 
        (stratification) while ensuring that groups are not split between training and testing sets.
    -------------------------------------------------------------------------------------------------
    := param: preProcessedDataFrame - Pre-processed dataframe.
    := param: useSMOTE - Perform synthetic oversampling on each fold's training set.
    := param: n_splits - Number of folds for k-fold cross-validation.
    := param: randomState - Integer value used to guarantee the reproducibility of the results.
    := param: verbose - Boolean value which decides whether or not to provide additional information during the function execution.
    := return: list of tuples. Each tuple contains the train and test sets for features and labels in the format (X_train, X_test, y_train, y_test).
    """
    
    # Check if a dataframe was provided
    if preProcessedDataFrame is None:
        raise ValueError("A dataframe was not passed to the function!")

    # Define default values for the arguments
    useSMOTE = False if useSMOTE is None else useSMOTE
    n_splits = 5 if n_splits is None else n_splits
    randomState = 123 if randomState is None else randomState
    verbose = False if verbose is None else verbose

    # Make a copy of the dataframe
    df = preProcessedDataFrame.copy()

    # Initialize a list to store the data for all the folds
    folds = []

    # Create a 'group' column (Column containing the patient-ID) from the 'nodule_id'
    df['group'] = df['nodule_id'].str[10:14]
    groups = df['group']

    # Define the features (X) and the target variable (y)
    X = df.drop(['malignancy', 'nodule_id', 'group'], axis=1)
    y = df['malignancy']

    # Initialize StratifiedGroupKFold
    sgkf = StratifiedGroupKFold(n_splits=n_splits, shuffle=True, random_state=randomState)

    # Perform the split
    for train_idx, test_idx in sgkf.split(X, y, groups=groups):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
        
        # Apply SMOTE to the training data only [if necessary]
        if useSMOTE:
            smote = SMOTE(random_state=randomState)
            X_train, y_train = smote.fit_resample(X_train, y_train)

        # Optionally, print the training and testing sizes or check the stratification
        if verbose:
            print(f"Training set size: {X_train.shape[0]}, Test set size: {X_test.shape[0]}")
            print(f"Training malignancy distribution:\n{y_train.value_counts()}")
            print(f"Test malignancy distribution:\n{y_test.value_counts()}")
        
        # Add the current fold to the list
        folds.append((X_train, X_test, y_train, y_test))

    return folds