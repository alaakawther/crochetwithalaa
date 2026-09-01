from data.projects import PROJECTS
from utils.display import print_title, show_message, pause


def show_project(project_id):
    project = PROJECTS.get(project_id)

    if project is None:
        print_title("PROJECT NOT FOUND")
        show_message("Sorry, that project does not exist.")
        pause()
        return

    print_title(f"{project['name'].upper()}")
    show_message(f"You selected: {project['name']}")
    show_message("")
    show_message("! Copy this link into YouTube!")
    show_message("")
    show_message(project["url"])
    pause()
