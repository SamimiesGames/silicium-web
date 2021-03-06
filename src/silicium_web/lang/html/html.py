from silicium import AbstractScene, Component
from silicium.utils import require
from .builder import HTMLBuilder

BOILER_PLATE_HTML = require(__file__, "templates", "index.html")


class BasicHTML(Component):
    @property
    def code(self) -> str:
        return BOILER_PLATE_HTML


class HTML(AbstractScene):
    def __init__(self):
        html_builder = HTMLBuilder()

        self.builder = html_builder

        self.builder.builder_component = BasicHTML(self, add=False)

    def run(self) -> None:
        print(f"Run scene: {self.__class__.__name__}")

        page = self.builder.build()

        with open("index.html", "w") as fh:
            fh.write(page)

        print(f"Run success: {self.__class__.__name__}")

