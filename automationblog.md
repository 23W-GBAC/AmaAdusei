# AUTOMATION PROJECT BLOG
AUTOMATING SCHEDULED MOTIVATIONAL AND INSPIRATIONAL QUOTES FOR MENTAL HEALTH.

I wrote a blog based on dealing with change as change can be hard on the mental health of an individual. So I thought it wise to automate a process whereby inspirational and motivational quotes would be generated consistently every 5 minutes to inspire the readers not to give up. This would be tiresome for me to do on a daily. I might even forget on somedays, hence the automation. 
For my automation project, I decided to use a simple python script with Virtual Code Studio and later uploaded into my github files.
# AIM
To automate a consistent  process of updating inspirational quotes. I am very new to all of this so I did not know how to acheieve what I wanted but during coding class for  foundation of sciences, we did something called "API". I had no idea what that was so I asked my classmate what it was and I got a basic idea. So I thought, why not get a quote API and put it in a Python Script?
Now, I had an idea of what to do but I did not know how. (I am still a beginner)
But I knew I needed an API and a Python Script. Initially, I wanted to use the knowledge from the sciences class to create my own API but I kept messing up and getting stuck till ChatGPT made me aware that I could access an API called,"ZEN QUOTES API" (Phew😅)
# Process
First, let me explain my Python Script. I have to acknowledge the fact that I couldn’t have written the script on my own, I used resources like ChatGPT, read two virtual books, ‘Automate THE BORING STUFF WITH PYTHON’ and ‘THINK PYTHON 2’. I even applied some of the knowledge I got from reading an article on scraping webpages with ‘Beautiful Soup’. 
Step one- So with my script like I mentioned before, I created it with Virtual Code Studio(VS code). I first created a Python file with the extension (.py) and opened it. 
Step two- I imported two python libraries.
import requests 
import json
The ‘requests’ library is for making HTTP requests.
The ‘json’ library is for handling JSON data. 
Then I used the ‘def’ Python function to define the string ‘get_random_quote’
(I included the block comments in the code so I don’t forget the meaning of the code myself. 
The line 6 of the code is to get random quotes from Zen Quotes API. I achieved this my putting the URL of Zen Quotes API into a variable (‘response’).
The remaining of the code checks if the request was successful and if yes returns with the quote and the author if unsuccessful, it would return,"Failed to fetch a code, try again later.
After writing this short script, I run it on my VS code to see if it worked before i uploded it to my repository

![IMG_2041](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/522e1bb9-fa61-4f7f-bcb8-66aa983b67a8)
HIP HIP HURRA🥳

# SETTING UP THE WORKFLOW
(with this particular task, I failed two times before it worked the third time when i was just clicking things on GitHub😂)
To set up the workflow for the script on GitHub, I went to the 'Actions' which led to to my workflows then i went to
