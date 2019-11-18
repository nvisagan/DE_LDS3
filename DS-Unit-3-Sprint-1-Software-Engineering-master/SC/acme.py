from random import randint


class Product():
    """ Acme Products """
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    
    def stealability(self):
        """ Function if the item can be stolen """
        theft = self.price / self.weight
        if theft < 0.5:
            return 'Not so stealable...'
        elif (theft >= 0.5) & (theft < 1):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'
    
    
    def explode(self):
        """ Function if the item is explosive """
        xplode = self.flammability * self.weight
        if xplode < 10:
            return '...fizzle.'
        elif (xplode >= 10) & (xplode < 50):
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    """ Subclass of product (BoxingGlove) """
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=randint(1000000, 10000000)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        """ Gloves can't explode """
        return "..it's a glove."

    def punch(self):
        """ The strength of the glove """
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 & self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'