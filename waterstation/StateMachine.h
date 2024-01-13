#include"Timer_Interrupt.h"
#include "sensor_data.h"
#include "espnow.h"

#define INIT          0
#define ReadEC        1
#define ReadSALINITY  2
#define ReadORP       3
#define ReadPH        4
#define ReadTEMP      5
#define WaitSensor    6
#define WaitResponse  7
#define Wait          8
#define SleepMode     9

#define SendEC        11
#define SendSALINITY  12
#define SendORP       13
#define SendPH        14
#define SendTEMP      15


extern uint8_t state;
extern uint8_t pre_state;
extern uint8_t next_state;
// Class Data for read value
extern SENSOR_RS485 data485;
void WaterStateMachine();
