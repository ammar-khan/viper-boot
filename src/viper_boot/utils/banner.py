"""Project Banner."""
from pygments import console


class Banner:
    """
    Banner for the project.

    Create project banner using online tool:
    @see: https://fsymbols.com/generators/tarty/
    """

    def __init__(self) -> None:
        """Initialise the class object."""
        pass  # pylint: disable=unnecessary-pass

    @staticmethod
    def paste() -> None:
        """Print the banner."""
        print(
            console.colorize(
                "blue",
                """

                ██╗░░░██╗██╗██████╗░███████╗██████╗░  ██████╗░░█████╗░░█████╗░████████╗
                ██║░░░██║██║██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
                ╚██╗░██╔╝██║██████╔╝█████╗░░██████╔╝  ██████╦╝██║░░██║██║░░██║░░░██║░░░
                ░╚████╔╝░██║██╔═══╝░██╔══╝░░██╔══██╗  ██╔══██╗██║░░██║██║░░██║░░░██║░░░
                ░░╚██╔╝░░██║██║░░░░░███████╗██║░░██║  ██████╦╝╚█████╔╝╚█████╔╝░░░██║░░░
                ░░░╚═╝░░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░░╚════╝░░░░╚═╝░░░
                """  # noqa: E501  # pylint: disable=line-too-long
            )
        )
