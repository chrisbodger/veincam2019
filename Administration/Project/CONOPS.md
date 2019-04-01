# Concept of Operations

## Version History
| Version | Description | Audit Version |
| --- | --- | --- |
| 2.0 | Mid-Term Document | Audit 2 |

## Table of Contents
* [Project Vision](#project-vision)
  * [Value Proposition](#value-proposition)
  * [Project Scope](#project-scope)
  * [Project Comparison](#project-comparison)
* [Stakeholders](#stakeholders)
  * [Project Team](#project-team)
  * [Project Client](#project-client)
  * [Shadow Team](#shadow-team)
  * [Course Tutor](#course-tutor)
  * [Course Convenor](#course-convenor)
  * [Users](#users)
* [Resources](#resources)
  * [Tools](#tools)
* [Project Management](#project-management)
  * [Deliverables](#deliverables)
  * [Milestones](#milestones)
  * [Audit Goals](#audit-goals)
  * [Work Breakdown Structure](#work-breakdown-structure)
  * [Decision Making and Conflict Resolution](#decision-making-and-conflict-resolution)
* [Risk Analysis](#risk-analysis)
  * [Safety Risk Analysis](#safety-risk-analysis)
* [References](#references)

---

## Project Vision
VeinCam is a device that enables the visualisation of the superficial veinous system. It's primary purpose is to educate curious minds on the inner workings of the human body. The current VeinCam iteration, submitted as a ANU Engineering Capstone Project in late 2018, is based on the 2017 [Venenfinder Hackaday project](https://hackaday.io/project/26158-assistance-system-for-vein-detection). The objective of the VeinCam project was to extend the Venenfinder to become smaller, portable, more afforable and easy to build by young students and inquisitive minds.

After recieving incredibly positive feedback during the final presentation of VeinCam, from both educational and medical professional's alike, the decision was made to continue the VeinCam project into 2019. The vision for this next phase of development is to produce a Bill of Materials and finalised software to handover to the primary client. The quality of the Bill of Materials and software should be of a standard where the primary client can create commercially-viable DIY kits that remains affordable and convenient to market to educators, for construction and development within a classroom environment. As such, our goal of this project is to create a product that is professional and of a commercial standard.  

Dependent on software performance testing to be performed towards the end of the project, two iterations of the VeinCam kit are planned: VeinCam and VeinCam Plus.

### Value Proposition
Our VeinCam device will help students better understand the human body by augmenting visualisation of upper limb veins. It will provide students with an interactive expereience and fun way to learn about the venous sites of the body. At an educational level, this has never been done before as commerically available products with similar capabilites are far beyond a price point that would be considered by educators. Our value proposition is to provide this experience and funcionality at a fraction of the cost. 

### Project Scope
This project aims to continue on the achievements of the team from last semester with the aim of polishing the device so that it is of a standard where it can marketable. This will include the optimization of the device's physical hardware and extending its software capabilities. To achieve this, we will explore the options of migrating to a new hardware platform and rewriting aspects of the current image processing code.

Two chassis (VeinCam and VeinCam Plus) will be designed and refined over several iterations, comparing off-the-shelf and custom made components using quotes from online stores and potential chassis manufacturers. The primary goal of this project is to supply the client with a complete bill of materials, costing and supplier sheet to then use for the order and manufacturing of educational kits.

### Product Comparison
The following table contains an overview of how the newer VeinCam will differentiate from the current iteration.

#### Feature Summary
| Current VeinCam Prototype (v2.3)| VeinCam 2019 | Future Development/Stretch Goals |
| :---: | :---: | :---: |
| One Version Design (VeinCam) | Two Versions (VeinCam, VeinCam Plus) |  |
| Raspberry Pi 3 B+ | Raspberry Pi Zero W (VeinCam), Raspberry Pi A+ (VeinCam Plus) |  |
| IR Illumination (840nm) | IR Illumination (840-940nm, adjustable) | |
| Basic LED Array | Custom LED PCB | |
| IR PiCamera | IR PiCamera |  |
| HTML/CSS User Interface | JavaScript User Interface | Smartphone App Development |
| Startup Time < 1 min | Startup Time < 30 seconds | |
| Wireless, Portable and Battery Powered | Wireless, Portable and Battery Powered  | |
| Large 3D Printed Enclousre | Smaller Off-The-Shelf/Custom Design Enclosure(s) | |
| Manual Camera Setting (Brightness, Contrast etc.) Adjustment | Automatic Camera Setting Adjustment and Framing | |
| Basic Image Processing | Vision-Based Image Processing | Vein Detection |
| Open Source | Polished, Manufacturable Design | Commercial Educational Kit  |

#### VeinCam v2.3 Features
Currently, the VeinCam utilises similar hardware to the Venenfinder project (Raspberry Pi, PiCam, IR LEDs) and extends the software's capabilities to perform a histogram equalisation to allow veins to come through the image clear and prominent. VeinCam also features a web interface which allows for the manual adjustment of the camera's brightness, contrast and saturation to produce the clearest image possible. Unlike other open-source and commercially available vein cameras, VeinCam is smaller, battery powered and completely wireless.

#### VeinCam 2019 Core Features
- Smaller, more polished chassis using either off the shelf components for easy manufacturing of kit, or custom manufactured casing.
- Image Processing with more aggressive equalization, automatic image pixel brightness adjustment to differentiate and illuminate the arm from the background, vein detection and optimization.
- Two Versions, VeinCam and VeinCam Plus 9R

---

## Stakeholders
The following groups have been identified as stakeholders for this project:

| Stakeholder | Project Interaction |
| --- | --- |
| Project Team | Produces the Project Output and actions constructive feedback from other stakeholders. Provides regular updates to stakeholders regarding process through the repository documentation and verbal communication |
| Project Client | Provides feedback on project progress and guides towards milestone objectives |
| Shadow Team | Observes the Project and provides constructive feedback |
| Course Tutor | Provides feedback on project progress |
| Course Convenor | Provides feedback on project progress |

### Project Team
The project team consists of six undergraduate engineers who each have roles as point people in the project. All members of the team should be present to support each other in whatever way is necessary to complete tasks and better the project. The designated roles give each member a lead position, they are responsible for their sections and as such if any questions from external stakeholders specifically address a section of the project they are the member to contact.

| Name | Role | Email |
| --- | --- | --- |
| Christopher Bodger | Procurement and Research | u5395595@anu.edu.au |
| Alexander Ollman | Stakeholder Liaison and Operations | u5826805@anu.edu.au |
| Alexander Binos | Software Engineer | u5799782@anu.edu.au |
| Patrick Wilton | Software Engineer | u6050506@anu.edu.au |
| Josh Johnson | Hardware Engineer | u6044123@anu.edu.au |
| Tomas Johnson | Secretary | u6080168@anu.edu.au |

#### Responsibilities of the project team to the project
* Fulfil the tasks assigned by the team within the desired time frame to the best of their ability.
* Communicate the progress and setbacks of their tasks regularly with the team.
* Commit to regularly attending scheduled meetings, or otherwise remain up to date with meeting minutes and contributing to meeting agendas.

##### Responsibilities of the Hardware Engineer
* Manage and design the hardware of the device.
* Design and test the layout and chassis of the device.
* Manufacture of the prototype device.

##### Responsibilities of the Software Engineer
* Design the code for the device to meet deliverables and requirements.
* Ensure the code is stable and respositories are up-to-date.

##### Responsibilities of the Stakeholder Liaison and Operations
* Be the point of contact for general communication between stakeholders.
* Organise meetings with the client and other stakeholders when necessary.
* Regularly update major documents when project deviates from documentation.
* Set and lead meetings.
* Manage the team and ensure goals and milestones are being achieved.

##### Responsibilities of Procurement and Research
* Perform research required to strengthen the project.
* Obtain financial information regarding the manufacture of the device components.
* Delegate research when necessary to other team members.

##### Responsibilities of the Secretary
* Maintain the repository, including all documentation and meeting agendas/minutes.

**These roles show who questions should be directed to and are not indicative of workload.**

### Project Client
Ben Healey (message2ben@gmail.com)

Ben is medical practitioner and an employee of ACT Health. He personally began this project using pointers from open source projects such as the 2017 Hackaday project and the Venenfinder project, to develop an affordable vein imaging device.

Due to Ben's increasing work commitments, both Chris Bodger and Alex Ollman will act as "Client by Proxy", due to their history with the project, and previous understanding of the project current progress and Ben's desired outcomes.

#### Responsibilities of the project team to the client
* Design a device to meet the established baseline requirements that the client has presented.
* Inform the client regularly with updated progress towards milestones and any setbacks they should be aware of.

#### Responsibilities of the client to the project
* Provide information and requirements about the project to the team.
* Respond to communications on a regular basis.
* Be present and prepared at scheduled meetings.

### Shadow Team
ANU undergraduate engineering students, tasked with reviewing this project to provide an external viewpoint on the outputs and governance of the project. Shadow Team still to be formed

| Name | Email |
| --- | --- |
| Elton Lu | u6096527@anu.edu.au |
| Patrick Dunphy | u6052409@anu.edu.au |
| Phillip Pulford | u5809328@anu.edu.au |
| Sha Shaharuddin | u5988860@anu.edu.au |
| Zachary Mason | u6080840@anu.edu.au |
| Ze Gan | u6051306@anu.edu.au |

#### Responsibilities of the project team to the shadow team
* Provide shadows access to all information surrounding the project, including repositories, documentation and relevant communications.  This information should be up-to-date and presented appropriately.
* Be open to feedback from all channels from shadows, and act on feedback appropriately.

#### Responsibilities of the shadow team to the project
* Remain up-to-date with the activities, outputs and governance of the project through information that is supplied to them.
* Commit to providing constructive, accurate and actionable feedback to the project through the pathways provided to them: including formal audit feedback, as well as verbal feedback in tutorial sessions and through the feedback forms supplied.

### Course Tutor
Jenny Simmons (jenny.simmons@anu.edu.au)

ANU ENGN4221 course tutor for Semester 1 2019. Tasked with formally organising and directing weekly tutorial sessions where the project is planned, presented and reflected upon.

#### Responsibilities of the project team to the course tutor
* Provide the tutor access to all information surrounding the project, including repositories, documentation and relevant communications. This information should be up-to-date and presented appropriately.
* Be open to feedback from the tutor, and act on feedback from all channels appropriately.
* Be present and prepared at all weekly tutorials (Tuesday 10-12), appropriate to the activity of the tutorial that week.
* Be informed of the structure of the course and related assessment milestones as established by the course convenor.
* Be prepared to submit assessments, and be open to grades and discussion of grades with the course tutor.

#### Responsibilities of the course tutor to the project
* Be present and prepared to lead the tutorial each week, appropriate to the activity of the tutorial, and remain up-to-date with the progress of the project.
* To a reasonable extent, assist the project team with the progress of the project, including answering relevant and reasonable questions, and providing constructive, actionable and accurate feedback, particularly at times of project audits and during tutorial sessions.
* Reply to correspondence (email) in a timely fashion, and grade formal assignments fairly and appropriate to the quality of the project.

### Course Convenors
Ankur Sharma (ankur.sharma@anu.edu.au)

ANU ENGN4221 course convenor for Semester 1 2019. The course convenor is the overall authority and organiser for this course, and hence this project as a subdivison of the course.

Chris Browne (chris.browne@anu.edu.au)

Former ANU ENGN4221 course convenor for Semester 1 2019. Advisor to the primary course convener.

#### Responsibilities of the project team to the course convenor
* Same as those applying to the course tutor.

#### Responsibilities of the course convenor to the project
* Same as the course tutor with the addition of:
* Organise the course appropriate to the desired outcomes and be receptive to feedback regarding this structure. Information regarding the structure and assessment milestones of the course should be available to students within a reasonable timeframe.

### Users
Members of the public, particularly students and educators who wish to utilise the device for educational purposes.

#### Responsibilities of the project team to the users
* Provide members of the public access to information that pertains to all aspects of the project.
* Design a device that is safe, stable and provides value.

#### Responsibilities of the users to the project
* Members of the public have little steadfast responsibility to the project team.
* Ideally, members of the public will provide feedback on the function of the device during requirements analysis or testing.

---

## Resources
The [Bill of Materials](/Hardware/Estimated%20Financials.xlsx) (BoM) outlines the current components of the device and their respective costs. The BOM will be regualrly updated as the choice of hardware is more refined as the project contiunues. The BoM will also be used to show what the procurement and research the team has arranged for component pricing with potential suppliers.

### Tools
With the potential to continue development with componentry, the tools likely to be used throughout this project include:
- Soldering Iron
- 3D Printer
- Laser Cutter
- Dremel
- Screwdriver, screws, nuts and bolts.

All safety precautions outlined by the ANU Makerspace's Terms and Conditions will be followed during the use of instrument or tool, regardless of where and how it is used. A safety risk analysis has been performed at the bottom of this document.

#### Project Administration
* GitHub
* Google Drive
* Discord (Primary Communications Platform)

#### Manufacturing and Testing
* Ian Ross Design Studio
* ANU Makerspace

#### Programming
Source code from the last semester of development will be modified for the optimisation of the current platform, or rewritten if deemed appropriate. A snapshot of the code has been captured and archived within the [repository](/master/Software/Initial%20Code). The code will be written on the Linux platform using Python and C++ programming languages, with all relevant extenral code referenced in the repository. 

## Project Management
### Deliverables
The initial deliverables are as follows:

#### Deliverables
* Determine the suitability of the current hardware and confirm final hardware solution.
* Optimise the software for the desired hardware to run more efficiently and detect veins more clearly to meet the desired system [requirements](Administration/Project/Requirements.md).
* Compile a list of procurement options and outline sources for the client to then purchase and build the kit for distribution.

### Milestones
Further detail on the optimisation of milestones and objectives of the project are detailed in the Requirements document.

#### Milestone 1
Decide on final hardware appropriate for the project's commercial vision.

#### Milestone 2
Optimise software to run as efficiently as possible for the desired hardware platform(s). Enclosure designs finalised.

#### Milestone 3
Compile quotations for external manufacture of components (PCBs, case, etc.)

#### Milestone 4
A kit of compiled components ready for the client for commercial distribution.

### Audit Goals
#### Audit 1
* Complete ConOps Version 1
* Reach Milestone 1

#### Audit 2
* Update ConOps to Version 2
* Complete requirements analysis
* Reach Milestone 2

#### Audit 3
* Achieve Milestone 3/4 with accompanying verification and validation

Milestones are subject to change as the project evolves. Changes will be made to this document to reflect project's new objectives.  

### Work Breakdown Structure
| Task | Time Allocation | Responsible Team(s)/Third Party | Status |
| --- | --- | --- | --- |
| ***1. Requirements Analysis***  |  | | |
|  -- 1.1. Review PoC   | 3 hours | All Teams | Complete |
|  -- 1.2. Perform risk analysis  | 1 hours | All Teams | Complete |
|  -- 1.3. Brainstorm requirements (in-house)   | 1 hour | Each Team Individually, Primary Client | Complete |
|  -- 1.4. Develop requirements with client | 1 hour | All Teams, Primary Client | Complete |
|  -- 1.5. Finalise requirements  | 2 hours | Each Team Individually| On going | 
| ***2. Prototyping***  | | | |
|  -- 2.1. Design new prototype  | 6 - 10 hours | Hardware | Complete |
|  -- 2.2. Manufacture and construct newest prototype | 4 - 8 hours | Hardware | In Progress |
|  -- 2.3. Design base software in line with new requirements  | 6 - 10 hours | Software | Complete |
|  -- 2.4. Integrate software  | 2 hours | Software | In Progress |
|  -- 2.5. Update software with stretch deliverables  | 4 - 8 hours | Hardware | Awaiting Completion (Dependent on 2.3, 2.4) |
| ***3. Validation & Verification***   | | | |
|  -- 3.1. Test prototype in-house  | 4 hours | All Teams | In Progress |
|  -- 3.2. Conduct performance review  | 2 hours | All Teams (Primarily Governance) | Awaiting Completion (Dependent on 3.1) |
|  -- 3.3. Finalize Software  | 2 - 6 hours | Software | Awaiting Completion (Dependent on 3.1) |
|  -- 3.4. FInalize Bill of Materials | 2 hours | Hardware | Awaiting Completion (Dependent on 3.1) |
| ***4. Documentation***  | | | |
|  -- 4.1. Write ConOps v1  | 4 hours | Governace | Complete |
|  -- 4.2. Update ConOps to version 2  | 2 hours | Governance | Complete |
|  -- 4.3. Create poster  | 2 - 5 hours | Governance | Awaiting Completion (Dependent on 3) |
|  -- 4.4. Keep Repository Organised  | 3 - 8 hours | Governance | On going |


### Decision Making and Conflict Resolution
Decision making will be by consensus in consultation with the client. When consensus cannot be reached the project team will seek advice from other stakeholders depending on the nature of the decision. For further detail please refer to the [Decision Log](https://github.com/chrisbodger/veincam2019/blob/master/Administration/Project/Decision-Log.md).

---

## Risk Analysis
All risk analysis performed throughout this project will be in accordance to the Australian and New Zealand Industry Standard AS/NZS 4360:2004.

![Risk Matrix](https://github.com/chrisbodger/VeinCam/blob/master/images/ConOps/risk-matrix.png)

Potential risks to the success of the project have been brainstormed in order to understand them and mitigate either their severity or likelihood.

| Risk | Consequences | Likelihood | Severity | Mitigation |
| :---: | :---: | :---: | :---: | :---: |
| Not clearly understanding or defining requirements for the project. | Product does not meet requirements, primary client dissatisfied, requires re-doing work, going over budget and schedule to redesign | D | 3 | Maintain regular contact with client regarding progress and milestone completion. |
| Not defining scope of project and setting clear and achievable milestones. | No clear definition of project progress, feature creep over time results in lack of physical product, no clear "stopping point" for project or completed product, client dissatisifed, product does not meet customer requirements, likely to be over-budget. | C | 3 | Defining scope early and ensuring we stick to milestones and their respective outputs to ensure we do not deviate on a project tangent. Meeting (at minimum) weekly to discuss progress and next actionable deliverable for each team member, who is then held accountable for achieving that deliverable in the given time frame. |


### Safety Risk Analysis
In developing the prototype there is a chance of injury, similar to above these risks have been listed and steps taken to mitigate their severity or likelihood.

| Risk | Consequences | Likelihood | Severity | Mitigation |
| :---: | :---: | :---: | :---: | :---: |
| Personal harm whilst using listed tools (incl. burns, shocks, cuts) | Pain, discomfort and possible medical attention. | D | 3 | Ensuring all team members are familiar with the safety training of the ANU Makerspace/Engineering workshop, supervision by one other team member when using potentially dangerous tools. |
| Damage to Hardware due to physical impact or electrostatic discharge (ESD) | Loss of data, hardware faliure, schedule delays to order and replace damaged hardware. | E | 4 | Ensuring hardware is never placed in an area where it is likely to be damaged, always in full visible sight. Observing proper ESD safety techniques, such as regularly grounding ourselves and only contacting circuitry by edges. |

---

## References
[Venenfinder Github](https://github.com/Myrijam/Venenfinder)

[Venenfinder Hackaday.io Page](https://hackaday.io/project/26158-assistance-system-for-vein-detection)

[Veincam Stage 1](https://github.com/chrisbodger/veincam)

---

This Project is licensed under the Creative Commons license.
