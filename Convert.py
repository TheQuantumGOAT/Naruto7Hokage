from bs4 import BeautifulSoup 
def check_html_tag(elemen):
 
    html_to_string = str(elemen)
    is_html_tag = bool(BeautifulSoup(html_to_string, "html.parser").find())
  
    return is_html_tag
def html_to_json(element):
    if not element:
       return { }
    return element.get_text('\n')
"""  l = list()
    for e in element:
        x = e.get_text('\n')
        l.append(x)
    return l
    """
""" def html_to_json(element):
    if not element:
       return { }
    nested_tags = list()
    
    for tag in element:
      
       if check_html_tag(tag):
         nested = html_to_json(tag)
         nested_tags.append(nested) 
        
    attribute =""
    try:    
        attribute = element.attrs 
    except:
        attribute ="" 
    name = element.name
    txt =element.text
    name = str(name)
    
    return {name:[{'text':txt} ,{'attribute':attribute},{'nested_tags':nested_tags} ]} """
