class ModelNotTrainedError(Exception):
    """Trying to eval a model thats not trained"""
    pass

class SimpleClassifier:
    def __init__(self):
        self.is_trained = False

    def predict(self,X):
        if not self.is_trained:
            raise ModelNotTrainedError("You must call train() before running predictions")
        return [0] * len(X)

model = SimpleClassifier()
try:
    model.predict([[1, 2, 3]])
except ModelNotTrainedError as e:
    print(f"Caught custom AI error: {e}")