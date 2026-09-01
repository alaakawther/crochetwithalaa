from utils.display import print_title, show_message
from utils.input_handler import get_choice
from features.tools import show_tool_info

TOOL_OPTIONS = {
    1: ("Yarn", "yarn"),
    2: ("Crochet Hooks", "hooks"),
    3: ("Scissors", "scissors"),
    4: ("Yarn Needle", "yarn_needle"),
    5: ("Measuring Tape", "measuring_tape"),
    6: ("Stitch Markers", "stitch_markers"),
    7: ("Crochet Abbreviations", "abbreviations"),
    8: ("Gauge", "gauge"),
    9: ("Tension", "tension"),
    10: ("Common Mistakes", "common_mistakes"),
    11: ("Important Crochet Tips", "tips"),
}


def show_tools_menu():
    while True:
        print_title("CROCHET TOOLS")

        for number, (label, _) in TOOL_OPTIONS.items():
            show_message(f"{number}. {label}")

        show_message("")
        show_message("0. Back to Main Menu")
        show_message("")

        choice = get_choice("Choose an option:", list(TOOL_OPTIONS) + [0])

        if choice == 0:
            return

        label, topic = TOOL_OPTIONS[choice]
        show_tool_info(topic, label)