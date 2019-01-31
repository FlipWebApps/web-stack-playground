from testwebapp import create_app, db, cli
from testwebapp.models import User, Post, Message, Notification, Task

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task}


# if this script is run directly then start flask. You might also consider using "flask run" / "flask shell"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
