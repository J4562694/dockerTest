from flask import Flask
from flask.blueprints import Blueprint



def createApp():
    app = Flask(__name__)
    app.secret_key = 'fg@#&hh$hjkD8*%)!@hdfsdfdfsd$@%^^$Dffghdf@'

    from app.module.apiRouter.hello.hello import router as helloRouter
    app.register_blueprint(helloRouter)
    
    return app

