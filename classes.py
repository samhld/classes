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
            print "my name is David and I'm the guitarist"
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
        
class Band(object):
    def __init__(self):
    
    bandMembers = [Bassist(Musician),Guitarist(Musician),Drummer(Musician)]
    
    def hire(bandMember):
        bandMembers.append(bandMember)
        
    def fire(bandMember):
        bandMembers.remove(bandMember)
        

    david = Bassist()
    derek = Guitarist()
    david.solo(6)

    print david.sounds

