"""
This file shows how to
"""
from university import Admin
from university.aggregation import Academic


class InstructorComposed:
    """
    Represents the ability to teach a course.

    This version is designed to be added to an object using composition.
    """
    def __init__(self):
        self.courses = []

    def teach_course(self, title):
        self.courses.append(title)


class LibrarianComposed(Admin):
    """
    A librarian is an Admin who can teach.

    This version adds the instructor ability using composition.
    This is the way most other languages do it.
    """
    def __init__(self, name, office):
        super().__init__(name, office)
        self.instructor = InstructorComposed()


class LecturerComposed(Academic):
    """
    A real subclass of the virtual Academic class, for academics who teach.

    Structured as above.
    """
    def __init__(self, name, office):
        super().__init__(name, office)
        self.instructor = InstructorComposed()
