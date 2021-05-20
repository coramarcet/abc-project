//code for pH sensor

#define SENSOR A0
#define OFFSET 0.00
#define LED 13
#define SAMPLING_INTERVAL 20
#define PRINT_INTERVAL 800
#define ARRAY_LENGTH 40
int PH_ARRAY[ARRAY_LENGTH];
int PH_ARRAY_INDEX = 0;
int pH;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED,OUTPUT);
  Serial.begin(9600); //serial communication
  //Serial.println("PH SENSOR KIT VOLTAGE TEST!");
}

void loop() {
  // put your main code here, to run repeatedly:
  static unsigned long SAMPLING_TIME = millis();
  static unsigned long PRINT_TIME = millis();
  static float VOLTAGE;
  static float pH;
  if(millis()-SAMPLING_TIME>SAMPLING_INTERVAL)
  {
    PH_ARRAY[PH_ARRAY_INDEX++]=analogRead(SENSOR);
    if(PH_ARRAY_INDEX==ARRAY_LENGTH)PH_ARRAY_INDEX=0;
    VOLTAGE=AVERAGE_ARRAY(PH_ARRAY,ARRAY_LENGTH);
    SAMPLING_TIME = millis();
  }
  if(millis()-PRINT_TIME>PRINT_INTERVAL)
  {
    //Serial.print("VOLTAGE OUTPUT");
    //Serial.println(VOLTAGE,4);
    pH = 6.7 + ((2.5 - VOLTAGE)/0.28)
    //Serial.print("pH OUTPUT");
    Serial.println(pH,4); //I've commented out all other println because the RPi only needs to read the pH
    text_file = open("data/nbl_names.txt","w")
    line = []
    line += pH
    text_file.writelines(line)
    text_file.close()
    digitalWrite(LED,digitalRead(LED)^1);
    PRINT_TIME = millis();
  }
}

double AVERAGE_ARRAY(int*ARR,int NUMBER) {
  int i;
  int max, min;
  double AVG;
  long AMOUNT=0;
  if(NUMBER<=0)
  {
    Serial.println("ERROR!/n");
    return 0;
  }
  if(NUMBER<5)
  {
    for(i=0; i<NUMBER; i++)
    {
      AMOUNT+=ARR[i];
    }
    AVG = AMOUNT/NUMBER;
    return AVG;
  }

  else
  {
    if(ARR[0]<ARR[i])
    {
      min = ARR[0];
      max = ARR[1];
    }
    
    else
    {
      min = ARR[1];
      max = ARR[0];
    }

    for(i=2;i<NUMBER;i++)
    {
      if(ARR[i]<min)
      {
        AMOUNT+=min;
        min = ARR[i];
      }

      else
      {
        if(ARR[i]>max)
        {
          AMOUNT+=max;
          max = AMOUNT+=ARR[i];
        }

        else
        {
          AMOUNT+=ARR[i];
        }
      }
    }
    AVG = (double)AMOUNT/(NUMBER-2);
  }
  return AVG;
}
