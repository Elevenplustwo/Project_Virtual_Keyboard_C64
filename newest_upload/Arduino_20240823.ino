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
#define RECHTS 14 
#define FEUER 15

// UMRECHNUNG DER ZAHLENINDEXE ZU ZAHLENCODES
// X0, X1, X2, Y0, Y1, Y2
int BinaerCodes[66] [6] =
{
  {0, 0, 1, 1, 1, 1 },   //BTN ARROW LEFT
  {0, 0, 0, 1, 1, 1 },   //BTN ONE  
  {0, 1, 1, 1, 1, 1 },   //BTN TWO
  {0, 0, 0, 0, 0, 1 },   //BTN THREE  
  {0, 1, 1, 0, 0, 1 },   //BTN FOUR
  {0, 0, 0, 0, 1, 0 },   //BTN FIVE
  {0, 1, 1, 0, 1, 0 },   //BTN SIX
  {0, 0, 0, 0, 1, 1 },   //BTN SEVEN
  {0, 1, 1, 0, 1, 1 },   //BTN EIGHT
  {0, 0, 0, 1, 0, 0 },   //BTN NINE
  {0, 1, 1, 1, 0, 0 },   //BTN ZERO
  {0, 0, 0, 1, 0, 1 },   //BTN PLUS
  {0, 1, 1, 1, 0, 1 },   //BTN MINUS
  {0, 0, 0, 1, 1, 0 },   //BTN POUND
  {0, 1, 1, 1, 1, 0 },   //BTN HOME
  {0, 0, 0, 0, 0, 0 },   //BTN DEL
  {1, 0, 0, 0, 0, 0 },   //BTN F1 F2
  {0, 1, 0, 1, 1, 1 },   //BTN CNTRL
  {1, 1, 0, 1, 1, 1 },   //BTN Q
  {0, 0, 1, 0, 0, 1 },   //BTN W
  {1, 1, 0, 0, 0, 1 },   //BTN E
  {0, 0, 1, 0, 1, 0 },   //BTN R
  {1, 1, 0, 0, 1, 0 },   //BTN T
  {0, 0, 1, 0, 1, 1 },   //BTN Y
  {1, 1, 0, 0, 1, 1 },   //BTN U
  {0, 0, 1, 1, 0, 0 },   //BTN I
  {1, 1, 0, 1, 0, 0 },   //BTN O
  {0, 0, 1, 1, 0, 1 },   //BTN P
  {1, 1, 0, 1, 0, 1 },   //BTN AT
  {0, 0, 1, 1, 1, 0 },   //BTN ASTERISK
  {1, 1, 0, 1, 1, 0 },   //BTN ARROW UP
  {0, 0, 0, 0, 0, 0 },   //--------------- RESTORE
  {1, 0, 1, 0, 0, 0 },   //BTN F3 F4
  {1, 1, 1, 1, 1, 1 },   //BTN RUN STOP
  {0, 0, 0, 0, 0, 0 },   //--------------- SHIFT LOCK
  {0, 1, 0, 0, 0, 1 },   //BTN A
  {1, 0, 1, 0, 0, 1 },   //BTN S
  {0, 1, 0, 0, 1, 0 },   //BTN D
  {1, 0, 1, 0, 1, 0 },   //BTN F
  {0, 1, 0, 0, 1, 1 },   //BTN G
  {1, 0, 1, 0, 1, 1 },   //BTN H
  {0, 1, 0, 1, 0, 0 },   //BTN J
  {1, 0, 1, 1, 0, 0 },   //BTN K
  {0, 1, 0, 1, 0, 1 },   //BTN L
  {1, 0, 1, 1, 0, 1 },   //-------------- BRACE OPEN
  {0, 1, 0, 1, 1, 0 },   //-------------- BRACE CLOSE
  {1, 0, 1, 1, 1, 0 },   //BTN EQUAL
  {0, 0, 1, 0, 0, 0 },   //BTN RETURN
  {1, 1, 0, 0, 0, 0 },   //BTN F5 F6
  {1, 0, 1, 1, 1, 1 },   //BTN COMMORDORE
  {1, 1, 1, 0, 0, 1 },   //BTN SHIFT
  {1, 0, 0, 0, 0, 1 },   //BTN Z
  {1, 1, 1, 0, 1, 0 },   //BTN X
  {1, 0, 0, 0, 1, 0 },   //BTN C
  {1, 1, 1, 0, 1, 1 },   //BTN V
  {1, 0, 0, 0, 1, 1 },   //BTN B
  {1, 1, 1, 1, 0, 0 },   //BTN N
  {1, 0, 0, 1, 0, 0 },   //BTN M
  {1, 1, 1, 1, 0, 1 },   //BTN COMMA
  {1, 0, 0, 1, 0, 1 },   //BTN DOT
  {1, 1, 1, 1, 1, 0 },   //BTN SLASH
  {1, 0, 0, 1, 1, 0 },   //BTN SHIFT RIGHT
  {1, 1, 1, 0, 0, 0 },   //BTN CURSOR UP DOWN
  {0, 1, 0, 0, 0, 0 },   //BTN CURSOR LEFT RIGHT
  {0, 1, 1, 0, 0, 0 },   //BTN F7 F8
  {1, 0, 0, 1, 1, 1 },   //BTN SPACE  
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

  //Joystick (auf low ziehen)
  //pinMode(12, INPUT);
  //pinMode(2, INPUT); 
  //pinMode(13, INPUT);
  //pinMode(14, INPUT);
  //pinMode(15, INPUT);
  
  //Joystick (Mit Oktopoppern)
  pinMode(12, OUTPUT);
  pinMode(2, OUTPUT); 
  pinMode(13, OUTPUT);
  pinMode(14, OUTPUT);
  pinMode(15, OUTPUT);
  

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
  Serial.println("Ready to go"); 
}

