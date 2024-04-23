from flask import Flask, render_template



def createApp():
    app = Flask(__name__)
    app.secret_key = 'fg@#&hh$hjkD8*%)!@hdfsdfdfsd$@%^^$Dffghdf@'

    @app.route('/')
    def home():
        return "hello"
    
    return app

