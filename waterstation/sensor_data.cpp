#include "sensor_data.h"

SENSOR_RS485::SENSOR_RS485(){
  data_water_ec = new uint8_t[8]{0x04, 0x03, 0x00, 0x00, 0x00, 0x02, 0xC4, 0x5E};
  data_water_salinity = new uint8_t[8]{0x04, 0x03, 0x00, 0x08, 0x00, 0x02, 0x45, 0x9C};
  data_water_ph = new uint8_t[8]{0x02, 0x03, 0x00, 0x01, 0x00, 0x02, 0x95, 0xF8};
  data_water_orp = new uint8_t[8]{0x05, 0x03, 0x00, 0x01, 0x00, 0x02, 0x94, 0x4F};
  data_water_temp = new uint8_t[8]{0x05, 0x03, 0x00, 0x03, 0x00, 0x02, 0x35, 0x8F};
};

SENSOR_RS485::~SENSOR_RS485() {
  delete[] data_water_ec;
  delete[] data_water_salinity;
  delete[] data_water_ph;
  delete[] data_water_orp;
  delete[] data_water_temp;
};

String SENSOR_RS485::floatToString(float value) {
  char buffer[20];  
  sprintf(buffer, "%.2f", value);
  return String(buffer);
}

uint8_t* SENSOR_RS485::getDataWATER_EC(){
  return data_water_ec;
};

uint8_t* SENSOR_RS485::getDataWATER_SALINITY(){
  return data_water_salinity;
};

uint8_t* SENSOR_RS485::getDataWATER_PH(){
  return data_water_ph;
};

uint8_t* SENSOR_RS485::getDataWATER_ORP(){
  return data_water_orp;
};

uint8_t* SENSOR_RS485::getDataWATER_TEMP(){
  return data_water_temp;
};

