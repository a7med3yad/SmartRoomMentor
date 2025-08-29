const API_URL = "http://127.0.0.1:5000";

function setThreshold() {
  const temp = document.getElementById("tempThreshold").value;
  const humidity = document.getElementById("humidityThreshold").value;

  fetch(`${API_URL}/iot/threshold`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + localStorage.getItem("token")
    },
    body: JSON.stringify({ temp, humidity })
  })
  .then(res => res.json())
  .then(data => alert(data.message));
}