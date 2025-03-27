# EmailGenix

The **EmailGenix** is a Flask-based web application designed to streamline email management and composition using AI and Gmail integration. It allows users to log in via Google OAuth, view their Gmail inbox, compose new emails, reply to existing threads, and generate polished email content with the help of the Gemini API. The app provides a user-friendly interface with features like tone customization, thread history display, logging, and error handling, all wrapped in a modern Bootstrap-powered UI.

## Technologies Used
- **Python**: Core programming language for the application.
- **Flask**: Lightweight web framework for building the backend and routing.
- **Gemini API**: AI-powered text generation for creating email drafts and replies.
- **Google API Client (Gmail API)**: Integration for fetching emails, sending messages, and managing threads.
- **google-auth-oauthlib**: Handles Google OAuth authentication for secure login.
- **Bootstrap**: Frontend framework for a responsive and professional user interface.
- **JavaScript**: Enhances interactivity (e.g., email generation and form handling).
- **python-dotenv**: Manages environment variables (e.g., API keys, client secrets).
- **Git**: Version control for tracking project development and changes.
- **Logging**: Custom logging system for debugging, monitoring, and error tracking.

---

## Project Setup Steps

### STEP 1: Project Setup and Initial Git Repository
**GOAL**: Establish the project foundation with a basic structure and Git version control.

#### **Project Setup and Initial Git Repository**
1. **Create the Project Directory and Clone the Empty Repo**
   ```bash
   git clone "URL" 
2. **Navigate to the Project Directory**
    ```bash
   cd EmailGenix
   ```
3. **Open Project in VS Code**
    ```bash
   code .
   ```

#### **Create the Directory Structure**
- Use the terminal or editor to create:
```bash
email_genix/
├── app/
│   └── __init__.py  # Marks 'app' as a Python package
├── logs/            # For storing log files
├── .env             # Environment variables (empty for now)
├── requirements.txt # Dependencies (empty for now)
└── run.py           # Entry point for the Flask app
└── README.md
```

#### **Add Initial Code**
- Edit **```run.py```**:
``` python
from app import create_app

# Create the Flask app instance
app = create_app()

# Run the app in debug mode on port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

- Edit **```app/__init__.py```**:
``` python
from flask import Flask

def create_app():
    # Initialize Flask application
    app = Flask(__name__)
    
    # Basic route for testing
    @app.route('/')
    def home():
        return "Welcome to EmailGenix!"
    
    return app
```

#### **Add a README**
- Create this README.md file with initial content:
``` bash
# EmailGenix
A Flask-based web app to generate and manage emails using AI and Gmail API.
```

#### **Install requirements**
- update **```requirements.txt```**
``` bash
Flask
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
google-generativeai
python-dotenv
requests
```

#### **Setup Virtual Environment in Python**
- Create a virtual environment in command prompt **```python -m venv venv```**
- Activate it: **```venv\Scripts\activate``** (Windows) or source **```venv/bin/activate``** (Linux/Mac)
- Install dependencies: **```pip install -r requirements.txt```

#### **Test**
- Run the app: **```python run.py```**

#### **Commit Changes (make sure to put .env in .gitignore)**
``` bash 
git add . 
```
``` bash 
git commit -m "Initial commit: Set up project structure and basic Flask app"
```
``` bash 
git push -u origin main
```