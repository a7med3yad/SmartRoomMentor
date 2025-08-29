const API_URL = "http://127.0.0.1:5000";

function toggleLED(state) {
  fetch(`${API_URL}/iot/led`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + localStorage.getItem("token")
    },
    body: JSON.stringify({ led_on: state })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("status").innerText = `LED Status: ${data.message}`;
  })
  .catch(err => {
    document.getElementById("status").innerText = `Error: ${err}`;
  });
}
