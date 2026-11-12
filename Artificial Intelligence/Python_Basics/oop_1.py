'''class NeuralLayer:
    def __init__(self,input_dim : int , output_dim : int ):
        self.input_dim = input_dim
        self.output_dim = output_dim
        print(f"Created Layer with input : {input_dim} , output : {output_dim}" )

# Creating an object
layer = NeuralLayer(input_dim=512 , output_dim=128)'''

class ModelConfig:
    framework = "PyTorch" #ClassVariable

    def __init__(self , model_name: str) :
        self.model_name = model_name

config1 = ModelConfig("ResNet")
config2 = ModelConfig("BERT")

print(config1.framework , config1.model_name)
print(config2.framework , config2.model_name)

