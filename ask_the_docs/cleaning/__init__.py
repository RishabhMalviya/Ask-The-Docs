from .utils import TextReplacer


class TextCleaner:
    def __init__(self):
        pass
    
    def clean(self, text: str) -> str:
        return text        


class RayDocsTextCleaner(TextCleaner):
    def __init__(self):
        super().__init__()
        self.newline_replacer = TextReplacer().replace_this(r"(\n)+").with_this(" ")
        self.hash_replacer = TextReplacer().replace_this(r"#").with_this(".")

    def clean(self, text: str) -> str:
        text = self.newline_replacer.run(text)
        text = self.hash_replacer.run(text)
        
        return text