import datetime
import json
import os


def check_key(key):
    # Get the key from the request
    data = {}
    data_file = 'database/data.json'
    # Open the file and load the dictionary
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
    except: 
        data = {} 

    # Check if the key exists in the dictionary
    if key in data:
        return data[key]["value"]
    else:
        return "None"

def add_item(key,value):
    data = {}

    data_file = 'database\data.json'
    # Check if the file exists and load its content
    #if os.path.exists(data_file):
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
    except: 
        data = {} 
    

    # Get the key and value from the request
    """ key = request.form.get('key')
    value = request.form.get('value') """

    # Add the new item to the dictionary
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%d/%m/%Y")
    
    data[key] = {
        'date_added': formatted_date,  # replace with the current date or desired date format
        'value': value
    }
    #file.close()

    # Save the updated dictionary to the file
    with open(data_file, 'w') as file:
        json.dump(data, file)
        #file.write(data)
    #file.close()    

    return 'Item added successfully.'



