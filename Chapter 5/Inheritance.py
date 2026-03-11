class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")
# ===========================================================


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"


my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.speak())
print(my_dog.breed)
print(my_dog.name)