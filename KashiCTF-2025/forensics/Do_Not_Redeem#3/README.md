# Do Not Redeem #3

**Domain:** Forensics

**Points:** 300

**Solves:** 10

### **Given Information**

> Too bad, Kitler did get scammed. Kitler met a lot of people recently, and is having a hard time trying to figure out who exactly the scammer could've been. Can you figure out the scammer's username (on the platform they met), and the link through which the scammer sent Kitler the scam app? Answer according to the below flag format:
>
> **Flag format:** `KashiCTF{username_link}`
> *e.g., `KashiCTF{savsch_https://www.youtu.be/dQw4w9WgXcQ}`*

### **Solution**

**Writeup author:** lvert

1. **Identifying the Source of Communication:**
   - The scammer likely communicated with Kitler via **Discord**.
   - Discord stores cached data files in its directory, typically found at:
     ```
     data/com.discord/
     ```

2. **Extracting Relevant Data:**
   - The provided dataset contains `.gz` compressed JSON files as part of Discord’s HTTP cache.
   - We extract them using the following command:
     ```bash
     gunzip *.gz
     ```
   - This decompresses the files for analysis.

3. **Searching for Suspicious Content:**
   - Since we need to find the scammer’s message containing a malicious link, we search for message contents within the extracted JSON files:
     ```bash
     grep -i "content" *
     ```
   - This reveals the scammer’s username (`savsch`) and the phishing link (`https://we.tl/t-Ku8Le7js`).

**Flag:** `KashiCTF{savsch_https://we.tl/t-Ku8Le7js}`

