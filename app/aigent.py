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
    endpoint_url =  API_URL + f"/assessments/nouns-and-verbs/{data_type}/{recording_filename}/team2"
    print(endpoint_url)


post_to_api('nouns', 'test_recording.wav', ["table", "car"])


# process nouns/verbs
@app.route('/tag', methods = ['POST'])
def get_nouns_verbs(data_object):
    data_object = {
                    'filename':'../aigent.txt',
                    'words':'Free listening exercises and activities for verbs listening tests from www.123 Listening.com   .  Many different audio downloads and many different worksheets that can be combined to be very simple for young learners or more difficult for older students.'
                    }
    fileName = '../aigent.txt' # data_object.file
    # File = open(fileName) #open file
    lines = data_object.words # File.read() #read all lines # data_object.words
    sentences = nltk.sent_tokenize(lines) #tokenize sentences
    nouns = [] #empty to array to hold all nouns
    verbs = [] #empty array to hold all verbs
    verb_tags = ['VB','VBD','VBG','VBN','VBP','VBZ']
    noun_tags = ['NN','NNP','NNS','NNPS']

    for sentence in sentences:
         for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
             if pos in noun_tags
                 nouns.append(word)
             elif pos in verb_tags:
                 verbs.append(word)
    print str(nouns)
    print str(verbs)
    # post_to_api('nouns', filename, nouns)
    # post_to_api('verbs', filename, verbs)

@app.route('/test_data',methods=['POST'] )
def assess(arg):
    pass
