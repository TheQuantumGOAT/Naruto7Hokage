from bs4 import BeautifulSoup
import lxml
import requests
import json
def fun(URL):
    def check_html_tag(elemen):
        
        html_to_string = str(elemen)
        is_html_tag = bool(BeautifulSoup(html_to_string, "html.parser").find())
        return is_html_tag
    
    def html_to_json(element):
        nested_tags = list()
        
        for tag in element:
            if check_html_tag(tag):
                nested = html_to_json(tag)
                nested_tags.append(nested) 
            
        attribute = element.attrs 
        name = element.name
        txt =element.text
        name = str(name)
        return {name:{'text':txt ,'attribute':attribute,'nested_tags':nested_tags }}   


    
    html_text = requests.get(URL) 
    content = requests.get(URL).text  
    soup = BeautifulSoup(content,'lxml')
    header = soup.find('header')
    soup = soup.find('body')
    list_of_object = list()
    for tag in soup:
     list_of_object.append(html_to_json(tag))
    dict_file ={"header":header,"body":list_of_object}
    json_file =json.dumps(dict_file)
    return json_file
    


    
   
   
   
    

