#include <M5Atom.h>
#include "sensor_data.h"
#include "StateMachine.h"
#include "Timer_Interrupt.h"
#include "espnow.h"

//
//hw_timer_t* timer = NULL; //khơi tạo timer
//portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;
//// hàm xử lý ngắt
//void IRAM_ATTR onTimer() {   
//  portENTER_CRITICAL_ISR(&timerMux); //vào chế độ tránh xung đột
//  timerRun();
//  portEXIT_CRITICAL_ISR(&timerMux); // thoát 
//}


void setup() {
  M5.begin(true, false, true);
  delay(50);
  M5.dis.fillpix(0x0000ff);
  Serial1.begin(115200, SERIAL_8N1, 3, 1);
  Serial2.begin(9600, SERIAL_8N1, 22, 19);
  WiFi.mode(WIFI_STA);
  delay(3000); //delay for set-up M5
//
//   if (esp_now_init() != ESP_OK) {
//      Serial1.println("ESPNow initialization failed!");
//      delay(100);
//    }
//    else {
//      Serial1.println("ESPNow initialization completed!");
//      delay(100);
//    }
//    esp_now_register_send_cb(OnDataSent);
//    esp_now_register_recv_cb(OnDataRecv);
//
//    memcpy(GateWayInfo.peer_addr, GateWayMacAddress, 6);
//    GateWayInfo.channel = 0;
//    GateWayInfo.encrypt = false; // No encryption
//    if(esp_now_add_peer(&GateWayInfo) != ESP_OK){
//      M5.dis.fillpix(0xff0000);
//      Serial1.println("Failed to add GateWay!");
//      delay(10);
//    } else {
//      M5.dis.fillpix(0x00ff00);
//      Serial1.println("Completed to add GateWay!");
//      delay(10);
//    }
//
//    memcpy(SoilAirInfo.peer_addr, SoilAirNode, 6);
//    SoilAirInfo.channel = 0;
//    SoilAirInfo.encrypt = false; // No encryption
//    if(esp_now_add_peer(&SoilAirInfo) != ESP_OK){
//      M5.dis.fillpix(0xff0000);
//      Serial1.println("Failed to add SoilAir!");
//      delay(10);
//    } else {
//      M5.dis.fillpix(0x00ff00);
//      Serial1.println("Completed to add SoilAir!");
//      delay(10);
//    }
//    timer = timerBegin(0, 80, true);
//    //khởi tạo hàm xử lý ngắt ngắt cho Timer
//    timerAttachInterrupt(timer, &onTimer, true);
//    //khởi tạo thời gian ngắt cho timer là 1ms (1000 us)
//    timerAlarmWrite(timer, 1000, true);
//    //bắt đầu chạy timer  
//    timerAlarmEnable(timer);
}

void loop() {
  WaterStateMachine();
}
