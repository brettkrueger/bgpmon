from setuptools import setup,find_packages

setup(
    name = "bgpmon",
    version = "0.1a2",
	install_requires = ["suds-jurko"],
    author = "Brett Krueger",
    author_email = "brett@jinsku.com",
    description = ("A simple Python wrapper for the BGPMon SOAP API."),
    license = "GNU",
    keywords = "bgpmon python wrapper",
    url = "https://github.com/brettkrueger/bgpmon/",
	packages=find_packages(exclude=['docs','tests']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities :: Internet :: Indexing/Search",
        "License :: OSI Approved :: GNU License",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 2.7"
    ],
)
