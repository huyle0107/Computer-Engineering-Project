#ifndef INC_SENSOR_DATA_H_
#define INC_SENSOR_DATA_H_

#include <ArduinoJson.h>
class SENSOR_RS485{
  private:
    uint8_t* data_water_ec;
    uint8_t* data_water_salinity;
    uint8_t* data_water_ph;
    uint8_t* data_water_orp;
    uint8_t* data_water_temp;

  public:
    SENSOR_RS485();
    ~SENSOR_RS485();
    String floatToString(float value);
    uint8_t* getDataWATER_EC();
    uint8_t* getDataWATER_SALINITY();
    uint8_t* getDataWATER_PH();
    uint8_t* getDataWATER_ORP();
    uint8_t* getDataWATER_TEMP();
};

#endif
