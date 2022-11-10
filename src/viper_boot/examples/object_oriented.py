"""Object-Oriented Python."""


class ExceptionHandler(RuntimeError):
    """Handle custom exception in the code base."""


class BaseClass:
    """A Base Class to demonstrate object-oriented implementation in Python."""

    # Class properties
    property_one: int

    # Class constructor with method overloading
    def __init__(
        self,
        attribute_one: int = 0,
        attribute_two: int = 0,
        attribute_three: int = 0,
    ) -> None:
        """
        Set class properties to default values.

        Parameters:
            attribute_one (int): attribute one
            attribute_two (int): attribute two
            attribute_three (int): attribute three
        """
        self.attribute_one = attribute_one or 2016
        self.attribute_two = attribute_two or 20
        self.attribute_three = attribute_three or 100
        BaseClass.property_one += 1  # pylint: disable=no-member

    # Instance takes self as the first argument.
    # They are also called Object or regular method.
    #
    # Instance method (Public)
    def instance_method_one(self) -> int:
        """
        Increase the attribute_three by 20.

        Returns:
            BaseClass.attribute_three + 20
        """
        return self.__sum(self.attribute_three, 20)

    # Instance method (Public)
    def instance_method_two(self) -> int:
        """
        Decrease the attribute_three by 50.

        Returns:
            BaseClass.attribute_three - 50
        """
        return self.__subtract(self.attribute_three, 50)

    # Instance method (Private)
    @staticmethod
    def __sum(operand_one: int, operand_two: int = 0) -> int:
        """
        Add two numbers.

        Parameters:
            operand_one (int): operand one
            operand_two (int): operand two

        Returns:
            operand_one + operand_two
        """
        return operand_one + operand_two

    # Instance method (Private)
    @staticmethod
    def __subtract(operand_one: int, operand_two: int = 0) -> int:
        """
        Subtract two numbers.

        Parameters:
            operand_one (int): operand one
            operand_two (int): operand two

        Returns:
            operand_one - operand_two
        """
        return operand_one - operand_two

    # Class takes cls as the first argument. cls refers to class.
    # To access a class variable within a method,
    # we use the @classmethod decorator, and pass the class to the method
    #
    # Class method (Public)
    @classmethod
    def class_method(cls) -> int:
        """
        Get total number of property_one.

        Returns:
            cls.property_one
        """
        return cls.property_one  # pylint: disable=no-member

    # Class method (Public)
    @classmethod
    def print_docstring(cls) -> None:
        """
        Print docstring of the class.

        We can also use the help() function to read the docstrings
        associated with various objects.

        Example: help(ClassName)

        """
        print(cls.__doc__)

    # Static doesn"t take anything as the first argument.
    # It has a limited use because
    # Neither you can access to the properties of an instance (object) of a
    # class NOR you can access to the attributes of the class.
    # The only usage is it can be called without an object.
    # It is mainly useful for creating helper or
    # utility functions like validation
    #
    # Static method (Public)
    @staticmethod
    def static_method(value: int) -> bool:
        """
        Check if there is a value.

        Parameters:
            value (int): number of instances

        Returns:
            value > 0
        """
        check: bool = value > 0
        return check

    # String representation of Class instance
    # This method should be at the bottom of the class ideally
    def __str__(self) -> str:
        """
        __str__ is used to produce readable representation of the object.

        Without __str__
            print(class_instance)
                __main__.BaseClass object at 0x0000019ECCCA05F8

        With __str__
            print(class_instance)
                Attribute 1: 0
                Attribute 2: 0
                Attribute 3: 0
                Property 1: 0

        Returns:
            class object string

        """
        # pylint: disable=no-member
        return (
            f"Attribute 1: {self.attribute_one}\n"
            f"Attribute 2: {self.attribute_two}\n"
            f"Attribute 3: {self.attribute_three}\n"
            f"Property 1: {self.property_one}"
        )


class SimpleInheritClass(BaseClass):
    """A Simple Child Class inherits Base Class."""

    pass  # pylint: disable=unnecessary-pass


class InheritClassWithExtraAttribute(BaseClass):
    """A Child Class inherits Base Class and add extra attribute."""

    # Class constructor with method overloading
    def __init__(self, extra_attribute: int = 0) -> None:
        """
        Set base class and self properties to default values.

        Parameters:
            extra_attribute (int): extra attribute

        """
        # Execute base class constructor
        super().__init__()
        self.extra_attribute = extra_attribute or 999


class InheritMultipleClasses(
    InheritClassWithExtraAttribute, SimpleInheritClass
):
    """
    A Child Class inherits multiple classes.

    Method Resolution Order (MRO) is the order in which methods should be
    inherited in the presence of multiple inheritance. You can view
    the MRO by using the __mro__ attribute.

    Example: _class_instance.__mro__
    """

    # Class constructor
    def __init__(self) -> None:
        """Set base class and self properties to default values."""
        # Execute base class constructor
        super().__init__()


