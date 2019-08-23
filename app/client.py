from flask import Blueprint, current_app, send_from_directory, make_response

client_bp = Blueprint('client_app', __name__)


@client_bp.route('/', defaults={'path': ''})
@client_bp.route('/<path:path>')
def index(path):
    print(path)
    dist_dir = current_app.config['DIST_DIR']
    # building response
    response = make_response(send_from_directory(dist_dir, "index.html"))
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-Frame-Options'] = 'deny'
    return response
