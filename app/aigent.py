from flask import Flask, request
import requests
import nltk
from textblob import TextBlob

API_URL = 'https://api.aigent.co'
TEST_URL = 'http://localhost:5000'

app = Flask(__name__)

# root URL
@app.route('/')
def home():
    return 'Aigent Classifier!'

# type options: nouns/verbs
def post_to_api(data_type, recording_filename='', payload_array=[]):
    endpoint_url =  API_URL + f"/assessments/nouns-and-verbs/{data_type}/{recording_filename}/team2"
    print(endpoint_url)
    r = requests.post(TEST_URL, data={'payload': payload_array})
    print(r.status_code, r.reason)

# method for testing purposes
@app.route('/test_data',methods=['POST'] )
def assess():
    print(request.data)


# post_to_api('nouns', 'test_recording.wav', ["table", "car"])
