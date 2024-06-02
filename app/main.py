import sys
from typing import Dict


allowed_commands = [ "exit", "echo" ]


def match_command(command, params) -> Dict:
    return_object = {}
    match command:
        case 'exit':
            if len(params) > 0:
                return_object = {'exit': int(params[0])}
        case 'echo':
            content = " ".join(params)
            sys.stdout.write(f"{content}\n")
            sys.stdout.flush()
    return return_object



def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        raw = input()
        user_input = raw.split(" ")
        command = user_input[0]
        params = user_input[1:]
        if command not in allowed_commands:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
            continue
        

        command_return = match_command(command, params)

        if 'exit' in command_return:
            sys.exit(command_return['exit'])


if __name__ == "__main__":
    main()
