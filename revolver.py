# Revolver
import random


class revolver:
    def __init__(self):
        self.name = "Colt Peacemaker .45"
        self.hammer = False
        self.cylinders = [False, False, False, False, False, False]
        self.chamber = 0 # This points to an address in the cylinders list
        self.loading = True


    def load(self):
        if self.cylinders[self.chamber] is False:
            self.cylinders[self.chamber] = True
            print 'Loaded a round'
        else:
            print 'Cylinder already loaded'


    def loadingGate(self):
        if not self.loading:
            self.loading = True
            print 'Opened loading gate'
        else:
            print 'Loading gate open'

    def fire(self):
        # Pulls the trigger
        print 'Pulling trigger'
        if self.hammer: # if cocked
            if self.cylinders[self.chamber]: # If bullet in chamber fire it
                self.cylinders[self.chamber] = False
                print 'BANG!'
            else:
                print 'Click! Empty!'
            self.hammer = False
        else: # If not cocked
            print 'Not cocked'

    def cock(self):
        # Cocks the hammer
        if not self.hammer: # If not cocked, cock and rotate
            self.rotateCylinder()
            self.hammer = True
            print 'Pulling hammer'
        elif self.hammer: # If cocked, take off hammer
            self.hammer = False
            print 'Taking hammer off'
        

        # print 'Hammer:',self.hammer
    def rotateCylinder(self):
        if self.chamber == 5:
            self.chamber = 0
        else:
            self.chamber += 1

    def spinCylinder(self):
        self.chamber = random.randint(0,5)
        print 'Spinning cylinder'

    def printStatus(self):
        print self.name,"\nCocked:",self.hammer,"\nLoaded:",self.cylinders,"\nChamber:",self.chamber



