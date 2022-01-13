from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Note, Img
import json


# NEW BLUEPRINT OBJECT FOR VIEWS
views = Blueprint('views', __name__)







# CREATE THE HOMEPAGE VIEW 
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
