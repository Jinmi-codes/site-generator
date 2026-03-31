import shutil
from textnode import TextNode, TextType
from file_functions import file_copy


#test = TextNode("Hey There!", TextType.PLAIN_TEXT)
#print(test)

def run_file_copy(src, dst):
    shutil.rmtree(dst)
    file_copy(src,dst)
    print("File copying done")

run_file_copy("./static", "./public")
