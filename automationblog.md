# AUTOMATION PROJECT BLOG

## WEEK ONE: Automating Scheduled Motivational and Inspirational Quotes for Mental Health

In today's fast-paced world, dealing with change can be incredibly challenging, often taking a toll on our mental health. As someone who deeply cares about the well-being of others, I've been reflecting on ways to offer consistent support and inspiration to those navigating through life's uncertainties. Thus, I embarked on a journey to automate a process that delivers motivational and inspirational quotes regularly to uplift spirits and ease the strain on mental health.

Change is inevitable, and it's during these times that we need reminders to stay resilient, to keep pushing forward, and to believe that everything will eventually fall into place. However, manually sourcing and posting motivational quotes daily can be both cumbersome and prone to lapses, especially amidst the hustle and bustle of everyday life. Therefore, automation seemed like the perfect solution to ensure a steady stream of encouragement for those who may need it the most.

Feeling overwhelmed and drained is a sentiment many of us can relate to, often during periods of change and uncertainty. It's in these moments that receiving inspirational quotes from renowned and anonymous writers alike can serve as a beacon of hope. These quotes offer reassurance that change is merely a process, not the final destination. They remind us that amidst the chaos, there's room for growth, resilience, and transformation.

By automating the delivery of such quotes, we're offering more than just words on a screen – we're providing a lifeline to those grappling with shattered hopes and dwindling motivation. Each quote becomes a spark, igniting the flame of possibility and reminding individuals of their inner strength. In this way, even the simplest of automations can have a profound impact, breathing new life into weary souls and guiding them towards brighter horizons.

My goal with this automation project is to create a seamless process for updating inspirational quotes at regular intervals. While I'm relatively new to the world of coding and automation, I was introduced to the concept of APIs (Application Programming Interfaces) during a foundational science class. Despite my initial confusion, I recognized their potential for accessing external data and integrating it into my projects.

Initially, I toyed with the idea of creating my own API, drawing from the knowledge gained in class. However, my attempts were met with frustration and dead ends. It was only through the guidance of resources like ChatGPT that I discovered the Zen Quotes API, a treasure trove of wisdom waiting to be tapped into.

Armed with newfound knowledge and a renewed sense of determination, I set out to build a simple Python script using Visual Studio Code. By leveraging the Zen Quotes API, I aim to automate the process of fetching and posting motivational quotes at regular intervals, providing a steady stream of encouragement for those in need.

After conducting an anonymous survey through a questionnaire, I found the results to be highly encouraging, reaffirming the necessity and potential impact of my automation project. The responses provided valuable insights into people's attitudes towards motivational quotes and their relevance in daily life.

The survey revealed a significant frequency of engagement with motivational quotes, with many participants indicating a regular habit of seeking out such content for inspiration and encouragement. Moreover, a majority expressed that motivational quotes have positively influenced their mood and mindset during challenging times, highlighting their perceived effectiveness in promoting well-being.

Overall, the survey outcomes served as a compelling validation of the importance of motivational quotes in people's lives and underscored the potential benefits of automating their delivery. Armed with this feedback, I am more determined than ever to continue with my automation project, confident in its ability to provide meaningful support and encouragement to individuals navigating through life's uncertainties.

Stay tuned as I dive deeper into the intricacies of automation and share the progress of my journey in the weeks to come.


# WEEK TWO; THE AUTOMATION PROCESS

First, let me explain my Python Script. I have to acknowledge the fact that I couldn’t have written the script on my own, I used resources like ChatGPT, read two virtual books, ‘AUTOMATE THE BORING STUFF WITH PYTHON’ and ‘THINK PYTHON 2’. I even applied some of the knowledge I got from reading an article on scraping webpages with ‘Beautiful Soup’. 
You will find the code amongst my files here on GitHub as,'quote_generator.py'

# PYTHON SCRIPT CREATION:
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

![IMG_2041](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/522e1bb9-fa61-4f7f-bcb8-66aa983b67a8)
HIP HIP HURRA🥳
# WEEK THREE; SETTING UP THE WORKFLOW
(with this particular task, I failed two times before it worked the third time when i was just clicking things on GitHub😂)
To set up the workflow for the script on GitHub, I went to the 'Actions' which led me to my workflows then I went to 'New workflow' and went on to set up a workflow for myself.  This action created a '.github workflow' folder with a 'yml' file embedded in it. Again, this workflow file is visible on my GitHub repo as, '.github/workflows.'
I then put in a code in the file which would run my Python quote_generator.py script every five minutes. After making the commit, I had to wait for the moment of truth. (It was so scary😂.)

![IMG_2042](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/10602e68-7151-418c-9ef3-9136fc7f6830)
TADAAAA😭😹

![IMG_2043](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/463cf264-5224-4c34-9659-134d3fd06425)
I am definately going into the ocean.🤩

(SIRI, PLAY ME,'IT'S A GOOD DAY TINEE NE'😭😹)

# WEEK FOUR; COMMENTS AND OVERALL IMPRESSION 
I shed a lot of tears and had a lot of migranes during this process.

Three times I caught myself nearly  saying,"Scheiße." To even decide on the automation project was tough.
After I knew what to do, the problem was not the code but the execution of the code. Before, I had no idea of what I was doing and I made so many errors. I even created a workflow file without having a corresponding Python Script.😹
I also made some radical decisions as well as silly ones. I created so many branches and some forks(which I deleted after) to test every step I made towards the automation project. This helped me to keep the mess from my main branch until I was sure of the progress. Once, I did feel lazy to work on a branch and I messed upn my main branch (I did cry) but before that i had previously copied all the files on my GitHub repo twice on my local machine and my phone also😹 so I deleted everything and copied it back.
I also sought advice from 'Stack Overflow' and 'Python Reddit' everytime I got an error with my workflow and they were indeed helpful.
In some months to come after gaining more insight, I look forward to making advancements.
I am open to any advice and adjustments. I am looking for ways to make the automation even better and I can not do that without your honest views, comments and contributions. Thank you.

