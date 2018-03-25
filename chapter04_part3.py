"""
Chapter Four -- Factory Pattern

Ingredient Factories.
"""

class DoughBase(object):
    """
    Pizza Dough base class
    """
    pass


class ThinCrustDough(DoughBase):
    """
    Thin Crust Dough class
    """
    pass


class ThickCrustDough(DoughBase):
    """
    Thick Crust Dough class
    """
    pass


class TomatoSauceBase(object):
    pass


class MarinaraSauce(TomatoSauceBase):
    pass


class PlumTomatoSauce(TomatoSauceBase):
    pass


class CheeseBase(object):
    pass


class ReggianoCheese(CheeseBase):
    pass


class MozzarellaCheese(CheeseBase):
    pass


class Vegetable(object):
    pass


class Garlic(Vegetable):
    pass


class Onion(Vegetable):
    pass


class Mushroom(Vegetable):
    pass


class RedPepper(Vegetable):
    pass


class PepperoniBase(object):
    pass


class SlicedPepperoni(PepperoniBase):
    pass


class ChoppedPepperoni(PepperoniBase):
    pass


class Clam(object):
    pass


class FreshClam(Clam):
    pass


class FrozenClam(Clam):
    pass


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


class NewYorkPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Factory for creating New-York style pizza ingredients
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


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Factory for creating New-York style pizza ingredients
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


class PizzaBase(object):
    """
    Represents a base pizza. Subclasses can add implementation
    of specific ingredients
    """
    def __init__(self):
        self.name = "Generic Pizza"
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print("-- bake at 350F for 25 min")

    def cut(self):
        print("-- cut into triangles")

    def box(self):
        print("-- put in the pizza box")


class CheesePizza(PizzaBase):
    """
    A basic cheese pizza
    """
    def __init__(self, ingredient_factory):
        super(CheesePizza, self).__init__()
        self.name = 'Cheese Pizza'
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("-- preparing a {}".format(self.name))

        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class VeggiePizza(PizzaBase):
    """
    A basic cheese pizza
    """
    def __init__(self, ingredient_factory):
        super(VeggiePizza, self).__init__()
        self.name = 'Veggie Pizza'
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("-- preparing a {}".format(self.name))

        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()


class PepperoniPizza(PizzaBase):
    """
    A basic cheese pizza
    """
    def __init__(self, ingredient_factory):
        super(PepperoniPizza, self).__init__()
        self.name = 'Pepperoni Pizza'
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("-- preparing a {}".format(self.name))

        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class ClamPizza(PizzaBase):
    """
    A basic clam pizza
    """
    def __init__(self, ingredient_factory):
        super(ClamPizza, self).__init__()
        self.name = 'Clam Pizza'
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("-- preparing a {}".format(self.name))

        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class ChicagoStyleMixin(object):
    """
    Make the pizza a Chicago-style pizza. This mixin is meant to
    be used with Pizza classes
    """
    def bake(self):
        """
        Bake the pizza a little longer
        """
        print("-- bake at 350F for 45 min")

    def cut(self):
        """
        Cut the pizza into square slices!
        """
        print("-- cutting the pizza into squares")


class PizzaStoreBase(object):
    """
    Represents a base pizza store.
    Subclasses need to decide what kind of store they want to run
    """
    # pizza_type: pizza_class
    _pizzas = {
        'cheese': CheesePizza,
        'veggie': VeggiePizza,
        'clam': ClamPizza,
        'pepperoni': PepperoniPizza
    }

    _ingredient_factory = None

    _name = "Basic Style"

    @property
    def pizzas(self):
        """
        Pizzas should return the dictionary of
        pizza_type to pizza_class
        """
        if not self._pizzas:
            raise NotImplementedError(
                "Subclass must implement self._pizzas dictionary")

        return self._pizzas

    @property
    def ingredient_factory(self):
        if not self._ingredient_factory:
            raise NotImplementedError(
                "Subclass must implement ingredient_factory property"
            )

        return self._ingredient_factory

    @property
    def name(self):
        return self._name

    def create_pizza(self, pizza_type):
        """
        Factory method for creating pizzas. A concrete
        subclass has to pick an ingredient factory where
        there ingredients will come from.
        :param pizza_type: string of pizza type
        :return: new pizza object
        """
        # the factory method is an abstract interface for
        # creating ONE product
        ingredient_factory = self.ingredient_factory()
        pizza_class = self.pizzas.get(pizza_type)

        pizza = None
        if pizza_class:
            pizza = pizza_class(ingredient_factory)
            pizza.name = "{} {}".format(self.name, pizza.name)
        return pizza

    def order_pizza(self, pizza_type):
        """
        Order the type of pizza passed in
        :param pizza_type:
        :return: pizza
        """
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NewYorkCityPizzaStore(PizzaStoreBase):
    """
    A new york city pizza store
    """
    _pizzas = {
        'cheese': CheesePizza,
        'veggie': VeggiePizza,
        'clam': ClamPizza,
        'pepperoni': PepperoniPizza
    }

    _ingredient_factory = NewYorkPizzaIngredientFactory
    _name = 'New York Style'

class ChicagoPizzaStore(PizzaStoreBase):
    """
    A Chicago city pizza store
    """
    _pizzas = {
        'cheese': CheesePizza,
        'veggie': VeggiePizza,
        'clam': ClamPizza,
        'pepperoni': PepperoniPizza
    }

    _ingredient_factory = ChicagoPizzaIngredientFactory
    _name = 'Chicago Style'

if __name__ == '__main__':
    # let's open some pizza stores
    nyc_store = NewYorkCityPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = nyc_store.order_pizza('cheese')
    print("I went to NYC and got a pizza: {}".format(pizza.name))

    pizza = chicago_store.order_pizza('cheese')
    print("I went to Chicago and got a pizza: {}".format(pizza.name))

    # what about a nasty clam pizza
    pizza = nyc_store.order_pizza('clam')
    print("I went to NYC and got a pizza: {}".format(pizza.name))

    pizza = chicago_store.order_pizza('clam')
    print("I went to Chicago and got a pizza: {}".format(pizza.name))
