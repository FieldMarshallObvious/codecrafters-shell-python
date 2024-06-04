import sys
import os
from typing import Dict, List, Set


allowed_commands = [ "exit", "echo", "type"]


def match_command(command: str, params: List[str], binaries: Dict[str, str]) -> Dict:
    return_object = {}
    match command:
        case 'exit':
            if len(params) > 0:
                return_object = {'exit': int(params[0])}
        case 'echo':
            content = " ".join(params)
            sys.stdout.write(f"{content}\n")
            sys.stdout.flush()
        case 'type':
            content = " ".join(params)
            if content in allowed_commands:
                sys.stdout.write(f"{content} is a shell builtin\n")
                sys.stdout.flush()
                return return_object
            if content in binaries:
                sys.stdout.write(f"{content} is {binaries[content]}\n")
                sys.stdout.flush()
                return return_object

            sys.stdout.write(f"{content} not found\n")
            sys.stdout.flush()
                
    return return_object

def getBinaries(path: str) -> Dict:
    binaries = {}
    for root, _, files in os.walk(path, topdown=True):
        for file in files:
            binaries[file] = os.path.join(root, file) 
    return binaries


def main():
    path_envs = os.getenv("PATH", "/bin:/usr/bin")
    path_envs = path_envs.split(":")
    binaries = {}
    for path in path_envs:
        binaries.update(getBinaries(path)) 

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
        

        command_return = match_command(command, params, binaries)

        if 'exit' in command_return:
            sys.exit(command_return['exit'])


if __name__ == "__main__":
    main()
