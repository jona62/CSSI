class Spaceship:
    def __init__(self, spaceship_name, spaceship_type, spaceship_pilot):
        self.name = spaceship_name
        self.type = spaceship_type
        self.pilot = spaceship_pilot

    def description (self):
        print "This is the %s and it travels at a very high speed. It's a %s. It is piloted by %s!" % (self.name, self.type, self.pilot)

DDR3=Spaceship("Millennium Falcon", "Cruiser", "Edward White")
AMD=Spaceship("Elysium", "Light Carrier", "Mercury Seven")

DDR3.description()
AMD.description()
