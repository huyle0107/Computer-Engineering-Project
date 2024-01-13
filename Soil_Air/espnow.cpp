#include "espnow.h"

uint8_t GateWayMacAddress[] = { 0x64, 0xb7, 0x08, 0x80, 0xc5, 0x44 };


struct_message message;
esp_now_peer_info_t GateWayInfo;
bool getResponseSoil = false;
bool getResponseAir = false;

// Callback when data is sent
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
//  Serial1.print("\r\nLast Packet Send Status:\t");
//  Serial1.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
  Serial1.print("\r\nLast Packet Send Status: \t");
  if (status != ESP_NOW_SEND_SUCCESS) {
    Serial1.println("Delivery Fail");
    Serial1.println("0");
  } else {
    Serial1.println("Delivery Success");
  }
}


// Callback when data is received
void OnDataRecv(const uint8_t *mac, const uint8_t *data, int len) {
  char receivedData[len + 1];
  memcpy(receivedData, data, len);
  receivedData[len] = '\0';
  Serial1.println(String(receivedData));
  if(String(receivedData) == "OK!S") {
    getResponseSoil = true;
  }
  else {
    getResponseAir = true;
  }
  
}

void SendDataSoil(const char *NodeID, const char *SensorID, float value) {
    getResponseSoil = false;
    const uint8_t *peer_addr = GateWayInfo.peer_addr;

    message.NodeID = NodeID;
    message.SensorID = SensorID;
    message.value = value;


    char messageStr[50];
    snprintf(messageStr, sizeof(messageStr), "%s/%s/%.2f", NodeID, SensorID, message.value);
  

    uint8_t messageData[strlen(messageStr)];
    memcpy(messageData, messageStr, strlen(messageStr));

    esp_err_t result = esp_now_send(peer_addr, messageData, strlen(messageStr));
    //Serial1.print("Sending result: "); 
    //Serial1.println(result);
}

void SendDataAir(const char *NodeID, const char *SensorID, float value) {
    getResponseAir = false;
    const uint8_t *peer_addr = GateWayInfo.peer_addr;

    message.NodeID = NodeID;
    message.SensorID = SensorID;
    message.value = value;


    char messageStr[50];
    snprintf(messageStr, sizeof(messageStr), "%s/%s/%.2f", NodeID, SensorID, message.value);
  

    uint8_t messageData[strlen(messageStr)];
    memcpy(messageData, messageStr, strlen(messageStr));


    esp_err_t result = esp_now_send(peer_addr, messageData, strlen(messageStr));
    //Serial1.print("Sending result: "); Serial1.println(result);
}
