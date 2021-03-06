class Tile:
    map_word = "Top cliff"
    
    def describe(self):
        print("You have reached the top of the cliff! You feel the fresh "
              "breeze in your face and you smell the salty sea! The view and "
              "the weather here are wonderful! You'd like to stay but the "
              "adventure spirit shakes you and you're on the move again.\n"
              "So which way?\n")

    def action(self, player, do):
        print("Sorry, I don't understand.")

    def leave(self, player, direction):
        if direction in ('s', 'w'):
            print("My dear traveler, you can't go there, you will fall of the "
                   "cliff!")
            return False
        elif direction in('e', 'n'):
            print("You follow the path downhill.")
            return True
