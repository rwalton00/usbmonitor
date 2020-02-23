import usb.core
import usb.util


class DeviceTree:
    def __init__(self):
        self.all_devices = usb.core.find(find_all=True)

    def get_connected_devices(self):
        return usb.core.show_devices(verbose=True)
