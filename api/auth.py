from flask import Blueprint
from flask_api import status
from flask_restful.reqparse import RequestParser
from services import auth_service
blueprint = Blueprint('auth', __name__)


@blueprint.route('/auth/<string:auth_token>', methods=['POST'])
def auth_user(auth_token):
    """ Login to user's account.
    """
    parser = RequestParser()
    parser.add_argument('auth_token', type=str, required=True)
    args = parser.parse_args()
    try:
        user = auth_service.get_user(auth_token=args['auth_token'])
        return user, status.HTTP_200
    except:
        return status.HTTP_404
