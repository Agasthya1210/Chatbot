import re
from fuzzywuzzy import fuzz
import time

bot_templete = "BOT : {0}"
user_templete = "USER : {0}"
import csv

def csv_to_dict(csv_file, key_column, value_column):
    result_dict = {}
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip headers if present
        for row in reader:
            key = row[key_column]
            value = row[value_column]
            result_dict[key] = value
    return result_dict


csv_file = 'questions.csv'
key_column_index = 0  # Index of the column containing keys
value_column_index = 1  # Index of the column containing values
responses = csv_to_dict(csv_file, key_column_index, value_column_index)


print('BOT : Hello I am EDUBOT, your college assistant. What can i help you with today?\n')
sample=input(user_templete.format(''))
time.sleep(0.5)
print('Before proceeding, Please tell me your name')
name=input(user_templete.format(''))
time.sleep(0.5)
print('Hi '+ name.capitalize()+' Let us know your roll number.')
rollno=input()
time.sleep(0.5)
print('Please provide us your phone number ')
mobile=input(user_templete.format(''))
mobile_num=str(mobile)
if len(mobile_num) != 10:
    print('Please provide a valid 10 digit mobile number')
    mobile=input(user_templete.format(''))
    mobile_num=str(mobile)
time.sleep(0.5)
print('BOT : Hello',name,'How can I help you today?')
time.sleep(0.5)

def get_best_match(input, responses):
    max_ratio = 0
    best_match = None
    for key in responses.keys():
        ratio = fuzz.ratio(key.lower(), input.lower())
        if ratio >= 50:  
            if ratio > max_ratio:
                max_ratio = ratio
                best_match = key
    return best_match

# In your while loop
while True:
    user_message = input(user_templete.format(''))
    user_message = user_message.lower().strip()

    if user_message == 'bye':
        time.sleep(0.5)
        print(bot_templete.format('Goodbye! Have a great day!'))
        break

    best_match = get_best_match(user_message, responses)
    if best_match:
        time.sleep(0.5)
        print(bot_templete.format(responses[best_match]))
    else:
        time.sleep(0.5)
        print(bot_templete.format('I am sorry, I do not understand.Could you please provide more details?'))
    time.sleep(1)
