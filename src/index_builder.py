import os

class Page:
    def __init__(self, title, url):
        self.title = title
        self.url = os.path.normpath(url)
        #self.next = next
        #self.previous = previous
        

def build_index(all_pages, template, dst, basepath="/"):
    list_items = []
    for page in all_pages:
        clean_url = page.url.replace("\\", "/")
        clean_url = clean_url.lstrip("./")
        if clean_url in ("index.html", "/index.html"):
            continue
        list_item = f"<li><a href=\"{clean_url}\">{page.title}</a></li>"
        list_items.append(list_item)

    with open(template, 'r') as temp:
        template = temp.read()

    template = template.replace("{{ Title }}", "Jinmi's Amazing blog!")
    template = template.replace("href=\"/", f"href=\"{basepath}")
    template = template.replace("src=\"/", f"src=\"{basepath}")
    final_html = template.replace("{{ Pages }}", "\n".join(list_items))
    
    with open(f"{dst}index.html", 'w') as index:
       index.write(final_html)
            