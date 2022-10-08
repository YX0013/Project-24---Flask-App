from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "contact": "0123456789",
        "name": "Mother",
        "done": False
    },
    {

        "id": 2,
        "contact": "0987654321",
        "name": "Father",
        "done": False

    }
]

@app.route("/add-task", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide all the data in the correct format."
        }, 400)

    contact = {
        "id": contacts[-1]["id"] + 1,
        "contact": request.json["contact"],
        "name": request.json["name"],
        "done": False
    }

    contacts.append(contact)

    return jsonify({
        "status": "success",
        "message": "Contact added to the contact list."
    })

@app.route("/get-tasks")
def getTask():
    return jsonify({
        "data": contacts
    })

if (__name__ == "__main__"):
    app.run(debug = True)