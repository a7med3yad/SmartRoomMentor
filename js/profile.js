const API_URL = "http://127.0.0.1:5000";

function loadProfile() {
  fetch(`${API_URL}/auth/profile`, {
    headers: { "Authorization": "Bearer " + localStorage.getItem("token") }
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      document.getElementById("profileInfo").innerHTML = `<p>${data.error}</p>`;
    } else {
      document.getElementById("profileInfo").innerHTML = `
        <p><strong>Name:</strong> ${data.name}</p>
        <p><strong>Email:</strong> ${data.email}</p>
        <p><strong>Joined:</strong> ${data.joined}</p>
      `;
    }
  });
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "index.html";
}

loadProfile();
