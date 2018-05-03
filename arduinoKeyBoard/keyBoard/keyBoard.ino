/*
 * By Alejandro G (Jano)
 * 03/05/2018
 * github.com/imthejano
 * facebook.com/imthejano
 * twitter.com/imthejano
*/
const int outPuts=25;
const int firstPin=22;
int key[outPuts];
int prevKey[outPuts];
void setup() {
  int i;
  for(i=firstPin;i<outPuts;i++){
    pinMode(i,INPUT);
    key[i]=0;
    prevKey[i]=0;
  }
  Serial.begin(115200);
}
String pickKey(int n){
  switch (n){
    case 1:return "a";
    case 2:return "b";
    case 3:return "c";
    case 4:return "d";
    case 5:return "e";
    case 6:return "f";
    case 7:return "g";
    case 8:return "h";
    case 9:return "i";
    case 10:return "j";
    case 11:return "k";
    case 12:return "l";
    case 13:return "m";
    case 14:return "n";
    case 15:return "o";
    case 16:return "p";
    case 17:return "q";
    case 18:return "r";
    case 19:return "s";
    case 20:return "t";
    case 21:return "u";
    case 22:return "v";
    case 23:return "w";
    case 24:return "x";
    default: return "";
  }
}
void loop() {
  int i;
  for(i=0;i<outPuts;i++){
    key[i]=digitalRead(i+firstPin);
  }
  for(i=0;i<outPuts;i++){
    int aux=(i+1)%outPuts;
    if(key[i]==1&&prevKey[i]==0){
      String outS=pickKey(aux);
      if(outS!=""){
        Serial.print(outS);
      }
    }
    prevKey[i]=key[i];
  }
  delay(10);

}
