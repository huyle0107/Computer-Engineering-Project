#include <M5Atom.h>
#include <esp_now.h>
#include <WiFi.h>
#include <Arduino.h>

hw_timer_t* timer = NULL; //khơi tạo timer
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;

int timer1 = 1000;
uint8_t timerflag = 0;

// hàm xử lý ngắt
void IRAM_ATTR onTimer() {   
  portENTER_CRITICAL_ISR(&timerMux); //vào chế độ tránh xung đột
  if(timer1 >= 0){
    timer1--;
    if (timer1 == 0)  timerflag = 1;
  }
  portEXIT_CRITICAL_ISR(&timerMux); // thoát 
}

// Variable to store if sending data was successful

uint8_t WaterNode[] = { 0xd4, 0xd4, 0xda, 0x9d, 0x0D, 0x00 };
uint8_t SoilAirNode[] = { 0xd4, 0xd4, 0xda, 0x9d, 0x05, 0x00};
uint8_t GateWayMacAddress[] = { 0x64, 0xb7, 0x08, 0x80, 0xc5, 0x44 };
//uint8_t GateWayMacAddress[] = { 0x4c, 0x75, 0x25, 0x97, 0xa9, 0x68 };

esp_now_peer_info_t WaterInfo;
esp_now_peer_info_t SoilAirInfo;

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
}


// Callback when data is received
void OnDataRecv(const uint8_t *mac, const uint8_t *data, int len) {
  Serial1.println("Receive");
  char receivedData[len + 1];
  memcpy(receivedData, data, len);
  receivedData[len] = '\0';
  Serial1.println(String(receivedData));
  if(receivedData[0] == 'S'){
    const char *message = "OK!SOIL";
    esp_now_send(mac, (uint8_t *)message, sizeof(message));
  }
  else if (receivedData[0] == 'A'){
    const char *message = "OK!AIR"; 
    esp_now_send(mac, (uint8_t *)message, sizeof(message));
  }
  else{
    const char *message = "OK!WATER";
    esp_now_send(mac, (uint8_t *)message, sizeof(message));
  }
  
}

void setup() {
  M5.begin(true, false, true);
  delay(50);
  M5.dis.fillpix(0x0000ff);
  Serial1.begin(115200, SERIAL_8N1, 3, 1);

  WiFi.mode(WIFI_STA);
  delay(1000);  //delay for set-up M5
  if (esp_now_init() != ESP_OK) {
    Serial1.println("ESPNow initialization failed!");
    delay(100);
  } else {
    Serial1.println("ESPNow initialization completed!");
    delay(100);
  }
  esp_now_register_send_cb(OnDataSent);
  esp_now_register_recv_cb(OnDataRecv);

  memcpy(WaterInfo.peer_addr, WaterNode, 6);
  WaterInfo.channel = 0;
  WaterInfo.encrypt = false;  // No encryption
  if (esp_now_add_peer(&WaterInfo) != ESP_OK) {
    M5.dis.fillpix(0xff0000);
    Serial1.println("Failed to add Water Station!");
    delay(10);
  } else {
    M5.dis.fillpix(0x00ff00);
    Serial1.println("Completed to add Water Station!");
    delay(10);
  }

  memcpy(SoilAirInfo.peer_addr, SoilAirNode, 6);
  SoilAirInfo.channel = 0;
  SoilAirInfo.encrypt = false;  // No encryption
  if (esp_now_add_peer(&SoilAirInfo) != ESP_OK) {
    M5.dis.fillpix(0xff0000);
    Serial1.println("Failed to add Soil-Air Station!");
    delay(10);
  } else {
    M5.dis.fillpix(0x00ff00);
    Serial1.println("Completed to add Soil-Air Station!");
    delay(10);
  }
  timer = timerBegin(0, 80, true);
  //khởi tạo hàm xử lý ngắt ngắt cho Timer
  timerAttachInterrupt(timer, &onTimer, true);
  //khởi tạo thời gian ngắt cho timer là 1ms (1000 us)
  timerAlarmWrite(timer, 1000, true);
  //bắt đầu chạy timer
  timerAlarmEnable(timer);
  M5.dis.fillpix(0x0000ff);
}

void loop() {

}
