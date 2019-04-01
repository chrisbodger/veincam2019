### Week 4 Audit - 18/03/2019
#### Hardware
The hardware team have spent their time over the last 2 weeks exploring options for alternative hardware. It was determined that the Raspberry Pi is still the preferable platform, given its flexibility as a micro-computer and development platform for small hobby projects. The RasPi Zero is still chosen as our primary device, however it could be worthwhile to have a device with more inherent processing power available. Enter the RasPi 3 A+. It will have the same function as the Pi Zero, but with the ability to run the VeinCam software faster and more efficiently due to its Quad-Core CPU (instead of the single-core in the Pi Zero). Preliminary pricing for these two models [has been determined](/Hardware/Estimated%20Financials.xlsx) and once these hardware requirements have been finalised, exploration of procurement options will commence.   

With this in mind, we hope to create a universal hardware platform for the VeinCam Software to utilise, while making the RasPi swappable. This means the VeinCam and its hardware will be able to run without issue regardless of the type of RasPi it is plugged into.

### Software
The software team have spent their time over the last 2 weeks understanding the current revision of the VeinCam software works and is integrated with hardware. A high-level software sub-system overview was made into a Visio diagram which greatly helped the team comprehend how the systems worked with each other. This also led to identifying areas for optimisation and improvement including: Python image processing, boot time optimisation, and front-end functionality and aesthetics.

The first area of focus following on from this initial learning curve will be the optimisation of boot time and improving the image processing, where a small amount of investigation has been done in each of these areas.
