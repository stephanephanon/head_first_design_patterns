"""
Chapter Four -- Factory Patterns

Another way... with a plain pizza object, and a
store that knows how to do more
"""

class DoughBase(object):
    """
    Pizza Dough base class
    """
    def __repr__(self):
        return 'generic dough'


class ThinCrustDough(DoughBase):
    """
    Thin Crust Dough class
    """
    def __repr__(self):
        return 'thin crust'


class ThickCrustDough(DoughBase):
    """
    Thick Crust Dough class
    """
    def __repr__(self):
        return 'thick crust'


class TomatoSauceBase(object):
    def __repr__(self):
        return 'tomato sauce'


class MarinaraSauce(TomatoSauceBase):
    def __repr__(self):
        return 'marinara sauce'


class PlumTomatoSauce(TomatoSauceBase):
    def __repr__(self):
        return 'plum tomato sauce'


class CheeseBase(object):
    def __repr__(self):
        return 'generic cheese'


class ReggianoCheese(CheeseBase):
    def __repr__(self):
        return 'reggiano cheese'


class MozzarellaCheese(CheeseBase):
    def __repr__(self):
        return 'mozzarella cheese'


class Vegetable(object):
    def __repr__(self):
        return 'generic vegetable'


class Garlic(Vegetable):
    def __repr__(self):
        return 'garlic'


class Onion(Vegetable):
    def __repr__(self):
        return 'onion'


class Mushroom(Vegetable):
    def __repr__(self):
        return 'mushroom'


class RedPepper(Vegetable):
    def __repr__(self):
        return 'red pepper'


class PepperoniBase(object):
    def __repr__(self):
        return 'generic pepperoni'


class SlicedPepperoni(PepperoniBase):
    def __repr__(self):
        return 'sliced pepperoni'


class ChoppedPepperoni(PepperoniBase):
    def __repr__(self):
        return 'chopped pepperoni'


class Clam(object):
    def __repr__(self):
        return 'generic clam'


class FreshClam(Clam):
    def __repr__(self):
        return 'fresh clam'


class FrozenClam(Clam):
    def __repr__(self):
        return 'frozen clam'


class PizzaIngredientFactory(object):
    """
    AbstractFactory base for creating pizza ingredients
    """
    # implemented as an abstract factory because we want
    # families of products -- each subclass fills in the details
    def create_dough(self):
        """
        Create and return a Dough instance
        """
        raise NotImplementedError

    def create_sauce(self):
        """
        Create and return a Sauce instance
        """
        raise NotImplementedError

    def create_cheese(self):
        """
        Create and return a Cheese instance
        """
        raise NotImplementedError

    def create_veggies(self):
        """
        Create and return a list of Veggie instances
        """
        raise NotImplementedError

    def create_pepperoni(self):
        """
        Create and return a Pepperoni instance
        """
        raise NotImplementedError

    def create_clam(self):
        """
        Create and return a Clam instance
        """
        raise NotImplementedError



class EastCoastPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Factory for creating pizza ingredients on the east coast
    """
    def create_dough(self):
        """
        Create and return a Dough instance
        """
        return ThinCrustDough()

    def create_sauce(self):
        """
        Create and return a Sauce instance
        """
        return MarinaraSauce()

    def create_cheese(self):
        """
        Create and return a Cheese instance
        """
        return ReggianoCheese()

    def create_veggies(self):
        """
        Create and return a list of Veggie instances
        """
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        """
        Create and return a Pepperoni instance
        """
        return SlicedPepperoni()

    def create_clam(self):
        """
        Create and return a Clam instance
        """
        return FreshClam()


class MidwestPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Factory for creating pizza ingredients in the midwest
    """
    def create_dough(self):
        """
        Create and return a Dough instance
        """
        return ThickCrustDough()

    def create_sauce(self):
        """
        Create and return a Sauce instance
        """
        return PlumTomatoSauce()

    def create_cheese(self):
        """
        Create and return a Cheese instance
        """
        return MozzarellaCheese()

    def create_veggies(self):
        """
        Create and return a list of Veggie instances
        """
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        """
        Create and return a Pepperoni instance
        """
        return ChoppedPepperoni()

    def create_clam(self):
        """
        Create and return a Clam instance
        """
        return FrozenClam()


class Pizza(object):
    """
    Class for any kind of pizza
    """
    def __init__(self):
        self.name = "Generic Pizza"
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    def __repr__(self):
        ingredients = [self.dough, self.sauce, self.cheese,
                       self.pepperoni, self.clam] + [v for v in self.veggies]
        ingredients = [str(i) for i in ingredients if i is not None]

        return ", ".join(ingredients)


class PizzaFactoryBase(object):
    """
    Represents a base pizza factory.
    Subclasses need to decide what kind of pizzas
    to make using specific ingredients
    """
    _ingredient_factory = None

    def __init__(self):
        self.ingredient_factory = self._ingredient_factory()

    def _create_basic_pizza(self):
        pizza = Pizza()
        pizza.dough = self.ingredient_factory.create_dough()
        pizza.sauce = self.ingredient_factory.create_sauce()
        pizza.cheese = self.ingredient_factory.create_cheese()
        return pizza

    def create_cheese(self):
        pizza = self._create_basic_pizza()
        pizza.name = 'Cheese Pizza'
        return pizza

    def create_pepperoni(self):
        pizza = self._create_basic_pizza()
        pizza.pepperoni = self.ingredient_factory.create_pepperoni()
        pizza.name = 'Pepperoni Cheese'
        return pizza

    def create_veggie(self):
        pizza = self._create_basic_pizza()
        pizza.veggies = self.ingredient_factory.create_veggies()
        pizza.name = 'Veggie Pizza'
        return pizza

    def create_clam(self):
        pizza = self._create_basic_pizza()
        pizza.clam = self.ingredient_factory.create_clam()
        pizza.name = 'Clam Pizza'
        return pizza


