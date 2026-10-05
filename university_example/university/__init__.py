"""
An __init__ file makes a directory importable in Python - like a package, but only locally.
"""

class Person:
    """
    A person employed at a university.
    This is an abstract class - you shouldn't create plain People!
    """
    def __init__(self, name, office):
        self.name = name
        self.office = office

    def __str__(self):
        """
        We're also going to define how a 'person' should look when you put them in a string.
        Custom classes don't have a default, so you just get "<Person instance @ memory address>" otherwise.
        """
        return f"{self.name}"


class Admin(Person):
    """
    An admin has no extra details beyond the base Person.
    But we make them a class so we can check if someone is an admin or not easily.
    """
    pass
