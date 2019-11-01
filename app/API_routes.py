from app import db, app
from app.json_schemas import *
from app.models import User
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity)
from flask import request, jsonify
from app.alias import get_hullinfo_list_by_alias, hullinfo_full_todict
@app.route('/api/alias', methods=['POST'])
# @jwt_required
def api_kereses():
        print(request.data)
        data = request.get_json()
        alias = data['alias']

        hull_list = get_hullinfo_list_by_alias(alias)
        if len(hull_list) > 0:
            ret = {hull.hull_id: hullinfo_full_todict(hull.hull_id) for hull in hull_list}
            statuscode=200
        else:
            ret = {
                'message' : 'not found'
            }
            statuscode = 404
        return jsonify({'ok': True, 'data': ret}), statuscode


@app.route('/api/')
def api_index():
    return jsonify({"message": "hello, this is server :)"})

@app.route('/api/test/auth',  methods=['GET'])
@jwt_required
def api_auth():
    return jsonify({"message": "hello, this is server :)"}), 200

@app.route('/api/auth', methods=['POST'])
def auth_user():
    ''' auth endpoint '''
    data = validate_user(request.get_json())
    if data['ok']:
        data = data['data']
        user = User.query.filter(User.username == data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=data)
            refresh_token = create_refresh_token(identity=data)
            user.token = access_token
            user.refresh = refresh_token
            print(access_token)
            db.session.flush()
            db.session.commit()
            ret = {
                'token': access_token,
                'refresh': refresh_token
            }
            return jsonify({'ok': True, 'data': ret}), 200
        else:
            return jsonify({'ok': False, 'message': 'invalid username or password'}), 401
    else:
        return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400

@app.route('/api/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    ''' refresh token endpoint '''
    current_user = get_jwt_identity()
    ret = {
            'token': create_access_token(identity=current_user)
    }
    return jsonify({'ok': True, 'data': ret}), 200
