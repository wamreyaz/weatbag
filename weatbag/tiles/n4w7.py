from weatbag import words
from weatbag.utils import transfer

class Tile:
    def __init__(self):
        self.challenge_completed = False
        
    def describe(self):
        if not self.challenge_completed:
            print("The only thing around this place is sand, small rocks, the "
                  "beach waters and about a dozen of kitties playing around.\n"
                  "You aproach the kitties and to your surprise they all start "
                  "rubbing at your legs and mewing! What is even more "
                  "surprising is that your brain understands and translates "
                  "meaws into words!\n"
                  "You can clearly hear them say:\n"
                  "'PLZ SIR, IT VRY HAWT HEER, CAN U TREAT US SUM  MICE "
                  "CREAM?! ALL U NED IZ 2 COMBINE SUM MICE AN SUM CREAM AN "
                  "READY IT IZ! PLEEEEASE!' *mieaw* *rub* *rub*\n")
            self.challenge_completed = True
        else:
            print("The only thing around this place is sand, small rocks, the "
                  "beach waters and about a dozen of kitties playing around.\n")

    def action(self, player, do):
        print("Sorry, I don't understand.\n")
        
        
test_items = ['mice', 'cream']

