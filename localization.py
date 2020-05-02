import importlib


class IgnoreDict(dict):
    """A dictionary that if passed to format_map, ignores the missing replacement fields."""
    def __missing__(self, key):
        return "{" + key + "}"


class Localization:
    def __init__(self, language, replacements=None):
        self.language = language
        self.module = importlib.import_module("strings." + language)
        self.replacements = replacements if replacements else {}

    @staticmethod
    def is_supported(language) -> bool:
        try:
            importlib.import_module("strings." + language)
        except ImportError:
            return False
        else:
            return True

    def get(self, key, **kwargs) -> str:
        string = self.module.__getattribute__(key)
        assert isinstance(string, str)
        formatter = IgnoreDict(**self.replacements, **kwargs)
        return string.format_map(formatter)
