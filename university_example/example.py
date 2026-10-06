"""
Example that runs through creating an instance of each class,
using their functionality, and then showing that it worked.
"""
from university import Person, Admin
from university.aggregation import Academic
from university.composition import LecturerComposed, LibrarianComposed
from university.inheritance import InstructorMixin, LecturerInherited, LibrarianInherited
from university.polymorphism import PhDStudent, ResearchSoftwareEngineer


# -----------------------------------------------
# First, we'll declare a bunch of different staff
# -----------------------------------------------
alice = Admin("Alice Archer", "B21/1003")
bob = LibrarianComposed("Bob Baker", "B10/3004")
carol = LibrarianInherited("Carol Cooper", "B12/2004")
dave = PhDStudent("Dave Driver", "B100/1012")
erin = LecturerComposed("Erin Earl", "B13/1031")
frank = LecturerInherited("Frank Fisher", "B26/2012")
grace = ResearchSoftwareEngineer("Grace Gardener", "B23/4002")

# We use type hinting to tell our IDE what type of variable something is.
# In this case, we tell it this is a list of subclasses of Person.
# Otherwise, it'll throw a bunch of unnecessary warnings!
staff_members: list[Person] = [ alice, bob, carol, dave, erin, frank, grace ]

# --------------------------------------------
# Let's see where everyone works (Inheritance)
# --------------------------------------------
print("\n--- Locating Staff ---")
for staff in staff_members:
    # Works for everyone, even though they're all different classes
    print(f"{staff} is in {staff.office}")

# --------------------------------------------------------------
# Now, let's get some research done (Polymorphism & Aggregation)
# --------------------------------------------------------------
print("\n--- Writing Papers ---")
erin.write_paper(
    "Teapot Studies With X-Ray Diffraction",
    "Teapots have long..."
)
shared_paper = dave.write_paper(
    "Teapot Modelling Via FEM",
    "Most teapots are..."
)
erin.coauthor_paper(shared_paper)
grace.coauthor_paper(shared_paper)  # You should see a different result from this!

# --------------------------------------
# Time to do some teaching (Composition)
# --------------------------------------
bob.instructor.teach_course("Citation For Students")
bob.instructor.teach_course("Citation Against Students")
erin.instructor.teach_course("Furthest Maths")

# --------------------------------------
# Time to do some teaching (Inheritance)
# --------------------------------------
carol.teach_course("Library Etiquette")
frank.teach_course("History of Etiquette")
frank.teach_course("Etiquette for History")

# -----------------------
# What has everyone done?
# -----------------------
print("\n--- Research & Teaching Outputs ---")
for staff in staff_members:
    # Are they an academic who can write papers, and who has written any?
    if isinstance(staff, Academic) and staff.publications:
        print(f"{staff} wrote {[paper.title for paper in staff.publications]}")

    # Do they have the ability to instruct? (via inheritance)
    if isinstance(staff, InstructorMixin) and staff.courses:
        print(f"{staff} taught {staff.courses}")

    # Do they have the ability to instruct? (via composition)
    if (instructor := getattr(staff, 'instructor', None)) and instructor.courses:
        print(f"{staff} taught {instructor.courses}")
        # This bit is less 'pythonic' - the checks are more complicated to do.
        # We use the 'walrus operator' :=, which sets the value of instructor,
        # then checks if it's not falsy (i.e. 0, None, False).

# --------------------
# Finally, Dave's done
# ---------------------
dave.graduate()
