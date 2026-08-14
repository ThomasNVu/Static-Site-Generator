from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_node: list[str] = old_node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i, section in enumerate(split_node):
            if section == "":
                continue
            if i % 2 == 0:
                text_node = TextNode(section, TextType.TEXT)
            else:
                text_node = TextNode(section, text_type)
            new_nodes.append(text_node)
    return new_nodes
