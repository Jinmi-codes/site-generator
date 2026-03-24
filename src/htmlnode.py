

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
		if self.props is None or len(self.props) <= 1:
			return ""
		result = []
		for key in props:
			result.append(f"{key}=\"{props[key]}\"")
		return " ".join(result)
	def _repr_(self):
		return f"HTMLnode({self.tag}, {self.value}, {self.children}, {self.props}) "



class LeafNode(HTMLnode):
	def __init__(self,tag, value, props=None):
		self.tag = None if not tag else tag
		super().__init__(value, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("node has no value!")
		if self.tag is None:
			return f"{value}"
		return f"<{tag} {self.props_to_html()}>{value}</{tag}>"
	def __repr__(self):
		return  f"LeafNode({self.tag}, {self.value}, {self.props}) "
