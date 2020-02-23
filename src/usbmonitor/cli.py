"""Command line interface module."""

import click


@click.group()
def cli() -> None:
    """USB port monitoring tool."""
    pass


@cli.command()
def view_devices() -> None:
    """View USB device tree."""
    print("here be a dev tree: ^")