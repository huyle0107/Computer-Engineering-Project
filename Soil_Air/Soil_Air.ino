#include <M5Atom.h>
#include "sensor_data.h"
#include "esp_now.h"
#include <WiFi.h>

// Class Data for read value
SENSOR_RS485 data485;

uint8_t WaterNode[] = { 0xd4, 0xd4, 0xda, 0x9d, 0x05, 0x00 };
uint8_t SoilAirNode[] = { 0xd4, 0xd4, 0xda, 0x83, 0xb2, 0x3c};
uint8_t GateWayMacAddress[] = { 0x64, 0xb7, 0x08, 0x80, 0xc5, 0x44 };

typedef struct struct_message {
    std::string NodeID;
    std::string SensorID;
    float value;
} struct_message;
struct_message message;
esp_now_peer_info_t GateWayInfo;

// Callback when data is sent
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial1.print("\r\nLast Packet Send Status:\t");
  Serial1.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}


// Callback when data is received
void OnDataRecv(const uint8_t *mac, const uint8_t *data, int len) {
  Serial1.print("Received data: ");
  Serial1.write(data, len);
  Serial1.println();
}

void SendData(const char *NodeID, const char *SensorID, float value) {
    const uint8_t *peer_addr = GateWayInfo.peer_addr;

    message.NodeID = NodeID;
    message.SensorID = SensorID;
    message.value = value;


    char messageStr[50];
    snprintf(messageStr, sizeof(messageStr), "%s/%s/%.2f", NodeID, SensorID, message.value);
  

    uint8_t messageData[strlen(messageStr)];
    memcpy(messageData, messageStr, strlen(messageStr));


    esp_err_t result = esp_now_send(peer_addr, messageData, strlen(messageStr));
    Serial1.print("Sending result: "); Serial1.println(result);
}

void setup() {
  M5.begin(true, false, true);
  delay(50);
  M5.dis.fillpix(0x0000ff);
  Serial1.begin(115200, SERIAL_8N1, 3, 1);
  Serial2.begin(9600, SERIAL_8N1, 22, 19);
  WiFi.mode(WIFI_STA);
  delay(3000); //delay for set-up M5

  if (esp_now_init() != ESP_OK) {
      Serial1.println("ESPNow initialization failed!");
      delay(100);
    }
    else {
      Serial1.println("ESPNow initialization completed!");
      delay(100);
    }
    esp_now_register_send_cb(OnDataSent);
    esp_now_register_recv_cb(OnDataRecv);

    memcpy(GateWayInfo.peer_addr, GateWayMacAddress, 6);
    GateWayInfo.channel = 0;
    GateWayInfo.encrypt = false; // No encryption
    if(esp_now_add_peer(&GateWayInfo) != ESP_OK){
      M5.dis.fillpix(0xff0000);
      Serial1.println("Failed to add Gateway!");
      delay(10);
    } else {
      M5.dis.fillpix(0x00ff00);
      Serial1.println("Completed to add Gateway!");
      delay(10);
    }
}



float air_temperature = 0, air_humidity = 0, air_illuminance = 0, air_CO2 = 0;
float soil_PH = 0, soil_temperature = 0, soil_humidity = 0, soil_N = 0, soil_P = 0, soil_K= 0, soil_EC =0;

