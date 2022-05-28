from setuptools import setup, find_packages
import pathlib


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding="utf8")

setup(
	name="ActivityDiscord",
	version="1.0.0",
	author="MagMigo and Roskiy",
	description="Use discord activities with your bot!",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/Forks-translates-nextcord-with-Roskiy/ActivityDiscord",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)
