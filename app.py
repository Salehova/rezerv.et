from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registerform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class RegisterForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(30))
    phone = db.Column(db.String(20))
    web_site = db.Column(db.String(20))
    user_name = db.Column(db.String(20))

    def __repr__(self):
        return f"RegisterForm('{self.name}', '{self.address}', '{self.phone}', '{self.web_site}','{self.user_name}')"


@app.route('/secondreg', methods=['GET', 'POST'])
def secondreg():
    return render_template('secondreg.html')

@app.route('/registerform', methods=['GET', 'POST'])
def registerform():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        web_site = request.form['web_site']
        user_name = request.form['user_name']
        user = RegisterForm(name=name, address=address, phone=phone, web_site=web_site, user_name=user_name) 
        db.session.add(user)
        db.session.commit()
        return 'You are successfully registered!'


@app.route('/users')
def users():
    users = RegisterForm.query.all() #bax indi test elemek ucun burdaki log var ordada test ede bilersen
    print(users) #yazaraq bunu sahesinde logda cixdi duzdur?
    return render_template('users.html', users=users)

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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

    #app.secret_key='secret123'
    