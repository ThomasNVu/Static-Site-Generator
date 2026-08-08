import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_props(self):
        node = LeafNode(
            "a",
            "Visit Boot.dev",
            {"href": "https://www.boot.dev"},
        )

        self.assertEqual(
            node.to_html(),
            '<a href="https://www.boot.dev">Visit Boot.dev</a>',
        )

    def test_to_html_without_tag(self):
        node = LeafNode(None, "Plain text")

        self.assertEqual(node.to_html(), "Plain text")

    def test_to_html_without_value(self):
        node = LeafNode("p", None)  # type: ignore

        with self.assertRaises(ValueError):
            node.to_html()

    def test_has_no_children(self):
        node = LeafNode("p", "Hello")

        self.assertIsNone(node.children)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_value_raises(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
