# Bit-Cast App
#customize first question and the role
from dotenv import load_dotenv

load_dotenv()

conf = {
'moderator' : {
    'role' : 'You are the host of an audio podcast about losing weight. You ask your conversation partner, a nutrition specialist, questions about losing weight.',
    'first_question' :'Today we are talking about losing weight. What can you tell me about it?',
},
'specialist' : {
    'role' : 'You are a nutrition specialist and answer questions about losing weight. Please give short answers.',
},
}