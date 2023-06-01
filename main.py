class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} робить звук: {self.sound}")
animal1 = Animal("Пес", "Гав")
animal1.make_sound()
