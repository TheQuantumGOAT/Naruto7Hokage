import json
import Convert
import WebSiteFetching
import base64
import os
import Check
import string
import requests
import socket
import random
#import configparse
import ML_Model

import scheduler
def get_host():
    return " "
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Get server IP address from the configuration file
    server_ip = config.get('Server', 'ip_address')
    return f"Server IP Address: {server_ip}"
   
    

def encode_url(url):
    def compress_string(url):
        url = str(url)
        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(6))  # Generate a 6-character short code
        encoded_url = short_code  # Replace "shorturl.com" with your desired domain
        # Store the mapping of the short code and the original URL in a database or key-value store if necessary
        return encoded_url


    encoded_url = base64.b64encode(url.encode('utf-8')).decode('utf-8')
    if len(encoded_url) > 166:
        encoded_url = compress_string(url)
    return encoded_url

def decode_url(encoded_url):
    decoded_url = base64.b64decode(encoded_url).decode('utf-8')
    return decoded_url







def creat_url(file_path,file_name):
    r = "/"
    full_file_path = file_path+r+file_name
    return full_file_path
def save_file(data, full_file_path):
    # Create the full file path
    #full_file_path = os.path.join(file_path, file_name)
   
    #full_file_path = file_path+"\\"+file_name
    #full_file_path = full_file_path.replace("\\\\","\\")
    
    try:
        # Open the file in write mode
        with open(full_file_path, 'w') as file:
            # Write the data to the file
            file.write(data)
        return full_file_path    
        #print(f"File saved successfully at {full_file_path}")
    except Exception as e:
       # print(f"Error saving the file: {str(e)}")
       return str(e)

def controller(URL):
    
    #return{"S":scheduler.fun()}
    folder_path = "Server_storage"
    try:
        s =Check.check_key(URL)
        if s!="None":
            URLs = s
            with open(URLs, 'r') as json_file:
                data = json.load(json_file)
            json_file = json.dumps(data)

            return{"URL":"http://127.0.0.1:5000/"+URLs,"file": json_file}
    except:
        folder_path = "Server_storage"
    

    """ block1_var = WebSiteFetching.extract_main_article_info(URL)
    main_article = block1_var['main_article']
    Title = block1_var['Title']
    Top_Image = block1_var['Top_Image']
    source_url = block1_var['source_url']
    text_content_with_newlines_splited = WebSiteFetching.retrieve_text_content_from_url(URL)
    TEXT_0 = ML_Model.delete_strings_before(text_content_with_newlines_splited, Title)
    # Remove unnecessary spaces from each element in the array
    TEXT_0 = ML_Model.remove_unnecessary_spaces(TEXT_0)
    TEXT =ML_Model.fun3(TEXT_0)
    original_lang = ML_Model.identify_original_language(TEXT)
    #SUMMARY = ML_Model.generate_summary_from_text(TEXT)
    #SUMMARY =  ML_Model.translate_for_summary(SUMMARY, original_lang) 
    Block7_var = ML_Model.extract_editing_and_publishing_dates(TEXT_0)
    E_Date = Block7_var["E_Date"]
    P_Date = Block7_var["P_Date"]
    author = ML_Model.get_author(TEXT_0) 
    data = {
    "Title": "Title",
    "P_Date": "P_Date",
    "author": "author",
    "SUMMARY": "SUMMARY",
    "Top_Image": "Top_Image",
    "source_url": "source_url"
} """
    json_file = ML_Model.fun(URL)


    """ html_file = WebSiteFetching.get_website(URL)
    list_of_div=list()
    header = Convert.html_to_json(html_file["header"])
    info = list()
    for tag in html_file['body']:
        name =  tag.name
        attribute =""
        try:    
            attribute = tag.attrs 
        except:
            attribute ="" 
        next_elem =tag.next_element    
        info.append([name,attribute,])
    


    for tag in html_file['body']:
       # if tag.name == "div":
            t = Convert.html_to_json(tag)
            l = list()
            l = t.splitlines()
            l =[x for x in l if x != ""]
            if l:
                list_of_div.append(l)
        
    dict_file = {"header":header,"body":list_of_div}
    json_file = json.dumps(dict_file)
     """

    
    
    encoded_url = encode_url(URL)
   
    file_name = encoded_url  + ".json"
    #file_name= "WebSiteURL.json"
    #file_name = file_name.replace("https://","\\")
   # file_name = file_name.replace("http://","\\")
    file_name = str(file_name) 
    js = json_file
    URLs =""
    full_file_path = creat_url(folder_path,file_name)
    URLs = save_file(js, full_file_path)
    Check.add_item(URL,full_file_path)
    host = get_host()+"/"+ URLs


    return{"Host":host,"URL":"http://127.0.0.1:5000/"+URLs,"file": json_file}
