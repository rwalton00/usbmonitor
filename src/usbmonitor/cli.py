"""Command line interface module."""

import click

from usbmonitor.usb import device_tree


@click.group()
def cli() -> None:
    """USB port monitoring tool."""
    pass


@cli.command()
def view_devices() -> None:
    """View USB device tree."""
    output_strs = []
    for d in device_tree.DeviceTree().iter_devices():
        try:
            output_strs.append(str(d))
        except Exception:
            continue
    print(f"Number of detected devices: {len(device_tree.DeviceTree())}\n")
    print(*output_strs, sep="\n\n")
