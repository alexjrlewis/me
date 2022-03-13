"""Module containing the BoolConverter class."""

from werkzeug.routing import BaseConverter


class BoolConverter(BaseConverter):
    """Converter for supplying a boolean as a URL, and vice versa.

    Attribute:
        VALUES: An array of lowercase strings that equals a truthful boolean.
    """

    VALUES = ["true", "1", "t", "y", "yes", "yeah", "yup", "certainly", "uh-huh"]

    def to_python(self, value: str) -> bool:
        """Converts and returns a string URL into a boolean.

        Args:
            value: The URL string representation of a boolean.
        Returns:
            A boolean value from a string.
        """
        return f"{value}".lower() in self.VALUES

    def to_url(self, value: bool) -> str:
        """Converts and returns a boolean into a URL string.

        Args:
            value: A boolean value.
        Returns:
            A URL string representation of a boolean.
        """
        return f"{value}"
