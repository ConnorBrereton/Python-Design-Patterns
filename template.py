from abc import ABC, abstractmethod

class AbstractClass(ABC):

    """Implement the prototypes."""
    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.base_operation3()
        self.hook2()


    """Implement the classes."""
    def base_operation1(self):
        print("Base operation 1")

    def base_operation2(self):
        print("Base operation 2")

    def base_operation3(self):
        print("Base operation 3")


    """Implement subclasses."""
    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass


    """Hooks that are used as extensions."""
    def hook1(self):
        pass

    def hook2(self):
        pass


class ConcreteClass(AbstractClass):

    """Implement all abstract operations of
    the base class."""
    def required_operation1(self):
        print("Concrete class 1")

    def required_operation2(self):
        print("Concrete class 2")

class ConcreteClassWithHook(AbstractClass):

    """Implement all abstract operations of
    the base class while overwriting the hook
    class."""
    def required_operation1(self):
        print("Concrete required operation 1.")

    def required_operation2(self):
        print("Concrete required operation 2.")

    def hook1(self):
        print("Concrete class hook overwritten.")

def client_code(AbstractClass):
    """Call the template method which calls
    all of the other methods in the order of
    the prototyping."""
    AbstractClass.template_method()

if __name__ == "__main__":
    print("Execute concrete class 1")
    client_code(ConcreteClass())
    print("")

    print("Executing concrete class 2")
    client_code(ConcreteClassWithHook())