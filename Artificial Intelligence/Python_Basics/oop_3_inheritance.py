'''import torch.nn as nn

# Base Parent Class
class BaseModel(nn.Module):
    def log_architecture(self):
        print("Logging Model Architecture")

# Child Class inheriting from BaseModel
class CustomClassifier(BaseModel):
    def __init__(self, num_classes = int ):
        super().__init__() # Call Parent Constructor
        self.fc = nn.Linear(128 , num_classes)

model = CustomClassifier(num_classes = 10)
model.log_architecture() #inherited Method'''

class Optimizer:
    def __init__(self, lr:float):
        self.lr = lr #public
        self.__momentum = 0.9 #private

    def get_momentum(self): #GetterMethod
        return self.__momentum

opt = Optimizer(0.01)
print(opt.get_momentum())