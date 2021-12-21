from setuptools import find_packages, setup

NAME = "silicium-web"
VERSION = "0.1.2"
URL = "https://github.com/SamimiesGames/silicium"

AUTHOR = "Samimies"
DESCRIPTION = "Silicium-web is a massive cookiecutter template library for building UI on the web with Python."


setup(
    name=NAME,
    version=VERSION,
    url=URL,
    author=AUTHOR,
    license="MIT",
    description=DESCRIPTION,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"], where="src"),
    package_dir={"": "src"}
)

