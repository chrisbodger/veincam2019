# Meeting Minutes 9/3/19

| Attending: | Absent: |
| :---: | :---: |
| Chris Bodger | Alex Ollman |
| Alex Binos |   |
| Josh Johnson  |   |
| Tomas Johnson |   |
| Patrick Wilton |   |

## Agenda
1. Meet and Greet with Ben
2. Project Discussion
---



---

## Actionables
* Chris to:
  * Finalise ConOps
* Josh to:
  * Continue research into hardware requirements
* Alex O to:
  *
* Tom to:
  * Develop Requirements document ready for Audit week
* Patrick to:
  * Understanding of code and its Operation
  * Streamline the OpenCV package to be lighter
* Alex B to:
  * Understanding of code and its Operation
  * Streamline the OpenCV package to be lighter
* All:
  *
  
## Project Discussion
### Last year shortcomings
* System too slow.
* Form factor too large.
* Enclosure took too long to 3D print. Heavier, larger and more expensive than desired.
* Didn’t have a printed circuit board (now do).

### Considerations moving forward
* Shrink enclosure down to be tight fitting (reasonable handle size).
* Move towards a kit set where someone can bring their own Raspberry Pi, battery, SD card etc. and assemble themselves. Will we opt to go down the kit set path?
* Improve speed of software.
* Currently the system sets up its own hotspot or alternatively connects to a router. (Raspberry pi is all python based) It will secondly initiated micro web framework Flask (written in Python) and loads Open Source Computer Vision library (CV module). Time taken for wifi connection should be aimed to be reduced. Additionally, is OpenCV necessary in terms of enhancing the image produced?
* Have options of incorporated or external battery; lithium cells, own portable battery etc..

### Goal for Project by end of semester:
* As a minimum, present a physical object.
* Get down to a kit form.
* Have a bill of materials.
* Hardware improvement: See if there’s a better platform than Raspberry Pi.
* Software improvement: See if theres a better language (maybe C or C++). Computational saving; only a small component of OpenCV is required (ind a way to not have to load the entire library).
* Currently approximately 1.5 minutes for start-up. This includes setting up wifi, Flask server, OpenCV, Intiating LEDs. Aim to reduce said start-up time.

### Decisions to be made
* Hardware
  * Optimise platform selection. Identify better platforms beyond Rasberry Pi.
  * Incorporated or external battery.
* Software
  * Optimise language selection. Identify better languages including, but not limited to, C or C++. Language must be computationally saving.
  * Requirement or lack thereof of comprehensive OpenCV incorporation.


