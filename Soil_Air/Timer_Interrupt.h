#define timeWaitSensor        1000
#define timeWaitResponse      1000
#define timeSleep             60000
#define timeWaitSend          30000
extern int timer_flag;
extern int timer1_flag;
extern bool isAvailable;
void setTimer(int duration);
void setTimer1(int duration);
void timerRun();
