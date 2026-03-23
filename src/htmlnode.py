

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



