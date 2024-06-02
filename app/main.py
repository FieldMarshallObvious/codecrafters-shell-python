import sys


allowed_commands = []

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input()

        if user_input not in allowed_commands:
            sys.stdout.write(f"{user_input}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
