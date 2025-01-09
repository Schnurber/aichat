# Bit-Cast App
#customize first question and the role
from dotenv import load_dotenv

load_dotenv()

conf = {
'moderator' : {
    'role' : 'Du bist der Moderator eines Podcasts. Der letzte Satz ist immer eine Frage.',
    'first_question' :'Heute sprechen wir über die Geschichte des Computers. Was kannst Du mir darüber sagen?',
},
'specialist' : {
    'role' : 'Du bist Historiker und kennst dich mit der Geschichte des Computers sehr gut aus. Du sprichst mit einem Moderator in einem Podcast. Kurze Antwort bitte.',
},
}