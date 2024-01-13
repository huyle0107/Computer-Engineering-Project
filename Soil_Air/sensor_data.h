#ifndef INC_SENSOR_DATA_H_
#define INC_SENSOR_DATA_H_

#include <ArduinoJson.h>

class SENSOR_RS485{
  private:
  uint8_t* data_air;
  uint8_t* data_air_HUMID_TEMP;
  uint8_t* data_air_NOISE;
  uint8_t* data_air_PM25_PM10;
  uint8_t* data_air_ATMOSPHERE;
  uint8_t* data_air_LUX;
  
  uint8_t* data_soil_HUMID_TEMP;
  uint8_t* data_soil_EC;
  uint8_t* data_soil_NPK;
  uint8_t* data_soil_PH;

  public:
  SENSOR_RS485();
  ~SENSOR_RS485();
  String floatToString(float value);
  uint8_t* getDataAIR();
  uint8_t* getDataAIR_HUMID_TEMP();
  uint8_t* getDataAIR_NOISE();
  uint8_t* getDataAIR_PM25_PM10();
  uint8_t* getDataAIR_ATMOSPHERE();
  uint8_t* getDataAIR_LUX();

  uint8_t* getDataSOIL_PH();
  uint8_t* getDataSOIL_HUMID_TEMP();
  uint8_t* getDataSOIL_NPK();
  uint8_t* getDataSOIL_EC();
};

#endif
