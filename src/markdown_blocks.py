def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_block = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_block.append(block)
    return filtered_block

