from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from marshmallow import ValidationError

from db.pg_db import db
from models import User, Role
from schemas import UserLoginSchema


def register_user(login, password, superuser=False):
    try:
        UserLoginSchema().load({"login": login, "password": password})
    except ValidationError as e:
        return jsonify(e.messages), 400
    if User.query.filter_by(login=login).first():
        return jsonify({'error': 'Пользователь с таким login уже зарегистрирован'}), 400
    if superuser:
        role_id = Role.query.filter_by(name='Admin').first().id
    else:
        role_id = Role.query.filter_by(name='BaseUser').first().id
    user = User(login=login, role_id=role_id)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    access_token = create_access_token(identity=login)
    refresh_token = create_refresh_token(identity=login)
    return jsonify({
        'message': f'Пользователь {login} успешно зарегистрирован',
        'access_token': access_token,
        'refresh_token': refresh_token
    }), 201



def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_administrator"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper