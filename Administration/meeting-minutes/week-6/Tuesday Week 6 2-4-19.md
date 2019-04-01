# Meeting Minutes Tuesday 2/4/19

## Participants
|Present|Absent|
|:---:|:---:|
|Josh||
|Chris||
|Alex B||
|Alex O||
|Tom||
|Patrick||

## Agenda
1. Project Discussion
2. System testing

## 1. Project Discussion
### Hardware
* Testing and designing of new case designs has occurred. The VeinCam Plus case is close to finalisation. We are currently awaiting the arrrival of parts. Once this happens, the design for the VeinCam Zero will begin. Printed Circuit Boards (PCBs) have arrived and been assembled, with initial checks working properly. Full functionality may be tested when software has developed the code further.
* Once assembled, the removal of the SD card becomes very difficult (we need tweezers or the like). This is a further consideration for design for protecting the SD card.
* LEDs are working.

### Software
* Frame rate has been improved through implementation of an alterantive image capturing method. This involved testing, debugging and exploration of technical details.
* The kit was tested during group meeting. Team is very happy with frame rate achieved (signfificant improvement). Veins are visible. We therefore know that the kit works.
* Without any LEDs and IR filter the veins showed up. Post processing that limited the frame rate to 3fps has been solved.
* With the major hurdle of frame rate being overcome, the user interface and Python files are being cleaned up.
* Boot time is quite fast. The system has some in-built mechanism where it tries to connect to the wifi automatically (taking ~90sec). Currently start up is ~30sec. The aforementioned mechanism will be attempted to be identified from its root and removed is desired.
* Minor bug in user interface where it states for example 11/5 lights. To be fixed.

### Governance
* During meeting, undertook update of readme from week 4 audit 1 to week 6 audit 2. This involved updating hardware and software
* To check whether or not we can actually get license to sell the kit with the open source software; is this legal; what is regarded as intellectual property of the client. To look further into all constituents of the software and investigate licenses for commercialisation/distribution of the kit.
* The current ConOps (to be signed off in tute) currently does not note the IP of the project-this is to be further investigated before comment is made.

## 2. System testing
* The system was tested during the group meeting prior to audit 2, the discussion during which is largely summarised in section 1. The testing proved that the kit was working well enough to have a demonstration during the audit 2 presentation.

## Actionables
* Minor bug in user interface to be fixed.
