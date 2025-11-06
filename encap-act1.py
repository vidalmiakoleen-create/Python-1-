class Animal:
    def speak(self, speak):
        print("their sounds")

class Dog(Animal):
    def speak(self):
        print("Wooooof wooff wooff woooff")

class Cat(Animal):
    def speak(self):
        print("Meoowww!")

Dog().speak()
Cat().speak()
