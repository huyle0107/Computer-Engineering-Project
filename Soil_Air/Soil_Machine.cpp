#include"Soil_Machine.h"

uint8_t state = INIT;
uint8_t pre_state;
uint8_t next_state;
SENSOR_RS485 data485;
float soil_PH = 0, soil_TEMP = 0, soil_HUMID = 0, soil_N = 0, soil_P = 0, soil_K= 0, soil_EC =0;
void SoilStateMachine(){
  switch(state){
    case INIT:
              Serial1.begin(115200, SERIAL_8N1, 3, 1);
              Serial2.begin(9600, SERIAL_8N1, 22, 19);
              state = ReadHUMID_TEMP;
              next_state = WaitSensor;        
              isAvailable = true;
    case ReadHUMID_TEMP:
              if(isAvailable){
                Serial1.println("Writing to SOILStation - HUMID and TEMP with data...");
                Serial2.write(data485.getDataSOIL_HUMID_TEMP(), 8);
                state = next_state;
                pre_state = ReadHUMID_TEMP;
                next_state = SendHUMID;
                setTimer(timeWaitSensor);
                isAvailable = false;
              }
              break;
    case ReadEC:
              if(isAvailable){
                Serial1.println("Writing to SoilStation - EC with data...");
                Serial2.write(data485.getDataSOIL_EC(), 8);
                state = next_state;
                pre_state = ReadEC;
                next_state = SendEC;
                setTimer(timeWaitSensor);  
                isAvailable = false;             
              }
              break;
    case ReadPH:
              if(isAvailable){
                Serial1.println("Writing to SoilStation - PH with data...");
                Serial2.write(data485.getDataSOIL_PH(), 8);
                state = next_state;
                pre_state = ReadPH;
                next_state = SendPH;
                setTimer(timeWaitSensor);
                isAvailable = false;  
              }
              break;    
    case ReadNPK:
              if(isAvailable){
                Serial1.println("Writing to SOILStation - NPK with data...");
                Serial2.write(data485.getDataSOIL_NPK(), 8);
                state = next_state;
                pre_state = ReadNPK;
                next_state = SendN;
                setTimer(timeWaitSensor);
                isAvailable = false;                     
              }
              break;
    case WaitSensor:
              if(timer_flag == 1){
                state = pre_state;
                next_state = WaitSensor;
              }
              if(Serial2.available())  {
                if(pre_state == ReadHUMID_TEMP){
                    uint8_t receivedData[9];
                    Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
//                    for (int i = 0; i <9 ; i++) {
//                      Serial1.print("0x");
//                      Serial1.print(receivedData[i], HEX);
//                      Serial1.print(", ");
//                    }
//                    Serial1.println();
//                    Serial1.print("SOIL TEMP =");
                    soil_TEMP = int16_t((receivedData[5] << 8 | receivedData[6])) / 10;
                    Serial1.println(data485.floatToString(soil_TEMP));
                    
                    Serial1.print("SOIL HUMIDITY =");
                    soil_HUMID = int16_t((receivedData[3] << 8 | receivedData[4])) / 10;
                    Serial1.println(data485.floatToString(soil_HUMID));
                    state = SendHUMID;
                }
                if(pre_state == ReadEC){
                    uint8_t receivedData[7];
                    Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
//                    for (int i = 0; i <7 ; i++) {
//                      Serial1.print("0x");
//                      Serial1.print(receivedData[i], HEX);
//                      Serial1.print(", ");
//                    }
//                    Serial1.println();
                    Serial1.print("Soil_EC =");
                    soil_EC = int16_t((receivedData[3] << 8 | receivedData[4]));
                    Serial1.println(data485.floatToString(soil_EC));
                    state = SendEC;
                }
                if(pre_state == ReadPH){
                    uint8_t receivedData[7];
                    Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
//                    for (int i = 0; i <7 ; i++) {
//                      Serial1.print("0x");
//                      Serial1.print(receivedData[i], HEX);
//                      Serial1.print(", ");
//                    }
//                    Serial1.println();
//                    Serial1.print("SOIL PH =");
                    soil_PH = int16_t((receivedData[3] << 8 | receivedData[4])) / 100;
                    Serial1.println(data485.floatToString(soil_PH));  
                    state = SendPH;               
                }
                if(pre_state == ReadNPK){
                    uint8_t receivedData[11];
                    Serial2.readBytes(receivedData, sizeof(receivedData));  // Read the message.
//                    for (int i = 0; i <11 ; i++) {
//                      Serial1.print("0x");
//                      Serial1.print(receivedData[i], HEX);
//                      Serial1.print(", ");
//                    }
//                    Serial1.println();
//                    Serial1.print("Soil_N =");
                    soil_N = int16_t((receivedData[3] << 8 | receivedData[4]));
                    Serial1.println(data485.floatToString(soil_N));
                
                    Serial1.print("Soil_P =");
                    soil_P = int16_t((receivedData[5] << 8 | receivedData[6]));
                    Serial1.println(data485.floatToString(soil_P));
                
                    Serial1.print("Soil_K =");
                    soil_K = int16_t((receivedData[7] << 8 | receivedData[8]));
                    Serial1.println(data485.floatToString(soil_K));             
                    state = SendN;     
                }
                 next_state = WaitResponse;  
                 isAvailable = true;     
              }                           
              break; 
    case SendHUMID:
              SendDataSoil("SoilStation","HUMID",soil_HUMID);
              state = next_state;
              next_state = SendTEMP;
              pre_state = SendHUMID;
              setTimer(timeWaitResponse);
              break;
    case SendTEMP:
              SendDataSoil("SoilStation","TEMP",soil_TEMP);
              state = next_state;
              next_state = Wait;
              pre_state = SendTEMP;
              setTimer(timeWaitResponse);
              break;
              
    case SendEC:
              SendDataSoil("SoilStation","EC",soil_EC);
              state = next_state;
              next_state = Wait;
              pre_state = SendEC;
              setTimer(timeWaitResponse);
              break;  
    case SendPH:
              SendDataSoil("SoilStation","PH",soil_PH);
              state = next_state;
              next_state = Wait;
              pre_state = SendPH;
              setTimer(timeWaitResponse);
              break;
    case SendN:
              SendDataSoil("SoilStation","N",soil_N);
              state = next_state;
              next_state = SendP;
              pre_state = SendN;
              setTimer(timeWaitResponse);
              break;
    case SendP:
              SendDataSoil("SoilStation","P",soil_P);
              state = next_state;
              next_state = SendK;
              pre_state = SendP;
              setTimer(timeWaitResponse);
              break;
    case SendK:
              SendDataSoil("SoilStation","K",soil_K);
              state = next_state;
              next_state = SleepMode;
              pre_state = SendK;
              setTimer(timeWaitResponse);
              break;
    case WaitResponse:
              if(getResponseSoil){
                 state = next_state;
                 if(state == SleepMode){
                  setTimer(timeSleep);
                  next_state = WaitSensor;
                 }
                 else{
                  setTimer(timeWaitSend);
                  if(pre_state == SendHUMID){
                    next_state = WaitResponse;
                  }
                  if(pre_state == SendTEMP){
                    next_state = ReadEC;
                  }
                  if(pre_state == SendEC){
                    next_state = ReadPH;
                  }
                  if(pre_state == SendPH){
                    next_state = ReadNPK;
                  }
                  if(pre_state == SendN){
                    next_state = WaitResponse;
                  }      
                  if(pre_state == SendP){
                    next_state = WaitResponse;
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
                state = ReadHUMID_TEMP;
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
