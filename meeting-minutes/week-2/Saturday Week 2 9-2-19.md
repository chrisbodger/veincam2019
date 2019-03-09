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
## Last year:
* Too slow.
* Form factor too large.
* Enclosure took too long to 3D print. Heavier, larger and more expensive than desired.
* Didn’t have a printed circuit board (now do).

## Moving forward:
* Shrink enclosure down to be tight fitting (reasonable size).
* Move towards a kit set where someone can bring their own raspberry Pi, Pi0 or Pi+, battery, SD card etc. and assemble themselves. Will we opt to go down the kit set path?
* Improve software to make it faster.
* Currently sets up own hotspot or connect to your router. Raspberry pi is all python based. It will secondly initiate flask action and load cv module. Cut down wifi connect time. Is open cv necessary in terms of enhancing the image produced?
* Have options of lithium cells, own portable battery (incorporate or external battery).

## Goal for project by end of semester:
* Get down to a kit form.
* At least present a physical object.
* Have a bill of materials.
* Hardware improvement: See if there’s a better platform than raspberry pi. Should we stick with 0 or go back.
* Software improvement: See if theres a better language – maybe C or C++. Computational saving. Only a small component of OpenCV is required – find a way to not have to load the entire library.
*Currently approximately 1.5 minutes for start-up -Set wifi, Flask server, Open cv, Intiating leds. Reduced said start-up time.



