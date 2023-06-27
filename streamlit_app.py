from flask import Flask, render_template, request

app = Flask(__name__)

allQuestions = [
    "What is your favorite memory of dating me?",
    "What is your favorite memory of us?",
    "What food reminds you of me?",
    "When was the last time you thought about me in a positive way?",
    "What is your favorite thing that I do for you?",
    "What movie reminds you of us?",
    # ... (add the remaining questions here)
    "Do you ever wish I could read your mind? When?",
    "What things about me make you know I’m the one for you?",
    # Additional questions added
    "What is your favorite memory of dating me?",
    "What is your favorite memory of us?",
    "What food reminds you of me?",
    "When was the last time you thought about me in a positive way?",
    "What is your favorite thing that I do for you?",
    "What movie reminds you of us?",
    "Which of your parents are you most like?",
    "Which of our kids are most like you? (or if you aren’t parents yet: Do you ever picture having kids?)",
    "What’s my best physical feature?",
    "What do you like most that I do in bed?",
    # ... (add the remaining questions here)
    "Do you think I’m more of an optimist, a pessimist, or a realist?",
    "As a teenager, did you ever rebel against your parents?",
    "Who’s the closest person to you in your extended family?",
    "Did you ever want more or fewer siblings?",
    "How did your siblings shape who you are?",
    "What was your favorite date night we ever had?",
    "What are your secret thoughts when you see me at the end of the day?",
    "Do you ever wish I could read your mind? When?",
    "What things about me make you know I’m the one for you?"
]

def generate_random_questions():
    import random
    selected_questions = random.sample(allQuestions, 10)
    return selected_questions

@app.route('/')
def index():
    questions = generate_random_questions()
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit_answers():
    answers = request.form.getlist('answer')
    # Process and store the answers as needed
    return 'Answers submitted successfully!'

if __name__ == '__main__':
    app.run()
