import json
from pathlib import Path

from utils.display import print_title, show_message, pause
from utils.input_handler import get_text

TUTORIALS_PATH = Path(__file__).resolve().parent.parent / "data" / "tutorials.json"


def load_tutorials():
    if not TUTORIALS_PATH.exists():
        return []

    try:
        with open(TUTORIALS_PATH, "r", encoding="utf-8") as file:
            tutorials = json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

    if not isinstance(tutorials, list):
        return []

    return tutorials


def save_tutorial(name, text):
    tutorials = load_tutorials()
    tutorials.append({"name": name, "tutorial": text})

    with open(TUTORIALS_PATH, "w", encoding="utf-8") as file:
        json.dump(tutorials, file, indent=4, ensure_ascii=False)


def create_tutorial():
    print_title("CREATE YOUR TUTORIAL")

    name = get_text("Tutorial name:")
    if not name:
        show_message("")
        show_message("A tutorial needs a name. Nothing was saved.")
        pause()
        return

    show_message("")
    text = get_text("Type your tutorial below:")
    if not text:
        show_message("")
        show_message("A tutorial needs some text. Nothing was saved.")
        pause()
        return

    save_tutorial(name, text)
    show_message("")
    show_message("Tutorial saved successfully! 🧶")
    pause()
