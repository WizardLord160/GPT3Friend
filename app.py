from dotenv import load_dotenv
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from sally import chat, continuation
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")

@app.route('/bot', methods=['POST'])
def sally():
    input_msg = request.values['Body']
    chat_log = session.get('chat_log')
    answer = chat(input_msg, chat_log)
    session['chat_log'] = continuation(input_msg, answer, chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)
