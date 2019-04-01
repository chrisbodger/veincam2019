
![VeinCam](https://github.com/chrisbodger/veincam2019/blob/master/Administration/images/veincam1.png)

VeinCam is an educational tool for vein visualisation that uses. It uses near infrared (nIR) light and a camera to stream a real-time image where veins can be easily seen. It is an open-source, build-it-yourself device so anyone who finds it useful will be able to construct it. There is a how-to guide of what materials to buy, how to put them together and the software to upload to get it all working.

This is the repository for the continuation of the VeinCam Project as an ANU Engineering Captone Project in 2019. The repository for the previous work can be found [HERE](https://www.github.com/chrisbodger/veincam). This repository will be used to delineate and document the progress made this semester, in what is to be the next chapter of this exciting projet. 

---
# Table Of Contents
1. [Project Goals](#1-project-goals)
2. [Feedback](#2-feedback)
3. [Project Updates](#3-project-updates)
4. [Concept of Operations](#4-concept-of-operations)
5. [Meeting Minutes](#5-meeting-minutes)
6. [Decision Log](#6-decision-log)


---
# 1. Project Goals
There are 3 goals we wish to achieve this semester:

1. Develop a set of hardware requirements that are suitable for the VeinCam Project.
2. Optimise the software to run more efficiently.
3. Compile procurement options to develop kits to be able to be sold onto those who wish to build a VeinCam for themselves.

# 2. Feedback
A feedback form has been created for the interest of our stakeholders, should they wish to pass on any changes or improvements they believe to be prudent. The form can be found [here](https://goo.gl/forms/8cw5eWdaOY5C1jBo1).

# 3. Project Updates
### Week 4 Audit - 18/03/2019
#### Hardware
The hardware team have spent their time over the last 2 weeks exploring options for alternative hardware. It was determined that the Raspberry Pi is still the preferable platform, given its flexibility as a micro-computer and development platform for small hobby projects. The RasPi Zero is still chosen as our primary device, however it could be worthwhile to have a device with more inherent processing power available. Enter the RasPi 3 A+. It will have the same function as the Pi Zero, but with the ability to run the VeinCam software faster and more efficiently due to its Quad-Core CPU (instead of the single-core in the Pi Zero). Preliminary pricing for these two models [has been determined](/Hardware/Estimated%20Financials.xlsx) and once these hardware requirements have been finalised, exploration of procurement options will commence.   

With this in mind, we hope to create a universal hardware platform for the VeinCam Software to utilise, while making the RasPi swappable. This means the VeinCam and its hardware will be able to run without issue regardless of the type of RasPi it is plugged into.

### Software

Most of the work done on software since the last audit was to improve the frame rate of the received image, this required us to find the processing bottleneck in the system. After hours of testing, debugging and exploring the technical details of the code we improved the frame rate significantly by implementing an alternative image capturing method.

With this major hurdle out of the way we plan to begin improving the image processing algorithm, improving the user front end and cleaning up the Python files.

### Previous Updates
Previous project updates can be found in the [Project Updates](Administration/project-updates) directory, and will be populated as progress updates are made. Team work diaries can be found in the [Hardware](/Hardware/HardwareDiary.md) and [Software](/Software/SoftwareDiary.md) folders, as well as team [Decision Logs](/Administration/Project/Decision-Log.md) are other locations for progress notes, should they not be located on this page.

# 4. Concept of Operations
Our Concept of Operations will be signed off this week.

The [Concept of Operations](Administration/Project/CONOPS.md) document can be found in our repository.

# 5. Meeting Minutes
The team regularly meet to formally discuss the project's progress, as well as through other communication channels. the minutes from the formal discussions can be found in the [Meeting Minutes](Administration/meeting-minutes/) directory.

# 6. Decision Log
Major decisions that affect the majority or all of the project's future work and/or operations can be found in the [Decision Log](Administration/Project/Decision-Log.md/). 

