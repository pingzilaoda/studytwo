# !/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask import request, make_response, abort
from . import main
from .forms import NameForm
from .. import db
from ..models import User,Role


@main.route("/",  methods=['GET', 'POST'])
def index():
       user_agent = request.headers.get('User-Agent')
       response = make_response("<h1>hell response<h1>")
       response.set_cookie('answer', '42')
       #return redirect('http://www.baidu.com')
       name = None
       form = NameForm()
       if form.validate_on_submit():
           username = form.name.data
           user_list =  Role.query.all()
           user = User.query.filter_by(username=form.name.data).first()
           #send_email()
           if user is None:
               user = User(username = form.name.data)
               db.session.add(user)
               session['known'] = False
           else:
               session['known'] = True
          # old_name = session.get('name')
          # if old_name is not None and old_name != form.name.data:
          #     flash('Looks like you have changed your name!')
           session['name'] = form.name.data
           form.name.data = ''
           return redirect(url_for('main.index'))
       return render_template('index.html', current_time=datetime.utcnow(), form=form, name= session.get('name'), known = session.get('known', False))

@main.route('/user/<name>')
def user(name):
    if name ==  'li':
        abort(404)
    return  render_template('user.html', name=name)