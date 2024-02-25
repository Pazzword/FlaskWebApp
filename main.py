from flask import Flask
from website import create_app


app = create_app()

app.config["LANGUAGES"] = ["en", "ru", "fr"]

if __name__ == "__main__":
    app.run(debug=True)
