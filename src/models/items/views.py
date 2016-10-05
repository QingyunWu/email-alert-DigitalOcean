from flask import Blueprint

__author__ = 'Qingyun Wu'


item_blueprint = Blueprint('items', __name__)


@item_blueprint.route('/item/<string:name>')
def item_page(name):
    pass

@item_blueprint.route('/load')
def load_item():
	"""
	loads an item's data using the store and return a json rep of it
	:return:
	"""