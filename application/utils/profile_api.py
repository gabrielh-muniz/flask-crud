import requests
import os
from dotenv import load_dotenv
from ..models.contact import Contact
from uuid import uuid4
import json

load_dotenv()

def import_profiles() -> list[Contact]:
  try:
    response = requests.get(os.getenv('API_URL'))
  except requests.exceptions.RequestException as e:
    print(f'Error on request: {e}')

  profile_list = response.json()['results']

  data = []

  for profile in profile_list:
    try:
      new_profile = Contact(
        str(uuid4()),
        profile.get('name').get('first'),
        profile.get('gender'),
        profile.get('phone'),
        profile.get('picture').get('thumbnail')
      )
      data.append(new_profile)
    except:
      print('Error on data cleaning')

  return data

def record(data: list[Contact]) -> None:
  json_data = json.dumps([obj.__dict__ for obj  in data], indent=2)
  try:
    with open(os.path.join(os.getcwd(), 'application/data/users.json'), 'w') as file:
      file.write(json_data)
  except:
    print('Error on writing file')


def get_users() -> None:
  data = []
  
  try:
    with open(os.path.join(os.getcwd(), 'application/data/users.json'), 'r') as file:
      data = json.load(file)
  except FileNotFoundError:
    print('File not found!!')

  return data

def write_users(data: list[dict]) -> None:
  try:
    with open(os.path.join(os.getcwd(), 'application/data/users.json'), 'w') as file:
      json.dump(data, file)
  except:
    print('Error on writing file')
