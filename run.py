from app import create_app

# Create the Flask app instance
app = create_app()

# Run the app in debug mode on port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)