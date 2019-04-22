# Meeting Minutes Saturday 7/4/19

## Agenda
1. Meeting with Client
2. Project discussion

### Hardware
* Ben has noted the thought process behind delivering two devices. Evidently that we are aiming to prove use case of having two soon. The idea is to decide as a group, but specifically to determine which version provides the best performance and just go with that option. Still working on both hardware platforms until software is finalised. When this occurrs we can decide to commit to the build of the one.
* Looking to focus merely on VeinCam Plus and scrap the Zero. Aim to have this decision finalised. It would be nice to keep both models and do testing with both and also have the two models for future teams, however. Financial consideration is that prices for boards will be increased if we were to buy both versions, and will be reduced if we go all in on one.
* Thinking of continuing with acryclic cases.
* The Pi camera; manually focusing the lense improved the performance and clarity. How will we consider this? Once assembled, you have to pull the case apart to adjust the camera. This consideration is worth looking into when we start getting prices.
* Ben is interested in headers and making them solderless. We are aiming to get the manufacturer to do the soldering for the boards. Also noted was that from china headers are 10c each.
* We've currently laser cut out a hole for the camera; consideration for taking care to not impact the camera lens.
* Ben has noted that we should consider that shape of which we are currently cutting acrylic; could go a square with rounded corners or the like to reduce the material wasted.
* Ben also noted the remapping of pins given new circuit board layout; the Pi has pulse width modulation (PWM) and theres only a few a number of pins that map to PWM. Ben wanted to check that this had been considered, which it has. 
* Licenses are all compatible with GPLV3; this is to be noted in repository.

### Software
* Main goal was to improve frame rate. This has been achieved and done by changing the way the image  was captured and sent to the server.
* Booting time; setting up a wifi hotspot takes a considerable amount of time. This is to be improved. Originially the system will either boot up and connect to a network or alternatively create its own hotspot. There was implemented a mechanism where the system starts to immediately create its own hotspot and this can be seen to take some time. There is the potential to edit the loop if need be; current boot up is within 30 seconds so if we can improve it that will be great but not necessary. We should also find out how long it takes to boot given making its own hotspot immediately.
* There has been an obvious change in quality due to changing process of capturing of images. Past method was quite intensive, capturing a lot of images and sending each one to the server. With Motion JPEG stream, the performance has doubled; we can just change a variable by a flask in python, so can make a front end button to increase/decrease resolution.
* There appears to be a tradeoff between image quality and frame rate. May be a slight image quality increase for a frame rate decrease.
* Still using OpenCV for iamge processing as the image processing is not affecting the frame rate.
* Next goal is to improve image quality; we have two wavelengths (veins and flesh) to consider.
* Stretch goal to improve front end and improve user experience.

### Governance
* Division of subteams at the start of the project was good.
* Requirements could have been generated in more detail.
* We are aiming to get feedback from primary schools. Said educational programs aim to get kids (years 3-6) involved with the engineering desing process. This will show us how the kids interact with the system and how easy it is for them to use. We will also aim to get feedback from educators. Ben has noted that we must be clear when writing up feedback from this; that which can be categorised into the engineering side of things and that which is from merely the users perspective; determine what realm the feedback is in and what is actually useful for the development of the project.
* Validation for commercialisation has been deemed as a group to be generally out of the scope of our project. A document has however been added to the repository for this, mostly for documentation purposed and to show evidence of such though to the tutor; we know the interest is there and that there is no other competitive product on the market. The document will have weighted criteria for commercialisation.
* Ben has noted that the documentation of decisions is of paramount importance and said documentation must continue at the current quality.
* For poster presentation, we can kill two birds with one stone and have the poster organised to be used for our presentation and additionally Ben's medical conference.

### Actionables
* To go through feedback from Audit 2 with Ben at next convenience.
* Alex O to coordinate with Bonython Primary School and secure meeting.
* To seek external council form Steph (past team member).
