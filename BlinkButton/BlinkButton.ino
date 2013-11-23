/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
 #include "pitches.h"
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int button = A2;
int buttonState = 0;
int playing = 0;
int buzzerPin = A1;
int debugLed = 13;

// notes in the melody:
int melody[] = {
 0, 195, 220, 233, 261, 233, 174, 0, 195, 220, 233, 261, 233, 195, 220, 233, 0, 233, 261, 233, 174, 293, 0, 311, 293, 261, 293, 233, 261, 195, 220, 0, 233, 261, 233, 174, 195, 220, 233, 261, 0, 233, 0, 0, 195, 220, 233, 174, 0, 174, 349, 293, 0, 233, 195, 311, 293, 261, 293, 0, 261, 0, 0, 174, 349, 293, 261, 349, 293, 233, 195, 0, 0, 0, 174, 233, 311, 293, 261, 0, 0, 195, 0, 220, 233, 0, 174, 0, 174, 0, 0, 349, 261, 293, 233, 0, 233, 0, 233, 195, 0, 0, 311, 293, 261, 293, 261, 0, 0, 0, 174, 349, 293, 261, 349, 293, 233, 195, 174, 155, 0, 0, 0, 174, 233, 311, 293, 261, 0, 0, 195, 0, 220, 0, 233, 0, 174, 0, 174, 349, 261, 293, 233, 0, 233, 233, 195, 174, 311, 0, 293, 261, 233, 0, 233
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {
64, 8, 5, 10, 5, 6, 28, 2, 9, 4, 10, 6, 34, 9, 5, 10, 1, 4, 5, 4, 7, 20, 1, 8, 5, 10, 5, 2, 33, 8, 4, 1, 11, 8, 4, 28, 9, 5, 10, 4, 1, 32, 1, 2, 9, 5, 8, 2, 1, 6, 8, 8, 1, 5, 10, 9, 4, 12, 5, 1, 21, 1, 4, 7, 25, 5, 19, 7, 25, 5, 40, 1, 2, 16, 5, 4, 24, 7, 56, 16, 16, 3, 1, 4, 25, 2, 3, 1, 5, 1, 2, 9, 8, 9, 6, 1, 3, 1, 4, 18, 2, 4, 15, 16, 16, 7, 62, 4, 2, 1, 5, 26, 5, 17, 7, 25, 4, 8, 4, 26, 2, 4, 16, 4, 4, 24, 8, 68, 4, 16, 3, 1, 3, 1, 26, 2, 3, 1, 8, 9, 7, 9, 6, 1, 4, 4, 16, 7, 15, 1, 16, 16, 4, 1, 76
};

int thresholds[7] = {0, 174, 233, 261, 293, 311, 311};
int ledPins[7] = {2, 3, 4, 5, 6, 7, 8};
// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  for (int i = 0; i < 7; ++i)
  {
     pinMode(ledPins[i], OUTPUT); 
  }
  pinMode(buzzerPin, OUTPUT);
  pinMode(button, INPUT);
}

void lightLed(int ledNumber, int note)
{
    if (note >= thresholds[ledNumber])
    {
       digitalWrite(ledPins[ledNumber], HIGH);
    }
    else
    {
       digitalWrite(ledPins[ledNumber], LOW); 
    }
}

void playSong()
{
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 158; thisNote++) {

    // to calculate the note duration, take one second 
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = noteDurations[thisNote] * 30;
    tone(buzzerPin, melody[thisNote],noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.3;
    
    for (int i = 0; i < 7; ++i)
    {
        lightLed(i, melody[thisNote]); 
    }
    
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(buzzerPin);
  }
  playing = 0;
  
  for (int i = 0; i < 7; ++i)
  {
     digitalWrite(ledPins[i], LOW); 
  }
}

// the loop routine runs over and over again forever:
void loop() {
  buttonState = digitalRead(button);
  if (buttonState == 0)
  {
  }
  else if (playing == 0)
  {
    playing = 1;
    playSong();
  }
}


