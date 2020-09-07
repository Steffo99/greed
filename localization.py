import importlib
import json
import logging
import types
from typing import *

log = logging.getLogger(__name__)


class IgnoreDict(dict):
    """A dictionary that if passed to format_map, ignores the missing replacement fields."""

    def __missing__(self, key):
        return "{" + key + "}"


class Localization:
    def __init__(self, language: str, *, fallback: str, replacements: Dict[str, str] = None):
        log.debug(f"Creating localization for {language}")
        self.language: str = language
        log.debug(f"Importing strings.{language}")
        self.module: types.ModuleType = importlib.import_module(f"strings.{language}")
        if language != fallback:
            log.debug(f"Importing strings.{fallback} as fallback")
            self.fallback_language: str = fallback
            self.fallback_module = importlib.import_module(f"strings.{fallback}") if fallback else None
        else:
            log.debug("Language is the same as the default, not importing any fallback")
            self.fallback_language = None
            self.fallback_module = None
        self.replacements: Dict[str, str] = replacements if replacements else {}

    def get(self, key: str, **kwargs) -> str:
        try:
            log.debug(f"Getting localized string with key {key}")
            string = self.module.__getattribute__(key)
        except AttributeError:
            if self.fallback_module:
                log.warning(f"Missing localized string with key {key}, using default")
                string = self.fallback_module.__getattribute__(key)
            else:
                raise
        assert isinstance(string, str)
        formatter = IgnoreDict(**self.replacements, **kwargs)
        return string.format_map(formatter)

    def boolmoji(self, boolean: bool) -> str:
        return self.get("emoji_yes") if boolean else self.get("emoji_no")


def create_json_localization_file_from_strings(language: str):
    module: types.ModuleType = importlib.import_module(f"strings.{language}")
    raw = module.__dict__
    clean = {}
    for key in raw:
        if not (key.startswith("__") and key.endswith("__")):
            clean[key] = raw[key]
    with open(f"locale/{language}.json", "w") as file:
        json.dump(clean, file)
