from twilio.rest import Client
from flask import Flask, request, jsonify

app = Flask(__name__)

# Twilio account SID and auth token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

@app.route('/webhook', methods=['POST'])
def respond():
    message_body = request.form['Body']
    from_number = request.form['From']

    # Customize your response message here
    response_message = "Hello! I have changed my number. Please contact me on my new number: +1234567890"

    # Send the response
    message = client.messages.create(
        body=response_message,
        from_='whatsapp:your_twilio_number',
        to='whatsapp:' + from_number
    )

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
