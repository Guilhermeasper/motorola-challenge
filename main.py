from screen.screen import Screen
import sys

USAGE = f'Usage: python {sys.argv[0]} -input="<path/to/input/file>" -output="<path/to/output/file>"'


def argparse():
    """Parse the command line arguments and returns input and output paths"""

    input_path = ""
    output_path = ""
    for arg in sys.argv[1:]:
        if arg.startswith("-input"):
            input_path = arg.split("=")[1]
        elif arg.startswith("-output"):
            output_path = arg.split("=")[1]
        else:
            raise SystemExit(USAGE)
    return input_path, output_path


def main():
    screen = Screen()
    input_path, output_path = argparse()

    try:
        input_file = open(input_path, "r")
        output_file = open(output_path, "w+")
    except FileNotFoundError:
        raise SystemExit(USAGE)

    for item in input_file.read().split("\n"):
        output_file.write(screen.change_state(item) + "\n")

    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()
