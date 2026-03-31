import shutil
from textnode import TextNode, TextType
from file_functions import file_copy, generate_page


#test = TextNode("Hey There!", TextType.PLAIN_TEXT)
#print(test)

def run_file_copy(src, dst):
    shutil.rmtree(dst)
    file_copy(src,dst)
    print("File copying done")

def main():
    run_file_copy("./static", "./public")
    generate_page("./content/index.md","./template.html", "./public/index.html")
