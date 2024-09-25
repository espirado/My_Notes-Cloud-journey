class dog:
    species = "german"

    def __init__(self,age,name,breed):
        self.name = name
        self.age = age
        self.breed = breed

    #instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self,sound):
        return f"{self.name} says {sound}" 
        
class zollo(dog):
    def speak(self,sound="woo"):
        return f"{self.name} says {sound}"