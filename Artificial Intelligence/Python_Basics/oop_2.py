class DataProcessor:
    def __init__(self , scaling_factor: float) :
        self.scaling_factor = scaling_factor

    #instance method
    def scale(self,value: float) -> float :
        return value*self.scaling_factor

    #class method (alternative constructor)
    @classmethod
    def from_preset(cls , present_type : str) :
        factor = 0.5 if present_type == "half" else 1.0
        return cls(scaling_factor = factor)


    # Static Method (Utility Function)
    @staticmethod
    def validate_shape(shape : tuple ) -> bool :
        return len(shape) > 0

processor = DataProcessor.from_preset("half")
print(processor.scale(10))
print(processor.validate_shape((3, 224, 224)))
