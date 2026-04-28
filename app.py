from flask import Flask, render_template, request
import pytesseract
from pdf2image import convert_from_path
import os

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

if __name__ == "__main__":
    app.run(debug=True)
