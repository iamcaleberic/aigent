from flask import Flask
import nltk
from textblob import TextBlob

API_URL = 'https://api.aigent.co'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Aigent Classifier!'

with open('example.txt','r') as f_open:
    data = f_open.read()

f_open.close()
text_blob = TextBlob(data)
print(text_blob.tags)


# type options: nouns/verbs
def post_to_api(data_type, recording_filename='', payload_array=[]):
    endpoint_url =  API_URL + f"/assessments/nouns-and-verbs/{type}/{recording_filename}/team2"
    print(endpoint_url)


post_to_api('nouns', 'test_recording.wav', ["table", "car"])


@app.route('/test_data',methods=['POST'] )
def assess(arg):
    pass
