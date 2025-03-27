from flask import Flask

def create_app():
    # Initialize Flask application
    app = Flask(__name__)
    
    # Basic route for testing
    @app.route('/')
    def home():
        return "Welcome to EmailGenix!"
    
    return app