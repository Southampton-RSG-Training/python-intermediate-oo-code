"""
Defines a range of different classes that are 'polymorphic' with Academic.
I.e., any of these ones can be used whenever an Academic is expected,
but the functionality may differ.
"""
from university.aggregation import Academic, Publication


class PhDStudent(Academic):
    """
    A real class representing PhD students.

    Not really polymorphic - it doesn't override any methods, it just adds a new one.
    """
    def graduate(self):
        """
        Congratulates them, and also publishes their thesis.
        """
        thesis = Publication(f"{self.name}'s Thesis", "The OED defines...")
        self.publications.append(thesis)
        print(f"Hooray, {self.name} has graduated!")


class ResearchSoftwareEngineer(Academic):
    """
    A real class representing RSEs.

    This class uses polymorphism to override the Academic's `coauthor_paper` method.
    To remind anyone co-authoring with them they should cite the software!
    """
    def coauthor_paper(self, paper):
        """
        Replacement version of the method, that can still access that original using `super()`.
        """
        print("Don't forget to cite the software!")
        super().coauthor_paper(paper)
