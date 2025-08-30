const API_URL = "http://127.0.0.1:5000";

function loadDashboard() {
  fetch(`${API_URL}/iot/sensors`, {
    headers: {
      "Authorization": "Bearer " + localStorage.getItem("token")
    }
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("dashboardData").innerHTML = `
      <p>Temperature: ${data.temp} °C</p>
      <p>Humidity: ${data.hum} %</p>
      <p>Gas: ${data.gas}</p>
      <p>Light: ${data.ldr}</p>
      <p>IR Sensor: ${data.ir == 0 ? "ON" : "OFF"}</p>
      <p>LED: ${data.led}</p>
    `;
  })
  .catch(err => {
    document.getElementById("dashboardData").innerText = `Error: ${err}`;
  });
}

setInterval(loadDashboard, 3000); 
loadDashboard();
