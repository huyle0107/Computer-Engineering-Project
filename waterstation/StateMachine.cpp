#include"StateMachine.h"

uint8_t state = INIT;
uint8_t pre_state;
uint8_t next_state;
SENSOR_RS485 data485;

float Water_EC = 0, Water_PH = 0, Water_ORP = 0, Water_TEMP = 0, Water_SALINITY = 0;
void WaterStateMachine(){
  switch(state){
    case INIT:
              Serial1.begin(115200, SERIAL_8N1, 3, 1);
              Serial2.begin(9600, SERIAL_8N1, 22, 19);
              state = ReadEC;
              next_state = WaitSensor;        
    case ReadEC:
              Serial1.println("Writing to WaterStation - EC with data...");
              Serial2.write(data485.getDataWATER_EC(), 8);
              state = next_state;
              pre_state = ReadEC;
              next_state = SendEC;
              setTimer(1000);
              break;
    case ReadSALINITY:
              Serial1.println("Writing to WaterStation - SALINITY with data...");
              Serial2.write(data485.getDataWATER_SALINITY(), 8);
              state = next_state;
              pre_state = ReadSALINITY;
              next_state = SendSALINITY;
              setTimer(1000);
              break;
    case ReadORP:
              Serial1.println("Writing to WaterStation - ORP with data...");
              Serial2.write(data485.getDataWATER_ORP(), 8);
              state = next_state;
              pre_state = ReadORP;
              next_state = SendORP;
              setTimer(1000);
              break;    
    case ReadPH:
              Serial1.println("Writing to WaterStation - PH with data...");
              Serial2.write(data485.getDataWATER_PH(), 8);
              state = next_state;
              pre_state = ReadPH;
              next_state = SendPH;
              setTimer(1000);
              break;
    case ReadTEMP:
              Serial1.println("Writing to WaterStation - TEMP with data...");
              Serial2.write(data485.getDataWATER_TEMP(), 8);
              state = next_state;
              pre_state = ReadTEMP;
              next_state = SendTEMP;
              setTimer(1000);
              break;
    case WaitSensor:
              if(timer_flag == 1){
                state = pre_state;
                next_state = WaitSensor;
              }
              if (Serial2.available()) {    // If the serial port receives a message.
                 uint8_t receivedData[9];
                 Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
                 for (int i = 0; i <9 ; i++) {
                   Serial1.print("0x");
                   Serial1.print(receivedData[i], HEX);
                   Serial1.print(", ");
                 }
                 Serial1.println();
                 if(pre_state == ReadEC){
                    Serial1.print("EC =");
                    Water_EC = decode_32bit(receivedData);
                    Serial1.println(data485.floatToString(Water_EC));
                    state = SendEC;
                 }
                 if(pre_state == ReadSALINITY){
                    Serial1.print("SALINITY =");
                    Water_SALINITY = decode_32bit(receivedData);
                    Serial1.println(data485.floatToString(Water_SALINITY));
                    state = SendSALINITY;
                 }
                 if(pre_state == ReadORP){
                    Serial1.print("ORP =");
                    Water_ORP = decode_32bit(receivedData);
                    Serial1.println(data485.floatToString(Water_ORP));
                    state = SendORP;
                 }                 
                 if(pre_state == ReadPH){
                    Serial1.print("PH =");
                    Water_PH = decode_32bit(receivedData);
                    Serial1.println(data485.floatToString(Water_PH));
                    state = SendPH;
                 }
                 if(pre_state == ReadTEMP){
                    Serial1.print("TEMP =");
                    Water_TEMP = decode_32bit(receivedData);
                    Serial1.println(data485.floatToString(Water_TEMP));
                    state = SendTEMP;
                 }
                 next_state = WaitResponse;       
              }                           
              break; 
    case SendEC:
              SendData("WaterStation","EC",Water_EC);
              state = next_state;
              next_state = Wait;
              pre_state = SendEC;
              setTimer(5000);
              break;
    case SendSALINITY:
              SendData("WaterStation","SALINITY",Water_SALINITY);
              state = next_state;
              next_state = Wait;
              pre_state = SendSALINITY;
              setTimer(5000);
              break;  
    case SendORP:
              SendData("WaterStation","ORP",Water_ORP);
              state = next_state;
              next_state = Wait;
              pre_state = SendORP;
              setTimer(5000);
              break;
    case SendPH:
              SendData("WaterStation","PH",Water_PH);
              state = next_state;
              next_state = Wait;
              pre_state = SendPH;
              setTimer(5000);
              break;    
    case SendTEMP:
              SendData("WaterStation","TEMP",Water_TEMP);
              state = next_state;
              next_state = SleepMode;
              pre_state = SendTEMP;
              setTimer(5000);
              break;
    case WaitResponse:
              if(getResponse){
                 state = next_state;
                 if(state == SleepMode){
                  setTimer(30000);
                  next_state = WaitSensor;
                 }
                 else{
                  setTimer(2000);
                  if(pre_state == SendEC){
                    next_state = ReadSALINITY;
                  }
                  if(pre_state == SendSALINITY){
                    next_state = ReadORP;
                  }
                  if(pre_state == SendORP){
                    next_state = ReadPH;
                  }
                  if(pre_state == SendPH){
                    next_state = ReadTEMP;
                  }                
                 }
              }
              if(timer_flag == 1){
                state = pre_state;
                next_state = WaitResponse;
              }
              break;

    case SleepMode:
              if(timer_flag == 1){
                state = ReadEC;
                next_state = WaitSensor;
              }
              break;
    case Wait:
              if(timer_flag == 1){
                state = next_state;
                next_state = WaitSensor;
              }
              break;
    default:
            break;
  }
}
