from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import os 

UPLOAD_FOLDER = 'E:/Documents/Coding/SJWTrigger/uploaded images'
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return "Welcome to the Mickey Mouse Funhaus!" + render_template('menu.html')

@app.route('/upload-image', methods=["GET", "POST"])
def upload_image():
    if request.method == 'POST':

        if "file" not in request.files:
            flash ("no file")
            return redirect(request.url)

        image = request.files["file"]
        
        if image.filename == "":
            flash("no file")
            return redirect(request.url)

        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        return "upload successful :)"

    return render_template('uploader.html')


if __name__ == "__main__":
    app.run(debug=True)