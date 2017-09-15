# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify, request, abort
from localSearch import ProductSearch

api = Blueprint('api', __name__)


def data_path(filename):
    data_path = current_app.config['DATA_PATH']
    return u"%s/%s" % (data_path, filename)


@api.route('/search', methods=['GET'])
def search():
    print 'Run Get request'

    return jsonify({'condition': 0})


@api.route('/search', methods=['POST'])
def receive_conditions():
    condition = {
        'count': request.json['count'],
        'radius': request.json['radius'],
        'position': request.json['position'],
        'tags': request.json.get('tags', "")
    }

    print condition

    result = ProductSearch(condition)

    return jsonify({'product': result}), 201
