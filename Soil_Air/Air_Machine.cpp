#include"Air_Machine.h"

uint8_t air_state = AIR_INIT;
uint8_t air_pre_state;
uint8_t air_next_state;
SENSOR_RS485 air_data485;
float air_TEMP = 0, air_HUMID = 0, air_NOISE = 0, air_PM25 = 0, air_PM10 = 0, air_ATMOSPHERE = 0, air_LUX = 0;
void AirStateMachine(){
  switch(air_state){
    case AIR_INIT:
              Serial1.begin(115200, SERIAL_8N1, 3, 1);
              Serial2.begin(9600, SERIAL_8N1, 22, 19);
              air_state = AIR_ReadAll;
              air_next_state = AIR_WaitSensor;        
    case AIR_ReadAll:
              if(isAvailable){
                Serial1.println("Writing to AirStation with data...");
                Serial2.write(air_data485.getDataAIR(), 8);
                air_state = air_next_state;
                air_pre_state = AIR_ReadAll;
                air_next_state = AIR_SendHUMID;
                setTimer1(timeWaitSensor);
                isAvailable = false;
              }
              break;
    case AIR_WaitSensor:
              if(timer1_flag == 1){
                air_state = air_pre_state;
                air_next_state = AIR_WaitSensor;
              }
              if(Serial2.available())  {
                  uint8_t receivedData[21];
                  Serial2.readBytes(receivedData, sizeof(receivedData));   //Read the message.
                  for (int i = 0; i <21 ; i++) {
                    Serial1.print("0x");
                    Serial1.print(receivedData[i], HEX);
                    Serial1.print(", ");
                  }
                  Serial1.println();
                  Serial1.print("AIR HUMIDITY =");
                  air_HUMID = int16_t((receivedData[3] << 8 | receivedData[4])) / 10;
                  Serial1.println(air_data485.floatToString(air_HUMID));
              
                  Serial1.print("AIR TEMP =");
                  air_TEMP = int16_t((receivedData[5] << 8 | receivedData[6])) / 10;
                  Serial1.println(air_data485.floatToString(air_TEMP));
              
                  Serial1.print("AIR NOISE =");
                  air_NOISE = int16_t((receivedData[7] << 8 | receivedData[8])) / 10;
                  Serial1.println(air_data485.floatToString(air_NOISE));
              
                  Serial1.print("AIR PM2.5 =");
                  air_PM25 = int16_t((receivedData[9] << 8 | receivedData[10]));
                  Serial1.println(air_data485.floatToString(air_PM25));
                  
                  Serial1.print("AIR PM10 =");
                  air_PM10 = int16_t((receivedData[11] << 8 | receivedData[12]));
                  Serial1.println(air_data485.floatToString(air_PM10));
                  
                  Serial1.print("AIR ATMOSPHERE =");
                  air_ATMOSPHERE = int16_t((receivedData[13] << 8 | receivedData[14])) / 10;
                  Serial1.println(air_data485.floatToString(air_ATMOSPHERE));
                  
                  Serial1.print("LUX =");
                  air_LUX = int32_t(receivedData[15] << 24 | receivedData[16] << 16| receivedData[17] << 8 | receivedData[18]);
                  Serial1.println(air_data485.floatToString(air_LUX));
                  air_state = AIR_SendHUMID;
                  air_next_state = AIR_WaitResponse;       
              }
              isAvailable = true;                           
              break; 
    case AIR_SendHUMID:
              SendDataAir("AirStation","HUMID",air_HUMID);
              air_state = air_next_state;
              air_next_state = AIR_Wait;
              air_pre_state = AIR_SendHUMID;
              setTimer1(timeWaitResponse);
              break;
    case AIR_SendTEMP:
              SendDataAir("AirStation","TEMP",air_TEMP);
              air_state = air_next_state;
              air_next_state = AIR_Wait;
              air_pre_state = AIR_SendTEMP;
              setTimer1(timeWaitResponse);
              break;
              
    case AIR_SendNOISE:
              SendDataAir("AirStation","NOISE",air_NOISE);
              air_state = air_next_state;
              air_next_state = AIR_Wait;
              air_pre_state = AIR_SendNOISE;
              setTimer1(timeWaitResponse);
              break;  

    case AIR_SendPM25:
              SendDataAir("AirStation","PM2.5",air_PM25);
              air_state = air_next_state;
              air_next_state = AIR_Wait;
              air_pre_state = AIR_SendPM25;
              setTimer1(timeWaitResponse);
              break;  

    case AIR_SendPM10:
              SendDataAir("AirStation","PM10",air_PM10);
              air_state = air_next_state;
              air_next_state = AIR_Wait;
              air_pre_state = AIR_SendPM10;
              setTimer1(timeWaitResponse);
              break;  

    case AIR_SendATMOSPHERE:
              SendDataAir("AirStation","ATMOSPHERE",air_ATMOSPHERE);
              air_state = air_next_state;
              air_next_state = AIR_Wait;
              air_pre_state = AIR_SendATMOSPHERE;
              setTimer1(timeWaitResponse);
              break;

    case AIR_SendLUX:
              SendDataAir("AirStation","LUX",air_LUX);
              air_state = air_next_state;
              air_next_state = AIR_SleepMode ;
              air_pre_state = AIR_SendLUX;
              setTimer1(timeWaitResponse);
              break;
    
    case AIR_WaitResponse:
              if(getResponseAir){
                 air_state = air_next_state;
                 if(air_state == AIR_SleepMode){
                  setTimer1(timeSleep);
                  air_next_state = AIR_WaitSensor;
                 }
                 else{
                  setTimer1(timeWaitSend);
                  if(air_pre_state == AIR_SendHUMID){
                    air_next_state = AIR_SendTEMP;
                  }
                  if(air_pre_state == AIR_SendTEMP){
                    air_next_state = AIR_SendNOISE;
                  }  
                  if(air_pre_state == AIR_SendNOISE){
                    air_next_state = AIR_SendPM25;
                  }
                  if(air_pre_state == AIR_SendPM25){
                    air_next_state = AIR_SendPM10;
                  }
                  if(air_pre_state == AIR_SendPM10){
                    air_next_state = AIR_SendATMOSPHERE;
                  }     
                  if(air_pre_state == AIR_SendATMOSPHERE){
                    air_next_state = AIR_SendLUX;
                  }        
                 }
              }
              if(timer1_flag == 1){
                air_state = air_pre_state;
                air_next_state = AIR_WaitResponse;
              }
              break;

    case AIR_SleepMode:
              if(timer1_flag == 1){
                air_state = AIR_ReadAll;
                air_next_state = AIR_WaitSensor;
              }
              break;
    case AIR_Wait:
              if(timer1_flag == 1){
                air_state = air_next_state;
                air_next_state = AIR_WaitResponse;
              }
              break;
    default:
            break;
  }
}
