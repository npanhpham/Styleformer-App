from flask import Flask, render_template, request
from styleformer import Styleformer


app = Flask(__name__)

# style = [0=Casual to Formal, 1=Formal to Casual, 2=Active to Passive, 3=Passive to Active etc..]
sf = Styleformer(style = 2) 

def active_passive(sentence):
    target_sentence = sf.transfer(sentence,inference_on=-1, quality_filter=0.95, max_candidates=5)
    return target_sentence

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        sentence = request.form['sentence']
        passive_sentence = active_passive(sentence)
       
        return render_template('result.html', sentence=sentence, passive_sentence=passive_sentence)

if __name__ == '__main__':
    app.run(debug=True)
