from flask import Flask, request, jsonify
from flask_cors import CORS
from contact import send_email as contact_me

app = Flask(__name__)

# Allow your frontend + localhost
CORS(app, supports_credentials=True, resources={
    r"/*": {
        "origins": [
            "http://localhost:3000",
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
            return jsonify({"error": response["error"]}), 500
        return jsonify({"success": "Message sent"}), 200

    except Exception as e:
        print("Unexpected /contact error:", e)
        return jsonify({"error": "Server error"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)