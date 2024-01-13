#include"Timer_Interrupt.h"
#include "sensor_data.h"
#include "espnow.h"


#define INIT                  0
#define ReadHUMID_TEMP        1
#define ReadEC                2
#define ReadPH                3
#define ReadNPK               4
#define WaitSensor            6
#define WaitResponse          7
#define Wait                  8
#define SleepMode             9

#define SendTEMP              11
#define SendHUMID             12
#define SendEC                13
#define SendPH                14
#define SendN                 15
#define SendP                 16
#define SendK                 17


extern uint8_t state;
extern uint8_t pre_state;
extern uint8_t next_state;
// Class Data for read value
extern SENSOR_RS485 data485;
void SoilStateMachine();
