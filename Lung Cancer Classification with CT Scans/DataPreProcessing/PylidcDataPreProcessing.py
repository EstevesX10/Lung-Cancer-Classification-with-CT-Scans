import numpy as np
import pandas as pd
import customPylidc as pl
from customPylidc import (ClusterError)
import statistics as stats

def createPylidcInitialDataframe() -> pd.DataFrame:
    """
    # Description
        -> This function aims to create a empty dataframe 
        with the proper columns to store the extracted features 
        from the pylidc package

    := return: Empty pandas dataframe
    """

    # Define the initial structure of the Dataframe
    df = pd.DataFrame(columns=['nodule_id',           # Nodule Identification Number [Form “LIDC-IDRI-dddd-ii” where dddd is a string of integers and ii is the identifier of the patient's nodule 
                               'slice_thickness',     # DICOM attribute (0018,0050)
                               'pixel_spacing',       # Dicom attribute (0028,0030)
                               'slice_spacing',       # Space between slices
                               'subtlety',            # Difficulty of detection
                               'internalStructure',   # Internal composition of the nodule
                               'calcification',       # Pattern of calcification
                               'sphericity',          # Three-dimensional shape of the nodule 
                               'margin',              # How well-defined the nodule margin is
                               'lobulation',          # Degree of lobulation
                               'spiculation',         # Extent of spiculation present
                               'texture',             # Radiographic solidity - internal texture
                               'diameter',            # Maximal diameter
                               'surface_area',        # Estimated surface area
                               'volume',              # Estimated 3D volume of the annotated nodule
                               'malignancy',          # likelihood of malignancy -> Target [What we want to predict]
                            ])
    return df

def extractPylidcFeatures(pylidcFeaturesFilename:str) -> pd.DataFrame:
    """
    # Description
        -> This function aims to extract the important features from 
           the CT data scans through the Pylidc package.
           It will find the mode / mean values for each nodule's 
           annotations throughout all the available patients.

    := param: pylidcFeaturesFilename - Path to save the final dataset to
    := return: df - Dataframe with the propely formated results
    """
    # Initialize the dataframe
    df = createPylidcInitialDataframe()
    
    # Fetch all the Patient Ids Available
    patientIds = sorted(np.unique([scan.patient_id for scan in pl.query(pl.Scan).all()]))

    # Creating a list to store all the patient's whose nodule's clustering failed
    failedClusterAnalysis = []
    
    # Iterate over all the patient Ids
    for patientId in patientIds:
        # Get all the Scans associated with the current patient
        patientScan = pl.query(pl.Scan).filter(pl.Scan.patient_id == patientId).first()
        
        try:
            # Debug: print scan ID and basic info
            print(f"Processing scan {patientScan.patient_id}")
            
            # Fetch the nodes associated with each patient Scan
            patientNodules = patientScan.cluster_annotations(tol=2.0)

        except ClusterError:
            print(f"ClusterError for patient {patientId}, scan {patientScan.patient_id}. Adjusting tolerance.")
            failedClusterAnalysis.append(patientId)
            continue
           
        # Iterate over the patient nodules
        for noduleId, nodule in enumerate(patientNodules):
            # Define a dictionary with the important features as keys and list with the current nodule
            allAttributes = dict([(col, []) for col in df.columns[1:]])
        
            # Initialize a dictionary with the df's attributes / columns and empty strings
            attributes  = dict((col, "") for col in df.columns)
            
            # Iterate over the nodule annotations and save the important attributes inside the allAttributes dictionary
            for annotation in nodule:
                for noduleAttribute in df.columns[1:]:
                    if hasattr(patientScan, noduleAttribute):
                        allAttributes[noduleAttribute] += [getattr(patientScan, noduleAttribute)]
                    elif hasattr(annotation, noduleAttribute):
                        allAttributes[noduleAttribute] += [getattr(annotation, noduleAttribute)]
                    else:
                        print(f"The attribute '{noduleAttribute}' does not exist in Annotation nor Scan classes.")

            # Add an ID for the patient nodule
            attributes['nodule_id'] = f"{patientId}-{noduleId + 1}"
            
            # Normalizing the collected data
            for noduleAttribute in df.columns[1:]:
                if isinstance(allAttributes[noduleAttribute][0], float):
                    attributes[noduleAttribute] = np.mean(allAttributes[noduleAttribute])
                elif isinstance(allAttributes[noduleAttribute][0], int):
                    attributes[noduleAttribute] = stats.mode(allAttributes[noduleAttribute])
                else:
                    attributes[noduleAttribute] = stats.mode(allAttributes[noduleAttribute])
            
            # Convert the new row into a Dataframe and add it to the previous one
            df_new_nodule = pd.DataFrame.from_dict([attributes])
            df = pd.concat([df, df_new_nodule], ignore_index=True)

    # Sort the dataframe based on the patient ID feature
    df = df.sort_values(by=['nodule_id'], ascending=[True])
    
    # Save the results into a .csv file
    df.to_csv(pylidcFeaturesFilename, sep=',', index=False)

    # Print failed processes
    print(f"\nFailed analysing the nodules from {len(failedClusterAnalysis)} patients.")
    
    # Return the Final dataframe
    return df