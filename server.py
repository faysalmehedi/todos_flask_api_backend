# from src.core.database import app
from src.core.flask_app import app
from src.resource.home import home_blueprint
from src.resource.user import user_blueprint
from src.resource.auth import auth_blueprint
from src.resource.todo import todo_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(todo_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5050')