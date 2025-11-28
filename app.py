from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from database import db
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = "my-secret-key-for-tests"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        username = data.get("username")
        password = data.get("password")

        if username and password:
            #buscar login
            user = User.query.filter_by(username=username).first()

            if user and user.password: 
                login_user(user)
                print(current_user.is_authenticated)
                return jsonify({"message": "Usuário autenticado com sucesso!"}), 200
                
        return jsonify({"message": "Credenciais inválidas!"}), 401 
    except:
        return jsonify({"message": "Erro ao processar login!"}), 500
        


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Lagout realizado com sucesso"}), 200


@app.route('/user', methods=["POST"])
def create_user():
    data = request.json
    try:
        username = data.get("username")
        password = data.get("password")

        if username and password: 
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201
        return jsonify({"message": "Dados inválidos!"}), 401

    except:
        return jsonify({"message": "Erro no servidor ao cadastrar usuário!"}), 500
    

@app.route('/user', methods=["DELETE"])
@login_required
def delete_user():
    data = request.json
    try:
        username = data.get("username")

        if username: 
            user = User.query.filter_by(username=username).first()

            if user:
                db.session.delete(user)
                db.session.commit()
            return jsonify({"message": "Usuário removido com sucesso!"}), 200
        
        return jsonify({"message": "Dados inválidos!"}), 401

    except:
        return jsonify({"message": "Erro no servidor ao cadastrar usuário!"}), 500



with app.app_context():
    db.create_all()

@app.route("/", methods=['GET'])
def hello_world():
    return jsonify({"message": "API running"}), 200

if  __name__ == '__main__':
    app.run(debug=True)