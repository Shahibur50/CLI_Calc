"""
CLI_Calc
Version: 1.0.0

Copyright (c) 2022 Shahibur Rahaman
Licensed under MIT License.
"""

import time
import shutil


def main():
    program_info()
    while True:
        print("\nEval> ", end="")
        try:
            expression = str(input().lower())
            if expression != "":
                if expression == "license":
                    program_license()
                elif expression == "exit":
                    program_exit()
                elif expression == "help":
                    program_help()
                else:
                    print(f"    > {expression} = {eval(expression)}")
        except EOFError:
            print("ERROR! EOF detected")
            program_exit()
        except KeyboardInterrupt:
            print("ERROR! Keyboard interrupt detected")
            program_exit()
        except SyntaxError:
            print("ERROR! Syntax error")
            continue
        except NameError:
            print("ERROR! Not a valid operation")
            continue


def program_help():
    print(
        """
CLI_Calc v1.0.0

Usage:

Eval> 15 + 5 [This is an example of user-input]
    > 15 + 5 = 20 [This the output that the program will generate]
""",
        end="",
    )


def program_info():
    print(
        r"""
Welcome to CLI_Calc
Version: 1.0.0

Copyright (c) 2022 Shahibur Rahaman

For more info and updates visit:
https://github.com/Shahibur50/CLI_Calc

Type "license", or "help" for more information.
Type "exit" to exit the program.
""",
        end="",
    )


def program_license():
    with open("LICENSE", "r") as main_license:
        lines = main_license.readlines()
    prompt = "Hit Return for more, or q (and Return) to " "quit: "
    line_count = len(lines)
    is_break = False
    i = 0
    while line_count > 0 and (is_break == False):
        height = shutil.get_terminal_size()[1]
        for _ in range(height - 1):
            if line_count == 0:
                break
            print(lines[i].rstrip("\n"))
            line_count -= 1
            i += 1

        while True:
            value = input(prompt).lower()
            if value == "":
                break
            elif value == "q":
                is_break = True
                break
            else:
                continue


def program_exit():
    print("Exiting...")
    time.sleep(1)
    exit()


if __name__ == "__main__":
    main()
