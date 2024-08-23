from flask import Flask, request, render_template, send_file
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the tokenizer and model
with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        result = generate_text(text)
        return render_template('index.html', input_text=text, prediction=result)
    return render_template('index.html')

@app.route('/download')
def download_file():
    path = "sample_text.txt"  # Path to your text file
    return send_file(path, as_attachment=True)

def generate_text(text, num_words=10):
    for _ in range(num_words):
        token_text = tokenizer.texts_to_sequences([text])[0]
        padded_token_text = pad_sequences([token_text], maxlen=56, padding='pre')
        pos = np.argmax(model.predict(padded_token_text))

        for word, index in tokenizer.word_index.items():
            if index == pos:
                text += " " + word
                break
    return text

if __name__ == '__main__':
    app.run(debug=True)
