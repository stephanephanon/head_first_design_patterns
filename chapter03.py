"""
Chapter Three -- Decorator Pattern

This pattern lets us add additional responsibilities
to an object dynamically.
It is an alternative to subclassing for extending functionality.
"""


class Beverage(object):
    """
    An abstract class representing a beverage
    """
    description = None

    def get_description(self):
        """
        Return the description of the beverage
        :return: string
        """
        return self.description

    def cost(self):
        """
        Return the cost of the beverage
        :return: float
        """
        raise NotImplementedError


class CondimentDecorator(Beverage):
    """
    Decorator class that extends beverage class
    """
    def get_description(self):
        raise NotImplementedError


# ------------------------
# Concrete Condiment Implementations
# ------------------------
class Mocha(CondimentDecorator):
    """
    Class to add Mocha option
    """
    def __init__(self, beverage):
        self.description = "Mocha"
        self.beverage = beverage

    def get_description(self):
        return "{}, {}".format(self.beverage.get_description(), self.description)

    def cost(self):
        return 0.20 + self.beverage.cost()


class Soy(CondimentDecorator):
    """
    Class to add Soy option
    """
    def __init__(self, beverage):
        self.description = "Soy"
        self.beverage = beverage

    def get_description(self):
        return "{}, {}".format(self.beverage.get_description(), self.description)

    def cost(self):
        return 0.50 + self.beverage.cost()


class Whip(CondimentDecorator):
    """
    Class to add Whip option
    """
    def __init__(self, beverage):
        self.description = "Whip"
        self.beverage = beverage

    def get_description(self):
        return "{}, {}".format(self.beverage.get_description(), self.description)

    def cost(self):
        return 0.10 + self.beverage.cost()


# ------------------------
# Concrete Beverage Implementations
# ------------------------
class Espresso(Beverage):
    """
    Class that represents an espresso drink
    """
    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    """
    Class that represents a house blend coffee
    """
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self):
        return 1.00


class DarkRoast(Beverage):
    """
    Class that represents a dark roast coffee
    """
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self):
        return 1.00


class Decaf(Beverage):
    """
    Class that represents a decaf coffee
    """
    def __init__(self):
        self.description = "Decaf Coffee"

    def cost(self):
        return 1.00


if __name__ == '__main__':
    # let's run the coffee shop

    # customer one wants espresso
    beverage = Espresso()
    print("{}: ${:.2f}".format(beverage.get_description(), beverage.cost()))

    # customer two wants a double mocha dark roast
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    print("{}: ${:.2f}".format(beverage2.get_description(), beverage2.cost()))

    # customer three wants a soy mocha whip house blend
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print("{}: ${:.2f}".format(beverage3.get_description(), beverage3.cost()))
