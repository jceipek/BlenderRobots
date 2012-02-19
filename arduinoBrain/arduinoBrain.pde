//
// arduinoBrain.pde - reads from the RX digital pin
// to get values from the EEG
//
// Based on "brain example" by Eric Mika, 2010
//

#include <Brain.h>

// Set up the brain parser, pass it the hardware serial object you want to listen on.
Brain brain(Serial);

void setup() {	
	// Start the hardware serial.
	Serial.begin(9600);
}

void loop() {
	// Expect packets about once per second.
	if (brain.update()) {
		//Serial.println("EEG:"+String(brain.readCSV())); //Reads from the Mindflex EEG
                Serial.println(String(brain.readCSV())); //Reads from the Mindflex EEG
	}
	
}
