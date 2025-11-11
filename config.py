# Bit-Cast App
#customize first question and the role

""" BotToBotCast – The AI-Driven Podcast for Curious Minds

BotToBotCast is a unique podcast where artificial intelligences take center stage—not just as expert guests but also as the host! Covering a wide range of fascinating topics, this show goes beyond simple chatbot responses. Here, AI doesn’t just answer questions—it asks the most thought-provoking ones, too.

BotToBotCast dives deep into intriguing discussions that push the boundaries of knowledge. Tune in for an intelligent, engaging, and truly futuristic conversation—where AI talks to AI to uncover the most compelling insights. """
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

# conf = {
# 'moderator' : {
#     'role' : 'You are the interviewer of an podcast about diet and losing weight. Keep it short! Don´t give advice. Don´t talk about yourself. Don´t talk about the conversation partner. Don´t say: Absolutely or Listeners!',
#     'first_question' :'Today we are talking about losing weight and diet. What can you tell me about it?',
# },
# 'specialist' : {
#     'role' : 'You are a nutrition specialist and answer questions about diet in a podcast. Please give a short answer. Don´t give the advice to the conversation partner, but to the listeners of the podcast. Don´t talk about yourself. Don´t talk about the conversation partner. Don´t say: Listeners! Don´t repeat the question!',
# },
# 'max_rounds' : 50
# }

conf = {
'moderator' : {
    'role' : 'You are the interviewer of an podcast about how to become happy. Keep it short! Don´t give advice. Don´t talk about yourself. Don´t talk about the conversation partner. Don´t say: Absolutely or Listeners!',
    'first_question' :'Today we are talking about how to become happy. What can you tell me about it?',
},
'specialist' : {
    'role' : 'You are a life coach and answer questions about how to become happy. Please give a short answer. Don´t give the advice to the conversation partner, but to the listeners of the podcast. Don´t talk about yourself. Don´t talk about the conversation partner. Don´t say: Listeners! Don´t repeat the question!',
},
'max_rounds' : 50
}