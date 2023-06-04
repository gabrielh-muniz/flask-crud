from flask import Blueprint
from ..controller import user_controller as handler

view = Blueprint('view', __name__)

view.route('/home')(handler.home)

view.route('/register', methods=['GET', 'POST'])(handler.register)

view.route('/add', methods=['GET', 'POST'])(handler.add)

view.route('/edit/<id>', methods=['GET', 'POST'])(handler.edit)

view.route('/delete/<id>', methods=['GET', 'POST', 'DELETE'])(handler.delete)
