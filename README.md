# Shaback-Challenge-2018-solution

## Opening Challenge

### Overview
The opening challenge starts with a page displaying the Shin Bet (Shabak) logo. Initially, the page seems unremarkable, but hovering over the logo reveals a map. Zooming in on the map, six marked points become visible, each containing shapes that form letters when viewed up close. The letters spell "JOINUS," marking the start of the challenge.

### Step-by-Step Solution

#### Initial Steps
1. **Page Inspection**: Hover over the Shin Bet logo to reveal a map.
2. **Map Exploration**: Zoom into each of the six marked points to identify the shapes forming the letters "JOINUS."

## Stage One: Software and Data Science
1. **Challenge Selection**: Choose the "software and data science" track.
2. **ZIP File Decryption**: 
   - A ZIP file is provided but requires a password.
   - Use `Fcrakzip` with the `rockyou.txt` wordlist to perform a dictionary attack.
3. **ZIP File Content**:
   - Extract two images and a text file.
   - Analyze the images and the text file. The images contain no useful information, but the text file includes Python code.
4. **Code Execution**:
   - Run the provided Python code, which generates a new image.
   - Inspect the new image to find "BINARY, START 10,000, - FIBONACCI."
5. **Binary Extraction**:
   - Combine bits from the second image starting at position 10,000, following the Fibonacci sequence.
   - The resulting message is "you got it."
6. **Submit the Answer**: Enter "you got it" to proceed to the next stage.

## Stage Two: The Persian
1. **File Analysis**:
   - A new image file is received but cannot be opened normally.
   - Use a Hex Editor to inspect the file and reveal hidden text.
2. **Hex Analysis**:
   - Decode the hex values to find the phrase: "return in base64 sum values below median."
   - Note the recurring "U05" pattern, representing Hebrew letters.
3. **Value Calculation**:
   - Sum the gematria values (Hebrew numerical values) of the letters.
   - Compute the median of all values and sum those below it.
   - Encode the result in base64.
4. **Submit the Answer**: The base64 result is "MjUwMTU3Nw==."

## Stage Three: The Usual Suspect
1. **Data File Inspection**:
   - Download and extract a CSV file and a `hint.txt` file.
   - The CSV contains four columns: `Id`, `ip`, `data`, and `url`.
2. **Suspect Identification**:
   - The `hint.txt` file lists 10 suspect IDs.
   - Analyze the CSV to find the behavior patterns of these suspects.
3. **Statistical Analysis**:
   - Check the number of IPs each suspect ID interacts with.
   - Identify the 10 users with the most IP interactions.
4. **Answer Submission**:
   - Return the most frequent IPs used by the suspects.
   - The final answer is "41.239.144.6,103.205.114.34,127.95.83.100."

