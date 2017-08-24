
int ledr = 13;
int ledp = 10; 
int ledy = 7;
const int sound = 4;

void setup() {
  // put your setup code here, to run once:.
pinMode (ledr, OUTPUT);
pinMode (ledp, OUTPUT);
pinMode (ledy, OUTPUT);
pinMode (sound, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite (ledr, HIGH);
delay (1000);
digitalWrite (ledp, HIGH);
delay(700);
digitalWrite (ledy, HIGH);
tone (sound, 7);
delay (400);
digitalWrite(ledr, LOW);
delay (1000);
digitalWrite(ledp, LOW);
delay (700);
digitalWrite(ledy, LOW);
delay (400);
tone (sound, 0);

digitalWrite (ledr, LOW);
delay (00);
digitalWrite (ledp, LOW);
delay (1000);
tone (sound, 3);
digitalWrite (ledy, LOW);
delay(500);
digitalWrite (ledy, HIGH);
delay (400);
digitalWrite (ledy, LOW);
digitalWrite (ledr, HIGH);
delay (300);
tone (sound, 9);
digitalWrite (ledr, LOW);
delay (200);
digitalWrite (ledy, HIGH);
delay (1000);
digitalWrite (ledy, LOW);
delay (500);
}
