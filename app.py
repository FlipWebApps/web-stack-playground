from testwebapp import app, db
from testwebapp.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


# if this script is run directly then start flask. You might also consider using "flask run" / "flask shell"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
