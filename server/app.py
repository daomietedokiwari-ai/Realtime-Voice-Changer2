from flask import Flask, request, jsonify
import os

app = Flask(_name_)

UPLOAD_FOLDER = "../voice_uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return {"status": "Server running"}

@app.route("/upload_voice", methods=["POST"])
def upload_voice():
    if "file" not in request.files:
        return {"error": "No file provided"}, 400
    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return {"message": "Voice uploaded successfully", "file": file.filename}

@app.route("/models", methods=["GET"])
def list_models():
    model_list = os.listdir("../models")
    return {"models": model_list}

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=50021)
