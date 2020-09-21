from pdpyras import APISession, PDClientError
from flask import Blueprint
from os import environ as ENV


bp = Blueprint('views', __name__)


@bp.route('/hello-world', methods=['GET'])
def hello_world_route():
    return f"Hello, World. {ENV.get('TEST_KEY')}"


@bp.route('/test-pdpyras', methods=['GET'])
def test_pdpyras_route():
    session = APISession(ENV.get('PAGERDUTY_REST_API_KEY'))

    # Using requests.Session.get:
    response = session.get('/users?total=true')
    if response.ok:
        total_users = response.json()['total']
        return f"Account has {total_users} users."
