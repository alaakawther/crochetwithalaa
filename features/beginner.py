from utils.display import print_title, show_message
from utils.input_handler import get_choice
from features.tools import show_tool_info
from menus.patterns_menu import show_patterns_menu

BEGINNER_TOOLS = {
    1: ("Yarn", "yarn"),
    2: ("Crochet Hooks", "hooks"),
    3: ("Scissors", "scissors"),
    4: ("Yarn Needle", "yarn_needle"),
    5: ("Measuring Tape", "measuring_tape"),
    6: ("Stitch Markers", "stitch_markers"),
    7: ("Other Useful Accessories", "accessories"),
}


def show_beginner_path():
    while True:
        print_title("STARTING FROM ZERO")
        show_message("First, let's learn the tools")
        show_message("and materials we need to crochet! 🧶")
        show_message("")

        for number, (label, _) in BEGINNER_TOOLS.items():
            show_message(f"{number}. {label}")

        show_message("")
        show_message("0. I'm ready for my first project")
        show_message("")

        choice = get_choice("Choose an option:", list(BEGINNER_TOOLS) + [0])

        if choice == 0:
            show_patterns_menu(category="beginner")
            return

        label, topic = BEGINNER_TOOLS[choice]
        show_tool_info(topic, label)
