const broker = "wss://broker.hivemq.com:8884/mqtt";
const topicControl = "smartroom/led";
const topicData = "smartroom/data";

let client = mqtt.connect(broker);

client.on("connect", function () {
  console.log("✅ Connected to HiveMQ broker");
  
  client.subscribe(topicData, function (err) {
    if (!err) {
      console.log("Subscribed to:", topicData);
    }
  });
});

client.on("message", function (topic, message) {
  if (topic === topicData) {
    let data = message.toString();
    console.log("📩 Data:", data);

    let dashboard = document.getElementById("dashboardData");
    if (dashboard) {
      dashboard.innerText = "Sensor Data: " + data;
    }
  }
});

function ledOn() {
  client.publish(topicControl, "ON");
  console.log("💡 LED ON");
}

function ledOff() {
  client.publish(topicControl, "OFF");
  console.log("💡 LED OFF");
}
