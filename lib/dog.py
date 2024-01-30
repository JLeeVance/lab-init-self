#!/usr/bin/env python3

class Dog:
    
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
    
gracie = Dog("Gracie", "Labradoodle")
print(gracie.name)
