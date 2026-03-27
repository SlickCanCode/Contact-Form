from flask import Flask, request, jsonify
from flask_cors import CORS
from contact import send_email as contact_me

app = Flask(__name__)

CORS(app, supports_credentials=True, resources={
    r"/*": {
        "origins": [
            "http://localhost:5173",
            "https://ahavat-olam-farm-website.vercel.app"
        ]
    }
})

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()

        name = data.get('name')
        company = data.get('company')
        email = data.get('email')
        message = data.get('message')

        response = contact_me(name, company, email, message)

        if "error" in response:
            return jsonify({"error": "email failed"}), 500
        return jsonify({"success": True}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500