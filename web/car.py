# Example Car class

class Car(object):
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def info(self):
        print(f"Name of Car is {self.name}")
        print(f"Model of Car is {self.model}")

