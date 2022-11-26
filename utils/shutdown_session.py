from app import app

@app.teardown_appcontext
def shutdown_session(exception=None):
    pass