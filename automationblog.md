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
# WEEK THREE; SETTING UP THE WORKFLOW
(with this particular task, I failed two times before it worked the third time when i was just clicking things on GitHub😂)
To set up the workflow for the script on GitHub, I went to the 'Actions' which led me to my workflows then I went to 'New workflow' and went on to set up a workflow for myself.  This action created a '.github workflow' folder with a 'yml' file embedded in it. Again, this workflow file is visible on my GitHub repo as, '.github/workflows.'
I then put in a code in the file which would run my Python quote_generator.py script every five minutes. After making the commit, I had to wait for the moment of truth. (It was so scary😂.)

![IMG_2042](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/10602e68-7151-418c-9ef3-9136fc7f6830)
TADAAAA😭😹

![IMG_2043](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/463cf264-5224-4c34-9659-134d3fd06425)
I am definately going into the ocean.🤩

(SIRI, PLAY ME,'IT'S A GOOD DAY TINEE NE'😭😹)

# WEEK FOUR: COMMENTS AND OVERALL IMPRESSION

Reflecting on the past four weeks, I find myself immersed in a whirlwind of emotions, challenges, and triumphs. The journey towards automating inspirational quotes has been nothing short of transformative, marked by tears, migraines, and moments of sheer frustration. Yet, amidst the chaos, I've discovered profound lessons and invaluable insights that have reshaped my understanding of coding, perseverance, and personal growth.

The inception of this automation project was not without its hurdles. From the arduous task of selecting a suitable project to grappling with the intricacies of code execution, every step presented its own set of challenges. The initial ambiguity surrounding the project left me feeling overwhelmed and uncertain, teetering on the brink of exasperation. However, as I delved deeper into the intricacies of coding and automation, clarity began to emerge from the fog of uncertainty.

One of the most significant challenges I encountered was the discrepancy between conceptualizing the code and executing it effectively. While the logic behind the code seemed straightforward, translating it into functional scripts proved to be a formidable task. Countless errors and missteps punctuated my journey, leading to moments of self-doubt and frustration. However, with each setback came an opportunity for growth and learning.

The iterative nature of the development process allowed me to experiment, iterate, and refine my approach. Radical decisions, such as creating multiple branches and forks to test different strategies, proved instrumental in mitigating risks and minimizing disruptions to the main branch. Despite occasional setbacks and moments of despair, the resilience of the human spirit prevailed, propelling me forward in pursuit of my goals.

The support and guidance garnered from online communities such as Stack Overflow and Python Reddit served as beacons of light in moments of darkness. The collective wisdom and camaraderie shared within these forums offered solace and reassurance, reminding me that I was not alone in my struggles.

In the months to come, I aspire to build upon the foundation laid during this journey, striving for continuous improvement and innovation. The prospect of enhancing user experience through notifications and integrating automation results into the Markdown README file excites me, fueling my passion for exploration and discovery.

The cost-benefit analysis of this automation project reveals a compelling narrative of efficiency and impact. While the initial investment of time and effort may have been substantial, the dividends reaped in terms of time saved, resources conserved, and lives inspired far outweigh the costs incurred. As an economist, I am acutely aware of the rationality underlying this decision, affirming the inherent value of automation in enhancing productivity and well-being.

As the curtain falls on this chapter of my journey, I find solace in the knowledge that my humble automation endeavor has the power to spread joy, inspire hope, and perhaps, even save lives. The profound impact of this journey transcends mere code and algorithms, resonating deeply with the human experience.

In retrospect, these four weeks have been a testament to the resilience of the human spirit and the transformative power of perseverance. As I bid farewell to this chapter and embark on new adventures, I carry with me the lessons learned, the memories forged, and the unwavering belief in the limitless potential of the human spirit.


[Link to File 1]()
