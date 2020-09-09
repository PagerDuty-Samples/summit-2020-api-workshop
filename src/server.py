from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    import startup
    startup.startup()

    import views
    app.register_blueprint(views.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
