from my_project import create_app
from flask import Flask, request, Response, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from .my_project.sportsman.domain.user import User

app = create_app()
app.config['SECRET_KEY'] = 'your_strong_secret_key'
app.config["JWT_SECRET_KEY"] = 'your_jwt_secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['headers']

jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print('Received data:', username , password)

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'Login Success', 'access_token': access_token})
    else:
        return jsonify({'message': 'Login Failed'}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)