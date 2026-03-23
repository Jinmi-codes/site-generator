import unittest

from htmlnode import HTMLnode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node2 = HTMLnode(props={"hey":"hello", "Chicken":"Egg"})
        print(node2.props_to_html())


if __name__ == "__main__":
    unittest.main()