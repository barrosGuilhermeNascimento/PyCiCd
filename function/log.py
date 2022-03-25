import os
from datetime import date, datetime

def GenerateLog(message, location = ""):

    logFile = datetime.now().strftime("%Y-%m-%d")  + ".log" 
    _checkFolder()
    with open(f'./logs/{logFile}', "a+") as f:
        f.write(f'{message} at {location} - TIME: {datetime.now().strftime("%Y-%m-%d%H-%M-%S")}\n')
        

def _checkFolder():
    if (not os.path.isdir('./logs')):
        os.mkdir('./logs')