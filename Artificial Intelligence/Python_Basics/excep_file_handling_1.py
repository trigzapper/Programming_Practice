import json

def load_hyperparameters(filepath:str):
    try:
        # Trying to open and read config file
        with open(filepath,'r') as f :
            config = json.load(f)

    except FileNotFoundError:
        print(f" Error in config file , {filepath} not found . Using Defaults" )
        config = {"learning_rate" : 0.01 , "batch_size" : 32 }
    except json.JSONDecodeError:
        print(" Error : Config file is corrupted , not a valid JSON ")
        config = {}
    else:
        print("Loaded configuration successfully!")
        print("File contents")
        print(json.dumps(config,indent= 4))
    finally:
        print(" Finished checkpoint loading attempt")

    return config

cfg = load_hyperparameters(r"C:\Users\ssury\Desktop\Programming\Artificial Intelligence\Python_Basics\test.json" )


def initialize_weights(shape: tuple):
    if len(shape) != 2:
        raise ValueError(f"Expected a 2D shape (rows, cols), but got {len(shape)}D shape.")
    print(f"Initializing weights for shape: {shape}")

initialize_weights((3, 224, 224))  # Triggers ValueError!
