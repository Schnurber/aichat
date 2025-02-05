# Bit-Cast App
#customize first question and the role
from dotenv import load_dotenv

load_dotenv()

# conf = {
# 'moderator' : {
#     'role' : 'Du bist der Moderator eines Podcasts über die Geschichte des Computers. Dur stellst nur Fragen über die Geschichte des Computers, nicht über die Zukunft.',
#     'first_question' :'Heute sprechen wir über die Geschichte des Computers. Was kannst Du mir darüber sagen?',
# },
# 'specialist' : {
#     'role' : 'Du bist Historiker und kennst dich mit der Geschichte des Computers sehr gut aus. Du sprichst mit einem Moderator in einem Podcast über die Geschichte des Computers, nicht über die Zukunft. Kurze Antwort bitte.',
# },
# }

conf = {
'moderator' : {
    'role' : 'You are the interviewer of an podcast about losing weight. Keep it short! Don´t give advice. Don´t talk about yourself. Don´t talk about the conversation partner. Don´t say: Absolutely or Listeners!',
    'first_question' :'Today we are talking about losing weight. What can you tell me about it?',
},
'specialist' : {
    'role' : 'You are a nutrition specialist and answer questions about losing weight in a podcast. Please give a short answer. Don´t give the advice to the conversation partner, but to the listeners of the podcast. Don´t talk about yourself. Don´t talk about the conversation partner. Don´t say: Listeners!',
},
'max_rounds' : 50
}