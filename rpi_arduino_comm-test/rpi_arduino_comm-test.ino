int counter = 0;//1 ha megkapta az emelet- és a sorszámot
String row = "";
String floor = "";

void setup() {
  Serial.begin(9600);
}
void loop(){

  if((Serial.available()>0) && counter == 0){
    floor = Serial.readStringUntil('\n');
    row = Serial.readStringUntil('\n');
    counter = 1;    //delay(1000);
  }
  if(counter == 1)
    Serial.println("fin");
    //delay(1000);
  
}
