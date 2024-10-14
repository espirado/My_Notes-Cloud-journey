class person:
    def __init__(self,name, age) -> None:
        self.name= name
        self.age = age
    def __del__(self):
        print("object is being deconstructed")

       