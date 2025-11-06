def make_it_speak(obj):
    obj.speak()

class Bird:
    def speak(self):
        print("Tweett tweett!")

class Robot:
    def speak(self):
        print("Beepp boop!")

make_it_speak(Bird())
make_it_speak(Robot())
