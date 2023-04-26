from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Success page
@app.route("/success", methods = ["POST"])
def success():
    if 'image' not in request.files:
        return render_template('index.html', error_msg='No file selected. Please select a file to upload.')
    file = request.files['image']
    if file.filename == '':
        return render_template('index.html', error_msg='No file selected. Please select a file to upload.')
    return render_template('success.html')
    
@app.route('/success_page')
def success_page():
    return render_template('success.html')

# @app.route("/success", methods=['POST'])
# def success():
#     if request.method=='POST':
#         image_used = request.form['image']
#         print(image_used)
#         return "image uploaded"


if __name__=="__main__":
    app.run(debug=True,port=3000)