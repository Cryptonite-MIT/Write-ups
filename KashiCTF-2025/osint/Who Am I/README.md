# Who am I??

Domain: OSINT

Points: 100

Solves: 485

### Given information

> You've stumbled upon a bustling street with political posters. Find out after which politician this road is named. Flag Format: KashiCTF{Full_Name}
> 
> Flag format clarification: The full name is in Title_Case, without any diacritics, with each "special character (anything other than a-zA-Z)" replaced by an underscore.
> 
>![Road_Not_Taken](https://github.com/user-attachments/assets/d8dd6c2b-2deb-4f95-9959-f29d26b52bf5)
 

### Solution

Writeup author: Guitaristsam, teayah

1. Noticed the email address: `bazilika@dh.hu`.       
2. Recognized `.hu` as the country code for **Hungary**.       
3. Searched for "bazilika dh.hu" and found:         
   **[https://dh.hu/iroda/bazilika](https://dh.hu/iroda/bazilika)**
4. The webpage mentioned an address:       
   **1065 Budapest, 6th district, Bajcsy-Zsilinszky street 25**.
5. Looked up the full name associated with Bajcsy-Zsilinszky street:    
   **Endre Bajcsy-Zsilinszky**.
6. Constructed the flag:     
   **KashiCTF{Endre_Bajcsy_Zsilinszky}**


**Flag: `KashiCTF{Endre_Bajcsy_Zsilinszky}`**

Note:
- Another approach could be to search the company whose office is in the picture, which turns out to be `Duna House`, and to find its location that matches the photo on Google Maps.
