from utils.display import print_title, show_message
from utils.input_handler import get_choice
from data.projects import PROJECTS

TITLES = {
    None: "🧵 CROCHET PATTERNS",
    "beginner": "🧵 BEGINNER PATTERNS",
    "advanced": "🧵 ADVANCED PATTERNS",
}


def show_patterns_menu(category=None):
    while True:
        print_title(TITLES.get(category, "🧵 CROCHET PATTERNS"))

        available = []
        for project_id, project in PROJECTS.items():
            if category is None or project["category"] == category:
                show_message(f"{project_id}. {project['name']}")
                available.append(project_id)

        show_message("")
        show_message("0. ✍️ Make Your Own Tutorial")
        show_message("99. Back")
        show_message("")

        choice = get_choice("Choose an option:", available + [0, 99])

        if choice == 99:
            return
