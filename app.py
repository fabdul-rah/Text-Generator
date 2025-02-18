from flask import Flask, jsonify
import generateSentences

app = Flask(__name__)

@app.route('/generate_sentence', methods=['GET'])
def generate_sentence():
    sentence = generateSentences.generate_sentence()  # Assuming generate_sentence() is the function in generateSentences.py
    return jsonify({'sentence': sentence})

if __name__ == '__main__':
    app.run(debug=True)