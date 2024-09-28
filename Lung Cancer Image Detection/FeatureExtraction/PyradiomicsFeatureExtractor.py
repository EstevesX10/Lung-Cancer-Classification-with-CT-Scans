import os

def extractPyradiomicsFeatures(Lidc_IdrFilesPath:str=None,
                               pyradiomicsDcmScriptPath:str=None,
                               pyradiomicsParamsFilePath:str=None,
                               pyradiomicsFeatureDictFilePath:str=None,
                               startPatient:int=None,
                               outputDirectoryPath:str=None,
                               tempDirectoryPath:str=None) -> None:
    
    """
    # Description
        -> This script iterates through all the patient's folders extracting important data from the .dcm files into a pyradiomics_features.csv file
    
    := param: Lidc_IdrFilesPath - Global path for files from the LIDC-IDR dataset
    := param: pyradiomicsDcmScriptPath - Path to the pyradiomics-dcm.py script used to extract features from the images on the dataset [Available on the pyradiomics GitHub Repository: https://github.com/AIM-Harvard/pyradiomics/tree/master/labs/pyradiomics-dcm]
    := param: pyradiomicsParamsFilePath - Path for the parameters file with the Pyradiomics feature extractor positional arguments [Available on the pyradiomics GitHub Repository: https://github.com/AIM-Harvard/pyradiomics/tree/master/labs/pyradiomics-dcm]
    := param: pyradiomicsFeatureDictFilePath - Path for the features to be considered during the extraction [Available on the pyradiomics GitHub Repository: https://github.com/AIM-Harvard/pyradiomics/blob/master/labs/pyradiomics-dcm/resources/featuresDict_IBSIv7.tsv]
    := param: startPatient - Number of the Patient to start the extraction from [Allows a better feature extraction management]
    := param: outputDirectoryPath - Path to the directory for saving the resulting DICOM file
    := param: tempDirectoryPath - Path to the directory to store intermediate results [Including the pyradiomic_features.csv]
    := return: None, since we are simply extracting data from the LIDC-IDR dataset images
    """

    # Add Restrictions to the Script Execution
    if Lidc_IdrFilesPath is None:
        raise ValueError('A path for the LIDC-IDR dataset was not given!')
    
    if pyradiomicsDcmScriptPath is None:
        raise ValueError('A path for the pyradiomics-dcm.py script was not given!')
    
    if pyradiomicsParamsFilePath is None:
        raise ValueError('A path for the Pyradiomics_Params.yaml file was not given!')
    
    if pyradiomicsFeatureDictFilePath is None:
        raise ValueError('A path for the featuresDict.tsv file was not given!')
    
    if outputDirectoryPath is None:
        raise ValueError('A Output Directory [used to save the resulting DICOM file] was not given!')
    
    if tempDirectoryPath is None:
        raise ValueError('A Path to the directory used to store intermediate results was not given!')

    if not os.path.isabs(Lidc_IdrFilesPath):
        raise ValueError('The path for the LIDC-IDR dataset is relative! Make sure to use a global path')

    # Save the Initial working directory
    initialDirectoryPath = os.getcwd()

    # Setting default parameters
    startPatient = 0 if startPatient is not None else startPatient
    startPatient = 0 if startPatient is not None else startPatient

    # Switch to the path with the LIDC-IDR dataset
    os.chdir(Lidc_IdrFilesPath)
    main_directory = os.listdir()

    # Iterate through all the Patients
    for patient in main_directory:
        # Skip the output and temp directories alonsgside all the unnecessary patient files (according to the initial patient) and other non-directory files
        if (not os.path.isdir(patient)) or patient == "OutputSR" or patient == "TempDir" or startPatient > int(patient[len(patient)-4:]):
            continue
        
        # Get the current Patient's Data Folder (Contains the CT-Scan and X-Ray)
        patientFolders = os.listdir(patient)
        path = ""
        content = 0
        
        # Finding the CT-scan folder (has the most content - directories with each segmentation and directory with the input DICOM series)
        for folder in patientFolders:
            segmentations_or_series = os.listdir(patient + "\\" + folder)
            if (len(segmentations_or_series) > content):
                content = len(segmentations_or_series)
                path = folder
        
        # Save the Directory with the Patient's Scans
        patientScansFolder = os.listdir(patient + "\\" + path)
        main = ""

        # Finding the series folder
        for folder in patientScansFolder:
            if not "Annotation" in folder:
                main = folder
                break
        
        # Create a index to track the current segmentation
        seg_index = 1
        
        # Iterate through all the segmentations and extract their features into a new entry on the .csv output file [Identified with <Patient_Name>-<Segmentation_Number> nomenclature]
        for folder in patientScansFolder:
            if "Segmentation" in folder:
                print("\n\nPACIENT [" + patient + "] - SEGMENTATION [" + str(seg_index) + "]")
                os.system(f'"""python {pyradiomicsDcmScriptPath} --input-image-dir "{patient}\{path}\{main}" --input-seg-file "{patient}\{path}\{folder}\\1-1.dcm" --output-dir {outputDirectoryPath} --temp-dir {tempDirectoryPath} --parameters {pyradiomicsParamsFilePath} --features-dict {pyradiomicsFeatureDictFilePath} --name {patient}-{seg_index}"""')
                seg_index+=1
    
    # Go back to the initial directory
    os.chdir(initialDirectoryPath)