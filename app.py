from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.routes.iot_routes import iot_bp
from backend.services.mqtt_service import start_mqtt

app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app)


app.register_blueprint(iot_bp)
start_mqtt()

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/<path:path>')
def serve_frontend(path):
    return send_from_directory(app.static_folder, path)

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory("css", filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory("js", filename)

if __name__ == "__main__":
    app.run(debug=True)
