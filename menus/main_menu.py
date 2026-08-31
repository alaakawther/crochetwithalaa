from utils.display import print_title, show_message
from utils.input_handler import get_choice
from menus.learn_menu import show_learn_menu
from menus.patterns_menu import show_patterns_menu
from menus.tools_menu import show_tools_menu


def show_main_menu():
    while True:
        print_title("🧶 CROCHET WITH ALAA")
        show_message("Welcome, beginner! 🌸")
        show_message("")
        show_message("1. Learn Crochet")
        show_message("2. Crochet Patterns")
        show_message("3. Crochet Tools")
        show_message("4. Exit")
        show_message("")

        choice = get_choice("Choose an option:", [1, 2, 3, 4])

        if choice == 1:
            show_learn_menu()
        elif choice == 2:
            show_patterns_menu()
        elif choice == 3:
            show_tools_menu()
        else:
            show_message("")
            show_message("Happy crocheting! 🧶 Goodbye!")
            return
