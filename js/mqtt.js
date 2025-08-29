// لازم تحمل مكتبة MQTT.js من CDN
// حط السطر ده في <head> بتاع home.html:
// <script src="https://unpkg.com/mqtt/dist/mqtt.min.js"></script>

const broker = "wss://broker.hivemq.com:8884/mqtt"; // public HiveMQ broker
const topicControl = "smartroom/led";
const topicData = "smartroom/data";

let client = mqtt.connect(broker);

client.on("connect", function () {
  console.log("✅ Connected to HiveMQ broker");
  
  // الاشتراك في التوبيكات
  client.subscribe(topicData, function (err) {
    if (!err) {
      console.log("Subscribed to:", topicData);
    }
  });
});

// استقبال البيانات
client.on("message", function (topic, message) {
  if (topic === topicData) {
    let data = message.toString();
    console.log("📩 Data:", data);

    // مثال: عرض البيانات في صفحة dashboard
    let dashboard = document.getElementById("dashboardData");
    if (dashboard) {
      dashboard.innerText = "Sensor Data: " + data;
    }
  }
});

// إرسال أمر للتحكم في الـ LED
function ledOn() {
  client.publish(topicControl, "ON");
  console.log("💡 LED ON");
}

function ledOff() {
  client.publish(topicControl, "OFF");
  console.log("💡 LED OFF");
}
