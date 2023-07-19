import datetime
import json
import os
import time
import atexit
def delet_old_files():
    data = {}

    data_file = 'database\data.json'
    # Check if the file exists and load its content
    #if os.path.exists(data_file):
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
    except: 
        data = {} 
    

    """ current_date = datetime.date().today() # Get the current date
    one_week_ago = current_date - datetime.timedelta(weeks=1)  # Subtract one week from the current date
    formatted_date = one_week_ago.strftime("%d/%m/%Y")  """
    current_date = datetime.date.today() - datetime.timedelta(weeks=1)
    formatted_date = current_date.strftime("%d/%m/%Y") 
    l = [x for x in data if data[x]["date_added"] <= formatted_date]
    li = list()
    for ele in l:
        s = data[ele]["value"]
        try:
            os.remove(s)
        except:
            s=""
    for ele in l:
        del data[ele]
    with open(data_file, 'w') as file:
        json.dump(data, file)
        
    return l


from apscheduler.schedulers.background import BackgroundScheduler


def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


scheduler = BackgroundScheduler()
scheduler.add_job(func= delet_old_files, trigger="interval", hours=24)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())