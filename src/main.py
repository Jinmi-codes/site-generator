import shutil, sys,os
from textnode import TextNode, TextType
from file_functions import file_copy, generate_page_recursive, generate_cname
from index_builder import build_index

#test = TextNode("Hey There!", TextType.PLAIN_TEXT)
#print(test)

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
 

def run_file_copy(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    file_copy(src,dst)
    print("File copying done")

def main():
    run_file_copy("./static", "./docs")
    all_pages = generate_page_recursive("./content/","./template.html", "./docs/", basepath)
    generate_cname("./docs")
    build_index(all_pages, "./main.html", "./docs/", basepath)
    

main()