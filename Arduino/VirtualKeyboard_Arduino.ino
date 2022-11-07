#include <SoftwareSerial.h> 
SoftwareSerial MyBlue(14, 15); // RX | TX 
boolean rec = false;
String resulttext = "";
boolean pinmode = 1;

// DEFINIEREN DER PINS ZU SPRECHERENDEN NAMEN
#define CSW 16 //Joystick: Switch

#define Z1 17 //Key: Freeze
#define Z2 18 //Key: Reset
#define Z3 19 //Key: Menu

#define AX0 11
#define AX1 10
#define AX2 9

#define AY0 8
#define AY1 7
#define AY2 6

#define STROBE 5
#define DATA 4
#define RESET 3

#define VORNE 12
#define HINTEN 2
#define LINKS 13
#define RECHTS 20
#define FEUER 21

// UMRECHNUNG DER ZAHLENINDEXE ZU ZAHLENCODES
// X0, X1, X2, Y0, Y1, Y2
int BinaerCodes[66] [6] =
{
  {1, 1, 0, 1, 1, 1 },   //BTN ARROW LEFT
  {1, 1, 1, 1, 1, 1 },   //BTN ONE  
  {0, 0, 0, 1, 1, 1 },   //BTN TWO
  {1, 1, 1, 1, 1, 0 },   //BTN THREE  
  {0, 0, 0, 1, 1, 0 },   //BTN FOUR
  {1, 1, 1, 1, 0, 1 },   //BTN FIVE
  {0, 0, 0, 1, 0, 1 },   //BTN SIX
  {1, 1, 1, 1, 0, 0 },   //BTN SEVEN
  {0, 0, 0, 1, 0, 0 },   //BTN EIGHT
  {1, 1, 1, 0, 1, 1 },   //BTN NINE
  {0, 0, 0, 0, 1, 1 },   //BTN ZERO
  {1, 1, 1, 0, 1, 0 },   //BTN PLUS
  {0, 0, 0, 0, 1, 0 },   //BTN MINUS
  {1, 1, 1, 0, 0, 1 },   //BTN POUND
  {0, 0, 0, 0, 0, 1 },   //BTN HOME
  {1, 1, 1, 0, 0, 0 },   //BTN DEL
  {0, 1, 1, 0, 0, 0 },   //BTN F1 F2
  {1, 0, 1, 1, 1, 1 },   //BTN CNTRL
  {0, 0, 1, 1, 1, 1 },   //BTN Q
  {1, 1, 0, 1, 1, 0 },   //BTN W
  {0, 0, 1, 1, 1, 0 },   //BTN E
  {1, 1, 0, 1, 0, 1 },   //BTN R
  {0, 0, 1, 1, 0, 1 },   //BTN T
  {1, 1, 0, 1, 0, 0 },   //BTN Y
  {0, 0, 1, 1, 0, 0 },   //BTN U
  {1, 1, 0, 0, 1, 1 },   //BTN I
  {0, 0, 1, 0, 1, 1 },   //BTN O
  {1, 1, 0, 0, 1, 0 },   //BTN P
  {0, 0, 1, 0, 1, 0 },   //BTN AT
  {1, 1, 0, 0, 0, 1 },   //BTN ASTERISK
  {0, 0, 1, 0, 0, 1 },   //BTN ARROW UP
  {0, 0, 0, 0, 0, 0 },   //--------------- RESTORE
  {0, 1, 0, 0, 0, 0 },   //BTN F3 F4
  {1, 0, 0, 1, 1, 1 },   //BTN RUN STOP
  {0, 0, 0, 0, 0, 0 },   //--------------- SHIFT LOCK
  {1, 0, 1, 1, 1, 0 },   //BTN A
  {0, 1, 0, 1, 1, 0 },   //BTN S
  {1, 0, 1, 1, 0, 1 },   //BTN D
  {0, 1, 0, 1, 0, 1 },   //BTN F
  {1, 0, 1, 1, 0, 0 },   //BTN G
  {0, 1, 0, 1, 0, 0 },   //BTN H
  {1, 0, 1, 0, 1, 1 },   //BTN J
  {0, 1, 0, 0, 1, 1 },   //BTN K
  {1, 0, 1, 0, 1, 0 },   //BTN L
  {0, 1, 0, 0, 1, 0 },   //-------------- BRACE OPEN
  {1, 0, 1, 0, 0, 1 },   //-------------- BRACE CLOSE
  {0, 1, 0, 0, 0, 1 },   //BTN EQUAL
  {1, 1, 0, 0, 0, 0 },   //BTN RETURN
  {0, 0, 1, 0, 0, 0 },   //BTN F5 F6
  {0, 1, 0, 1, 1, 1 },   //BTN COMMORDORE
  {1, 0, 0, 1, 1, 0 },   //BTN SHIFT
  {0, 1, 1, 1, 1, 0 },   //BTN Z
  {1, 0, 0, 1, 0, 1 },   //BTN X
  {0, 1, 1, 1, 0, 1 },   //BTN C
  {1, 0, 0, 1, 0, 0 },   //BTN V
  {0, 1, 1, 1, 0, 0 },   //BTN B
  {1, 0, 0, 0, 1, 1 },   //BTN N
  {0, 1, 1, 0, 1, 1 },   //BTN M
  {1, 0, 0, 0, 1, 0 },   //BTN COMMA
  {0, 1, 1, 0, 1, 0 },   //BTN DOT
  {1, 0, 0, 0, 0, 1 },   //BTN SLASH
  {0, 1, 1, 0, 0, 1 },   //BTN SHIFT RIGHT
  {1, 0, 0, 0, 0, 0 },   //BTN CURSOR UP DOWN
  {1, 0, 1, 0, 0, 0 },   //BTN CURSOR LEFT RIGHT
  {0, 0, 0, 0, 0, 0 },   //BTN F7 F8
  {0, 1, 1, 1, 1, 1 },   //BTN SPACE  
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
  pinMode(16, OUTPUT);
  pinMode(17, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(13, OUTPUT);
  //pinMode(1, OUTPUT);
  //pinMode(0, OUTPUT);

  digitalWrite (RESET, LOW);
  digitalWrite (STROBE, LOW);

  //digitalWrite (0, HIGH);
  //digitalWrite (1, HIGH);

  //analogWrite (6, 255);
  //analogWrite (7, 255);

  //LINKS = 12
  //REchts = 2
  //Hoch = 13

  //VIOLETT = FEUER
  //ORANGE = LINKS
  //GELB = RECHTS
  //BLAU = UNTEN
  //GRÜN = OBEN
  
  Serial.begin(9600); 
  MyBlue.begin(9600); 
  Serial.println("Ready to connect\nPassword is 1234"); 
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
         //Full recieved String Output for Debugging
         Serial.println(resulttext);
         StringSplit(resulttext);
       }
   }
}  

