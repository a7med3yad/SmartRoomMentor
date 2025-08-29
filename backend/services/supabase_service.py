from supabase import create_client
from backend.config.supabase_config import SUPABASE_URL, SUPABASE_KEY

# Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# ---------- Insert Sensor Data ----------
def insert_sensor_data(tmp: float, hum: float, light: str, ir_reading: bool):
    """
    Insert a new sensor reading into Supabase
    """
    data = {
        "tmp": tmp,
        "hum": hum,
        "light": light,
        "ir_reading": ir_reading
    }
    try:
        response = supabase.table("sensor_readings").insert(data).execute()
        if response.data:
            print("✅ Sensor data inserted:", response.data)
        else:
            print("⚠️ Insert attempted but no data returned!")
        return response.data
    except Exception as e:
        print(f"❌ Error inserting sensor data: {str(e)}")
        return None


# ---------- Get All Sensor Data ----------
def get_all_sensor_data():
    """
    Retrieve all sensor data from Supabase
    """
    try:
        response = supabase.table("sensor_readings").select("*").execute()
        print(f"✅ Retrieved {len(response.data)} sensor records")
        return response.data
    except Exception as e:
        print(f"❌ Error getting all sensor data: {str(e)}")
        return []


# ---------- Get Latest Sensor Data ----------
def get_latest_sensor_data():
    """
    Retrieve the latest sensor reading (by created_at)
    """
    try:
        response = (
            supabase.table("sensor_readings")
            .select("*")
            .order("created_at", desc=True)
            .limit(1)
            .execute()
        )
        if response.data:
            print("✅ Latest sensor data:", response.data[0])
            return response.data[0]
        else:
            print("⚠️ No sensor data found!")
            return None
    except Exception as e:
        print(f"❌ Error getting latest sensor data: {str(e)}")
        return None