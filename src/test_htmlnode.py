import unittest

from htmlnode import HTMLnode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node2 = HTMLnode(props={"hey":"hello", "Chicken":"Egg"})
        print(node2.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()