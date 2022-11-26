from app import app, settings as env

if __name__ == '__main__':
    app.run(debug=env.DEBUG, host=env.DEV_HOST, port=env.DEV_POST)