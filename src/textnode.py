from enum import Enum

class TextType(Enum):
	PLAIN = "plain text"
	BOLD = "bold text"
	ITALIC = "italic text"
	CODE = "code text"
	LINK = "links"
	IMAGE = "images"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url if self.text_type is TextType.LINK else None

	def __eq__(self, other):
		if not self.text == other.text:
			return False
		if not self.text_type is other.text_type:
			return False
		if not self.url == other.url:
			return False
		return True
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"