from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        import startup
        startup.startup()
    except NotImplementedError:
        import traceback
        exceptiondata = traceback.format_exc().splitlines()
        exceptionarray = exceptiondata[:2]
        print ("----")
        print (exceptionarray[1])
        print ("NotImplementedError caught! exiting...")
        exit()

    import views
    app.register_blueprint(views.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
