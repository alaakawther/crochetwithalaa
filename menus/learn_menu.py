from utils.display import print_title, show_message
from utils.input_handler import get_choice
from menus.patterns_menu import show_patterns_menu


def show_learn_menu():
    while True:
        print_title("LEARN CROCHET")
        show_message("What is your crochet experience?")
        show_message("")
        show_message("1. I know nothing about crochet.")
        show_message("   I want to learn from 0.")
        show_message("")
        show_message("2. I know some things about crochet,")
        show_message("   but I've never made anything.")
        show_message("")
        show_message("3. I've made some small crochet projects.")
        show_message("")
        show_message("4. I've crocheted some big projects.")
        show_message("")
        show_message("0. Back to main menu")
        show_message("")

        choice = get_choice("Choose an option:", [0, 1, 2, 3, 4])

        if choice in (2, 3):
            show_patterns_menu(category="beginner")
        elif choice == 4:
            show_patterns_menu(category="advanced")
        else:
            return
