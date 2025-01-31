from flask import Flask, render_template_string, request, send_from_directory
import os

app = Flask(__name__)

# Path to the images folder
IMAGES_FOLDER = os.path.join(os.getcwd(), 'images')

# Updated clues with Bhagavad Gita theme
clues = [
    {"id": 1, "question": "Clue 1: Reverse-word Riddle\n‘I’m the opposite of ‘live,’ and I hold secrets untold.’", "answer": "maya"},
    {"id": 2, "question": "Clue 2: Decode this Vigenère Cipher using the previous answer 'Maya' as the key.\nEncrypted Message: ssyqkue rjvjr", "answer": "krishna"},
    {"id": 3, "question": "Clue 3: Symbols Puzzle\n☀️ = The Supreme God, 🌙 = Arjuna, 🔥 = The eternal fire of Dharma\nMessage: ☀️🌙🔥", "answer": "dharma"},
    {"id": 4, "question": "Clue 4: Solve this cryptogram to reveal the ultimate truth:\nCryptogram: Ivn czlzd.", "answer": "karma"},
    {"id": 5, "question": "Clue 5: Sanskrit Shloka\n‘कर्मण्येवाधिकारस्ते मा फलेषु कदाचन’ - What key concept does this line represent?", "answer": "duty"},
    {"id": 6, "question": "Clue 6: Number Riddle\nIn Chapter 2, Verse 47, Krishna emphasizes a key principle. What is the 4-letter English word that describes this principle?", "answer": "work"}
]

game_state = {'current_clue': 0, 'message': ''}

# Custom route to serve images
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGES_FOLDER, filename)

@app.route("/", methods=["GET", "POST"])
def index():
    if game_state['current_clue'] >= len(clues):
        return render_template_string("""
        <html><head><style>
        body { background-color: #1a1a1a; color: #fff; font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        h1 { font-size: 40px; }
        .message { font-size: 22px; color: #f1c40f; }
        </style></head>
        <body>
            <h1>🙌 Hari Bol! You have completed the challenge!</h1>
            <p class="message">Krishna’s wisdom has guided you well.</p>
            <img src="{{ url_for('serve_image', filename='gita-02.jpg') }}" alt="Krishna's Teachings" style="max-width: 100%; height: auto;">
        </body></html>
        """)
    
    clue = clues[game_state['current_clue']]
    user_answer = ''
    
    if request.method == "POST":
        user_answer = request.form['answer'].strip().lower()
        if user_answer == clue["answer"]:
            game_state['message'] = "Correct! Moving to the next clue."
            game_state['current_clue'] += 1
        else:
            game_state['message'] = "Incorrect! Try again."
    
    return render_template_string("""
    <html><head><style>
    body { background-color: #222; color: #fff; font-family: Arial, sans-serif; text-align: center; padding: 50px; }
    .clue-box { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; display: inline-block; }
    input { padding: 10px; font-size: 18px; border-radius: 5px; border: none; margin: 10px; }
    .btn { background: #f39c12; color: white; padding: 10px 20px; font-size: 18px; border-radius: 5px; border: none; cursor: pointer; }
    .btn:hover { background: #e67e22; }
    </style><title>Krishna’s Wisdom Challenge</title></head>
    <body>
        <h1>Krishna’s Wisdom Challenge</h1> <!-- Updated this line to reflect the new title -->
        <div class="clue-box">
            <p>{{ clue['question'] }}</p>
            <form method="POST">
                <input type="text" name="answer" placeholder="Enter your answer" required>
                <button class="btn" type="submit">Submit</button>
            </form>
        </div>
        <p class="message">{{ game_state['message'] }}</p>
    </body></html>
    """, clue=clue, game_state=game_state)

if __name__ == "__main__":
    app.run(debug=True)
