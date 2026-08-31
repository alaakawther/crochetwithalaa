def get_choice(prompt, valid_options):
    while True:
        print(prompt)
        raw = input("> ").strip()

        try:
            choice = int(raw)
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            print()
            continue

        if choice not in valid_options:
            print("❌ Invalid option. Please choose one of the options shown above.")
            print()
            continue

        return choice


def get_text(prompt):
    print(prompt)
    return input("> ").strip()
