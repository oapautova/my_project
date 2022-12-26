#!/usr/bin/python3
class animals:
    def __init__(self, age, wool, spine, weight, voice, herbivorous, limbs):
        self.age = age
        self.wool = wool
        self.spine = spine
        self.weight = weight
        self.voice = voice
        self.herbivorous = herbivorous
        self.limbs = limbs

class mammals(animals):
   def __init__(self, age, wool, spine, weight, voice, herbivorous, limbs, breastfeeding, gender): 
    super().__init__(age, wool, spine, weight, voice, herbivorous, limbs)
    self.breastfeeding = breastfeeding
    self.gender = gender

class human(mammals):
    def __init__(self, age, wool, spine, weight, voice, herbivorous, limbs, breastfeeding, gender, name, height):
        super().__init__(age, wool, spine, weight, voice, herbivorous, limbs, breastfeeding, gender)
        self.name = name
        self.height = height
    def say(self):
        print(f'Hello! My name is {self.name}.')


Ann = human(35, 'no', 'yes', 50, 'yes', 'no', 4, 'yes', 'female', 'Ann', 160)

class cat(mammals):
    def  __init__(self, age, wool, spine, weight, voice, herbivorous, limbs, breastfeeding, gender, name, naughty):
       super().__init__(age, wool, spine, weight, voice, herbivorous, limbs, breastfeeding, gender)
       self.name = name
       self.naughty = naughty

Tom = cat(4, 'yes', 'yes', 4, 'yes', 'no', 4, 'yes', 'male', 'Tom', 'yes')

class dog(mammals):
    def  __init__(self, age, wool, spine, weight, voice, herbivorous, limbs, breastfeeding, gender, name, faithful):
         super().__init__(age, wool, spine, weight, voice, herbivorous, limbs, breastfeeding, gender)
         self.name =  name
         self.faithful = faithful

Snoopy = dog(5, 'yes', 'yes', 25, 'yes', 'no', 4, 'yes', 'male', 'Snoopy', 'yes')
