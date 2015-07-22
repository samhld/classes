import time

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)]
        print ""
 
class Bassist(Musician):
    def __init__(self):
        #call the __init__ method of the parent class
        print "my name is David and I'm the bassist"
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])
    
class Guitarist(Musician):
    def __init__(self):
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["Boom","Boom","Clap"])
    
    def fourCount(self):
        for i in range(1,5):
            print i
            time.sleep(.5)
    def combust(self):
        print "I've combusted"
        
class Band(object):
    def __init__(self):
        
        self.bandMembers = []
    
    
    def hire(self, bandMember):
        self.bandMembers.append(bandMember)
        
    def fire(self, bandMember):
        self.bandMembers.remove(bandMember)
        

david = Bassist()
derek = Guitarist()
don = Drummer()
david.solo(6)
don.fourCount()

print david.sounds


band = Band()
band.hire(david)
band.hire(derek)

print band.bandMembers