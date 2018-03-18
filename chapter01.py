"""
Chapter One -- Intro to Design Patterns
"""

# -----------------
# Flying interfaces
# -----------------
class FlyBehaviorMixinBase(object):
    def fly(self):
        raise NotImplementedError


class FlyWithWingsMixin(FlyBehaviorMixinBase):
    def fly(self):
        print("I'm flying!")


class FlyNoWayMixin(FlyBehaviorMixinBase):
    def fly(self):
        print("I can't fly")


class FlyRocketPoweredMixin(FlyBehaviorMixinBase):
    def fly(self):
        print("I'm flying in a rocket!")


# -------------------
# Quacking interfaces
# -------------------
class QuackBehaviorMixinBase(object):
    def quack(self):
        raise NotImplementedError


class QuackMixin(QuackBehaviorMixinBase):
    def quack(self):
        print("quack!")


class MuteQuackMixin(QuackBehaviorMixinBase):
    def quack(self):
        print('<< silence >>')


class SqueakMixin(QuackBehaviorMixinBase):
    def quack(self):
        print('squeak!')


# -----------------
# Ducks
# -----------------
class DuckABC(object):
    """
    Abstract base class representing a generic duck
    """
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks can swim!")


class MallardDuck(DuckABC):
    def __init__(self):
        self.quack_behavior = QuackMixin()
        self.fly_behavior = FlyWithWingsMixin()


class ModelDuck(DuckABC):
    def __init__(self):
        self.fly_behavior = FlyNoWayMixin()
        self.quack_behavior = QuackMixin()

# -----------------
# Ducks, version 2
# -----------------
# This version feels more like regular python to me. :)
class Duck(object):
    """
    Base class representing a generic duck
    """
    def __init__(self, quack_behavior_cls, fly_behavior_cls):
        self._fly_behavior = fly_behavior_cls()
        self._quack_behavior = quack_behavior_cls()

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, new_behavior_cls):
        self._fly_behavior = new_behavior_cls()

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, new_behavior_cls):
        self._quack_behavior = new_behavior_cls()

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks can swim!")


# if I only have a couple of ducks, just make them
mallard = Duck(QuackMixin, FlyWithWingsMixin)
model_duck = Duck(QuackMixin, FlyNoWayMixin)


# but, suppose we have a lot of ducks
class DuckFactory(object):
    """
    Factory to make ducks!
    """
    def create_mallard(self):
        return Duck(QuackMixin, FlyWithWingsMixin)

    def create_model_duck(self):
        return Duck(QuackMixin, FlyNoWayMixin)


if __name__ == '__main__':
    print("Let's make a mallard duck!")
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.swim()

    print("Let's make a model duck")
    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPoweredMixin())
    model.perform_fly()

    print("Let's make some factory ducks")
    duck_factory = DuckFactory()
    factory_mallard = duck_factory.create_mallard()
    factory_mallard.perform_fly()

    factory_model_duck = duck_factory.create_model_duck()
    factory_model_duck.perform_fly()
    factory_model_duck.fly_behavior = FlyRocketPoweredMixin
    factory_model_duck.perform_fly()
