# Requirements

| Author        | Date Modified           | Version | Completion Status  |
| :-------------: |:-------------:| :-----:| :----:|
| Alexander Ollman   | 13/05/2019 | 2.0 | Completed for Audit 3 |

| System Requirement  | Metric | Test | Validation | Client Importance (1-5) | Requirement Met? |
| :-------------: |:-------------:| :-------------:| :-------------: | :-----:| :----:|
| Compared to other devices with similar functionality, the produced device must be relatively inexpensive.  | Dollars, Australian | <$500AUD (Typical Public School Science Budget) | Cost of production VeinCam (minus packaging, freight, external costs) is less than $150 to consumer. | 3 | Yes, with reservation. |
| The device must be simple to construct, easily reproduced (and/or easily manufacturable).  | Cost per unit | Cost per unit is <50% of total cost to consumer; contains mostly off-the-shelf components; can be manufactured with common machines, worldwide. | Cost per unit of is $13.49 for designed componentry, remainder of cost is from off-the-shelf components (Raspberry Pi A+, PiCam). Designs are open source and easily manufacutred with a laser cutter and PCB routing machine. | 5 | Yes, with reservation. |
| The device must be simple to use. Ease of use should be correlated with the intended educational application of the device, and as such be relevant for expected users. | Time, minutes | Time taken to assemble by unknown party, student. | Nursing student (Rachael Weigand) assembled VeinCam prototype closely resembling final design in 8 minutes (without camera focus adjustment, software setup) | 2 | Yes, with reservation. |
| The device must be able to use near infrared (NIR) illumination and real-time image processing to make veins appear most visible in an efficient manner. This criterion must be of a level of quality that is satisfactory for educational use. | #Infrared LED's | #Infrared LED's > 0, Veins Clearly Visible | There are six dual-wavelength (840nm and 950nm) infrared LED's which provide sufficient illumination on a subject and show clear, defined veins in the majority of test subjects (dependent on skin type, body fat) | 2 | Yes.|




### System Requirements:
1. Compared to other devices with similar functionality, the produced device must be relatively inexpensive.
2. The device must be simple to construct, easily reproduced (and/or easily manufacturable?)
3. The device must be simple to use. Ease of use should be correlated with the intended educational application of the device, and as such be relevant for expected users.
4. The device must be able to use near infrared (NIR) illumination and real-time image processing to make veins appear most visible in an efficient manner. This criterion must be of a level of quality that is satisfactory for educational use.
5. The device must run primarily off of battery power.
6. The device must be able to wirelessly connect to an external device with a screen.
7. The device must be portable and mobile.
8. The device must be reasonably easy to maintain, clean and fix in the event of failure/break/degradation.
9. The device should display veins in as many use-cases as possible (e.g. dark-skinned, tattooed, hairy). (Stretch deliverable)
10. The device is manufacturable to ***have the potential*** to be put to a commercial market. (Stretch deliverable)

### Requirements of Hardware Team
1. Redesign device enclosure(s) to accomodate Raspberry Pi A+ and Raspberry Pi Zero.
2. Design required printed circuit board assemblies to succesfully integrate all required functionality. 
3. Ensure Design for Manufacturing and Assembly is considered during the above two steps.
4. Full Bill of Materials ready for client. 

### Requirements of Software Team
1. Modify current image processing code to be more efficient.
2. Improve start up time.
3. Clean up front end user interface.
4. Research most optimal programming language for image processing (C++ vs Python)
5. Introduce photo image processing on top of the equalised image to detect veins within relative bounds (Stretch Deliverable)

