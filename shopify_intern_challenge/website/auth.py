from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from os import system
from .models import User, Img
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, login_required, logout_user, current_user
import base64
auth = Blueprint('auth', __name__)





'''
-This is the flask route to the login method.
-The child page represented as '/login'
-This accepts GET and POST requets.
-Upon POST request, the webpage accept an email, and password.
-If user (filtered by email) exists, check the sha1 hash of 
 the database password against the entered password.
-If the password hashes match, flash success message 'Login Successful'.
-If the password hashes do not match, flash error message 'Invalid Login' 
-If the email query is unsuccessful, flash error message 'User does not exist'
-Return the login HTML template (return to the login page regardless)'''
@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first() #filter emails, return first result
        if user:
            if check_password_hash(user.password,password):
                flash("Login Successful", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Invalid Login", category="error")
        else:
            flash("User does not exist", category="error")
    return render_template('login.html',user=current_user)





'''
-This is the flask route to the sign up method.
-The child page represented as '/sign-up'
-This accepts GET and POST requets.
-Upon POST request, the webpage accept an email, 
 full name, password, and confirmation password.
-If user already exists, flash error message 'User already exists'
-If @ not included in email entry, flash error message 'Email invalid'
-If name does not include at least 1 whitespace character, flash 
 message 'Name Must include a space'
-Password must be 7 characters long and match the confirmation password'''
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





'''
-This is the route to the image upload method.
-The child page represented as '/upload'
-This accepts ONLY POST request.
-If user tries to upload an empty file, return 400 error
-The HTML source tag can only return the BLOB image file if converted to base64
-Create an Image object using the Img class, with selected params
-If the file is not "png", "gif", "jpg", "jpeg", flash error message
-If the file is accepted, commit to database
-Return to homepage (refresh page)'''
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





'''
-This is the route to the get image method.
-User must be logged in to access this method.
-The child page represented as '/{imgage-id}'
-Retrieve the image by its integer id 
-If the image id does not exist, return 404'''
@auth.route('/<int:id>')
@login_required
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return ("Image Not Found.", 404)
    return Response(img.img, mimetype=img.mimetype)





'''
-This is the route to the get image method.
-User must be logged in to access this method.
-The child page represented as '/logout'
-Upon logout, redirect to login page'''
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

