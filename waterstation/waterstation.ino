#include <M5Atom.h>
#include "sensor_data.h"
#include <esp_now.h>
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

float decode_32bit(uint8_t receivedData[9]) {
  int A = int(receivedData[5]);
  int B = int(receivedData[6]);
  int C = int(receivedData[3]);
  int D = int(receivedData[4]);
  long long int my_32_bit = A << 24 | B << 16 | C << 8 | D;

  uint8_t sign_bit = (my_32_bit >> 31) & 0x01;
  float exponent = 0;
  for (int j = 30; j > 22; j--) {
    exponent += pow(2, (j - 23)) * ((my_32_bit >> j) & 0x01);
  }

  float mantissa = 0;
  int power_count = -1;
  for (int j = 22; j >= 0; j--) {
    mantissa += pow(2, power_count) * ((my_32_bit >> j) & 0x01);
    power_count--;
  }
  mantissa += 1;
  return pow(-1, sign_bit) * pow(2, exponent - 127) * mantissa;
}

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
      Serial1.println("Failed to add peer!");
      delay(10);
    } else {
      M5.dis.fillpix(0x00ff00);
      Serial1.println("Completed to add peer!");
      delay(10);
    }
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



float Water_EC = 0, Water_PH = 0, Water_ORP = 0, Water_TEMP = 0, Water_SALINITY = 0;
void loop() {
  SendData("WaterStation","EC",1.15);
  delay(10000);
  // Serial1.println("Writing to WaterStation - EC with data...");
  // Serial2.write(data485.getDataWATER_EC(), 8);
  // delay(1000);
  // if (Serial2.available()) {    // If the serial port receives a message.
  //   uint8_t receivedData[9];
  //   Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
  //   for (int i = 0; i <9 ; i++) {
  //     Serial1.print("0x");
  //     Serial1.print(receivedData[i], HEX);
  //     Serial1.print(", ");
  //   }
  //   Serial1.println();
  //   Serial1.print("EC =");
  //   Water_EC = decode_32bit(receivedData);
  //   Serial1.println(data485.floatToString(Water_EC));
  // }
  // SendData(1,Water_EC);
  // delay(2000);

  // Serial1.println("Writing to WaterStation - SALINITY with data...");
  // Serial2.write(data485.getDataWATER_SALINITY(), 8);
  // delay(1000);
  // if (Serial2.available()) {    // If the serial port receives a message.
  //   uint8_t receivedData[9];
  //   Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
  //   for (int i = 0; i <9 ; i++) {
  //     Serial1.print("0x");
  //     Serial1.print(receivedData[i], HEX);
  //     Serial1.print(", ");
  //   }
  //   Serial1.println();
  //   Serial1.print("SALINITY = ");
  //   Water_SALINITY = decode_32bit(receivedData);
  //   Serial1.println(data485.floatToString(Water_SALINITY));
  // }
  // SendData(2,Water_SALINITY);
  // delay(2000);

  // Serial1.println("Writing to WaterStation - PH with data...");
  // Serial2.write(data485.getDataWATER_PH(), 8);
  // delay(1000);
  // if (Serial2.available()) {    // If the serial port receives a message.
  //   uint8_t receivedData[9];
  //   Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
  //   for (int i = 0; i <9 ; i++) {
  //     Serial1.print("0x");
  //     Serial1.print(receivedData[i], HEX);
  //     Serial1.print(", ");
  //   }
  //   Serial1.println();
  //   Serial1.print("PH = ");
  //   Water_PH = decode_32bit(receivedData);
  //   Serial1.println(data485.floatToString(Water_PH));
  // }
  // SendData(3,Water_PH);
  // delay(2000);


  // Serial1.println("Writing to WaterStation - ORP with data...");
  // Serial2.write(data485.getDataWATER_ORP(), 8);
  // delay(1000);
  // if (Serial2.available()) {    // If the serial port receives a message.
  //   uint8_t receivedData[9];
  //   Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
  //   for (int i = 0; i <9 ; i++) {
  //     Serial1.print("0x");
  //     Serial1.print(receivedData[i], HEX);
  //     Serial1.print(", ");
  //   }
  //   Serial1.println();
  //   Serial1.print("ORP = ");
  //   Water_ORP = decode_32bit(receivedData);
  //   Serial1.println(data485.floatToString(Water_ORP));
  // }
  // SendData(4,Water_ORP);
  // delay(2000);

  // Serial1.println("Writing to WaterStation - TEMP with data...");
  // Serial2.write(data485.getDataWATER_TEMP(), 8);
  // delay(1000);
  // if (Serial2.available()) {    // If the serial port receives a message.
  //   uint8_t receivedData[9];
  //   Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
  //   for (int i = 0; i <9 ; i++) {
  //     Serial1.print("0x");
  //     Serial1.print(receivedData[i], HEX);
  //     Serial1.print(", ");
  //   }
  //   Serial1.println();
  //   Serial1.print("TEMP = ");
  //   Water_TEMP = decode_32bit(receivedData);
  //   Serial1.println(data485.floatToString(Water_TEMP));
  // }
  // SendData(5,Water_TEMP);
  // delay(30000);
}