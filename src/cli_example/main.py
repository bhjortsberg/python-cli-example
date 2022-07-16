import argparse

from cli_example.commands.list import list_command


def main():
    argp = argparse.ArgumentParser(description="Python CLI example")

    sargp = argp.add_subparsers(title="Example Commands", metavar="Command", help="Description", dest='command')
    argp.add_argument('--version', action='version', version='1.0')
    argp.add_argument('--dev', action='store_true', help='Developer variant')

    list_parser = sargp.add_parser('list', help='Example command')
    list_parser.add_argument('--long', action='store_true', help='Show extended list')
    list_parser.set_defaults(func=list_command)

    args = argp.parse_args()
    if args.command:
        args.func(args)


if __name__ == '__main__':
    main()