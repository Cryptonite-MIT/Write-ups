# Kings

Domain: OSINT

Points: 456

Solves: 50

### Given information

> Did you know the cosmic weapons like this? I found similar example of such weapons on the net and it was even weirder. This ruler's court artist once drew the most accurate painting of a now extinct bird. Can you tell me the coordinates upto 4 decimal places of the place where this painting is right now.
> 
> Flag Format: `KashiCTF{XX.XXXX_YY.YYYY}`

### Solution

Writeup author: teayah

The 'cosmic weapon' attached is *Tutankhamun's meteoric iron dagger*. 

Searching for other meteoric daggers, you could find this list 

[https://www.cnet.com/pictures/swords-from-the-stars-weapons-forged-from-meteoric-iron/](https://www.cnet.com/pictures/swords-from-the-stars-weapons-forged-from-meteoric-iron/)

Connecting this list with the other hint about the painting in the description, the ruler in question is *Jahangir*, whose court artist was `Ustad Mansur`, who's also attributed for making the most accurate painting of a dodo.

This article says that the painting of the dodo is kept in the *Hermitage Museum, St. Petersburg.* 

[https://www.tbsnews.net/feature/travel/dodos-mughal-court](https://www.tbsnews.net/feature/travel/dodos-mughal-court)

The coordinates required for the flag are around the front area of the museum and required a bit of a brute-force approach to be found.

**Flag: `KashiCTF{59.9399_30.3149}`**
