"""Interface to the system USB Device Tree."""

import usb.core
import usb.util
import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\\Users\\Rob\\.local\\bin\\libusb-1.0.dll")


class DeviceTree:
    """USB Device Tree."""

    def __init__(self):
        """Initialise the object."""
        self.all_devices = usb.core.find(find_all=True, backend=backend)

    def __len__(self):
        return len(list(self.all_devices))

    def iter_devices(self):
        """Return information about the connected devices."""
        for device in self.all_devices:
            try:
                yield device
            except (usb.core.USBError, NotImplementedError):
                continue
