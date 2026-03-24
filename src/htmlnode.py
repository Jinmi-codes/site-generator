

class HTMLnode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	def to_html(self):
		raise NotimplementedError('	Pass')

	def props_to_html(self):
		props = self.props
		if self.props is None or len(self.props) < 1:
			return ""
		result = []
		for key in props:
			result.append(f" {key}=\"{props[key]}\"")
		return "".join(result)
	def _repr_(self):
		return f"HTMLnode({self.tag}, {self.value}, {self.children}, {self.props}) "



class LeafNode(HTMLnode):
	def __init__(self,tag, value, props=None):
		super().__init__(tag,value,props=props)

	def to_html(self):
		if self.value is None:
			raise ValueError("node has no value!")
		if self.tag is None:
			return f"{self.value}"
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
	def __repr__(self):
		return  f"LeafNode({self.tag}, {self.value}, {self.props}) "


class ParentNode(HTMLnode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, children=children, props=props)

	def to_html(self):
		if self.tag is None:
			raise ValueError("No tag found!")
		if self.children is None:
			raise ValueError("Parent has no children!")
		result = ""

		for child in self.children:
			result += child.to_html()

		return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
