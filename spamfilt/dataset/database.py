import pandas as pd
from constant.path import ROOT_PATH

def read_file(file, path = f"{ROOT_PATH}/src ´/data/"):
    with open("./src/data/SMSSpamCollection") as file:
        return file.readlines()
    
def get_df():
    file_content = read_file("SMSSpamColletion")
    labels = list()
    messages = list()
    for line in file_content:
        label, message = line.split("\t")
        labels.append(label)
        messages.append(message)
    
    df = pd.DataFrame({"x": messages, "y": labels})
    return df