void loop() {
  Serial1.println("Writing to AirStation - TEMP and HUMID with data...");
  Serial2.write(data485.getDataAIR_HUMIDITY_TEMPERATURE(), 8);
  delay(1000);
  if (Serial2.available()) {    // If the serial port receives a message.
    uint8_t receivedData[9];
    Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
    for (int i = 0; i <9 ; i++) {
      Serial1.print("0x");
      Serial1.print(receivedData[i], HEX);
      Serial1.print(", ");
    }
    Serial1.println();
    Serial1.print("AIR TEMP =");
    air_temperature = int16_t((receivedData[5] << 8 | receivedData[6])) / 10;
    Serial1.println(data485.floatToString(air_temperature));
    
    Serial1.print("AIR HUMIDITY =");
    air_humidity = int16_t((receivedData[3] << 8 | receivedData[4])) / 10;
    Serial1.println(data485.floatToString(air_humidity));
  }
  SendData(3,1,air_temperature);
  delay(1000);
  SendData(3,2,air_humidity);
  delay(1000);

  Serial1.println("Writing to SoilStation - PH with data...");
  Serial2.write(data485.getDataSOIL_PH(), 8);
  delay(1000);
  if (Serial2.available()) {    // If the serial port receives a message.
    uint8_t receivedData[7];
    Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
    for (int i = 0; i <7 ; i++) {
      Serial1.print("0x");
      Serial1.print(receivedData[i], HEX);
      Serial1.print(", ");
    }
    Serial1.println();
    Serial1.print("SOIL PH =");
    soil_PH = int16_t((receivedData[3] << 8 | receivedData[4])) / 100;
    Serial1.println(data485.floatToString(soil_PH));
  }
  SendData(2,1,soil_PH);
  delay(2000);


  Serial1.println("Writing to SoilStation - TEMP and HUMID with data...");
  Serial2.write(data485.getDataSOIL_TEMPERATURE_HUMIDITY(), 8);
  delay(1000);
  if (Serial2.available()) {    // If the serial port receives a message.
    uint8_t receivedData[9];
    Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
    for (int i = 0; i <9 ; i++) {
      Serial1.print("0x");
      Serial1.print(receivedData[i], HEX);
      Serial1.print(", ");
    }
    Serial1.println();
    Serial1.print("SOIL TEMP =");
    soil_temperature = int16_t((receivedData[5] << 8 | receivedData[6])) / 10;
    Serial1.println(data485.floatToString(soil_temperature));
    
    Serial1.print("SOIL HUMIDITY =");
    soil_humidity = int16_t((receivedData[3] << 8 | receivedData[4])) / 10;
    Serial1.println(data485.floatToString(soil_humidity));
  }
  SendData(2,2,soil_temperature);
  delay(1000);
  SendData(2,3,soil_humidity);
  delay(1000);

  Serial1.println("Writing to SoilStation - NPK with data...");
  Serial2.write(data485.getDataSOIL_NPK(), 8);
  delay(1000);
  if (Serial2.available()) {    // If the serial port receives a message.
    uint8_t receivedData[11];
    Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
    for (int i = 0; i <11 ; i++) {
      Serial1.print("0x");
      Serial1.print(receivedData[i], HEX);
      Serial1.print(", ");
    }
    Serial1.println();
    Serial1.print("Soil_N =");
    soil_N = int16_t((receivedData[3] << 8 | receivedData[4]));
    Serial1.println(data485.floatToString(soil_N));

    Serial1.print("Soil_P =");
    soil_P = int16_t((receivedData[5] << 8 | receivedData[6]));
    Serial1.println(data485.floatToString(soil_P));

    Serial1.print("Soil_K =");
    soil_K = int16_t((receivedData[7] << 8 | receivedData[8]));
    Serial1.println(data485.floatToString(soil_K));
  }
  SendData(2,4,soil_N);
  delay(1000);
  SendData(2,5,soil_P);
  delay(1000);
  SendData(2,6,soil_K);
  delay(1000);


  Serial1.println("Writing to SoilStation - EC with data...");
  Serial2.write(data485.getDataSOIL_CONDUCTIVITY(), 8);
  delay(1000);
  if (Serial2.available()) {    // If the serial port receives a message.
    uint8_t receivedData[7];
    Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
    for (int i = 0; i <7 ; i++) {
      Serial1.print("0x");
      Serial1.print(receivedData[i], HEX);
      Serial1.print(", ");
    }
    Serial1.println();
    Serial1.print("Soil_EC =");
    soil_EC = int16_t((receivedData[3] << 8 | receivedData[4]));
    Serial1.println(data485.floatToString(soil_EC));
  }
  SendData(2,7,soil_EC);
  delay(30000);
}

