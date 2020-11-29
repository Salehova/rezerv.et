from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html', title="Home", content="Home")


@app.route('/about')
def about():
    return render_template('about.html', title="About", content="About")

@app.route('/pricing')
def pricing():
    return render_template('pricing.html', title="pricing", content="pricing")

@app.route('/register')
def register():
    title = "rezerv.et for you"
    return render_template('register.html', title=title)


@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    title="Thank you!"
    return render_template('form.html', title=title, first_name=first_name, last_name=last_name, email=email)

@app.route('/admin', methods=["POST"])
def admin():
    username = request.form.get("username")
    email = request.form.get("email")
    address = request.form.get("address")
    phone = request.form.get("phone")
    image = request.form.get("image")
    web_site = request.form.get("web_site")
    title = "Welcome your page"
    return render_template('admin.html', title=tile, username=username, email=email, address=address, phone=phone, imag=image, web_site=web_site)



@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    return render_template("public/upload_image.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

    #app.secret_key='secret123'
    