class NewYorkPizzaFactory(PizzaFactoryBase):
    _ingredient_factory = EastCoastPizzaIngredientFactory


class ChicagoPizzaFactory(PizzaFactoryBase):
    _ingredient_factory = MidwestPizzaIngredientFactory


class PizzaStoreInterface(object):
    """
    Represents a base pizza store behavior.
    Implementers need to decide what kind of store they want to run
    """
    _name = "Pizza Store Interface"

    def order_pizza(self, pizza_type):
        """
        Order a pizza of 'pizza type'
        :param pizza_type: string
        :return: Pizza object
        """
        raise NotImplementedError(
            "Implementers must implement this method")


class FreshPizzaStoreBase(PizzaStoreInterface):
    """
    Implements the pizza store interface to provide
    fresh and tasty pizza
    """
    def __init__(self):
        self.pizza_factory = None

    def create_pizza(self, pizza_type):
        pizza_factory = self.pizza_factory()

        pizza = None
        if pizza_type == 'cheese':
            pizza = pizza_factory.create_cheese()
        elif pizza_type == 'pepperoni':
            pizza = pizza_factory.create_pepperoni()
        elif pizza_type == 'clam':
            pizza = pizza_factory.create_clam()
        elif pizza_type == 'veggie':
            pizza = pizza_factory.create_veggie()

        if pizza:
            print("-- preparing a {} with toppings: {} ".format(pizza.name, pizza))

        return pizza

    def bake_pizza(self, pizza):
        """
        Bake the pizza
        :param pizza: pizza object
        :return: baked pizza
        """
        print("-- bake {} at 350F for 25 min".format(pizza.name))

    def cut_pizza(self, pizza):
        """
        Cut the pizza
        :param pizza: pizza object
        :return: cut pizza
        """
        print("-- cut {} into triangles".format(pizza.name))

    def box_pizza(self, pizza):
        """
        Put the pizza in the box
        :param pizza: pizza object
        :return: boxed pizza
        """
        print("-- put {} in the pizza box".format(pizza.name))

    def order_pizza(self, pizza_type):
        """
        Order the type of pizza passed in
        :param pizza_type:
        :return: pizza
        """
        pizza = self.create_pizza(pizza_type)

        if pizza:
            self.bake_pizza(pizza)
            self.cut_pizza(pizza)
            self.box_pizza(pizza)
        else:
            print("Unable to make your pizza. We don't sell it.")

        return pizza


class FrozenPizzaStoreBase(PizzaStoreInterface):
    """
    Implements PizzaStoreInterface to provide a
    microwaved frozen pizza
    """
    def create_pizza(self):
        pizza = Pizza()
        pizza.name = "Totino's Pizza"
        pizza.dough = DoughBase()
        pizza.sauce = TomatoSauceBase()
        pizza.cheese = CheeseBase()
        pizza.pepperoni = ChoppedPepperoni()
        print("-- preparing a frozen {}".format(pizza.name))
        return pizza

    def microwave_pizza(self, pizza):
        """
        Warm up the pizza
        """
        print("-- microwave {} for 2 minutes".format(pizza.name))

    def order_pizza(self, pizza_type):
        """
        Order the only type of pizza we sell --
        a frozen cheese and cubed pepperoni pizza
        """
        pizza = None
        if pizza_type == 'pepperoni':
            pizza = self.create_pizza()
            self.microwave_pizza(pizza)
        else:
            print("Unable to make your pizza. We don't sell it.")

        return pizza


class NewYorkCityPizzaStore(FreshPizzaStoreBase):
    """
    A new york city pizza store
    """
    _name = 'New York Style'

    def __init__(self):
        super(NewYorkCityPizzaStore, self).__init__()
        self.pizza_factory = NewYorkPizzaFactory


class ChicagoPizzaStore(FreshPizzaStoreBase):
    """
    A Chicago city pizza store
    """
    _name = 'Chicago Style'

    def __init__(self):
        super(ChicagoPizzaStore, self).__init__()
        self.pizza_factory = ChicagoPizzaFactory

    def bake_pizza(self, pizza):
        print("-- bake {} at 350F for 45 min".format(pizza.name))

    def cut_pizza(self, pizza):
        print("-- cutting {} the pizza into squares".format(pizza.name))


class GasStationPizzaStore(FrozenPizzaStoreBase):
    """
    A gas station pizza store
    """
    _name = 'Chicago Style'


if __name__ == '__main__':
    # let's open some pizza stores
    nyc_store = NewYorkCityPizzaStore()
    print("I went to New York and got some pizza")
    pizza = nyc_store.order_pizza('cheese')
    pizza = nyc_store.order_pizza('clam')

    chicago_store = ChicagoPizzaStore()
    print("I went to Chicago and got some pizza")
    pizza = chicago_store.order_pizza('cheese')
    pizza = chicago_store.order_pizza('veggie')

    # and some gas station pizza
    gas_station = GasStationPizzaStore()
    print("I went to the Gas Station and ordered some pizza")
    pizza = gas_station.order_pizza('cheese')
    pizza = gas_station.order_pizza('pepperoni')
