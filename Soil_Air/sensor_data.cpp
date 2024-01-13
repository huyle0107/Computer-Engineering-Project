#include "sensor_data.h"
///////////////////////////////////////
String SENSOR_RS485::floatToString(float value) {
  char buffer[20]; 
  sprintf(buffer, "%.2f", value);
  return String(buffer);
}

SENSOR_RS485::SENSOR_RS485(){
  data_air = new uint8_t[8]{0x14, 0x03, 0x01, 0xF4, 0x00, 0x08, 0x06, 0xC7};
  data_air_HUMID_TEMP = new uint8_t[8]{0x14, 0x03, 0x01, 0xF4, 0x00, 0x02, 0x86, 0xC0};
  data_air_NOISE = new uint8_t[8]{0x14, 0x03, 0x01, 0xF6, 0x00, 0x01, 0x67, 0x01};
  data_air_PM25_PM10 = new uint8_t[8]{0x14, 0x03, 0x01, 0xF7, 0x00, 0x02, 0x76, 0xC0};
  data_air_ATMOSPHERE = new uint8_t[8]{0x14, 0x03, 0x01, 0xF9, 0x00, 0x01, 0x57, 0x02};
  data_air_LUX = new uint8_t[8]{0x14, 0x03, 0x01, 0xFA, 0x00, 0x02, 0xE7, 0x03};
  
  data_soil_HUMID_TEMP = new uint8_t[8]{0x01, 0x03, 0x00, 0x12, 0x00, 0x02, 0x64, 0x0E};
  data_soil_EC = new uint8_t[8]{0x01, 0x03, 0x00, 0x15, 0x00, 0x01, 0x95, 0xCE};
  data_soil_NPK = new uint8_t[8]{0x01, 0x03, 0x00, 0x1E, 0x00, 0x03, 0x65, 0xCD};
  data_soil_PH = new uint8_t[8]{0x01, 0x03, 0x00, 0x06, 0x00, 0x01, 0x64, 0x0B};
};

SENSOR_RS485::~SENSOR_RS485() {
  delete[] data_air;
  delete[] data_air_HUMID_TEMP;
  delete[] data_air_NOISE;
  delete[] data_air_PM25_PM10;
  delete[] data_air_ATMOSPHERE;
  delete[] data_air_LUX;
  
  delete[] data_soil_PH;
  delete[] data_soil_HUMID_TEMP;
  delete[] data_soil_NPK;
  delete[] data_soil_EC;
};

uint8_t* SENSOR_RS485::getDataAIR(){
  return data_air;
};

uint8_t* SENSOR_RS485::getDataAIR_HUMID_TEMP(){
  return data_air_HUMID_TEMP;
};

uint8_t* SENSOR_RS485::getDataAIR_NOISE(){
  return data_air_NOISE;
};

uint8_t* SENSOR_RS485::getDataAIR_PM25_PM10(){
  return data_air_PM25_PM10;
};

uint8_t* SENSOR_RS485::getDataAIR_ATMOSPHERE(){
  return data_air_ATMOSPHERE;
};

uint8_t* SENSOR_RS485::getDataAIR_LUX(){
  return data_air_LUX;
};


uint8_t* SENSOR_RS485::getDataSOIL_PH(){
  return data_soil_PH;
};

uint8_t* SENSOR_RS485::getDataSOIL_HUMID_TEMP(){
  return data_soil_HUMID_TEMP;
};

uint8_t* SENSOR_RS485::getDataSOIL_NPK(){
  return data_soil_NPK;
};

uint8_t* SENSOR_RS485::getDataSOIL_EC(){
  return data_soil_EC;
};
