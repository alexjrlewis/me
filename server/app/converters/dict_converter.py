"""Module containing the DictConverter class."""

from typing import Any, Dict
from werkzeug.routing import BaseConverter


class DictConverter(BaseConverter):
    """Converter for supplying a dictionary as a URL, and vice versa.

    Attributes:
        DELIMITER: The delimiter to join key/values in the dictionary.
        KEY_VALUE_DELIMITER: The delimiter seperating the keys and values.
        WHITESPACE_DELIMITER: The delimiter used to fill whitespaces.
    """

    DELIMITER = "&"
    KEY_VALUE_DELIMITER = "="
    WHITESPACE_DELIMITER = "+"

    def to_python(self, value: str):
        """Converts and returns a URL string into a dictionary.

        Args:
            value: The URL string containing the dictionary.
        Returns:
            A dictionary generated from the URL supplied.
        """
        data = {}
        for kv in value.split(self.DELIMITER):
            key, value = kv.split(self.KEY_VALUE_DELIMITER)
            data[key] = value.replace(self.WHITESPACE_DELIMITER, " ")
        return data

    def to_url(self, values: Dict[str, str]):
        """Converts and returns a dictionary into a URL string.

        Args:
            values: The dictionary to convert into a URL string.
        Returns:
            A URL string containing the dictionary supplied.
        """
        url = []
        for key, value in values.items():
            v = value.replace(" ", self.WHITESPACE_DELIMITER)
            url.append(f"{key}{self.KEY_VALUE_DELIMITER}{v}")
        return self.DELIMITER.join(url)
