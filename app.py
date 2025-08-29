from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.routes.iot_routes import iot_bp
from backend.services.mqtt_service import start_mqtt

app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app)

# تسجيل الـ routes
app.register_blueprint(iot_bp)
start_mqtt()

# route للرئيسية → index.html
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

# أي ملف جوه frontend (html تانية مثلاً)
@app.route('/<path:path>')
def serve_frontend(path):
    return send_from_directory(app.static_folder, path)

# نخلي css يترجع من فولدر css/
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory("css", filename)

# نخلي js يترجع من فولدر js/
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory("js", filename)

if __name__ == "__main__":
    app.run(debug=True)
