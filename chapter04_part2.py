"""
Chapter Four -- Factory Pattern

Factory Method Pattern.
Define an interface for creating an object, but let the subclasses
decide which class to instantiate. Defer instantiation to subclasses.
"""

# notes from the text:
# dependency inversion:
# -- high and low-level components each depend on (and interact through) abstractions
# -- this is the 'D' in SOLID

# program to abstractions:
# -- no references to concrete classes (use a factory)
# -- no class inheritance from concrete class (depending on implementation)
# -- no methods should override a method in the base class

# these techniques let us encapsulate change


class PizzaBase(object):
    """
    Base pizza class. This pizza only has tomato sauce
    """
    def __init__(self):
        self.name = 'generic pizza'
        self.dough = 'generic dough'
        self.sauce = 'tomato sauce'
        self.toppings = [self.sauce]

    def prepare(self):
        print('-- making the pizza with {}'.format(self.toppings))

    def bake(self):
        print("-- baking the pizza")

    def cut(self):
        print("-- cutting the pizza")

    def box(self):
        print("-- boxing the pizza")


class CheesePizza(PizzaBase):
    """
    Plain cheese pizza. Sauce and cheese.
    """
    def __init__(self):
        super(CheesePizza, self).__init__()
        self.name = 'cheese pizza'
        self.toppings.append('cheese')


class PepperoniPizza(CheesePizza):
    """
    Pepperoni and cheese pizza
    """
    def __init__(self):
        super(PepperoniPizza, self).__init__()
        self.name = 'pepperoni pizza'
        self.toppings.append('pepperoni')


class ClamPizza(CheesePizza):
    """
    Clam and cheese pizza
    """
    def __init__(self):
        super(ClamPizza, self).__init__()
        self.name = 'clam pizza'
        self.toppings.append('clam')


class VeggiePizza(CheesePizza):
    """
    Veggie and cheese pizza
    """
    def __init__(self):
        super(VeggiePizza, self).__init__()
        self.name = 'veggie pizza'
        self.toppings.append('veggie')


class NewYorkStylePizzaMixin(object):
    """
    Make the Pizza class a NY-style pizza. This mixin is meant to
    be used with Pizza classes
    """
    def __init__(self):
        """
        Set the NY-style parameters for this pizza
        """
        super(NewYorkStylePizzaMixin, self).__init__()
        self.name = 'New York Style ' + self.name
        self.dough = 'thin crust'
        self.sauce = 'marinara sauce'

        # add the special grated cheese
        self.toppings.append("grated reggiano cheese")


class ChicagoStylePizzaMixin(object):
    """
    Make the pizza a Chicago-style pizza. This mixin is meant to
    be used with Pizza classes
    """
    def __init__(self):
        """
        Set the Chicago-style parameters for this pizza
        """
        super(ChicagoStylePizzaMixin, self).__init__()
        self.name = 'Chicago Style ' + self.name
        self.dough = 'deep dish crust'
        self.sauce = 'plum tomato sauce'

        # always add extra cheese
        self.toppings.append("extra mozzarella cheese")

    def cut(self):
        """
        Cut the pizza into square slices!
        """
        print("-- cutting the pizza into squares")


class NewYorkStyleCheesePizza(NewYorkStylePizzaMixin, CheesePizza):
    pass


class NewYorkStylePepperoniPizza(NewYorkStylePizzaMixin, PepperoniPizza):
    pass


class NewYorkStyleClamPizza(NewYorkStylePizzaMixin, ClamPizza):
    pass


class NewYorkStyleVeggiePizza(NewYorkStylePizzaMixin, VeggiePizza):
    pass


class ChicagoStyleCheesePizza(ChicagoStylePizzaMixin, CheesePizza):
    pass


class ChicagoStylePepperoniPizza(ChicagoStylePizzaMixin, PepperoniPizza):
    pass


class ChicagoStyleClamPizza(ChicagoStylePizzaMixin, ClamPizza):
    pass


class ChicagoStyleVeggiePizza(ChicagoStylePizzaMixin, VeggiePizza):
    pass


# now the factory method rolls into the pizza store classes
# they will implement their own 'create_pizza' methods
class PizzaStoreBase(object):
    """
    Represents a base pizza store.
    Subclasses need to decide what kind of store they want to run
    """
    # pizza_type: pizza_class
    _pizzas = {}

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

    def create_pizza(self, pizza_type):
        """
        Factory method for creating pizzas
        :param pizza_type: string of pizza type
        :return: new pizza object
        """
        pizza_class = self.pizzas.get(pizza_type)
        return pizza_class() if pizza_class else None

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


class NewYorkPizzaStore(PizzaStoreBase):
    """
    NYC Style Pizza Store
    """
    _pizzas = {
        'cheese': NewYorkStyleCheesePizza,
        'veggie': NewYorkStyleVeggiePizza,
        'clam': NewYorkStyleClamPizza,
        'pepperoni': NewYorkStylePepperoniPizza
    }


class ChicagoPizzaStore(PizzaStoreBase):
    """
    Chicago Style Pizza Store
    """
    _pizzas = {
        'cheese': ChicagoStyleCheesePizza,
        'veggie': ChicagoStyleVeggiePizza,
        'clam': ChicagoStyleClamPizza,
        'pepperoni': ChicagoStylePepperoniPizza
    }


if __name__ == '__main__':
    # let's open some pizza stores
    nyc_store = NewYorkPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = nyc_store.order_pizza('cheese')
    print("I went to NYC and got a pizza: {}".format(pizza.name))

    pizza = chicago_store.order_pizza('cheese')
    print("I went to Chicago and got a pizza: {}".format(pizza.name))
