from textnode import TextNode, TextType


def main():
    text = "Some sample text"
    node = TextNode(text, TextType.BOLD, None)
    print(node)


if __name__ == "__main__":
    main()
