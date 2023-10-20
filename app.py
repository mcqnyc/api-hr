from flask import Flask

stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


def create_app():
    app = Flask(__name__)

    @app.get("/store")
    def get_stores():
        return {"stores": stores}

    @app.route("/status")
    def status():
        return {"status": "OK"}

    return app
