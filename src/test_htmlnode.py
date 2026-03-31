import unittest

from htmlnode import HTMLnode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node2 = HTMLnode(props={"hey":"hello", "Chicken":"Egg"})
        #print(node2.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    #parent node tests > 
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild2_node = LeafNode("b", "a child")

        child2_node = ParentNode("a", [grandchild2_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node, child2_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><a><b>a child</b></a></div>",
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")



if __name__ == "__main__":
    unittest.main()