import numpy as np
import pandas as pd
import customPylidc as pl
import statistics as stats

def refactorPyradiomicsDataset(df_pyradiomics:pd.DataFrame, pyradiomicsRefactoredFeaturesFilename:str, verbose:bool=False) -> pd.DataFrame:
    """
    # Description
        -> This function aims to refactor the pyradiomics dataset so that we take into
        consideration the mode / average values for all the nodules features parting
        from the annotations of the nodules provided by the pyradiomics_feature dataset

    := param: df_pyradiomics - Extracted dataframe with the raw information
    := param: pyradiomicsFeaturesFilename - Path to save the refactored version of the dataset
    := param: verbose - Boolean that enables valuable information during the function execution (reagarding the data being dealt with)
    := return: Pandas dataframe with a refactored version of the pyradiomics dataframe
    """
    # Define the columns for the refactored pyradiomics dataset
    cols = ['nodule_id'] + list(df_pyradiomics.columns)

    # Create a new empty dataframe for the refactored dataset
    df = pd.DataFrame(columns=cols)

    # Fetch all the Patient Ids Available
    patientIds = sorted(np.unique([scan.patient_id for scan in pl.query(pl.Scan).all()]))

    # Iterate over all the patient Ids
    for patientId in patientIds:
        if verbose:
            print(f"\n-> [NEW PATIENT: {patientId}]\n")
        
        # Fetch the patient's scan
        patientScan = pl.query(pl.Scan).filter(pl.Scan.patient_id == patientId).first()

        # Creating a mask to filter the current patient data from the pyradiomics dataframe
        mask = df_pyradiomics[df_pyradiomics.columns[0]].str.contains(patientId)
        
        # Get the segment of the dataframe with the current patient
        pyradiomicsPatientDf = df_pyradiomics.loc[mask]

        if pyradiomicsPatientDf.shape[0] == 0:
            print(f"Patient {patientId} not found inside the Pyradiomics extracted dataset!")
            continue
        
        if verbose:
            print(f"Patient dataframe shape: {pyradiomicsPatientDf.shape}")
        
        # Get the Patient Nodules Annotations
        patientNodules = patientScan.cluster_annotations()

        if verbose:
            print(f"Number of nodules: {len(patientNodules)}")
        
        # Iterate over the patient nodules
        for noduleId, nodule in enumerate(patientNodules):
            if verbose:
                print(f"[NEW NODULE: {noduleId + 1}]")
                print(f"Number of annotations: {len(nodule)}")
            
            # Check that the nodule list is not empty
            if len(nodule) == 0:
                print(f"Skipping empty nodule: {noduleId}")
                continue
            
            # Define a dictionary with the important features as keys and list with the current nodule
            allAttributes = dict([(col, []) for col in df.columns[1:]])
        
            # Initialize a dictionary with the df's attributes / columns and empty strings
            attributes = dict((col, "") for col in df.columns)
            
            # Iterate over the nodule annotations and save the important attributes inside the allAttributes dictionary
            for currentAnnotation in range(len(nodule)):
                if verbose:
                    print(f"[NEW ANNOTATION: {currentAnnotation + 1}]")
                
                # Check if the number of annotations matches
                if currentAnnotation >= pyradiomicsPatientDf.shape[0]:
                    print(f"Skipping invalid annotation at index {currentAnnotation}")
                    continue
                
                for noduleAttribute in df.columns[1:]:
                    try:
                        allAttributes[noduleAttribute] += [pyradiomicsPatientDf[noduleAttribute].values[currentAnnotation]]
                    except KeyError:
                        print(f"Skipping unknown attribute: {noduleAttribute}")
                        continue

            # Add an ID for the patient nodule
            attributes['nodule_id'] = f"{patientId}-{noduleId + 1}"
            
            # Normalizing the collected data
            for noduleAttribute in df.columns[1:]:
                # print(allAttributes[noduleAttribute])
                if isinstance(allAttributes[noduleAttribute][0], float):
                    attributes[noduleAttribute] = np.mean(allAttributes[noduleAttribute])
                elif isinstance(allAttributes[noduleAttribute][0], int):
                    attributes[noduleAttribute] = stats.mode(allAttributes[noduleAttribute])
                else:
                    attributes[noduleAttribute] = allAttributes[noduleAttribute][0]
            
            # Convert the new row into a Dataframe, reset index, and add it to the main dataframe
            df_new_nodule = pd.DataFrame.from_dict([attributes])
            
            # Concatenate ensuring index consistency
            if verbose:
                print(f"Before concat: df shape: {df.shape}, new nodule shape: {df_new_nodule.shape}")
            
            df = pd.concat([df, df_new_nodule], ignore_index=True)

            if verbose:
                print(f"After concat: df shape: {df.shape}")
    
    # Sort the dataframe based on the patient ID feature
    df = df.sort_values(by=['nodule_id'], ascending=[True]).reset_index(drop=True)
    
    # Save the results into a .csv file
    df.to_csv(pyradiomicsRefactoredFeaturesFilename, sep=',', index=False)

    # Return the refactored dataframe
    return df