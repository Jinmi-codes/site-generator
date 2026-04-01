import re
import os, shutil
from markdown_blocks import markdown_to_html_node


def file_copy(src, dst):
    src = os.path.normpath(src)
    dst = os.path.normpath(dst)
    if not os.path.exists(src):
        raise Exception("source filepath doesn't exists.")
    if not os.path.exists(dst):
        os.mkdir(dst)
    content = os.listdir(src)
    for file in content:
        if os.path.isfile(os.path.join(src, file)):
            shutil.copy(os.path.join(src, file),os.path.join(dst, file))
        else:
            file_copy(os.path.join(src, file), os.path.join(dst,file))
        


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No header found.")
            
def generate_page(src, template_src, dst, basepath):
    print(f"Generating page from {src}, to {dst} using the {template_src} template.")
    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    
    with open(src, 'r') as md:
        content = md.read()
    with open(template_src, 'r') as template:
        html_template = template.read()
    
    content_html = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    final_html = html_template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", content_html)
    final_html = final_html.replace("href=\"/", f"href=\"{basepath}")
    final_html = final_html.replace("src=\"/", f"src=\"{basepath}")
    
    with open(dst, 'w') as html:
        html.write(final_html)
    
def generate_page_recursive(src, temp_src, dst, basepath):
    pages = os.listdir(src)
    
    for page in pages:
        if os.path.isfile(os.path.join(src, page)):
            generate_page(os.path.join(src, page), temp_src, os.path.join(dst, f"{page.split(".md")[0]}.html" ), basepath)
        else:
            generate_page_recursive(os.path.join(src, page),temp_src, os.path.join(dst,page), basepath)
            
    
    
def generate_cname(dst):
    with open(f"{dst}/CNAME", 'w') as cname:
        cname.write("blog.jinmi.dev")
