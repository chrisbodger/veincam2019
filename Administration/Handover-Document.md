**INCOMPLETE DRAFT. SEE AFTER WEDNESDAY 15/03 COB**

# Handover Document

This document is intended for the use of the Primary Client Ben Healy, for future project teams who are continuing with this project in future semesters. This document summarizes the development and progress of the project summarised as of November 2018.

## 1. Aims and purpose of this project
This project was started by the client who wished to develop an accessible and low-cost device that could be developed for the public for the purpose of enhanced vein visualisation using infra-red light - the VeinCam.

The client was delivered a preliminary prototype of the VeinCam at the end of the second semester in 2018
A full list of the project goals and stretch goals are in the [Concept of Operations document (ConOps)](/docs/CONOPS.md).

The project team is a group of four undergraduate ANU Engineering Students who completed a course which involved development of something as per the requirements and directions of the client. The course began in July 2018 and completed in November 2018.
A full list of the relevant stakeholders and their responsibilities at this stage of the project are
in the[ConOps](/docs/CONOPS.md).

The requirements developed by the project team and agreed upon by the client are listed in detail in the [Requirements](/docs/REQUIREMENTS.md)

## 2. Key development milestones and decisions
Key decisions are summarised only in this document, with full dates, relevant teams involved and justifications in the [Decision Log](/Administration/Project/Decision-Log.md)

Main milestones in Software and Hardware development are summarised below. For more details, visit their respective work diaries:
[Software Work Diary](/Software/SoftwareDiary.md)
[Hardware Work Diary](/Hardware/Team-Work-Diary.md)


### 2.1. Software Development
####Increased Frame Rate and Functionality
At the beginning of the semester much of the code was taken from open-source resources without many changes; and although this provided a good initial proof of concept of what the VeinCam was capable of. Considering the commercialisation goals for this semester it was important to evaluate what areas the team needed to improve upon for VeinCam to become a viable product. The most obvious of these was the frame rate of the device which at the start of the project was sitting on a max of around 3 FPS. This was fixed by changing to MJPEG recording and splitting the frames within the bytes stream (now 20-30 FPS). After the code had been cleaned (described below) other functionality including the following was added to increase VeinCam's clean aesthetic and list of features:
* The ability to use continuous image capture (YUV - the old method) for very slightly better image quality for taking still image screenshots
* Colour functionality (This only works without the IR filter of course and reduces the frame rate to around 8 FPS), under many lighting conditions this can make the veins stand out quite a bit (Dark Blue colour)
* Dynamic scaling (to a max value) of the image on the web page UI and fixed unnecessary scrolling
* Boot LED will come on after the pi has finished its normal boot process for a better indication of process
* Ready LED will come on once app.py has finished its imports and the server is running
* Camera can now be turned on and off quickly on the server side without causing the app to crash
    * Many other small bug fixes that would cause the script to raise an error under certain conditions

####Code Readability and Room for Extra Features
Following on from improving the frame rate and gathering an understanding of how each of the components of the code worked together, the team wanted to make the code more readable, reduce its complexity and inherently make it more original and flexible so that it could be used better as an open source project for others to expand upon. The two scripts dedicated to the camera functionality and image processing were merged into one with an easy to read three class structure including one class specifically for the new MJPEG stream output. The altering functions within app.py were all merged into one and generally both scripts needed many redundancies removed, variable name changes and other syntax fixes for consistency across the code.

####Potential Improvements
Currently many things could be improved in software for extra functionality. The UI is in very usable state, but could still be more dynamic and better designed for use with mobile devices and very large computer screens (such as projectors). It may be worth looking into building much of what is there from scratch rather than taking almost every HTML class from large css libraries. The possibility of creating a binary image of the veins was investigated though due to the power of raspberry pi, this tended to reduce the frame rate too much, just global or adaptive thresholding alone would put the frame rate down to around 5 FPS on average let alone if you wanted to then perform eroding and dilating. Though it would be good to at least have this option because it can look quite good as a concept. Smart ways of increasing the resolution or even the focus in software could be very useful, as they seemed to be largest part of negative feedback after frame rate from the original design. The raspberry pi's resolution is tied to its field of view so for this project it was decided to first focus on other things.


### 2.2. Hardware Development
####Low cost, easy to assemble enclosure   
Last semester, the previous team had a 3d printed enclosure that was perfect for a prototype, however would not be appropiate for mass manufacturing. As the goal for this semester was to get the product ready for commercialisation, the enclosure was redesigned to allow for production in quantity at a low unit cost, along with being cheap and easy to ship and assemble. This resulted in a laser cut acrylic case which is held together with screws, which is both cheap and easy to manufacture and ship, but can also be assembled easily with a phillips head screwdriver.   

####Design of a highly integrated printed circuit board  
Moving to production hardware required a printed circuit board to hold the IR array, status LEDs, and the NoIR camera. This board played a key role in both the electrical and mechanical design, as on the electrical side it enabled a low cost and easily manufacturable way to connect all of the electronic components, whilst also allowing for the NoIR camera to be mounted in a low profile manner. 

####Potential Improvements
There is still room for improvement in the mechanical design, as whilst the method of holding the IR lens in place is functional, it is not exactly elegant.   
Currently the VeinCam also requires an external battery pack, which adds extra volume and makes it harder to hold onto. Whilst a version of the VeinCam with an integrated battery was partially designed, it was abandoned due to the added complexity of a fully integrated solution. An area for improvement may be taking a middle ground through figuring out a way to mount an external battery pack to the VeinCam, which will make it into one unit whilst not having the complexity and cost of a fully integrated solution.   


