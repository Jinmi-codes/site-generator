import unittest

from htmlnode import HTMLnode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node2 = HTMLnode(props={"hey":"hello", "Chicken":"Egg"})
        print(node2.props_to_html())

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


if __name__ == "__main__":
    unittest.main()