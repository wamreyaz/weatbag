class Tile:
    map_word = "Cliff"

    def describe(self):
        print("Big rocks around the place, and the sound of small waves at the "
              "western sea makes you calm! \n")

    def action(self, player, do):
        print("Sorry, I don't understand.")

    def leave(self, player, direction):
        if direction == "w":
            print("My dear traveler, you can't fall off the cliff! "
                  "I won't let you do it.")
            return False
        elif direction == "e":
            print("It looks like the back of a wooden hut.\n"
                  "Since you don't walk through walls (yet) "
                  "you can't go there.")
            return False
        elif direction == "s":
            print("You follow the path uphill.")
            return True
        else:
            return True
