import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is a test text", None, None)
        test_string = "HTLMNode(p, This is a test text, None, None)"
        self.assertEqual(str(node), test_string)

    def test_prop(self):
        node = HTMLNode("p", "This is a test text", None, {"href": "https://www.google.com", "target": "_blank"})
        #print(node.props_to_html())
        test_string = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), test_string)

    def test_leaf(self):
        node = LeafNode("p", "This is a test text", None)
        test_string = "<p>This is a test text</p>"
        self.assertEqual(node.to_html(), test_string)

    def test_leaf_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        test_string = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), test_string)

        

if __name__ == "__main__":
    unittest.main()