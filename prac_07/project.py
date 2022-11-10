from prac_07.project_management import Project
from operator import attrgetter
from datetime import date, datetime

MENU = """(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit"""

FILENAME = 'projects.txt'


def main():
    project, projects = load_projects()
    # FILENAME = input("Filename:  ")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            project, projects = load_projects()
        # elif choice == "S":
        #     save_projects(projects, FILENAME)
        elif choice == "D":
            print_incomplete_projects(projects)
            print_completed_projects(projects)
        elif choice == "F":
            filter_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_projects(project, projects)
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


def print_incomplete_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(project)


def print_completed_projects(projects):
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print(project)


def update_projects(project, projects):
    index = 0
    for project in projects:
        print(index, project)
        index += 1
    is_valid_input = False
    while not is_valid_input:
        choice = int(input("Project choice: "))
        if choice < 1:
            print("Number must be >=1")
        else:
            print(projects[choice])
            is_valid_input = True
        new_percentage = int(input("New Percentage: "))
        projects[choice].is_complete = new_percentage
    return projects, project


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate: $"))
    percent_complete = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def filter_date(projects):
    chosen_date = input("Show projects that start after date (dd/mm/yy): ")
    chosen_date = datetime.strptime(chosen_date, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > chosen_date:
            print(project)


main()
