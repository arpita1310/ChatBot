# importing the required modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# creating a chatbot
myBot = ChatBot(
    name='prophet',
    read_only=True,
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ]
)

# training the chatbot
small_convo = [
    'Hi there!',
    'Hi',
    'Hello',
    'Hey!',
    'How are you?',
    'I\'m fine.What about you?',
    'I\'m cool.',
    'Nice.',
    'I\'m Okay',
    'Glad to hear that.',
    'I\'m fine',
    'I feel awesome',
    'Excellent, glad to hear that.',
    'Not so good',
    'Sorry to hear that.',
    'What\'s your name?',
    ' I\'m Sakura. Ask me a math question, please.'
]

formula_1 = [
    'Sin theeta',
    'Opposite side/ Hypotenuse.'
]

formula_2 = [
    'Cos theeta',
    'Adjacent side/ Hypotenuse.'
]

formula_3= [
    'Tan theeta',
    'Opposite side/ Adjacent side.'
]

formula_4 = [
    'Sec theeta',
    'Adjacent side/ Hypotenuse.'
]

formula_5= [
    'Cosec theeta',
    'Hypotenuse/ Opposite side.'
]

formula_6= [
    'Cot theeta',
    'Adjacent side / Opposite side.'
]

formula_7= [
    'sin (π/2 – A) ',
    'cos A & cos (π/2 – A) = sin A.'
]

formula_8= [
    'sin (π/2 + A)',
    'cos A & cos (π/2 + A) = – sin A.'
]

formula_9= [
    'sin (3π/2 – A)',
    '– cos A & cos (3π/2 – A)  = – sin A'
]

formula_10= [
    'sin (3π/2 + A)',
    '– cos A & cos (3π/2 + A) = sin A.'
]

formula_11= [
    'sin (π – A)',
    'sin A &  cos (π – A) = – cos A.'
]

formula_12= [
    'sin (π + A)',
    '– sin A & cos (π + A) = – cos A.'
]

formula_13= [
    'sin (2π – A)',
    '– sin A & cos (2π – A) = cos A.'
]

formula_14= [
    'sin (2π + A)',
    'sin A & cos (2π + A) = cos A.'
]

formula_15= [
    'Sin(90°−x)',
    'Cos X.'
]

formula_16= [
    'Cos(90°−x)',
    'Sin X.'
]

formula_17= [
    'Tan(90°−x)',
    'Cot X.'
]

formula_18= [
    'Cot(90°−x)',
    'Tan X.'
]

formula_19= [
    'Sec(90°−x)',
    'Cosec X.'
]

formula_20= [
    'Cosec(90°−x)',
    'Sec X.'
]


# using the ListTrainer class
list_trainee = ListTrainer(myBot)
for i in (small_convo, formula_1, formula_2):
    list_trainee.train(i)

# using the ChatterBotCorpusTrainer class
corpus_trainee = ChatterBotCorpusTrainer(myBot)
corpus_trainee.train('chatterbot.corpus.english')

j=0
while(j==0):
    a=input("Enter your que : ")
    print(myBot.get_response(a))
    ch=input("Enter choice y/n : ")
    if(ch=='n' or ch=='N'):
        j=j+1
