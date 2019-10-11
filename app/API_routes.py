from app.routes import *
from app.json_schemas import *
from app.models import *
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity)


@app.route('/api/kereses', methods=['POST'])
def api_kereses():
 return jsonify({"message":"Hello there"})


@app.route('/api/')
def api_index():
    return jsonify({"message": "hello, this is server :)"})

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
            return jsonify({'ok': True, 'token': user.token, 'refresh': user.refresh}), 200
        else:
            return jsonify({'ok': False, 'message': 'invalid username or password'}), 401
    else:
        return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400
