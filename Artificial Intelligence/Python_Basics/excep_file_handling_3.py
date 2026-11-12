'''log_path = "training_log.txt"

with open(log_path,"w") as f :
    f.write("Epoch1 : Loss = 0.4 \n")
    f.write("Epoch2 : Loss = 0.3 \n")

with open(log_path,"r") as f :
    contents = f.read()
    print(contents)'''

import json

metrics = {
    "Model_Name" : "Qwen3.5 27B",
    "Accuracy"  : 0.731,
    "Epochs_Trained" : 100
}

# save metrics to a file

with open("metrics.json" , "w") as f :
    json.dump(metrics , f , indent = 4 ) # indent = 4 makes it pretty printed

# Load Metrics Back
path = "metrics.json"

with open(path , "r") as f :
    mets = json.load(f)

print(mets)