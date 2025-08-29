const API_URL = "http://127.0.0.1:5000";
const token = localStorage.getItem("token");

let temp = 25.0;
let hum = 25.0;
let gas = 25.0;
let led = "OFF";
let ir = false;

function randomFluctuate(value, step = 0.1, min = 0, max = 100) {
  const change = (Math.random() * step * 2) - step;
  let newValue = value + change;
  if (newValue < min) newValue = min;
  if (newValue > max) newValue = max;
  return parseFloat(newValue.toFixed(2));
}

function updateUI(data, source = "api") {
  if (source === "realtime") {
    document.getElementById("sensorData").innerHTML = `
      <p>Temperature: ${data.temp ?? "-"} °C</p>
      <p>Humidity: ${data.hum ?? "-"} %</p>
      <p>Gas: ${data.gas ?? "-"}</p>
      <p>Object Detected: ${data.ir ? "Detected" : "Not Detected"}</p>
      <p>LED State: ${data.led ?? "-"}</p>
    `;
  } else {
    document.getElementById("temperature").innerText = data.temperature ?? "-";
    document.getElementById("humidity").innerText = data.humidity ?? "-";
    document.getElementById("gas").innerText = data.gas_level ?? "-";
    document.getElementById("object").innerText = data.object_detected
      ? "Detected"
      : "Not Detected";
  }
}

async function fetchSensorData() {
  try {
    temp = randomFluctuate(temp, 0.1, 24, 27);
    hum = randomFluctuate(hum, 0.1, 24, 27);
    gas = randomFluctuate(gas, 0.1, 24, 27);
    led = Math.random() > 0.5 ? "ON" : "OFF";

    const data = {
      temperature: temp,
      humidity: hum,
      gas_level: gas,
      object_detected: ir,
      led: led,
    };

    console.log("🔄 Simulated latest sensor data:", data);
    updateUI(data, "api");
  } catch (error) {
    console.error("❌ Error fetching sensor data:", error);
  }
}

async function loadSensors() {
  try {
    temp = randomFluctuate(temp, 0.1, 24, 27);
    hum = randomFluctuate(hum, 0.1, 24, 27);
    gas = randomFluctuate(gas, 0.1, 24, 27);
    led = Math.random() > 0.5 ? "ON" : "OFF";

    const data = {
      temp: temp,
      hum: hum,
      gas: gas,
      ir: ir,
      led: led,
    };

    console.log("🔄 Simulated realtime sensor data:", data);
    updateUI(data, "realtime");
  } catch (error) {
    console.error("❌ Error loading sensors:", error);
  }
}

// تغيير حالة IR كل دقيقة
setInterval(() => {
  ir = Math.random() > 0.5; // نص نص Detected/Not Detected
  console.log("🕒 IR state updated:", ir ? "Detected" : "Not Detected");
}, 60000);

// تحديث باقي القيم
setInterval(fetchSensorData, 5000);
setInterval(loadSensors, 3000);

fetchSensorData();
loadSensors();