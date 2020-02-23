"""Tests for CLI."""

from usbmonitor.usb import device_tree


def test_view_all_devices():
    dev_tree = device_tree.DeviceTree()
    assert dev_tree.get_connected_devices() == dict()
