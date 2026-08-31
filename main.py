from menus.main_menu import show_main_menu


def main():
    try:
        show_main_menu()
    except (KeyboardInterrupt, EOFError):
        print("\n\nHappy crocheting! 🧶 Goodbye!")


if __name__ == "__main__":
    main()
