## Overview
The intent of this project is to easily capture InfraRed signals from a remote control, and then create Arduino functions to replicate the signal.

### 1. Setup Arduino

* Setup Arduino and [IR sensor](http://www.adafruit.com/products/157) to capture IR signals and print them to a serial monitor

* Code Arduino is running: [Arduino Sketch](../master/rawirdecode/rawirdecode.ino)
![Arduino setup](https://s3.amazonaws.com/octoporess_blog/github_media/IMG_1223.JPG =450x "Arduino setup IR receiver")


### 2. Capture IR Codes
* Point remote at IR sensor, and capture resulting data in files to process later
![IR signals from serial](https://s3.amazonaws.com/octoporess_blog/github_media/animation.gif "IR signals from serial")

### 3. Process Captured IR Codes
* Different observations of the same signal will capture slightly different codes because of processor overhead and light interference.

For example, the first observation of the signal from the `ON` bottom might show 

```
++++++++++++++++  ++++++++++++++++  ++++++++++++++++
|Observation 1 |  |Observation 2 |  |Observation 3 |
|-------|------|  |-------|------|  |-------|------|
| OFF   | ON   |  | OFF   | ON   |  | OFF   | ON   |
|-------|------|  |-------|------|  |-------|------|
| 1660  | 600  |  | 1660  | 580  |  | 1660  | 580  |
| 40620 | 8920 |  | 40580 | 8940 |  | 40580 | 8960 |
| 2200  | 580  |  | 2180  | 580  |  | 2160  | 600  |
++++++++++++++++  ++++++++++++++++  ++++++++++++++++

```

In this case each observation needs to be averaged together and rounded properly.

### 4. Create Arduino Functions that replicate capture IR codes
* Now that we know the IR codes, we can create an Arduino function that we can call to emit the same IR code that the remote-control did.

For example, the code for the `ON` would be (ignore first `OFF` and use arbitrary last `OFF`):

```
void SendON(){
  pulseIR(580);    delayMicroseconds(40600);
  pulseIR(8940);    delayMicroseconds(2180);
  pulseIR(580);    delayMicroseconds(2200);  
}
```
