from flask import Flask, render_template, request, jsonify, session
import re
from fuzzywuzzy import fuzz, process
import time
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

questions_answers = {}
with open('questions.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        question, answer = row
        questions_answers[question.lower()] = answer

def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'name' not in session:
        session['name'] = user_input
        return f"Welcome {session['name']}! How can I assist you today?"
    
    
        

    # Find the best match for the user input
    best_match = process.extractOne(user_input, questions_answers.keys(), scorer=fuzz.partial_ratio)
    
    if best_match and best_match[1] > 70:  # Adjust the threshold as needed
        return questions_answers[best_match[0]]
    else:
        return "I'm sorry, I don't understand that question. Can you please rephrase?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
