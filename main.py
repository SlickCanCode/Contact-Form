from flask import Flask, request, jsonify
from contact import send_email as contact_me
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    
    name = data.get('name')
    company = data.get('company')
    email = data.get('email')
    message = data.get('message')

    response = contact_me(name, company, email, message)

    if "error" in response:
        return jsonify({"error": "An Error Occured, Pls contact us directly via email or whatsapp"}), 500
    else:
        return jsonify({"success": "message sent"}),200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
