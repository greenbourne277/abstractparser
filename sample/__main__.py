import sys
import xmlparser


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print(xmlparser.get_answer())
    print("This is the main routine.")
    print("It should do something interesting.")

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do. Return values are exit codes.


if __name__ == "__main__":
    sys.exit(main())

