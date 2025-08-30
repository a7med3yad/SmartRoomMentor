from flask import Blueprint, request, jsonify
from backend.services.mqtt_service import publish_led, publish_threshold, get_last_data
from backend.services.supabase_service import (
    get_all_sensor_data,
    get_latest_sensor_data,
    insert_sensor_data
)

# Blueprint
iot_bp = Blueprint("iot", __name__, url_prefix="/iot")

# =======================
# MQTT ROUTES
# =======================

@iot_bp.route("/led", methods=["POST"])
def control_led():
    data = request.get_json()
    state = data.get("led_on")
    if state is not None:
        publish_led("ON" if state else "OFF")  # نأكد إن القيمة ON أو OFF
        return jsonify({"message": f"LED turned {'ON' if state else 'OFF'}"}), 200
    return jsonify({"error": "Invalid state"}), 400

@iot_bp.route("/sensors", methods=["GET"])
def get_sensors():
    """آخر قراءة جاية من الميكرو مباشرة (MQTT)"""
    data = get_last_data()
    return jsonify(data if data else {}), 200

@iot_bp.route("/threshold", methods=["POST"])
def set_threshold():
    data = request.get_json()
    temp = data.get("temp")
    hum = data.get("hum")
    gas = data.get("gas")

    if temp is not None:
        publish_threshold("temp", str(temp))
    if hum is not None:
        publish_threshold("hum", str(hum))
    if gas is not None:
        publish_threshold("gas", str(gas))
    
    return jsonify({"message": "Thresholds updated successfully"}), 200

# =======================
# SUPABASE ROUTES
# =======================

@iot_bp.route("/db/sensors", methods=["GET"])
def get_all_sensors():
    """جلب كل البيانات من جدول Supabase"""
    response = get_all_sensor_data()
    return jsonify(response.data), 200

@iot_bp.route("/db/sensors/latest", methods=["GET"])
def get_latest_sensor():
    """جلب آخر قراءة من Supabase"""
    response = get_latest_sensor_data()
    return jsonify(response.data[0] if response.data else {}), 200

@iot_bp.route("/db/sensors", methods=["POST"])
def add_sensor():
    """إضافة بيانات جديدة إلى Supabase"""
    data = request.get_json()
    temp = data.get("temperature")
    hum = data.get("humidity")
    gas = data.get("gas_level")
    obj = data.get("object_detected")
    user_id = data.get("user_id", 1)  

    response = insert_sensor_data(temp, hum, gas, obj, user_id)
    return jsonify(response.data), 201
