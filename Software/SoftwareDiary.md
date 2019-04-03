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