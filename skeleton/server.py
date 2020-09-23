from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        import startup
        startup.startup()
    except NotImplementedError:
        import traceback
        exceptiondata = traceback.format_exc().splitlines()
        exceptionarray = exceptiondata[-3:]
        print ("----")
        print (exceptionarray[0])
        print ("NotImplementedError caught! Looks like you need to implement: " + str(e))
        exit()

    import views
    app.register_blueprint(views.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
