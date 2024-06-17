# Shaback Challenge 2018 Solution

**Solution provided by:** Elhanan Haenel

**Note:** All challenge files are uploaded except for the third level due to its large files size.

## The Shabak Challenge Adventure
![Shabak Logo](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/1.jpg)

The Shabak challenge began with a seemingly ordinary page displaying the Shabak logo. At first glance, it appeared unremarkable. However, as soon as I hovered the cursor over the logo, it magically transformed into a map.

![Map with Marked Points](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/2.jpg)

This unexpected change revealed six marked points on the map. Intrigued, I zoomed into each point, discovering that the shapes formed letters. Together, these letters spelled out "JOINUS," signaling the official start of the challenge.

![Map with Marked Points](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/3.jpg)

With excitement, I embarked on the software and data science track.

## Stage One: Find The Code


![ZIP File](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/4.jpg)

The first stage presented a ZIP file that required a password to unlock. Knowing this would be a tough nut to crack, I used `Fcrakzip` on `rockyou.txt` wordlist to perform a dictionary attack.
After some effort, I successfully decrypted the ZIP file. Inside, I found two images and a text file. The images seemed unimportant at first glance, but the text file contained Python code. After correcting and running the code, a new image was generated. Upon examining this image, I found a message: "BINARY, START 10,000, - FIBONACCI." Following these instructions, I extracted bits from the second image, starting at position 10,000 and using the Fibonacci sequence. This revealed the message "you got it."

![Decrypted Image](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/6.jpg)

With the correct answer in hand, I advanced to the next stage.

## Stage Two: The Persian

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


whoami = {} #the content file, I didn't add it here beacese its to big

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


```

Encoding this result in base64 provided the answer "MjUwMTU3Nw==," allowing me to proceed to the next stage.

![Hex Editor](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/8.jpg)

## Stage Three: The Usual Suspect

We got to the last challenge:

![Last Challenge](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/9.jpg)

The third stage challenged me to identify suspects based on provided data. After downloading and extracting a CSV file and a `hint.txt` file, I discovered the CSV contained four columns: `Id`, `ip`, `data`, and `url`. The `hint.txt` listed 10 suspect IDs. Analyzing the CSV, I identified patterns in the suspects' behavior. By checking how many IPs each suspect ID interacted with, I pinpointed the 10 users with the highest number of IP interactions.

```python
"""""
get the ip of suspects
"""""

id_of_suspects = [2449, 6796, 9237, 4024, 3538, 3608, 7239, 435, 5206, 2211]
ip = []

address = "log.csv"
input_file = open(addres, 'rb')
lines = []
for line in input_file:
    lines.append(line)



print len(lines)
for line in lines:
    #  print line
    y = line.split(",")

    if y[1] not in ip and int(y[0]) in x:
        ip.append(x[1])
input_file.close()

"""""
get the id that use the suspect ip
"""""

id_use_ip_of_suspect = []

address = "log.csv"
input_file = open(addres, 'r')
lines = input_file.read()
lines = lines.split('\n')
for line in lines:
    line = line.split(',')
    if len(line) > 2 and line[0] != "uid":
        if (line[1]) in ip and line[0] not in id_use_ip_of_suspect:
            id_use_ip_of_suspect.append(line[0])
input_file.close()

""""
print the num of ip the potential suspect used
"""""

num_of_ip_used = []

address = "log.csv"
input_file = open(addres, 'r')
lines = input_file.read()
lines = lines.split('\n')
for id in id_use_ip_of_suspect:
    for line in lines:
        line = line.split(',')
        if len(line) > 2 and line[0] != "uid":
            if (line[1]) in ip and line[1] not in num_of_ip_used and int(line[0]) == id:
                num_of_ip_used.append(line[1])
    print str(id), ":", str(len(num_of_ip_used))
input_file.close()


```


Returning the most frequent IPs used by these suspects, I found the final answer: "41.239.144.6,103.205.114.34,127.95.83.100."

![CSV File](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/10.jpg)

With that, I completed the Shabak challenge. The experience was a thrilling and enjoyable journey into the world of puzzles and code-breaking!

![Completion](https://github.com/ElhananHaenel/Shaback-Challenge-2018-solution/blob/main/image/11.jpg)

