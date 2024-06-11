# Shaback Challenge 2018 Solution

Solution provided by: Elhanan Haenel

## The Shabak Challenge Adventure
![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/1.jpg)

The Shabak challenge kicked off with a seemingly plain page displaying the Shabak logo. At first glance, there appeared to be nothing significant about the page. However, as soon as I hovered the cursor over the logo, it magically transformed into a map.

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/2.jpg)

This unexpected change revealed six marked points on the map. Intrigued, I zoomed into each point, discovering that the shapes formed letters. Together, these letters spelled out "JOINUS," signaling the official start of the challenge. 

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/3.jpg)

With excitement, I embarked on the software and data science track.

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/4.jpg)

The first stage presented a ZIP file that required a password to unlock. Knowing this would be a tough nut to crack, I used `Fcrakzip` on `rockyou.txt` wordlist to perform a dictionary attack.

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/5.jpg)

After some effort, I successfully decrypted the ZIP file. 

Inside, I found two images and a text file. The images seemed unimportant at first glance, but the text file contained Python code. After correcting and running the code, a new image was generated. Upon examining this image, I found a message: "BINARY, START 10,000, - FIBONACCI." Following these instructions, I extracted bits from the second image, starting at position 10,000 and using the Fibonacci sequence. This revealed the message "you got it." 

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/6.jpg)

With the correct answer in hand, I advanced to the next stage.

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/7.jpg)

In the second stage, I was given an image file that refused to open normally. I turned to a Hex Editor to dig deeper into the file. The hex values translated into the phrase: "return in base64 sum values below median." Additionally, I noticed a recurring pattern "U05," which represented Hebrew letters. Realizing that I needed to calculate the gematria values (Hebrew numerical values) of these letters, I summed them up, computed the median, and summed the values below the median.

```python
from statistics import median


def clean(str):
    """
    gets string, return only hebrew unicode characters
    """
    # remove punctuation:
    str = str.translate([None, " .,"])
    chars = str.split("u05")[1:]
    # remove garbage characters
    for i, chr in enumerate(chars):
        chars[i] = chr[:2]
    return chars


def gematria(letter):
    """
    gets a hebrew letter, returns it's gematria
    """
    value = {"d0": 1, "d1": 2, "d2": 3, "d3": 4, "d4": 5, "d5": 6, "d6": 7, "d7": 8, "d8": 9, "d9": 10, "db": 20, "dc": 30, "de": 40, "e0": 50, "e1": 60, "e2": 70, "e4": 80, "e6": 90, "e7": 100, "e8": 200, "e9": 300, "ea": 400}
    return value[letter]

def calc(text):
    """
    gets list of chars, returns sum of gematria
    """
    text = clean(text)
    sum = 0
    for chr in text:
        sum += gematria(chr)
    return sum

whoami ={"0x1": [{"text": "z9u05d3su05e9u05d7u05e4gz p2P u05d4u05d1u05e2 Yu05d2E3b Wpu05e7khiku05d4u05dbhu05dc Mu05deTu05d2u05e6MYtu05d2Wu05d9 E4u05d8TAsu05deu05e4u05e8u05d2u05d6V 1wT u05e2u05e6 OKVHD u05d6u05dbTpgFJu05e7 u05d6u05d8Du05e2pgwtTu05d3u05dbq vLZdpeaA u05e6u....}]} #its not all the file(its big for this file

values = []
# whoami: 22 dictionaries (list of dictionaries)
for dict_list in whoami.values():
    # dict list: few dictionaries (text, value pairs)
    for pairs_dict in dict_list:
        g = calc(pairs_dict["text"])
        print("Original value:" + str(pairs_dict["value"]) + "    Calculated vlue:" + str(g))
        # print(calc(sub_dict["text"]))
        values.append(g)
print(values)
print(len(values))
print("Sum of values below median:")
print(sum(filter(lambda x: x<median(values), values)))


Encoding this result in base64 provided the answer "MjUwMTU3Nw==," allowing me to proceed to the next stage.

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/8.jpg)

We got to the last challenge:

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/9.jpg)

The third stage challenged me to identify suspects based on provided data. After downloading and extracting a CSV file and a `hint.txt` file, I discovered the CSV contained four columns: `Id`, `ip`, `data`, and `url`. The `hint.txt` listed 10 suspect IDs. Analyzing the CSV, I identified patterns in the suspects' behavior. By checking how many IPs each suspect ID interacted with, I pinpointed the 10 users with the highest number of IP interactions. Returning the most frequent IPs used by these suspects, I found the final answer: "41.239.144.6,103.205.114.34,127.95.83.100."

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/10.jpg)

With that, I completed the Shabak challenge. The experience was a thrilling and enjoyable journey into the world of puzzles and code-breaking!

![](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/11.jpg)
