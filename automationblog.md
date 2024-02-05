# AUTOMATION PROJECT BLOG
# WEEK ONE
AUTOMATING SCHEDULED MOTIVATIONAL AND INSPIRATIONAL QUOTES FOR MENTAL HEALTH.

I wrote a blog based on dealing with change as change can be hard on the mental health of an individual. So I thought it wise to automate a process whereby inspirational and motivational quotes would be generated consistently every 5 minutes to inspire the readers not to give up. In the process of change which is mostly overwhelming to the individuals, it would be nice to be reminded consistently that evrything would pan out. This would help reduce stress and strain on the mental health of individuals. Finding and posting the motivational quotes manually would be tiresome for me to do on a daily. I might even forget on somedays, hence the automation. 
For my automation project, I decided to use a simple python script with Virtual Code Studio and later uploaded into my github files.

# AIM
To automate a consistent  process of updating inspirational quotes. I am very new to all of this so I did not know how to acheieve what I wanted but during coding class for  foundation of sciences, we did something called "API". I had no idea what that was so I asked my classmate what it was and I got a basic idea. So I thought, why not get a quote API and put it in a Python Script?
Now, I had an idea of what to do but I did not know how. (I am still a beginner)
But I knew I needed an API and a Python Script. Initially, I wanted to use the knowledge from the sciences class to create my own API but I kept messing up and getting stuck till ChatGPT made me aware that I could access an API called,"ZEN QUOTES API" (Phew😅)
# Process
First, let me explain my Python Script. I have to acknowledge the fact that I couldn’t have written the script on my own, I used resources like ChatGPT, read two virtual books, ‘AUTOMATE THE BORING STUFF WITH PYTHON’ and ‘THINK PYTHON 2’. I even applied some of the knowledge I got from reading an article on scraping webpages with ‘Beautiful Soup’. 
You will find the code amongst my files here on GitHub as,'quote_generator.py'
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
# SETTING UP THE WORKFLOW
(with this particular task, I failed two times before it worked the third time when i was just clicking things on GitHub😂)
To set up the workflow for the script on GitHub, I went to the 'Actions' which led me to my workflows then I went to 'New workflow' and went on to set up a workflow for myself.  This action created a '.github workflow' folder with a 'yml' file embedded in it. Again, this workflow file is visible on my GitHub repo as, '.github/workflows.'
I then put in a code in the file which would run my Python quote_generator.py script every five minutes. After making the commit, I had to wait for the moment of truth. (It was so scary😂.)

![IMG_2042](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/10602e68-7151-418c-9ef3-9136fc7f6830)
TADAAAA😭😹

![IMG_2043](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/463cf264-5224-4c34-9659-134d3fd06425)
I am definately going into the ocean.🤩

(SIRI, PLAY ME,'IT'S A GOOD DAY TINEE NE'😭😹)

# COMMENTS AND OVERALL IMPRESSION 
I shed a lot of tears and had a lot of migranes during this process.

Three times I caught myself nearly  saying,"Scheiße." To even decide on the automation project was tough.
After I knew what to do, the problem was not the code but the execution of the code. Before, I had no idea of what I was doing and I made so many errors. I even created a workflow file without having a corresponding Python Script.😹
I also made some radical decisions as well as silly ones. I created so many branches and some forks(which I deleted after) to test every step I made towards the automation project. This helped me to keep the mess from my main branch until I was sure of the progress. Once, I did feel lazy to work on a branch and I messed upn my main branch (I did cry) but before that i had previously copied all the files on my GitHub repo twice on my local machine and my phone also😹 so I deleted everything and copied it back.
I also sought advice from 'Stack Overflow' and 'Python Reddit' everytime I got an error with my workflow and they were indeed helpful.
In some months to come after gaining more insight, I look forward to making advancements.
I am open to any advice and adjustments. I am looking for ways to make the automation even better and I can not do that without your honest views, comments and contributions. Thank you.

