from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from os import system
from .models import User, Img
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, login_required, logout_user, current_user
import base64



# NEW BLUEPRINT OBJECT FOR AUTHORIZATION
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first() #filter emails, return first result
        if user:
            # if the hashes match
            if check_password_hash(user.password,password):
                flash("Login Successful", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Invalid Login", category="error")
        else:
            flash("User does not exist", category="error")
    
    return render_template('login.html',user=current_user)








@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method=='POST':
        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first() #filter emails, return first result
        if user:
            flash("User already exists.", category="error")
        elif "@" not in email:
            flash("Email invalid", category="error")
        elif " " not in fullName:
            flash("Name Must include a space", category="error")
        elif len(password1)< 7:
            flash("Password too short", category="error")
        elif password1 != password2:
            flash("Passwords must match", category="error")
        else:
            new_user = User(email=email,fullName=fullName,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created", category="success")
            return redirect(url_for("views.home"))
    return render_template('sign_up.html',user=current_user)








@auth.route('/upload', methods=['POST'])
def upload():
    extensions_allowed = ["png", "gif", "jpg", "jpeg"]

    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400
     
    encoded_img = base64.b64encode(pic.read())
    encoded_img= encoded_img.decode('utf-8')

    img = Img(img=encoded_img, name=filename, mimetype=mimetype, user_id = current_user.id)
    file_type = img.name.split(".")[1]
    if file_type not in extensions_allowed:
        flash("Filetype Not Supported. Please use .png, .gif, .jpg, or .jpeg ", category="error")
    else:
        db.session.add(img)
        db.session.commit()
        flash("Image Uploaded", category="success")
        system("clear")

    return redirect(url_for("views.home"))









@auth.route('/<int:id>')
@login_required
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return ("Image Not Found.", 404)
    return Response(img.img, mimetype=img.mimetype)






@auth.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('views.home', filename='/' + filename), code=301)







@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

