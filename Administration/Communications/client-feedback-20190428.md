Hey guys.

Thanks for the img file.  I managed to get it and have created a shrunk version (~3.3GB). Just be aware that if you use this it will go through an expansion process the first time you boot (can go on different sized microSDs), which takes a while. It'll reboot itself when done.

I got the A+ up and running relatively easily with the hardware and software provided - thanks for that.

Based on where things are now, here are my thoughts.

## Hardware:
* Nicely done! Everything fits together well, maintains the key promises of the kit, and seems robust (didn’t break when I’ve dropped it!).
* On first run (prior to adjusting the camera focal length) I was getting a number of circular artifacts from in the image, which I think was due to the light interacting with the edges of the LED circular cutouts in the case. This might be resolved by making the cutouts much larger. Indeed, that would also be useful if opaque versions of the case are produced.
* Adjustment of the camera lens appears to be essential to producing a usable image. Is there any way to make this a simple process for users and reducing the risk of camera damage for them?  I used a pair of tweezers to make the adjustment, but this is probably not ideal.  I know mention was made of incorporating a tool into the case design - any further thoughts on that?
* It appears the MidOpt IR filter (3mm thick) is better.  Is that your impression too?  If so, then is there a way to make it smaller by a couple of mm (eg from 9mm to 7mm diameter), and to use a flexible spacer to enable this while excluding visible light?  Perhaps there is an off-the-shelf thin black rubber spacer that would do the trick. This way the 3mm filter might fit entirely within the clear case (rather than sitting proud) which will protect it better, and the spacer will allow for both a smaller diameter and accommodate variation in the depth of corner hole spacers once screws are tightened.  
* Related - I’m keen to hear what you think of the different filter options.  Is the acrylic as good as glass?  Is the midopt (3mm) acrylic better than the Edmund (1mm) acrylic?
Is there any particular path the cable should take when putting it together?  My guess is quite twisted, but works fine.  I’m wondering if I’ve got it wrong.
* As I think was mentioned, the notch for the microSD is a little short at the moment - still need a set of pliers to pull it out, and having the nuts flush with the end of the bolt would be nice.  I think you are already onto that.

## Software:
* I’ve not had a chance to take an in-depth look at the detail as yet, sorry, but you’ve made good progress.  Here are my thoughts so far:
### Image/quality.
* The frame rate is clearly a huge improvement for usability, and with camera adjustment the clarity is good.  With the after-processing there were quite a few linear artifacts at the frame rate, which it will be important to resolve as possible as they significantly distort the view of key veins (which also tend to be linear).  These were also an issue when I was developing for the Zero, and I think relate to the CLAHE settings relative to the size of the region-of-interest size.  However, since you may not have played with those settings, they may relate to the frame rate and shift to video rather than still processing.  In which case, I wonder if throttling the frame rate down a little (20-25?) will help resolve them.
* I think focusing on removing as many processing artifacts as possible will be important.
* Time to first page load.  I think of ‘setup’ speed as till the user can load the app page.  This has two components:
* Boot speed - time till a hotspot is accessible. Currently around 30-35s
* Is there someone working on cutting this time by going straight to a hotspot setup (rather than attempting to poll for a local network)?
* App load speed. Currently ~10sec from starting the app to getting the flask server running.  
* Do you know how much of this time is CV2 load?
### Light pin mapping.
* I think setting ‘1’ for light is off entirely at the moment, with ‘2’ being a minimal setting but with all lights on.  Is this due to the board design (ie, is it not possible to address the 2 set of LED circuits - 3v vs 5v - independently now), or is it just a software decision?
* Sorry the feedback is limited at this point - I’ll can give more later, and am happy if you have specific things you want me to look at.  


## Audit feedback:
* I’ve taken a look at this and agree that progress has been great.
* The main things I’d add or reinforce are:
* The need for focus with a roadmap of deliverables/priorities, laid out by the time left on the project (active device development time, rather than presso prep and event prep).  Can you guys put one together?  Focus will likely need to be more on software than hardware, since I get hardware is now up to fine tuning phase.
Related to this, I’m presuming the team is now only developing on/for the A+ (a decision I support).  Please let me know if that’s not the case.
* Considering a shift in roles toward more software team members.  There are three streams (in order of priority) in which software development is likely to make gains:
* Image quality (since this is the key selling point / promise of the device)
* Time to first page load
* Modifying / tidying user interface

And thanks again for your hard work and enthusiasm to date - I know my involvement has been limited by availability but you’ve been a very easy group to work with!

Cheers,
Ben.

# Actionables
### Hardware
* Increase LED cutout size for optical clarity
* Easier method to adjust camera lens (bundled tool made from a cheap material, thin acrylic perhaps?)
* Definitive testing of IR acrylic filters - shrink diameter of 3mm filter and make flush with top plate
* shorter camera cables?
* make SD card notch larger - cannot remove from device without tools

### Software
* clear up linear artefacts
* look into CLAHE
* boot time reduction - remove polling for local internet
* app profiling - anyway to reduce load times further? how much of it is CV2?
* Light Pin mapping - dimming settings (3V and 5V rail access by both LEDs) 




# Comments

## Hardware

* Cool!
* We hadn't noticed that before, will make the holes larger to ensure it dosen't happen. 
* Will add a cutout to the bottom plate which mates with the camera lens and allows adjustment. 
* The SW guys (who have the VeinCams) agree that 3mm is better. We have an idea which will get the IR acrylic down to 5mm dia whilst ensuring that is sits flush. Josh will get a new set of prototypes cut end of week and go from there. 
* We were thinking that it would be good to hide the SD card to stop kids pulling it out, but added the indent so it can still be removed. Thoughts? Happy to make it anywhere from real easy to really hard to remove. 
<<<<<<< HEAD
* We were unable to source the correct length / dia screws locally, have ordered correct parts and most have arrived, only the M2.5 nuts are left and it will all be flush.
=======
>>>>>>> 9181c3f38bf58092e107a537d45127ca17124996

## Software 
*
*
*
*
*
*
*
*
* (Josh here) It's not a hardware issue, all LEDs of the same nm are controlled at the same time, probably a quick software fix. 