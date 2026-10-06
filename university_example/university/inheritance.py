"""
This file shows how to add functionality by inheriting from multiple classes.
"""
from university import Admin
from university.aggregation import Academic


class InstructorMixin:
    """
    Represents the ability to teach a course.

    This version is designed to work with multiple inheritance.
    In Python, we call classes that exist to add functionality by multiple inheritance 'Mixins'.
    """
    def __init__(self, *args, **kwargs):
        """
        The initialiser uses `*args` and `**kwargs` to forward all the arguments,
        whatever they are, up the chain of parent classes.
        """
        super().__init__(*args, **kwargs)
        self.courses = []

    def teach_course(self, title):
        """
        Just sticks the title we've been given onto our list of courses declared in the initialiser.
        """
        self.courses.append(title)


class LecturerInherited(InstructorMixin, Academic):
    """
    A real class representing academics who teach.

    This version uses multiple inheritance to make them an instructor.
    It's easier, but can have compatibility issues.
    For example, only one `__init__` will be called - the first one in the chain.
    You have to explicitly call up the chain!
    """
    def __init__(self, *args, **kwargs):
        """
        The initialiser uses `*args` and `**kwargs` to forward all the arguments,
        whatever they are, to the other parent class.
        """
        super().__init__(*args, **kwargs)


class LibrarianInherited(InstructorMixin, Admin):
    """
    A librarian is an admin who can teach.
    """
    def __init__(self, *args, **kwargs):
        """
        The initialiser uses `*args` and `**kwargs` to forward all the arguments,
        whatever they are, to the other parent class.
        """
        super().__init__(*args, **kwargs)
