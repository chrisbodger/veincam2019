# Commercial Viability 

For a product to be commercially viable there are a number of key considerations which need to be taken into account. This document will cover a number of considerations which are relevant to the VeinCam project. 

### Manufacturing  
The first part of ensuring that VeinCam is a commercial success is making sure that it can be manufactured in volume at a reasonable price. Some of the key considerations to ensure this are listed below.  

- Utilising proven manufacturing techniques such as laser cutting and two layer printed circuit boards lowers the risk of the product not being able to be fabricated / fabricated at a reasonable cost. 
- Reducing the part count (both electrical and mechanical) has benefits from both a cost and complexity standpoint. This has occurred with VeinCam, as the part count has been reduced during the prototyping stages to a point where is cannot be reduced further whilst keeping the current feature set. One such example of this is integrating the camera adjustment tool into the bottom acrylic plate, as otherwise a separate tool would need to be shipped which adds complexity and cost.    
- Ensuring that the design of the printed circuit assembly has taken into account design for manufacturing and assembly requirements lowers the risk of the board failing fabrication and assembly. Specifically, using wide traces (10 mil) and large vias (0.6/0.3mm) ensures that any board house can manufacture the board as old process technology can be used. 
- Furthermore, using large components (0603), along with laying out the board with DFM considerations in mind ensures that the assembly process will have a high yield. This results from layout decisions which prevent tombstoning of components during reflow, and sufficent spacing of components from the edge of the board to prevent stress failures during depanelising. 

### Durability
Once the product is assembled, we need to ensure that it will stand up to the use and abuse which can be expected of a consumer electronics product. This primarily involves ensuring that material selection and assembly methods are sufficiently durable.   

- Utilising acrylic as the external enclosure ensures that it is strong enough to withstand scratching, dropping, and other forms of physical damage. Furthermore, the mechanical properties of acrylic do not degrade over the expected lifecycle of the product, and as such it can be expected that the VeinCam will be able to withstand these the above mentioned damage for its whole lifecycle. 
- Another important consideration is the durability of the PCB. Whilst the PCBA contains primarily surface mount components due to their smaller size and lower assembly cost, the Raspberry Pi connector has been chosen as a through hole part as it provides much greater mechanical strength which is required for a large connector of its type which can be expected to be inserted and removed a considerable number of times in its lifespan. 
- The mechanical assembly of the device, in using metal bolts to secure both the camera to the PCBA, and to hold the whole device together ensure that once assembled, the VeinCam will not be falling apart due to the front and rear panels not being attached to each other.
- Due to the design of the lens and the way it mounts to the front panel ensures that it is unable to fall out post assembly, due to both parts having draft angles which when assembled prevent the lens to move through the front of the front acrylic, and the camera being mounted flush behind the lens prevents it from falling out backwards. 
- The likelihood of electronic failure of the device is also quite low, as the Raspberry Pi and NoIR camera are both known as to be reliable products, and due to the good design considerations and trivial nature of the VeinCam board the likelihood of it failing is quite low. 
- The most likely failure methods of the device are damage to the flat flex cable during assembly, which can be mitigated through showing the best method to assemble it in the assembly instructions, and water damage, which could be mitigated through making a water resistant enclosure, however this would increase the physical size and cost of the VeinCam and as such it was decided against. 

### Safety

Is is obvious that if a product is to be commercially viable, is must be safe for the user to use. Outlined below are a few of the safety concerns we have considered in the development of the VeinCam. 

- One safety concern is the likelihood of any sharp edges cutting the user, small parts being able to be swallowed, or other forms of contact damage to the user. This has been mitigated through radiusing every corner on the device and insetting the SD card from the edge of the enclosure such that it can not be accidentally removed. 
- Amongst its other uses, the bottom acrylic plate serves as a way to protect the user from scraping their fingers across the numerous sharp pins sticking out of the Raspberry Pi, whilst also proving a way of holding the device which prevents the user from sticking their fingers into the sandwich of circuit boards. 
- If the user did somehow manage to stick their fingers into the printed circuit assemblies, the highest voltage on the board is 5 VDC, which falls into the 'extremely low voltage' IEC voltage range and is not considered hazardous. See [AS/ACIF S009:2006, Page 18](https://www.commsalliance.com.au/__data/assets/pdf_file/0009/2421/S009_2006r.pdf) for more information.
- The safety of the users images also needs to be considered, as if they were comprised it could lead to a number of issues. Due to the streaming nature of the device, images are not stored anywhere and as such cannot be easily stolen by an adversary. The easiest attack vector to gain images from the device would to be log into a currently streaming VeinCam and record the images displayed, however this would require the adversary to know the WiFi password of the VeinCam, and for them to be in close proximity of the device to be able to access the broadcast WiFi network.   

### Sourcing
Sourcing of the components also needs to be taken into consideration, as failure to source any given component of the VeinCam would prevent use and sale of the device. 
- All parts excluding the Raspberry Pi, NoIR camera, and the IR LEDs can be sourced from multiple suppliers at ease and are not a sourcing risk. Whilst the Raspberry Pi and NoIR camera are only available from a single source, they are mass produced items with high stock availability and is only a slightly higher risk item.  
- The high power IR LEDs on the other hand are only available from one supplier, and there are no other similar components available on the market. At the time of writing there are only 6700 LEDs available globally, and any quantities higher than that have a 5 month lead time. Fortunately only 6000 LEDs are required for a 1000 unit production run, and as such even accounting for overages there is enough supply to satisfy the VeinCams needs. However this could change at any point in time and as such it is an item which has a high risk of causing production delays if there is insufficient supply to meet the production demands.    

**Modularity:**
- Design considerations
- DIY kit design

**Price:**
- Design Considerations
- Price and cost of repair
- Comparible products for their cost
- Competing products.

## Competing Products
Competing Products (All medical devices, not fit for the educational market due to price point and licensing requirements as stated below):

### AccuVein
(https://www.accuvein.com/)
Displays a map of vasculature in real time on the surface of the skin. It comes up as red light where veins come up dark.
Difficult to find a price anywhere. Requires direct contact with AccuVein.

### VeinViewer
(https://www.christiemed.com/products/our-technology)
Displays similar to AccuVein but with green light.
Need to contact for quote or have a registered medical practitioner check the price at (http://www.balancemedical.com.au/order/)

### Veinsite
(https://vuetekscientific.com/veinsite-vein-finder/)
Portable, hands-free, big camera that sits on top of the head and covers the eyes with an IR lens. 
Similarly to AccuVein. Price unavailabe.

### UMTEC Portable Vein Detector
(https://www.amazon.com/Infrared-UMTEC-Portable-Illumination-Visualization/dp/B01NA0D98U)
Shines IR light on the skin, looks quite difficult to see the vein still.
Roughly $1000.




