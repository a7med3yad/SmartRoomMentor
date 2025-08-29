// auth.js

// users الثابتين
const users = [
  { name: "Ahmed Ayad", email: "3yad@example.com", password: "0000" },
  { name: "Test User", email: "test@example.com", password: "1234" },
  { name: "Admin", email: "admin@example.com", password: "admin" }
];

function login() {
  let email = document.getElementById("loginEmail").value;
  let password = document.getElementById("loginPassword").value;

  const user = users.find(u => u.email === email && u.password === password);

  if (user) {
    localStorage.setItem("loggedInUser", JSON.stringify(user));
    window.location.href = "home.html";
  } else {
    alert("Invalid email or password");
  }
}

function signup() {
  let name = document.getElementById("signupName").value;
  let email = document.getElementById("signupEmail").value;
  let password = document.getElementById("signupPassword").value;

  if (name && email && password) {
    const newUser = { name, email, password };
    users.push(newUser);
    localStorage.setItem("loggedInUser", JSON.stringify(newUser));
    window.location.href = "home.html";
  } else {
    alert("Please fill all fields");
  }
}

// دالة تستخدم في home.html لعرض بيانات اليوزر
function loadProfile() {
  const user = JSON.parse(localStorage.getItem("loggedInUser"));
  if (user) {
    document.getElementById("profileName").textContent = user.name;
    document.getElementById("profileEmail").textContent = user.email;
  } else {
    window.location.href = "login.html"; // لو مفيش يوزر يرجعه للوجين
  }
}
