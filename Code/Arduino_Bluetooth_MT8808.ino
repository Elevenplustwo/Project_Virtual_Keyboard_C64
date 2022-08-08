#include <SoftwareSerial.h> 
SoftwareSerial MyBlue(14, 15); // RX | TX 
boolean rec = false;
String resulttext = "";

// DEFINIEREN DER PINS ZU SPRECHERENDEN NAMEN
#define AX0 11
#define AX1 10
#define AX2 9

#define AY0 8
#define AY1 7
#define AY2 6

#define STROBE 5
#define DATA 4
#define RESET 3

// UMRECHNUNG DER ZAHLENINDEXE ZU ZAHLENCODES
// X0, X1, X2, Y0, Y1, Y2
int BinaerCodes[64] [6] =
{
  {1, 0, 0, 0, 0, 0 },
  {0, 0, 0, 0, 0, 1 },  
  {0, 0, 0, 0, 1, 0 },
  {0, 0, 0, 0, 1, 1 },    
};

//Programmstart
void setup() 
{   
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(3, OUTPUT);

  digitalWrite (RESET, LOW);
  digitalWrite (STROBE, LOW);
  
  Serial.begin(9600); 
  MyBlue.begin(9600); 
  Serial.println("Ready to connect\nDefualt password is 1234 or 000"); 
} 

//MAIN LOOP
void loop() 
{ 
   //Check if Bluetooth is Available
   if (MyBlue.available()) 
   { 
       //Read and Transform Bluetooth Signal
       int text = MyBlue.read();
       char temp = char(text);

       //Record Mutliple Line input and Transform to one String
       if(temp == char(40))
       {
         rec = true;
         resulttext = "";
       }
       if(rec && temp != char(40) && temp != char(41))
       {
         resulttext += temp;
       }
       if(temp == char(41))
       {
         rec = false; 
         //Here come the Code
         Serial.println(resulttext);
         StringSplit(resulttext);
       }
   }
}  

// AUSFÜHREN DER METHODE SWITCH_SWITCH_NEW MIT DEN PARAMETERN AUS DEM ZAHLENARRAY
void run_switch_new(int Character, boolean sense)
{
  Serial.println("Löst aus Taste: " + String(Character) + " Mit Funktion: " + String(sense) );
  switch_switch_new (BinaerCodes[Character] [0], BinaerCodes[Character] [1], BinaerCodes[Character] [2], BinaerCodes[Character] [3], BinaerCodes[Character] [4], BinaerCodes[Character] [5], sense);
}

// SETZEN EINES NEUEN PINS 
void switch_switch_new (int AX0p, int AX1p, int AX2p, int AY0p, int AY1p, int AY2p, boolean sense)
{
  digitalWrite (AX0, AX0p);
  digitalWrite (AX1, AX1p);
  digitalWrite (AX2, AX2p);
  
  digitalWrite (AY0, AY0p);
  digitalWrite (AY1, AY1p);
  digitalWrite (AY2, AY2p);

  digitalWrite (DATA, sense);
  digitalWrite (STROBE, HIGH);
  digitalWrite (STROBE, LOW);
  
}

// MERKEN FÜR SPÄTER
void StringSplit(String PayloadParam)
{
  String Payload = PayloadParam;
  int index = Payload.indexOf(',');
  int length = Payload.length();
  String Number = Payload.substring(0,index);
  String Sense  = Payload.substring(index+1,length);
  run_switch_new(Number.toInt(), true);
}
