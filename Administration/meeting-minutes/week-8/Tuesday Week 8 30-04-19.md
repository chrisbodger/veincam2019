# Meeting Minutes Tuesday Week 8 30-04-19

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
1. Ben's feedback
2. Audit feedback
3. Project discussion

## Main Discussion
### Governance
* Aim to be better in harmony with what Ben expects and what subteam priorities are.
* Need to clarify what educational experience/resources we aim to present students with and how we aim to do so. While the education/involvement of students is important we are prioritising teacher feedback. Must develop questions that we want to be asked as feedback.
* To consider poster and development on this from last semester.

### Software
* Histogram equalisation failing to be optimised. Linear artefacts are presents. This may simply be the tradeoff for high frame rates; therefore simply can't resolve the presence of linear artefacts. Ben thinks its an issue of the Histrogram settings - Patrick has played with said settings sufficiently. This issue has surely been overcome by someone else and is therefore worth investigating, but not absolutely critical.
* Ben believed that boot up time is ~32 seconds and that this was attributed to hotspotting; the Raspberry Pi can be attributed to this first ~30 seconds. Therefore it is all prior to any code running. This improvement is not critical. Image processing is more important.
* Change brightness settings for LEDs. Include on/off button and 1-5 brightness or the like. Decided on 3 modes; off, medium and high; 0,1,2,3. (Decision log)
* Image quality and boot time can't be improved much more with the power we have. User-interface can be improved to enhance the user experience and educational understanding.

### Hardware
* Circular artefacts. Ben noticed said artefacts when testing Veincam.
* Add tooling shaped on the back of the case so you can adjust the lense when everything is assembled.
* Tightening of lense greatly impacts on image quality; focus is highly sensitive to tightening. The kit works fine however without agjusting for optimal iamge quality. For the general case this is therefore probably not an issue; most kids won't care or notice the difference.
* Filter: Size of acrylic to be reduced; expensive component that Ben want to reduce cost of, however optimising clarity and image quality mandates it.
* Ribbon cable is twisted due to being unnecessarily long. This is a minor issue as we can't buy shorter ones.
* Notch for microSD. Group believes that having the microSD inaccessible is probably better. It will most likely be the case that only teachers will be assembling the kit. Having the SD inaccessible to students who  may destroy the hardware is important. (Decision log)

## Decisions Made
* Notch for microSD. Group believes that having the microSD inaccessible is probably better.
* Change brightness settings for LEDs. Include on/off button and 1-5 brightness or the like. Decided on 3 modes; off, medium and high; 0,1,2,3.

## Deliverables
* Governance to attend Monday session regarding poster presentation and begin work on this.
* Governance to develop feedback questions for teacher for school presentation.
* Hardware and Software to consider Ben's feedback; filter, LED brightness settings.
