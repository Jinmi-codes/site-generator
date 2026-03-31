import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()