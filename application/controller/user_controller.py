from flask import render_template, redirect, request, url_for
import os
import json
from ..models.contact import Contact
from uuid import uuid4
from ..utils.profile_api import write_users, get_users


def home():
  return render_template('home.html', users=get_users())


def register():
  return render_template('register.html')


def add():
  if request.method == 'POST':
    name, gender, phone, avatar = request.form.values()
    new_contact = Contact(
      str(uuid4()),
      name,
      gender,
      phone,
      avatar
    )
    contact_list = get_users()
    contact_list.append(new_contact.__dict__)
    write_users(contact_list)
    return redirect(url_for('view.home'))
  return 'error'

def edit(id):
  contact_list = get_users()
  temp = list(filter(lambda x: x.get('id') == id, contact_list))
  contact_index = contact_list.index(temp[0])
  if request.method == 'GET':
    if temp:
      return render_template('edit.html', contact=temp[0])
    return 'error'
  elif request.method == 'POST':
    name, gender, phone, avatar = request.form.values()
    edit_contact = {
      'name': name,
      'gender': gender,
      'phone': phone,
      'avatar': avatar
    }
    contact_list[contact_index].update(edit_contact)
    write_users(contact_list)
    return redirect(url_for('view.home'))
  return 'error'

def delete(id):
  contact_list = get_users()
  temp = list(filter(lambda x: x.get('id') == id, contact_list))
  contact_index = contact_list.index(temp[0])
  if temp:
    del contact_list[contact_index]
    write_users(contact_list)
    return redirect(url_for('view.home')) 
  return 'error'
