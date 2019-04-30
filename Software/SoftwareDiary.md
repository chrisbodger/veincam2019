# Software Log

### Week Beginning 04/03/2019
* Took time to understand the previous code at a high level with help from previous team members
    * Resulted in the creation of a Visio diagram to visualize the overall system and what files were being used in what order.
    * Used the existing functioning RPi Zero to understand the limitations it currently has and how it performed under different conditions
* Ensured screen capture capabilities were working for virtual meetings for later code visualisation

### Week Beginning 11/03/2019
* Identified areas of optimisation and improvement including:
    * Further image processing to better identify the veins
    * Optimisation of boot time and better indication to user of the boot progress
    * Improving front-end web page including more options, functionality, usability and information
    * General code cleaning and optimisation
* Static image processing testing was set up for quick idea verification using MATLAB given its inbuilt image processing capabilities
* Steps were taken towards getting the existing code's 'development' mode working on a windows machine for easy testing using the Flask server

### Week Beginning 18/03/2019
* Officially got development server working on multiple Windows 10 systems
    * Using this the cropping and histogram image regions were adjusted for better testing
    * Variables such as frame rate and histogram equalisation values were generalised for easier testing as well
* Brainstorming took place discussing how a new front end might look and whether a small loading screen would be beneficial
    * An example loading gif was made with external help to be implemented later on


### Week Beginning 25/03/2019
* Initial VeinCam software was tested on the newly acquired hardware
    * Existing software proved to work on both the Pi A+, B+ and Zero W models
* Begun testing the software for bottlenecks: mainly looking for boot time and frame rate issues
    * Image processing confirmed not to be a problem through testing on camera_piopencv
        * Also investigated image resolution, array storage, pi gpu memory, server refresh rate, 
        camera video capabilities, and frame rate manipulation on the development server.
    * Looks as though the python script speed is not the cause of poor frame rate.
    * CPU capabilities were ruled out as cause of poor frame rate
    * More investigation needs to be done to find the root cause of poor frame rate
    
### Week Beginning 01/04/2019
* Cause of poor frame rate was found to be method of capturing images for processing as pi camera has small amount
of inbuilt post processing on captured images in specific formats
* Changed to a MJPEG stream and captured images via splitting bytes string.
    * Was followed up by decoding to a row vector and converting to a grey scale image
    * This did lose a small amount of image quality and hence will investigate how we can improve this
    * Initial tests indicate that now the pi A+ is capable of 30 FPS and the Zero W ~5-10 FPS
* Code was changed so that LEDs were mapped to correct pins on new prototype VeinCam/Plus hardware
* Code was improved slightly for readability, much more will be done on this now that frame rate is fixed
    * New code will be uploaded once this to a reasonable standard as at the moment code has had to be changed almost
    entirely via nano text editor so this is a slow process, even with local SSH capabilities
* Development started to better indicate boot progress with new boot and status LEDs. Will continue into next week.

### Week Beginning 08/04/2019
* Boot LED now writes directly after Pi finishes normal boot process
    * This gives a better indication of boot progress, talk of using hardware to put this light on from actual boot (using negative logic)
    * General syntax fixes were made to camera_emulated code
* General testing of current revision of code was done to test camera under different lighting conditions
    * Linear artifacts were noticed most likely due to MJPEG stream
    
## Week Beginning 15/04/2019
* Planning for how code would be cleaned (mainly converging camera_piopencv and camera_base) including defining each function and how they interact with eachother
* Plans for how software will move forward were set
    * It is difficult to say whether Image quality can be further improved
        * This is due to the capabilities of the pi. Resolution is tied to Field of View
        * Almost no image processing is done and even with image processing off, frame rate and quality does not improve
        * Changes to camera settings such as sharpness, gain, etc. do not make the image more clear especially in temrms of veins and can slightly reduce framerate.
* Plans to make a code document for how each function works for educational tools and handover will be made once cleanup has commenced

## Week Beginning 22/04/19
* Code for camera_piopencv and camera_base was significantly changed to now be in one file with only three classes
    * Readability was improved, many code redundancies were found and removed, and many other minor variable name changes and syntax fixes were changed for user readability
* Small amount of commenting was added, and references to open source code were kept where necessary.
* Small hardware faults and changes were pointed out and fixed or revised for further board spins including:
    * IR LEDs being the on the opposite pins to what they were on original schematics
        * This was changed in software and subsequently changed on the schematic
    * SD card is still too difficult to remove, although it was brought up whether we want to be able to remove it at all depending age group client wants to most target
        * Notch in current acrylic will be made slightly wider
    * HDMI port on the A+ gets a little too hot after prolonged use of having the camera on (maybe 10 minutes)
        * This will be brought up with the client as future iterations of the project may want to go to a fully enclosed design
        * For the moment, the acrylic was made slightly wider on all sides
        
## Week Beginning 29/04/2019
* Plans of how app.py will be cleaned and made more readable
* Feedback from client of current software (outputs not actual code) were acted upon where necessary
    * Meeting will be set up as to where the software needs to go within the next three weeks
    * In the meantime app.py will be cleaned, software documentation will be written (including how each function works with new Visio diagram)
        * This will hopefully be included in current front end soon
* Some other members will now move on to helping with front end ideas implementation
    * First priority is getting loading GIF working, and making current front end mobile friendly especially with the video output