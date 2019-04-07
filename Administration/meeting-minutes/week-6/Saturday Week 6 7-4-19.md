# Meeting Minutes Saturday 7/4/19

## Agenda
1. Meeting with Client
2. Project discussion

### Feedback
* Ben has noted thinking of two devices. Evident that we are aiming to prove use case of having two soon. Idea is to decide as a group, but determine which version provides best performance and just go with that.

### Hardware
* Josh still working on both hardware platforms until software is finalised, then we can hit build on one.
* Thinking of continuing with acryclic cases.
* The Pi camera; manually focusing the lense improved the performance and clarity. How will we consider this? Once assembled, you have to pull the case apart to adjust the camera. Worth looking into when we start getting prices.
* Ben interested in headers and making the solderless - get manufacturer to do the soldering for the bigger (blue board), red board might need the user to solder. From china headers are 10c each.
* Josh in support of A+. Looking to focus merely on VeinCam Plut and scrap the Zero. Aim to have this decision finalise; would nice to keep both models and do testing with both and also have both models for future teams. Prices for boards will be increased if we were to buy both versions, and will be reduced if we go all in on one.
* Weve currently laser cut out a hole for the camera; consideration for taking care to not impact the camera lens.
* Ben - Current acrylic; consider shape of cut out of acrylic piece; could go a square with rounded corners or the like to reduce the material wasted.
* Ben - remapping of pins given new circuit board layout; the Pi has pulse width modulation (PWM), theres only a few a number of pins the map to PWM. Ben wanted to check that this was the case. Josh has done so 

* Licenses are all compatible with GPLV3; this is to be noted in repository.

### Software
* Main goal was to improve frame rate; achieved and done by changing the way the image  was captured and sent to the server.
* Booting time; setting up a wifi hotspot takes considerable amount of time. This is to be improved. The system will either boot up and connect to a network or alternatively create its own hotspot. There was implemented a mechanism where the system starts to immediately create its own hotspot-takes some time. To edit the loop if need be; current boot up is within 30 seconds so if we can improve it that will be great but not necessary; find out how long it takes to boot given making its own hotspot immediately.
* Obvious change in quality due to changing capturing of images. Past method was quite intensive, capturing a lot of images. What Pat has achieved with mjpeg stream has double its performance; can just change a variable by a flask in python, so can make a front end button to increase/decrease resolution.
* May be a slight image quality increase for a frame rate decrease.
* Still using opencv for iamge processing as the image processing is not affecting frame rate.
* Next goal is to improve image quality; we have two wavelengths (veins and flesh). This is to be considered when improving image quality.
* Stretch goal to improve front end, improve user experience.

### Governance
* Division of subteams at the start of the project was good.
* Requirements could have been inputted more.
* To get feedback from primary schools. Programs aim to get kids involved with engineering desing process. Yr 3-6 kids. this will show us how the kids interact with it/how easy it is for them. Also to get feedback from educators. Ben says be clear when writing up feedback from this; what is the engineering side of things and that which is from the users perspective; determine what realm the feedback is in and what is actually useful for the project.
* Validation for commercialisation has been deemed as a group to be mostly out of the scope of our project. Alex O is putting together a document for this mostly for documentation prupose; we know the interest is there and that theres no other competitive product. The document will have weighted criteria for commercialisation. Commercialisation is a bit outside of the realm of this project.

* Ben has said documentation of goals is paramount.
* For poster presentation, we can kill two birds with one stone and have the poster organised to be used for our presentation and Ben's medical conference.


### Actionables
* To go through feedback from Audit 2 with Ben at next convenience.
* Alex to coordinate with Bonython Primary School and secure meeting.
* To seek external council form Steph (past team member).
