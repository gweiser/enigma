The hardware for Enigma consists of three main parts:

- Keyboard
- Lampboard
- Rotor Configuration Interface (RCI)

All three systems connect to a Raspberry Pi Pico on a PCB, which runs the code. I decided against building the plugboard, as I had a strict deadline with this being my final project for school and I would not have had the time to design this feature as well.


## Keyboard
The keyboard consists of 26 push-buttons screwed onto a wooden board. The buttons are connected to screw terminals, soldered to a 5x5 diode matrix, which is in turn soldered to a Sparkfun [SX1509 Expander Breakout board.](https://www.sparkfun.com/sparkfun-16-output-i-o-expander-breakout-sx1509.html).


<img name="diodematrix" src="https://github.com/user-attachments/assets/a2172c4a-a325-4448-8583-f6457253375c" width="50%" height="50%">
<p></p>
<img name="keyboard" src="https://github.com/user-attachments/assets/c9cdc9da-8833-4581-ba29-0fc2521e1bb3" width="70%" height="70%">

## Lampboard
The lampboard consists of 26 mini-LEDs, whch fit into holes drilled into a wooden board. The distances between the lamps equal those of the keyboard. Each LED is soldered onto a SX1509 Expander Breakout board, which is why I added two of them. The lamps are covered by laminated letters slotted into a 3D-printed mount I designed. 

<img name="lamps" src="https://github.com/user-attachments/assets/5295385d-0ebf-4bc4-b6cf-b65de1191872" height="50%" width="50%">

<img name="lampboardcover" src="https://github.com/user-attachments/assets/ac46c7f5-5210-4b78-9620-d2e25dd0b955" width="50%" height="50%">


## Rotor Configuration Interface
In order to change the rotor, ring setting and starter position, the user selects a value using the first three push buttons and lock them in using the rightmost button. The values are displayed on a 16x2 LCD fitted with an I2C adapter.

<img name="rci" src="https://github.com/user-attachments/assets/1c8520de-e8e3-497e-8d0f-af21736ed1bd" width="50%" height="50%">


## PCB
I designed a PCB in KiCad to connect all screw terminals to the Pi Pico.

<img name="pcbempty" src="https://github.com/user-attachments/assets/6f6d75b5-6219-45e3-869b-99ff5606e799" width="50%" height="50%">  <img name="pcbfull" src="https://github.com/user-attachments/assets/9c24fb57-3ac2-4eef-9e4c-e624f9f44994" width="50%" height="50%">


## Enclosure
I built the wooden box completely from scratch, as I wanted to improve my woodworking skills. The edges are held together by finger joints, which had to fit perfectly.

<img name="box" src="https://github.com/user-attachments/assets/3f3e3f2d-2b0b-471d-ae37-513b7b398563" width="50%" height="50%">

The components of Enigma are screwed into wooden spacers inside the box, so that they sit flush at the top.

<img name="base" src="https://github.com/user-attachments/assets/e7f67551-c5df-4c90-ad00-a8a4b41debe6" width="50%" height="50%">









