# WEEK TWO; THE AUTOMATION PROCESS

First, let me explain my Python Script. I have to acknowledge the fact that I couldn’t have written the script on my own, I used resources like ChatGPT, read two virtual books, ‘AUTOMATE THE BORING STUFF WITH PYTHON’ and ‘THINK PYTHON 2’. I even applied some of the knowledge I got from reading an article on scraping webpages with ‘Beautiful Soup’. 
You will find the code amongst my files here on GitHub as,'quote_generator.py'

##### PYTHON SCRIPT CREATION:
Step one- So with my script, like I mentioned before, I created it with Virtual Code Studio(VS code). I first created a Python file with the extension (.py) and opened it. 

Step two- I imported two python libraries.
import requests 
import json
The ‘requests’ library is for making HTTP requests.
The ‘json’ library is for handling JSON data. 
Then I used the ‘def’ Python function to define the string ‘get_random_quote’
(I included the block comments in the code so I don’t forget the meaning of the code myself. 
The line 6 of the code, 'response = requests.get("https://zenquotes.io/api/random")' is to get random quotes from Zen Quotes API. I achieved this my putting the URL of Zen Quotes API into a variable (‘response’).
The remaining of the code checks if the request was successful and if yes returns with the quote and the author if unsuccessful, it would return,"Failed to fetch a code, try again later."
After writing this short script, I run it on my VS code to see if it worked before i uploded it to my repository

```
import requests
import json

def get_random_quote():
    # Fetch a random quote from the Zen Quotes API
    response = requests.get("https://zenquotes.io/api/random")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        quote_data = json.loads(response.text)

        # Extract and return the quote and author
        quote = quote_data[0]['q']
        author = quote_data[0]['a']

        return f'"{quote}"\n- {author}'
    else:
        return "Failed to fetch a quote. Try again later."

# Print a random quote
print(get_random_quote())

```
![IMG_2041](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/bb1782bf-20da-4820-886d-87ab10e1a2a4)

HIP HIP HURRA🥳
