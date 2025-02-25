# Old Diner

Domain: OSINT

Points: 411

Solves: 72

### Given information

> My friend once visited this place that served ice cream with coke. He said he had the best Greek omlette of his life and called it a very american experience. Can you find the name of the diner and the amount he paid?
> 
> Flag Format: `KashiCTF{Name_of_Diner_Amount}`
> 
> (**For clarification on the flag format**: The diner's name is in title case with spaces replaced by underscores. The amount is without currency sign, and in decimal, correct to two decimal places, i.e. `KashiCTF{Full_Diner_Name_XX.XX}`)

### Solution

Writeup author: teayah

 Searching for an old diner with ice cream and coke, you'd find that challenge description and title reference a recurring Internet meme circulated often on X (Twitter) called *This 97 year old diner still serves coke the old fashioned way*
 
Googling the diner name gives you `Lexington Candy Shop`

Looking up its menu, you would find the prices of the dishes `Greek Omelette` & `WW Favorite Greek Omelette`, but researching further such as looking for 'Greek' in the reviews for the place on Tripadvisor, you'd find this review: 

[https://www.tripadvisor.in/ShowUserReviews-g60763-d522599-r737610550-Lexington_Candy_Shop-New_York_City_New_York.html](https://www.tripadvisor.in/ShowUserReviews-g60763-d522599-r737610550-Lexington_Candy_Shop-New_York_City_New_York.html)

The image of the receipt attached has the amount in question for the flag.

**Flag: `KashiCTF{Lexington_Candy_Shop_41.65}`**
