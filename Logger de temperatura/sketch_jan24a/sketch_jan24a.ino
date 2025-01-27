#include <OneWire.h>
#include <DallasTemperature.h>


const int Pino_Termometro = 2;
bool Medindo = false;

OneWire oneWire(Pino_Termometro); 
DallasTemperature sensor(&oneWire);

void setup() {
  
  Serial.begin(9600);
  sensor.begin();
  sensor.requestTemperatures();
  
}

void loop() {
  if(Serial.availableForWrite())
  {
    if (Serial.read() == 'b')
    {
      Medindo = true; 
    }
  }
  if (Medindo)
  {
    sensor.requestTemperatures();
    Serial.println((String)sensor.getTempCByIndex(0));
  }

  if(Serial.availableForWrite())
  {
    if (Serial.read() == 'd')
    {
      Medindo = false;
    }
  }
}