// AUSFÜHREN DER METHODE SWITCH_SWITCH_NEW MIT DEN PARAMETERN AUS DEM ZAHLENARRAY
void run_switch_new(int Character, boolean sense)
{
  boolean test = false;
  Serial.println("Löst aus Taste: " + String(Character) + " Mit Funktion: " + String(sense) );
  Serial.println(String(sense));
  if(Character != 70 && Character != 69 && Character != 68 && Character != 67&& Character != 71 && Character != 72 && Character != 73 && Character != 74 && Character != 75 )
  {
    switch_switch_new (BinaerCodes[Character -1] [5], BinaerCodes[Character -1] [4], BinaerCodes[Character -1] [3], BinaerCodes[Character -1] [2], BinaerCodes[Character -1] [1], BinaerCodes[Character -1] [0], sense);
  }else{
    if(Character == 70) //Joystick
    {
      if(sense == 0) //Only React Onces --> Recieving (Low & High) signal but only react on LOW 
      {
        if(pinmode == 0)
        {
          Serial.println("Joystick Switch: Low");
          pinmode = 1;
          digitalWrite (CSW, LOW);
        }else{
          Serial.println("Joystick Switch: HIGH");
          pinmode = 0;
          digitalWrite (CSW, HIGH);
        }
       }
     }
     if(Character == 69) //Key: Reset
     {
        Serial.println("Key: Reset");
        digitalWrite (Z2, sense);
     }
     if(Character == 68) //Key: Menu
     {
       Serial.println("Key: Menu");
       digitalWrite (Z3, sense);
     }
     if(Character == 67) //Key: Freeze
     {
       Serial.println("Key: Freeze");
       digitalWrite (Z1, sense);
     }
     if(Character == 71) //Key: LINKS
     {
       Serial.println("Key: LINKS");
       digitalWrite (LINKS, sense);
     }
     if(Character == 72) //Key: RECHTS
     {
       Serial.println("Key: RECHTS");
       digitalWrite (RECHTS, sense);
     }
     if(Character == 73) //Key: VORNE
     {
       Serial.println("Key: VORNE");
       digitalWrite (VORNE, sense);
     }
     if(Character == 74) //Key: HINTEN
     {
       Serial.println("Key: HINTEN");
       digitalWrite (HINTEN, sense);
     }
     if(Character == 75) //Key: Feuer
     {
       Serial.println("Key: Feuer");
       digitalWrite (FEUER, sense);
     }
     
    }
  }


// SETZEN EINES NEUEN PINS 
void switch_switch_new (int AX0p, int AX1p, int AX2p, int AY0p, int AY1p, int AY2p, boolean sense)
{
  Serial.println(AX0p);
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

// STRING IN NUMBER UND SENSE SPLITTEN
void StringSplit(String PayloadParam)
{
  String Payload = PayloadParam;
  int index = Payload.indexOf(',');
  int length = Payload.length();
  String Number = Payload.substring(0,index);
  String SenseString  = Payload.substring(index+1,length);
  boolean Sense = false;
  Serial.println(Sense);
  if(SenseString == "LOW")
  {
    Sense = false;  
  }
  else{
    Sense = true;  
  }
  run_switch_new(Number.toInt(), Sense);
}
