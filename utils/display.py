LINE_WIDTH = 32


def print_separator():
    print("=" * LINE_WIDTH)


def print_title(text):
    print()
    print_separator()
    print(text.center(LINE_WIDTH))
    print_separator()
    print()


def show_message(text):
    print(text)


def pause():
    input("\nPress ENTER to go back...")
