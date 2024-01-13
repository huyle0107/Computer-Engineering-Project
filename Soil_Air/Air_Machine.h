#include"Timer_Interrupt.h"
#include "sensor_data.h"
#include "espnow.h"
#include <string>

#define AIR_INIT                  0
#define AIR_ReadAll               1
#define AIR_WaitSensor            2
#define AIR_WaitResponse          3
#define AIR_Wait                  4
#define AIR_SleepMode             5

#define AIR_SendHUMID             11
#define AIR_SendTEMP              12
#define AIR_SendNOISE             13
#define AIR_SendPM25              14
#define AIR_SendPM10              15
#define AIR_SendATMOSPHERE        16
#define AIR_SendLUX               17


extern uint8_t air_state;
extern uint8_t air_pre_state;
extern uint8_t air_next_state;
// Class Data for read value
extern SENSOR_RS485 air_data485;
void AirStateMachine();
