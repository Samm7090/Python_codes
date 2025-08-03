class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print(f"My name is {self.name}, and I am a {self.breed}.")

if __name__ == "__main__":
    dog1 = Dog("Tommy", "Beagle")
    dog2 = Dog("Max", "Bulldog")

    dog1.speak()
    dog2.speak()
