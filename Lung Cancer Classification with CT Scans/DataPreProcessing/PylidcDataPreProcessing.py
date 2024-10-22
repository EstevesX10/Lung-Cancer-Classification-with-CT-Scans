import numpy as np
import pandas as pd
import os
import customPylidc as pl
from customPylidc import (ClusterError)
import statistics as stats
from sklearn.cluster import (KMeans)
from sklearn.naive_bayes import (GaussianNB)

def createPylidcInitialDataframe() -> pd.DataFrame:
    """
    # Description
        -> This function aims to create a empty dataframe 
        with the proper columns to store the extracted features 
        from the pylidc package.
    -----------------------------------------------------------
    := return: Empty pandas dataframe.
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
    ----------------------------------------------------------------
    := param: pylidcFeaturesFilename - Path to save the final dataset.
    := return: df - Dataframe with the propely formated results.
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

def processIndeterminateNodules(df_pylidc:pd.DataFrame, method:str) -> pd.DataFrame:
    """
    # Description
        -> This function processes lung nodules labeled as 'Indeterminate' (malignancy level 3) in different ways based 
        on the selected method. You can either remove these cases or use clustering (K-Means) or probabilistic (Naive Bayes)
        approaches to assign them to one of the remaining malignancy classes (1, 2, 4, or 5).
    ------------------------------------------------------------------------------------------------------------------------
    := param: df_pylidc - The input DataFrame containing lung nodule data.
    := param: method - The method to process indeterminate nodules. Options are:
                        - "remove": Removes all entries with malignancy level 3.
                        - "moveToMalignant": Moves all the indeterminate entries target labels to Highly Suspicious.
                        - "kmeans": Uses K-Means clustering to assign indeterminate nodules to an existing class.
                        - "gaussian": Uses Naive Bayes to assign indeterminate nodules to an existing class based on probabilistic predictions.
    := return: A DataFrame where indeterminate nodules are either removed or reassigned to one of the non-indeterminate malignancy classes.
    """

    # Make a copy of the dataset received
    df_pylidc_copy = df_pylidc.copy()

    # Check if the given method is valid
    if method not in ["remove", "kmeans", "gaussian", "moveToMalignant"]:
        raise ValueError('Invalid Method Introduced!')
    
    if method == "remove":
        # Prune the indeterminate nodules
        df_binary_pylidc = df_pylidc_copy.loc[df_pylidc['malignancy'] != 3]
        return df_binary_pylidc
    
    elif method == "moveToMalignant":
        # Update the indeterminate nodules to be considered malignant
        df_pylidc_copy['malignancy'] = df_pylidc_copy['malignancy'].replace(3, 5)
        return df_pylidc_copy

    # Fetch the Id column
    idColumn = df_pylidc_copy.columns[0]
    ids = df_pylidc_copy[idColumn]

    # Drop the ID column
    df = df_pylidc_copy.drop(columns=idColumn)

    if method == "kmeans":
        # Get the dataset entries with a malignancy of 3 ('Indeterminate')
        indeterminateNodules = df[df['malignancy'] == 3]

        # Get the remaining nodules
        nonIndeterminateNodules = df[df['malignancy'] != 3]

        # Remove the target class to obtain the features (For both indeterminate and non determinate nodules)
        X_nonIndeterminateNodules = nonIndeterminateNodules.drop(columns=['malignancy'])
        X_indeterminateNodules = indeterminateNodules.drop(columns=['malignancy'])

        # Perform K-Means to cluster the non Indeterminate Nodules
        kmeans = KMeans(n_clusters=4)
        kmeans.fit(X_nonIndeterminateNodules)

        # Predict to which classes the Indeterminate nodules belong to
        indeterminateClusters = kmeans.predict(X_indeterminateNodules)

        # Retrieve the cluster labels
        clusterLabels = kmeans.labels_

        # Create a dictionary to map the clusters to already existing classes
        cluster_to_class_map = {cluster: nonIndeterminateNodules.iloc[clusterLabels == cluster]['malignancy'].mode()[0] for cluster in range(4)}

        # Map the Indeterminate nodules into the target class predicted by the K-means algorithm
        indeterminateNodules['malignancy'] = [cluster_to_class_map[cluster] for cluster in indeterminateClusters]

        # Merge back the indeterminate and non indeterminate nodules
        df_pylidc_kmeans = pd.concat([nonIndeterminateNodules, indeterminateNodules])

        # Reintroduce the nodule ID column
        df_pylidc_kmeans[idColumn] = ids

        # Insert the ID column back in the beginning of the dataset
        df_pylidc_kmeans = df_pylidc_kmeans[[idColumn] + [col for col in df_pylidc_kmeans.columns if col != idColumn]]
    
        return df_pylidc_kmeans
    
    elif method == "gaussian":
        # Separate the indeterminate nodules from the rest of the data
        X = df[df['malignancy'] != 3].drop(columns=['malignancy'])
        y = df[df['malignancy'] != 3]['malignancy']
        X_indeterminateNodules = df[df['malignancy'] == 3].drop(columns=['malignancy'])

        # Train the Naive Bayes model
        model = GaussianNB()
        model.fit(X, y)

        # Predict the probabilities for indeterminate nodules
        probabilities = model.predict_proba(X_indeterminateNodules)

        # Assign the class with the highest probability to each indeterminate nodule
        predicted_classes = model.predict(X_indeterminateNodules)

        # Create a new version of the dataset with the updated target labels
        df_pylidc_gaussian = df

        # Assign the predicted classes back to the 'Indeterminate' entries
        df_pylidc_gaussian.loc[df_pylidc_gaussian['malignancy'] == 3, 'malignancy'] = predicted_classes

        # Reintroduzir a coluna de ID
        df_pylidc_gaussian[idColumn] = ids

        # Organizar as colunas para ter 'ID' como a primeira coluna novamente
        df_pylidc_gaussian = df_pylidc_gaussian[[idColumn] + [col for col in df_pylidc_gaussian.columns if col != idColumn]]

        return df_pylidc_gaussian
    
def binarizeTargetLabel(df_pylidc:pd.DataFrame, method:str, filename:str) -> pd.DataFrame:
    """
    # Description
        -> This function transforms the 'malignancy' column in the given lung nodule dataset into a binary format, 
        where nodules with malignancy levels 1 or 2 are labeled as 0 (low malignancy) and those with levels 4 or 5 
        are labeled as 1 (high malignancy). The indeterminate cases (malignancy level 3) can be processed based on 
        the specified method before binarization. The final binarized dataset can also be saved to a file.
    --------------------------------------------------------------------------------------------------------------
    := param: df_pylidc - The input DataFrame containing lung nodule data.
    := param: method - The method to process indeterminate nodules. Options are:
                        - "remove": Removes all entries with malignancy level 3.
                        - "kmeans": Uses K-Means clustering to assign indeterminate nodules to an existing class.
                        - "gaussian": Uses Naive Bayes to assign indeterminate nodules to an existing class based on probabilistic predictions.
    := param: filename - The file path where the binarized dataset should be saved.
    := return: The modified DataFrame with the 'malignancy' column binarized (0 for low malignancy, 1 for high malignancy).
    """

    # Process the Indeterminate Nodules based on the given method
    df_pylidc_binary = processIndeterminateNodules(df_pylidc, method)

    # Perform Binarization on the entries with the remaining target labels
    df_pylidc_binary['malignancy'] = df_pylidc_binary['malignancy'].apply(lambda x: 0 if x <= 2 else 1)

    # Save the binarized dataset
    if not os.path.exists(filename):
        df_pylidc_binary.to_csv(filename, sep=',', index=False)

    # Return the binarized dataset
    return df_pylidc_binary