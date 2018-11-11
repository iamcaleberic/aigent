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

# process nouns/verbs
@app.route('/tag', methods = ['POST'])
def get_nouns_verbs(data_object):
    """
    Dymmy
    data_object = {
                    'filename':'../aigent.txt',
                    'words':'Free listening exercises and activities for verbs listening tests from www.123 Listening.com   .  Many different audio downloads and many different worksheets that can be combined to be very simple for young learners or more difficult for older students.'
                    }
    """
    fileName = data_object['file'] #'../aigent.txt' # data_object.file
    # File = open(fileName) #open file
    lines = data_object['words'] # File.read() #read all lines # data_object.words
    sentences = nltk.sent_tokenize(lines) #tokenize sentences
    nouns = [] #empty to array to hold all nouns
    verbs = [] #empty array to hold all verbs
    verb_tags = ['VB','VBD','VBG','VBN','VBP','VBZ']
    noun_tags = ['NN','NNP','NNS','NNPS']

    for sentence in sentences:
         for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
             if pos in noun_tags:
                 nouns.append(word)
             elif pos in verb_tags:
                 verbs.append(word)
    post_to_api('nouns', filename, nouns)
    post_to_api('verbs', filename, verbs)

get_nouns_verbs('x')

@app.route('/test_data',methods=['POST'] )
def assess(arg):
    pass

