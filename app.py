from flask import Flask, render_template, request, url_for, flash, redirect
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
    #password = db.Column(db.Sting(20)) (sqlalchemy add column etmeyi oyren)

    def __repr__(self):
        return f"RegisterForm('{self.name}', '{self.address}', '{self.phone}', '{self.web_site}','{self.user_name}')"


@app.route('/form', methods=['GET', 'POST'])
def secondreg():
    return render_template('form.html')


@app.route('/register', methods=['GET', 'POST'])
def RegisterForm():
    if request.method == 'POST':
        name = request.form['namez']
        address = request.form['address']
        phone = request.form['phone']
        web_site = request.form['web_site']
        user_name = request.form['user_name']
        #password = request.form['password']
        user = RegisterForm(name=namez, address=address, phone=phone, web_site=web_site, user_name=user_name) 
        db.session.add(user)
        db.session.commit()
        return 'You are successfully registered!'
    return render_template("form.html")


@app.route('/users')
def users():
    users = RegisterForm.query.all()
    return render_template('users.html', users=users)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['email'] != 'admin' or request.form['user_name'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
    else:
        return redirect(url_for('admin'))
        return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    return render_template(url_for('index'))

#@app.route('/admin', methods=['GET', 'POST'])
#def dashboard():
#    allbookings = BookingModel.query.get(restoran_id=3)
#    return render_template('admin.html', allbookings = allbookings)
    


#app.form("restoran/<resotran_id>")
#RegisterForm.query.get(restoran_id)
#BookingModel.query.get(restoran_id=3) (datalar ucun)

@app.route('/restoran/<id>', methods=['GET', 'POST'])
def restoran_page(id):
    # id is sent as an argument - cafenin idsi
    restoran_info = RegisterForm.query.get(id)
    if request.method == 'POST':
        name = request.form['name']
        hour = request.form['hour']
        phone = request.form['phone']
        email = request.form['email']
        booking = BookingModel(name=name, hour=hour, phone=phone, email=email, restoran_id=id)
        db.session.add(booking)
        db.session.commit()
    return render_template('admin.html', restoran=BookingModel)


#@app.route('/restoran')
#def Restoran():
#    return render_template('restoran.html')


@app.route('/restoran/<restoran_id>')
def Registration(id):
    restoran = RegisterForm.query.get(id) 
    return render_template('restoran.html', restoran="user_name")

class BookingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    hour = db.Column(db.String(10))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(20))
    restoran_id = db.Column(db.Integer)

    def __repr__(self):
        return f"booking('{self.name}', '{self.hour}', '{self.phone}','{self.email}','{self.restoran_id}')"


#Cmodel CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    hour = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
 
 
   def __init__(self, name, hour, email, phone):
 
     self.name = name
     self.hour = hour
     self.email = email
     self.phone = phone
 
 

@app.route('/admin')
def admin():
   all_data = Data.query.all()
   return render_template("admin.html")
 

#This route is for deleting guests
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = BookingModel.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Reservation Deleted Successfully")
 
    return redirect(url_for('admin'))


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        hour = request.form['hour']
        email = request.form['email']
        phone = request.form['phone']
 
        my_data = BookingModel(name, hour, email, phone)
        db.session.add(my_data)
        db.session.commit()
        flash("Guests Inserted Successfully")
        return redirect(url_for('admin'))
 
 
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = BookingModel.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.hour = request.form['hour']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
 
        db.session.commit()
        flash("Guests Updated Successfully")
 
        return redirect(url_for('admin'))
 



@app.route('/')
def index():
    return render_template('index.html', title="Home", content="Home")


@app.route('/about')
def about():
    return render_template('about.html', title="About", content="About")

@app.route('/pricing')
def pricing():
    return render_template('pricing.html', title="pricing", content="pricing")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)

    #app.secret_key='secret123'
    