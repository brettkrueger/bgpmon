from setuptools import setup,find_packages

setup(
    name = "bgpmon",
    version = "0.1a6",
	install_requires = ["suds-jurko"],
	author = "ZKSnarky",
	author_email = "therealmustymouse@gmail.com",
	description = ("A simple Python wrapper for the BGPMon SOAP API."),
	license = "GNU",
	keywords = "bgpmon python wrapper",
	url = "https://github.com/zksnarky/bgpmon/bgpmon/",
	packages=find_packages(exclude=['docs','tests']),
	classifiers=[
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 2.7"
    ],
)
