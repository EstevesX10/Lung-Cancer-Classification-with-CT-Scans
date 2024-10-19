import json

def dictToJsonFile(dictionary:dict, filePath:str) -> None:
    """
    # Description
        -> Converts a Python dictionary to a JSON file.
    ----------------------------------------------------------------
    := param: dictionary - The dictionary to convert into a JSON file.
    := param: filePath - The path (including filename) where the JSON file will be saved.
    := return: None, since we are only creating a json file.
    """

    # Check if a dictionary was passed
    if dictionary is None:
        raise ValueError("No dictionary was provided!")
    
    # Check if a save path was provided
    if filePath is None:
        raise ValueError("No file path was provided!")

    # Dump the dictionary into a json file
    try:
        with open(filePath, 'w') as json_file:
            json.dump(dictionary, json_file, indent=4)
    except Exception as e:
        return e

def jsonFileToDict(filePath:str) -> dict:
    """
    # Description
        -> Loads a JSON file and converts it to a Python dictionary.
    ----------------------------------------------------------------
    := param: filePath - The path (including filename) where the JSON file will be saved.
    := return: The dictionary loaded from the JSON file.
    """

    # Check if a save path was provided
    if filePath is None:
        raise ValueError("No json file path was provided!")

    # Load the dictionary from the json file
    try:
        with open(filePath, 'r') as json_file:
            dictionary = json.load(json_file)
        return dictionary
    except Exception as e:
        return None
