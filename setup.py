"""A command line utility for routing and monitoring MIDI ports."""

import pathlib
import lzma
import urllib

from setuptools import find_packages, setup
from distutils.command.build import build

here = pathlib.Path(__file__).absolute().parent


class FetchLibusbBuilder(build):
    def run(self):
        urllib.urlretrieve("https://github.com/libusb/libusb/releases/download/v1.0.23/libusb-1.0.23.7z", "libusb-1.0.23.7z")
        with lzma.open("libusb-1.0.23.7z") as libusblzma:
            pathlib.Path("libusb-1.0.23").write_bytes(lzma.decompress(libusblzma.read()))


def run():
    urllib.request.urlretrieve("https://github.com/libusb/libusb/releases/download/v1.0.23/libusb-1.0.23.7z", "libusb-1.0.23.7z")
    pathlib.Path("libusb-1.0.23").mkdir(exist_ok=True)
    Archive("libusb-1.0.23.7z").extractall("libusb-1.0.23")



# Get the long description from the README file
with open(str(pathlib.Path(here, "README.md")), encoding="utf-8") as f:
    long_description = f.read()

PROJECT_NAME = "usbmonitor"
DESCRIPTION = __doc__
INSTALL_REQUIRES = ["click", "pyusb"]
EXTRAS_REQUIRE = {
    "tests": ["pytest", "coverage[toml]>=5.0.2"],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + ["pre-commit"]
EXTRAS_REQUIRE["azure-pipelines"] = EXTRAS_REQUIRE["tests"] + ["pytest-azurepipelines"]

setup(
    name=PROJECT_NAME,
    version="1.0.0",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rwalton00/usbmonitor",
    author="Rob Walton",
    author_email="rwalton00@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="usb monitor diagnostics",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    entry_points={"console_scripts": ["usbmonitor=usbmonitor.main:main"]},
)