class PolymorphClass(BaseClass):
    """
    A Child Class to demonstrate Method Overriding and Method Overloading.

    Polymorphism means the ability to take various forms.
    It is an important concept when you deal with child and parent class.
    Polymorphism in python is applied through
    method overriding and method overloading.
    """

    # Class attributes
    _check: bool

    # Method overriding (Base class method)
    def instance_method_one(self) -> int:
        """
        Increase the attribute_three by 50.

        Method overriding allows us to have a method in the child class with
        the same name as in the parent class but the definition of the
        child class method is different from parent class method.

        Returns:
            attribute_three + 50
        """
        return self.attribute_three + 50

    # Method overloading
    def method_overload(self, value: int = 0) -> bool:
        """
        Check the value and return a boolean value.

        It allows you to define a function or method with flexibility
        so that you can call it with or without arguments.

        Parameters:
            value (int): value

        Returns:
            value > 0
        """
        self._check = value > 0
        return self._check


class DataEncapsulationClass(BaseClass):
    """
    A Child Class to demonstrate Data Encapsulation.

    Encapsulation of Data means restricting access to methods and variables.
    This can prevent the data from being modified by accident (mistake).

    -   When we use two underscores "__" before attribute name,
        it makes attribute not accessible outside class.
        It becomes private attribute which means you can"t read and write to
        those attributes except inside the class.
    -   When you don"t use underscore before attribute,
        it is a public attribute which can be
        accessed inside or outside a class.
    """

    # Class properties
    _private_property: str

    # Class constructor with method overloading
    def __init__(self, value: str = "") -> None:
        """
        Set base class and self properties to default values.

        Parameters:
            value (str): __private_attribute argument

        """
        # Execute base class constructor
        super().__init__()
        self._private_attribute = value
        self._private_property = value


class GetterSetterDeleterClass:
    """Class to demonstrate Getter, Setter & Deleter."""

    # Class properties
    _private_property: str

    # Class constructor with method overloading
    def __init__(
        self,
        attribute_one: str = "",
        attribute_two: str = "",
        attribute_three: str = "",
    ) -> None:
        """
        Set properties to default values.

        Parameters:
            attribute_one (str): attribute one
            attribute_two (str): attribute two
            attribute_three (str): attribute three

        """
        self._attribute_one = attribute_one
        self._attribute_two = attribute_two
        self._attribute_three = attribute_three

    # Getters, Setters & Deleter
    @property
    def attribute_one(self) -> str:
        """
        Getter method for attribute.

        Returns:
            attribute value
        """
        return self._attribute_one

    @attribute_one.setter
    def attribute_one(self, value: str) -> None:
        """
        Setter method for attribute.

        Parameters:
            value (str): value to set
        """
        self._attribute_one = value
        self._private_property = self._attribute_one + self._attribute_two

    @attribute_one.deleter
    def attribute_one(self) -> None:
        """Deleter method for attribute."""  # noqa
        del self._attribute_one

    @property
    def attribute_two(self) -> str:
        """
        Getter method for attribute.

        Returns:
            attribute value
        """
        return self._attribute_one

    @attribute_two.setter
    def attribute_two(self, value: str) -> None:
        """
        Setter method for attribute.

        Parameters:
            value (str): value to set
        """
        self._attribute_two = value
        self._private_property = self._attribute_one + self._attribute_two

    @attribute_two.deleter
    def attribute_two(self) -> None:
        """Deleter method for attribute."""  # noqa
        del self._attribute_two

    @property
    def attribute_three(self) -> str:
        """
        Getter method for attribute.

        Returns:
            attribute value
        """
        return self._attribute_one

    @attribute_three.setter
    def attribute_three(self, value: str) -> None:
        """
        Setter method for attribute.

        Parameters:
            value (str): value to set
        """
        self._attribute_three = value
        self._private_property = self._attribute_one + self._attribute_two

    @attribute_three.deleter
    def attribute_three(self) -> None:
        """Deleter method for attribute."""  # noqa
        del self._attribute_three


class SingletonClass:
    """
    A Class demonstrate singleton pattern.

    Inspired by Gang of Four and The Flyweight patterns
    """

    _instance = None

    # Singleton class constructor
    # Note: mypy does not (yet) support the special behavior of __new__()
    # using type: ignore
    def __new__(cls):  # type: ignore
        """
        Singleton object demonstration.

        Returns:
            (Any): singleton object
        """
        if cls._instance is None:
            print("Creating the object")
            cls._instance = super().__new__(cls)
            # Put any initialization here.
        return cls._instance
