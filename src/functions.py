import re
from textnode import TextType, TextNode



def split_nodes_delimiter(old_nodes, delimiter, text_type):
	result = []
	for node in old_nodes:
		if not node.text_type is TextType.TEXT:
			result.append(node) 
		else:
			parts = node.text.split(delimiter)
			if len(parts) % 2 == 0:
				raise Exception("Markdown not valid! delimiter not closed.")
			for i in range(0, len(parts)):
				if parts[i]:
					result.append(TextNode(parts[i], TextType.TEXT if ( ( (i+1) % 2) >= 1) else text_type ))
			
	return result

def extract_markdown_images(text):
    result = []
    pattern = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)")
    matches = pattern.finditer(text)
    for match in matches:
        result.append((match.group(1), match.group(2)))
    return result

def extract_markdown_links(text):
    result = []
    pattern = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")
    matches = pattern.finditer(text)
    for match in matches:
        result.append((match.group(1), match.group(2)))
    return result
    
def split_nodes_images(old_nodes):
    result = []
    for node in old_nodes:
        match node.text_type:
            case TextType.TEXT:
                if node.text:
                    images = extract_markdown_images(node.text)
                    if not images:
                        result.append(node)
                    else:
                        text = node.text
                        for image in images:
                            delimiter= f"![{image[0]}]({image[1]})"
                            first_split = text.split(delimiter,1)
                            if first_split[0]:
                                result.append(TextNode(first_split[0], TextType.TEXT ))
                            result.append(TextNode(image[0],TextType.IMAGE,image[1]))
                            rest = first_split[-1]
                            text = rest
                        if text:
                            result.append(TextNode(text, TextType.TEXT))
            case _:
                result.append(node)
                
    return result 
              
def split_nodes_links(old_nodes):
    result = []
    for node in old_nodes:
        match node.text_type:
            case TextType.TEXT:
                if node.text:
                    links = extract_markdown_links(node.text)
                    if not links:
                        result.append(node)
                    else:
                        text = node.text
                        for link in links:
                            delimiter= f"[{link[0]}]({link[1]})"
                            first_split = text.split(delimiter,1)
                            if first_split[0]:
                                result.append(TextNode(first_split[0], TextType.TEXT ))
                            result.append(TextNode(link[0],TextType.LINK,link[1]))
                            rest = first_split[-1]
                            text = rest
                        if text:
                            result.append(TextNode(text, TextType.TEXT))
            case _:
                result.append(node)
                
    return result 

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes


def markdown_to_blocks(text):
    result = []
    if text:
        blocks = text.split("\n\n")
        for block in blocks:
            if block.strip():
                result.append(block.strip())
    return result

