#ifndef ESPNOW_H
#define ESPNOW_H

#include <esp_now.h>
#include <WiFi.h>
#include "Timer_Interrupt.h"

extern uint8_t WaterNode[];
extern uint8_t SoilAirNode[];
extern uint8_t GateWayMacAddress[];

struct struct_message {
    std::string NodeID;
    std::string SensorID;
    float value;
};

extern bool getResponseSoil;
extern bool getResponseAir;
extern struct_message message;
extern esp_now_peer_info_t GateWayInfo;

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status);
void OnDataRecv(const uint8_t *mac, const uint8_t *data, int len);
void SendDataSoil(const char *NodeID, const char *SensorID, float value);
void SendDataAir(const char *NodeID, const char *SensorID, float value);
#endif  // ESPNOW_H
