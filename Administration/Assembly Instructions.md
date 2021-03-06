# Assembly Instructions

### Hardware
* Using the M2 screws, attach the NoIR Camera on the underside of the VeinCam hat. 
* Plug the flat flex cable into the camera connector on the Raspberry Pi.
* Connect the VeinCam hat to the Raspberry Pi, ensuring that the flat flex cable does not get pinched. The cable routing is not ideal, but it will all fit inbetween the two boards. 
* Follow the [Software](#Software) instructions to get the board up and running. This is required before continuing assembly as the cameras focus cannot be changed after assembly.
* Using the cross shaped cutout on the VeinCam back panel, adjust the focus ring on the camera until objects 20-30cm away from the lens are in focus. It may be required to use pliers or tweezers to initially move the focus ring, however once it is loose the provided tool can be used. 
* Insert the IR filter into the small cutout on the front acrylic panel. It will only go in from the back side of the acrylic, so if it does not fit try flipping the parts around until they fit. 
* Place the M2.5 screws through the front panel and place on the table top down. Slide 3mm spacers over the screws, one per screw.
* Position the 11mm spacers between the VeinCam hat and the Raspberry PI. Locate the holes in the VeinCam hat over the M2.5 screws and slide into position. May require moving the 11mm spacers until they line up with the holes. 
* Place the remaining 3mm spacers on top of the Raspberry Pi. Install the rear acrylic with the SD card cutout located over the SD card, and install the M2.5 nuts. Using a phillips head screwdriver tighted the screws until snug. 
* Congratulations, you can now look at your veins!    


### Software

#### Connecting to the pi

* Apply power to the raspberry pi through the USB power port
* Wait for the pi to boot, indicated by the 'ready' LED
* Connect to the pi's wifi network on the chosen device
* Connect to the VeinCam server through a web browser on the chosen device
* Press the 'on' switch to activate the camera  

#### Changing the user parameters 

* To change the base URL: 
    - Change the `10.0.0.5` variable in the autohotspot launch script

* To change the wifi name:
    - ssh into the pi 
    - Run: `cd /etc/`
    - Run: `nano hostname`
    - Change the host name
    - When finished press `ctrl + x`, `Y`, `Enter`
