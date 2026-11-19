import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_properties(self):
        text = "Sample text"
        text_type = TextType.IMAGE
        url = "12345"
        node = TextNode(text, text_type, url)
        self.assertEqual(node.text, text)
        self.assertEqual(node.text_type, text_type)
        self.assertEqual(node.url, url)

    def test_text_noneq(self):
        node = TextNode("Sample 1 text", TextType.BOLD)
        node2 = TextNode("Sample 2 text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_type_noneq(self):
        node = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Sample text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()
