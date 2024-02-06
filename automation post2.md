# WEEK TWO (28.12.2023): THE AUTOMATION PROCESS
Exploring potential solutions and embarking on iterative attempts to develop a viable solution are integral steps in any project. In the context of automating the delivery of motivational quotes, several approaches and attempts may have been considered. Here are some possible solutions and errand attempts that could have been pursued:

1. Manual Posting:

Initial Attempt: Manually curating and posting motivational quotes at regular intervals.
Limitations: Time-consuming, prone to inconsistency, and lacks scalability.
2. Third-Party Tools:

Attempt: Exploring third-party tools or platforms designed for scheduling and managing social media content.
Limitations: Limited customization, dependency on external services, and potential cost implications.
3. Custom Scripting:

Attempt: Developing a custom Python script to fetch and post motivational quotes from a predefined list.
Limitations: Requires programming knowledge, scalability challenges, and potential reliability issues.
4. API Integration:

Attempt: Integrating with an external API that provides a curated collection of motivational quotes.
Limitations: Dependency on external API availability, potential rate limits, and data reliability.
5. GitHub Actions:

Attempt: Leveraging GitHub Actions to automate the process of fetching and posting motivational quotes.
Limitations: Learning curve associated with GitHub Actions, potential configuration complexities, and troubleshooting challenges.
6. Community Support:

Attempt: Seeking guidance and support from online communities, forums, or developer networks.
Limitations: Reliance on external expertise, varying quality of advice, and potential delays in receiving assistance.
7. Continuous Iteration:

Attempt: Adopting an iterative approach to development, refining the solution based on feedback and testing.
Limitations: Time-consuming, potential setbacks, and the need for ongoing maintenance and optimization.
Each attempt and solution explored may have offered unique insights and learnings, contributing to the eventual development of a robust automation solution. Through perseverance, experimentation, and a willingness to adapt, the process of refining and evolving the solution ultimately leads to the creation of a successful automation project.

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
