# Meeting Minutes 12/3/19

|Attending:|Absent:|
|:---:|:----:|
|Chris Bodger||
|Alex Ollman||
|Josh Johnson||
|Alex Binos||
|Patrick Wilton||
|Tomas Johnson||

## Agenda
1. Project Discussion

## 1.Project Discussion


### Main discussion points
* **General**
* There is great potential for having two low/high price and quality systems, for both purely entertainment and educational purposes. In this was, an advanced system may be developed for advanced educational purposes, while a less sophisticated model may be opted for for less technical use.
* Greater depth in requirements necessary.
* We must keep the end goal of the project in mind as to not run into the issue of last semester of wasting time/misdirection.
* Audit 1; we should aim to present a well structured project outline with a well defined project scope.
* Members to keep a software and hardware diary for duration of semester to track progess/changes.

* **Hardware**
* Josh has determined that off the shelf cases are too big and expensive. As such, an acrylic (68x75x36) case has been found to be a reasonable option (with a 3A+ battery). With keeping the Raspberry 0 platform, optimisation enclosure wise mightn’t be possible.

* **Software**
* Alex B and Patrick have conducted a broad look into the operation of software as to better understand it (main python functions, java script, html etc). Have come up with questions since the last meeting for discussion/clarification with Alex O. Currently members have a broad idea of how the software works and just need clarification.
* Want to know where functions are coming from as there appear to be several classes that are unused, e.g. camera_base.py. Purpose clarified by Chris.
* Looking to cut down OpenCV library for computational saving. 
* Aim to cut down on start-up time.
* Trace back histogram function to understand what it does. Do histogram equalisation (used to improve contrast) and run more filtering to enhance images.
* Improve performance under different light conditions; IR close to 850nm begins losing performance due to inability to filter.
* Aim to increase frame rate and improve photo-image processing.
* Stretch goal to clean up user interface; make it look a bit nicer and easier to use.

### Deliverables
* **Hardware**
* Finalise designs of both proposed versions.

  * *Subsequently:*
    * Put together prices to give an indicative price for both versions of proposed systems. Raspberry 0 and Raspberry A+ models decided to be looked at.
    * Research materials and compare manufacture cases. 
    * Build a prototype of each.

* **Software**
* Understand software with Alex O help.

* **Admin/Governance**
* Review of Requirements; greater detail necessary.
* Finished ConOps
* Clear project outline and scope.

### Decisions made
* **Whole system**
* Investigate potential for two versions of system, of varying quality, for entertainment and more advanced educational use. Aim to gather relevant information, source pricing and present final kit versions.

### Goals for next week:
* **For Audit 1**
* Pricing ready for hardware.
* Software-get a good idea of software currently and where it wants to go.
* ConOps and Requirements to be done.
* Establish milestones (weekly etc) to keep project on track. Are we still following what was set out to be done.

### Actionables
* Chris
  * ConOps
* Josh
  *Hardware investigations for both versions of system. Materials list and estimate pricing.
* Alex O

* Alex B
  * Understand software.
* Patrick
  * Understand software.
* Tom
  * Requirements.
