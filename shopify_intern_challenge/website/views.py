from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Note, Img
import json


# NEW BLUEPRINT OBJECT FOR VIEWS
views = Blueprint('views', __name__)








'''
-This is the flask route to the homepage.
-This is the parent page, represented as '/'.
-This accepts GET and POST requets.
-Upon POST request, request the data for the user notes 
-If note length greater than 1 character, create object and commit to database
-Flash success method
-Return Homepage template'''
@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method== "POST":
        note = request.form.get('note')
        if len(note)<1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added.', category='success')
    return render_template('home.html',user= current_user)




'''

-This is the flask route to the delete note method.
-The child page, represented as '/delete-note'.
-This accepts ONLY POST requets.
-Query the note being selected, and commit changes
-Can only delete note of current user'''
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})








@views.route('/delete-img', methods=['POST'])
def delete_img():
    img = json.loads(request.data)
    imgId = img['imgId']
    img = Img.query.get(imgId)
    if img:
        if img.user_id == current_user.id:
            db.session.delete(img)
            db.session.commit()
    return jsonify({})
