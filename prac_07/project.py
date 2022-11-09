from prac_07.project_management import Project
from operator import attrgetter
import datetime

MENU = """(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit"""

FILENAME = 'projects.txt'


def main():
    # project, projects = load_projects()
    # FILENAME = input("Filename:  ")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            project, projects = load_projects()
        # elif choice == "S":
        elif choice == "D":
            display_projects(project, projects)
        # elif choice == "F":
        #
        # elif choice == "A":
        #
        # elif choice == "U":
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects():
    projects = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
            print(project)
    return project, projects


def display_projects(project, projects):
    projects.sort(key=attrgetter('priority'))  # Sort in ascending order of year
    print("Incomplete projects:")
    for project in projects:
        print(project)
        if project.is_complete():
            print("Completed projects:")
            print(project)

#Ask lindsay for help on Friday
main()
