from app import app

app.config['SECRET_KEY'] = 'YOUR _SECRET_KEY'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')