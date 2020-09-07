import logging
from typing import *

import toml

log = logging.getLogger(__name__)
CompareReport = Dict[str, Union[str, List[str], "Missing"]]


class NuConfig:
    def __init__(self, file: "TextIO"):
        self.data = toml.load(file)

    def __getitem__(self, item):
        return self.data.__getitem__(item)

    def cmplog(self, other) -> bool:
        """Compare two different NuConfig objects and log information about which keys are missing or invalid.
        Returns a bool, which is false if there was something to report and true otherwise."""
        compare_report: CompareReport = self.compare(other)
        self.__cmplog_log(compare_report)
        return compare_report == {}

    @staticmethod
    def __cmplog_log(compare_report: CompareReport, root: str = "") -> None:
        """The recursive portion of :meth:`.cmplog`."""
        for item in compare_report.get("__missing__", []):
            log.error(f"Missing key: {root}{item}")

        for item in compare_report.get("__invalid__", []):
            log.error(f"Key has an invalid type: {root}{item}")

        for key, value in compare_report.items():
            if key == "__missing__" or key == "__invalid__":
                continue
            NuConfig.__cmplog_log(value, root=f"{root}{key}.")

    def compare(self, other: "NuConfig") -> CompareReport:
        """Compare two different NuConfig objects and return a dictionary of the keys missing in the other."""
        if not isinstance(other, NuConfig):
            raise TypeError("You can only compare two NuConfig objects.")
        return self.__compare_recurse(self.data, other.data)

    @staticmethod
    def __compare_miss(self: dict) -> CompareReport:
        """Mark all keys of a dict as missing."""
        missing = []

        result = {}

        for key, value in self.items():
            missing.append(key)
            if isinstance(value, dict):
                result[key] = NuConfig.__compare_miss(value)

        if missing:
            result["__missing__"] = missing

        return result

    @staticmethod
    def __compare_recurse(self: dict, other: dict) -> CompareReport:
        """The recursive portion of :meth:`.compare`."""
        invalid = []
        missing = []

        result = {}

        for key, value in self.items():
            try:
                other_value = other[key]
            except KeyError:
                missing.append(key)
                if isinstance(value, dict):
                    result[key] = NuConfig.__compare_miss(value)
            else:
                if type(value) != type(other_value):
                    invalid.append(key)
                    if isinstance(value, dict):
                        result[key] = NuConfig.__compare_miss(value)
                elif isinstance(value, dict):
                    recursive_result = NuConfig.__compare_recurse(value, other_value)
                    if recursive_result != {}:
                        result[key] = recursive_result

        if invalid:
            result["__invalid__"] = invalid
        if missing:
            result["__missing__"] = missing

        return result