//MAIN
void loop() 
{ 
   //Check if Bluetooth is Available
  if (Serial.available()) 
  {
    //Safe received value into receivedInt as integer
    unsigned int receivedInt = Serial.read();
	
    Serial.println(receivedInt);
    //call function to interpret receivedInt
    InterpretReceivedInt(receivedInt);
  }
}  

// AUSFÜHREN DER METHODE SWITCH_SWITCH_NEW MIT DEN PARAMETERN AUS DEM ZAHLENARRAY
void run_switch_new(int Character, boolean sense)
{
  boolean test = false;
  Serial.println("Löst aus Taste: " + String(Character) + " Mit Funktion: " + String(sense) );
  Serial.println(String(sense));
  if(Character < 67 )
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
     if(Character == 71) //Oben
     {
       Serial.println("Key: Oben");
       //SET OBEN HIGH
       //pinMode(VORNE, OUTPUT);
       //digitalWrite(VORNE, LOW);
       digitalWrite(VORNE, HIGH);
       //SET REST LOW
       //pinMode(RECHTS, INPUT);
       //pinMode(LINKS, INPUT);
       //pinMode(HINTEN, INPUT);
       digitalWrite(RECHTS, LOW);
       digitalWrite(LINKS, LOW);
       digitalWrite(HINTEN, LOW);
     }
     if(Character == 72) //Oben Rechts
     {
       Serial.println("Key: Oben Rechts");
       //SET OBEN HIGH
       //pinMode(VORNE, OUTPUT);
       //digitalWrite(VORNE, LOW);
       digitalWrite(VORNE, HIGH);
       //SET RECHTS HIGH
       //pinMode(RECHTS, OUTPUT);
       //digitalWrite(RECHTS, LOW);
       digitalWrite(RECHTS, HIGH);
       //SET REST LOW
       //pinMode(LINKS, INPUT);
       //pinMode(HINTEN, INPUT);
       digitalWrite(LINKS, LOW);
       digitalWrite(HINTEN, LOW);
     }
     if(Character == 73) //Rechts
     {
       Serial.println("Key: Rechts");
       //SET RECHTS
       //pinMode(RECHTS, OUTPUT);
       //digitalWrite(RECHTS, LOW);
       digitalWrite(RECHTS, HIGH);
       //SET REST LOW
       //pinMode(VORNE, INPUT);
       //pinMode(LINKS, INPUT);
       //pinMode(HINTEN, INPUT);
       digitalWrite(LINKS, LOW);
       digitalWrite(VORNE, LOW);
       digitalWrite(HINTEN, LOW);
     }
     if(Character == 74) //Unten Rechts
     {
       Serial.println("Key: Unten Rechts");
       //SET UNTEN HIGH
       //pinMode(HINTEN, OUTPUT);
       //digitalWrite(HINTEN, LOW);
       digitalWrite(HINTEN, HIGH);
       //SET RECHTS HIGH
       //pinMode(RECHTS, OUTPUT);
       //digitalWrite(RECHTS, LOW);
       digitalWrite(RECHTS, HIGH);
       //SET REST LOW
       digitalWrite(LINKS, LOW);
       digitalWrite(VORNE, LOW);
     }
     if(Character == 75) //Unten
     {
       Serial.println("Key: Unten");
       //SET HINTEN
       //pinMode(HINTEN, OUTPUT);
       //digitalWrite(HINTEN, LOW);
       digitalWrite(HINTEN, HIGH);
       //SET REST LOW
       //pinMode(VORNE, INPUT);
       //pinMode(LINKS, INPUT);
       //pinMode(RECHTS, INPUT);
       digitalWrite(RECHTS, LOW);
       digitalWrite(LINKS, LOW);
       digitalWrite(VORNE, LOW);
     }
     if(Character == 76) //Unten Links
     {
       Serial.println("Key: Unten Links");
       //SET HINTEN HIGH
       //pinMode(HINTEN, OUTPUT);
       //digitalWrite(HINTEN, LOW);
       digitalWrite(HINTEN, HIGH);
       //SET LINKS HIGH
       //pinMode(LINKS, OUTPUT);
       //digitalWrite(LINKS, LOW);
       digitalWrite(LINKS, HIGH);
       //SET REST LOW
       //pinMode(RECHTS, INPUT);
       //pinMode(VORNE, INPUT);
       digitalWrite(RECHTS, LOW);
       digitalWrite(VORNE, LOW);
     }
     if(Character == 77) //Unten
     {
       Serial.println("Key: Links");
       //SET LINKS
       //pinMode(LINKS, OUTPUT);
       //digitalWrite(LINKS, LOW);
       digitalWrite(LINKS, HIGH);
       //SET REST LOW
       //pinMode(VORNE, INPUT);
       //pinMode(HINTEN, INPUT);
       //pinMode(RECHTS, INPUT);
       digitalWrite(VORNE, LOW);
       digitalWrite(RECHTS, LOW);
       digitalWrite(VORNE, LOW);
       
     }
     if(Character == 78) //OBen Links
     {
       Serial.println("Key: Oben Links");
       //SET VORNE HIGH
       //pinMode(VORNE, OUTPUT);
       //digitalWrite(VORNE, LOW);
       digitalWrite(VORNE, HIGH);
       //SET LINKS HIGH
       //pinMode(LINKS, OUTPUT);
       //digitalWrite(LINKS, LOW);
       digitalWrite(LINKS, HIGH);
       //SET REST LOW
       //pinMode(RECHTS, INPUT);
       //pinMode(HINTEN, INPUT);
       digitalWrite(RECHTS, LOW);
       digitalWrite(HINTEN, LOW);
     }
     if(Character == 79) //MITTEs
     {
       Serial.println("Key: MITTE");
       //SET REST LOW
       //pinMode(RECHTS, INPUT);
       //pinMode(HINTEN, INPUT);
       //pinMode(LINKS, INPUT);
       //pinMode(VORNE, INPUT);
       digitalWrite(RECHTS, LOW);
       digitalWrite(HINTEN, LOW);
       digitalWrite(LINKS, LOW);
       digitalWrite(VORNE, LOW);
     }
     if(Character == 80) //FEUER
     {
       Serial.println("Key: FEUER");
       //SET REST LOW
       if (sense == 0)
       {
         //pinMode(FEUER, INPUT);
         digitalWrite(FEUER, LOW);
       }else{
         //pinMode(FEUER, OUTPUT);
         //digitalWrite(FEUER, LOW);
         digitalWrite(FEUER, HIGH);
       }
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

// AUSWERTEN DES EMPFANGENEN INT
void InterpretReceivedInt(int receivedInt)
{
  boolean Sense = false;
  int character = receivedInt;
  //if character > 100, set Sense to False (HIGH) and take value (character - 100)
  if (character > 100)
  {
    character = character - 100;
    Sense = true;
  }
  else
  {
    Sense = false;
  }
  run_switch_new(character, Sense);
}
