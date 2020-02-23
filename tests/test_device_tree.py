"""Tests for CLI."""

from usbmonitor.usb import device_tree
from typing import Iterator


def test_iter_devices():
    dev_tree = device_tree.DeviceTree()
    assert isinstance(dev_tree.iter_devices(), Iterator)


def test_len_devices():
    dev_tree = device_tree.DeviceTree()
    assert len(dev_tree) >= 0
