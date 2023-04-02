import re


class TextReplacer:
    def __init__(self, to_replace=None, replace_with=None):
        self._to_replace = to_replace
        self._replace_with = replace_with

    def replace_this(self, to_replace):
        self._to_replace = re.compile(to_replace)

        return self

    def with_this(self, replace_with):
        self._replace_with = replace_with

        return self

    def run(self, text: str) -> str:
        text_with_replacement = None

        if callable(self._replace_with):
            text_with_replacement = re.sub(self._to_replace, self._replace_with, text)
        else:
            text_with_replacement = re.sub(self._to_replace, lambda x: self._replace_with, text)

        return text_with_replacement
