class Component:  # component class

    def __init__(self):  # component class constructor
        print('Component Class object created...')

    def component_method(self) -> None:  # component class method
        print('Component Class Method called...')


class Composite:  # composite class

    def __init__(self):  # composite class constructor
        self.component = Component()  # creating component class object
        print('Composite Class object created...')

    def composite_method(self) -> None:  # composite class method
        print('Composite Class Method called...')
        self.component.component_method()  # calling component class method

composite = Composite()  # creating object of composite class

composite.composite_method()  # calling composite class method