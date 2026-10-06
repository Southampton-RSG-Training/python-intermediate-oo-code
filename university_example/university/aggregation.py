"""
Defines the base class for all the different types of research staff,
and the paper class that they all use.
"""
from university import Person


class Publication:
    """
    Papers written by Academics
    """
    def __init__(self, title, text):
        self.title = title
        self.text = text


class Academic(Person):
    """
    An abstract class representing anyone who writes papers.
    """
    def __init__(self, name, office):
        """
        We use the 'superclass' (parent class) initialiser via `super()`,
        and then say we have a list of publications too.
        """
        super().__init__(name, office)
        self.publications = []

    def write_paper(self, title, text):
        """
        We create a new paper, and add it to our list of publications.
        We also return it, so any collaborators can record it too.
        """
        paper = Publication(title, text)
        self.publications.append(paper)
        return paper

    def coauthor_paper(self, paper):
        """
        We add the paper we're given to our list of publications.
        """
        self.publications.append(paper)


# ======== CALLOUT ========
# Why do we declare `publications = []` in the init, not on the class itself, e.g.
#
#   class Academic(Person):
#       publications = []
#
# Because then it'd belong to the *class itself*.
# All instances of the Academic class would share the same list of publications.
# =========================
