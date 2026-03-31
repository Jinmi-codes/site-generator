import re
from enum import Enum
from functions import markdown_to_blocks, text_to_textnodes
from htmlnode import text_node_to_html_node, HTMLnode, ParentNode
from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph block"
    HEADING = "header block"
    CODE = "code block"
    QUOTE = "quote block"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"
    


def block_to_block_type(text):
    lines = text.split("\n")
    if re.search(r"^#{1,6} ", text):
        return BlockType.HEADING
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if re.search(r"^> *", text):
        for line in lines:
            if not re.search(r"^> *", line):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if re.search(r"^- +", text):
        for line in lines:
            if not re.search(r"^- +", line):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if re.search(r"^1\. +", text):
        count = 0
        for line in lines:
            count+=1
            if not re.search(rf"^{count}\. +", line):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    result = []
    children = text_to_textnodes(text)
    for child in children:
        result.append(text_node_to_html_node(child))
    return result
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    new_blocks = []
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                block = " ".join(block.split("\n"))
                block_node = ParentNode('p',text_to_children(block))
                new_blocks.append(block_node)
                
            case BlockType.ORDERED_LIST:
                items = [line.split(". ")[1] for line in block.split("\n")]
                li_nodes = []
                for item in items:
                    li_nodes.append(ParentNode('li', text_to_children(item)))
                block_node = ParentNode('ol', li_nodes)
                new_blocks.append(block_node)
                
            case BlockType.UNORDERED_LIST:
                items = [line[2:] for line in block.split("\n")]
                li_nodes = []
                for item in items:
                    li_nodes.append(ParentNode('li', text_to_children(item)))
                block_node = ParentNode('ul', li_nodes)
                new_blocks.append(block_node)
                
            case BlockType.QUOTE:
                items = [line[2:] for line in block.split("\n")]
                block_node = ParentNode('blockquote', text_to_children("\n".join(items)))
                new_blocks.append(block_node)
            
            case BlockType.CODE:
                content = block[3:-3]
                block_node = ParentNode('pre', [ParentNode('code', [text_node_to_html_node(TextNode(content, TextType.TEXT)) ])])
                new_blocks.append(block_node)
            
            case BlockType.HEADING:
                hashes = 0
                for letter in block:
                    if letter == '#':
                        hashes+=1
                    else:
                        break
                content = block[hashes + 1:].strip()
                block_node = ParentNode(f"h{hashes}", text_to_children(content))
                new_blocks.append(block_node)
                        
    return ParentNode("div", new_blocks)
