"""
Chapter Four -- Factory Pattern

SimpleFactory.
Encapsulate object creation, have one place to make modifications
when the implementation changes
"""


class PizzaBase(object):
    """
    Base pizza class. This pizza only has tomato sauce
    """
    def __init__(self):
        self.toppings = ['tomato sauce']

    def prepare(self):
        print('--making the pizza with {}'.format(self.toppings))

    def bake(self):
        print("--baking the pizza")

    def cut(self):
        print("--cutting the pizza")

    def box(self):
        print("--boxing the pizza")


class CheesePizza(PizzaBase):
    """
    Plain cheese pizza. Sauce and cheese.
    """
    def __init__(self):
        super(CheesePizza, self).__init__()
        self.toppings.append('cheese')


class PepperoniPizza(CheesePizza):
    """
    Pepperoni and cheese pizza
    """
    def __init__(self):
        super(PepperoniPizza, self).__init__()
        self.toppings.append('pepperoni')


class ClamPizza(CheesePizza):
    """
    Clam and cheese pizza
    """
    def __init__(self):
        super(ClamPizza, self).__init__()
        self.toppings.append('clam')


class VeggiePizza(CheesePizza):
    """
    Veggie and cheese pizza
    """
    def __init__(self):
        super(VeggiePizza, self).__init__()
        self.toppings.append('veggie')


class SimplePizzaFactoryV1(object):
    """
    Factory to create pizzas based on
    pizza type string
    """
    def create_pizza(self, pizza_type):
        """
        Create a new pizza based on pizza_type.
        Return None if type is unknown
        """
        pizza = None

        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza()
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()

        return pizza


class SimplePizzaFactory(object):
    """
    Factory to create pizzas based on
    pizza type string.
    """
    # I think this seems like a more 'python' way to
    # break out the list of contenders
    pizzas = {
        'cheese': CheesePizza,
        'pepperoni': PepperoniPizza,
        'clam': ClamPizza,
        'veggie': VeggiePizza
    }

    def create_pizza(self, pizza_type):
        """
        Create a new pizza based on pizza_type.
        Return None if type is unknown
        """
        pizza_class = self.pizzas.get(pizza_type)
        return pizza_class() if pizza_class else None


class PizzaStore(object):
    """
    Represents a pizza store
    """
    def __init__(self, pizza_factory):
        self.factory = pizza_factory

    def order_pizza(self, pizza_type):
        pizza = self.factory.create_pizza(pizza_type)
        if pizza:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
        else:
            print("--you ordered a pizza that we don't have yet!")
        return pizza


if __name__ == '__main__':
    # Let's open a little pizza store
    pizza_factory = SimplePizzaFactory()
    pizza_store = PizzaStore(pizza_factory)
    print("I want a cheese pizza")
    pizza_store.order_pizza('cheese')

    print("I want a pepperoni pizza")
    pizza_store.order_pizza('pepperoni')

    print("I want a clam pizza")
    pizza_store.order_pizza('clam')

    print("I want a veggie pizza")
    pizza_store.order_pizza('veggie')

    print("I want a sausage pizza")
    pizza_store.order_pizza('sausage')
