from app import db, app
from app.json_schemas import *
from app.models import User
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies)
from flask import request, jsonify
from app.alias import get_hullinfo_list_by_alias, hullinfo_full_todict
from app.hova_dobjam_kimutatas import get_kuka_count_dict_b
from flask_cors import cross_origin



@app.route('/api/alias', methods=['POST'])
def api_kereses():
        print(request.data)
        data = request.get_json()
        alias = data['alias']
        ret = []

        hull_list = get_hullinfo_list_by_alias(alias)
        if len(hull_list) > 0:
            for hull in hull_list:
                ret.append(hullinfo_full_todict(hull.hull_id))
            statuscode=200
        else:
            ret = {
                'message': 'not found'
            }
            statuscode = 404
        return jsonify({'ok': True, 'data': ret}), statuscode


@app.route('/api/hullinfo/<hull_id>', methods=['GET'])
def api_hullinfo(hull_id):
    try:
        kuka_count_dict = get_kuka_count_dict_b(hull_id)
        ret = {
            'kuka_count': kuka_count_dict,
            # todo: hogyan dobjam infók is kellenének majd
        }

        statuscode=200
    except:
        ret = {
            'message': 'not found'
        }
        statuscode = 404
    return jsonify({'ok': True, 'data': ret}), statuscode


@app.route('/api/')
def api_index():
    return jsonify({"You_sent_me_cookies": request.cookies})


@app.route('/api/test/',  methods=['GET'])
@cross_origin(origins=['https://o2lrk.csb.app'], supports_credentials=True ) # Send Access-Control-Allow-Headers
@jwt_required
def api_auth():
    username = get_jwt_identity()
    return jsonify({'hello': 'from {}'.format(username)}), 200


@app.route('/api/auth', methods=['POST'])
def auth_user():
    ''' auth endpoint '''
    data = validate_user(request.get_json())
    if data['ok']:
        data = data['data']
        user = User.query.filter(User.username == data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.username)
            refresh_token = create_refresh_token(identity=user.username)
            user.token = access_token
            user.refresh = refresh_token
            db.session.flush()
            db.session.commit()
            resp =jsonify({'ok': True})
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)

            return resp, 200
        else:
            return jsonify({'ok': False, 'message': 'invalid username or password'}), 401
    else:
        return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400


@app.route('/token/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    # Create the new access token
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)

    # Set the JWT access cookie in the response
    resp = jsonify({'refresh': True})
    set_access_cookies(resp, access_token)
    return resp, 200
