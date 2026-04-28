from flask import Flask, render_template, request
from google.cloud import vision
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# create uploads folder
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Google Vision client
client = vision.ImageAnnotatorClient()

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""

    if request.method == "POST":
        file = request.files["file"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            with open(filepath, "rb") as image_file:
                content = image_file.read()

            image = vision.Image(content=content)
            response = client.text_detection(image=image)

            if response.text_annotations:
                text = response.text_annotations[0].description
            else:
                text = "No text found"

    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
