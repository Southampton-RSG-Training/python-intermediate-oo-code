"""
Defines a range of different classes that are all 'polymorphic' with Academic.
I.e., any of these ones can be used whenever an Academic is expected.
"""
from university.aggregation import Academic


class PhDStudent(Academic):
    """
    A real class representing PhD students.
    """
    def graduate(self):
        print(f"Hooray, {self.name} has graduated!")


class ResearchSoftwareEngineer(Academic):
    """
    A real class representing RSEs.

    This class uses polymorphism to override the Academic's `coauthor_paper` method.
    """
    def coauthor_paper(self, paper):
        """
        Replacement version of the method, that can still access that original using `super()`.
        """
        print("Don't forget to cite the software!")
        super().coauthor_paper(paper)
