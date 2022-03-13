"""Module containing the ListConverter class."""

from typing import Any, List
from werkzeug.routing import BaseConverter


class ListConverter(BaseConverter):
    """Converter for supplying a list as a URL, and vice versa.

    Attributes:
        DELIMITER: The delimiter to join elements within a list by.
    """

    DELIMITER = "+"

    def to_python(self, value: str):
        """Converts and returns a string URL into a list object.

        Args:
            value: The list as a string with elements joined by the delimiter.
        Returns:
            A list containing the elements of the string.
        """
        return value.split(self.DELIMITER)

    def to_url(self, values: List[Any]):
        """Converts and returns a list object into a URL string.

        Args:
            values: A list of any objects.
        Returns:
            A string representation of a list with elements joined by the
            delimiter.
        """
        return self.DELIMITER.join([f"{v}" for v in values])
