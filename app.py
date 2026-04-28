from flask import Flask, render_template, request
import pytesseract
from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""

    if request.method == "POST":
        file = request.files["file"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            img = Image.open(filepath)
            text = pytesseract.image_to_string(img)

    return render_template("index.html", text=text)

app.run(host="0.0.0.0", port=10000)import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""

    if request.method == "POST":
        file = request.files["file"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            images = convert_from_path(filepath, dpi=300)

            for img in images:
                text += pytesseract.image_to_string(img)

    return render_template("index.html", text=text)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
