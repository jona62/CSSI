# Defining the blueprint for a Musician.
class Musician:
    def __init__ (self, musician_name, musician_genre):
        self.name = musician_name
        self.genre = musician_genre

    def description(self):
        print "Hey, my name is %s and I make %s music." % (self.name, self.genre)

# Creating two Musician objects, using the Musician template.
beyonce = Musician('Whtiney Houston', 'R&B')
mozart = Musician('Mozart', 'Classical')

# Printing the properties of the Musician objects we've created.
print beyonce.name + ': ' + beyonce.genre
print mozart.name + ': ' + mozart.genre

# Calling the description method.
mozart.description()
