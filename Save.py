import os

def save_file(data, file_path, file_name):
    # Create the full file path
    full_file_path = os.path.join(file_path, file_name)
    full_file_path = file_path+"/"+file_name
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
