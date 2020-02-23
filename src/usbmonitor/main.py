"""usbmonitor is a command line tool allowing the user to monitor USB traffic."""

from usbmonitor import cli


def main() -> int:
    """Main entry point."""
    cli.cli()
    return 0
