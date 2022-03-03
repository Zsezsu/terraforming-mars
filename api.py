from flask import Blueprint, Flask, request, jsonify

import queries.insert_queries as insert_queries
import queries.select_queries as select_queries
import queries.update_queries as update_queries
import queries.delete_queries as delete_queries

api = Blueprint('api', __name__, template_folder='templates')

