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

![Image 06 02 24 at 01 08](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/eb98f82b-3465-4e52-be0a-f8661529a349)

https://docs.google.com/spreadsheets/d/1M2FSSApnnrnmazHNuAQqc5Iyf2U3OFHSTzO_C2emNx0/edit?usp=sharing


The survey revealed a significant frequency of engagement with motivational quotes, with many participants indicating a regular habit of seeking out such content for inspiration and encouragement. Moreover, a majority expressed that motivational quotes have positively influenced their mood and mindset during challenging times, highlighting their perceived effectiveness in promoting well-being.

Overall, the survey outcomes served as a compelling validation of the importance of motivational quotes in people's lives and underscored the potential benefits of automating their delivery. Armed with this feedback, I am more determined than ever to continue with my automation project, confident in its ability to provide meaningful support and encouragement to individuals navigating through life's uncertainties.

Stay tuned as I dive deeper into the intricacies of automation and share the progress of my journey in the weeks to come.


# WEEK TWO; THE AUTOMATION PROCESS
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
# WEEK THREE; SETTING UP THE WORKFLOW
Embarking on the journey to automate my inspirational quotes was not without its challenges. In fact, I encountered failure not once, but twice before finally achieving success on the third attempt. The process, marked by trial and error, taught me invaluable lessons in resilience, determination, and the power of perseverance.

With each failed attempt came an opportunity to learn and adapt. As I navigated through the labyrinth of GitHub's interface, I found myself confronted with a myriad of options and configurations, each seemingly more daunting than the last. Despite my initial trepidation, I resolved to conquer the challenge head-on, armed with little more than determination and a willingness to learn.

The journey began with a simple click, a humble gesture that would ultimately set the wheels of automation in motion. Navigating to the 'Actions' tab on GitHub, I found myself thrust into a world of workflows and configurations, each a testament to the vast potential of automation.

Undeterred by the complexities that lay ahead, I ventured forth, guided by a singular objective: to set up a workflow that would breathe life into my automation project. With bated breath, I clicked on 'New workflow', a seemingly innocuous action that would set the stage for the trials and tribulations that lay ahead.

As I delved deeper into the intricacies of workflow creation, I found myself grappling with unfamiliar concepts and terminology. 'YML files', 'actions', and 'triggers' became the building blocks of my digital odyssey, each contributing to the intricate tapestry of automation that I sought to weave.

The creation of the '.github/workflows' folder marked a pivotal moment in my journey, a tangible manifestation of my commitment to the automation cause. Within its digital confines lay the key to unlocking the full potential of my project, a beacon of hope amidst the sea of uncertainty.

With trembling hands and a racing heart, I began to populate the YML file with code, each line a testament to the countless hours spent poring over documentation and seeking guidance from online resources. The code, a delicate dance of syntax and semantics, held within its grasp the power to transform mere lines of text into a symphony of automation.

With a sense of trepidation, I made the final commit, a humble offering to the gods of automation in the hopes of securing their favor. And then, I waited. The moments stretched into eternity as I watched, breathless, for the faint glimmer of success amidst the darkness of failure.

And then, it happened. A flicker of light amidst the shadows, a beacon of hope in the vast expanse of uncertainty. The workflow sprung to life, its digital heart pulsating with the rhythm of automation as it executed my Python script with clockwork precision.

In that moment, I knew. I had conquered the beast of automation, vanquishing uncertainty and doubt with the indomitable power of human ingenuity. The journey had been long and arduous, fraught with pitfalls and setbacks, but in the end, victory was mine.

As I reflect on the trials and triumphs of the past, I am reminded of the timeless adage: "Through adversity comes strength." In the crucible of failure, I found the seeds of success, nurtured by perseverance and watered by determination.

And so, I march onward, emboldened by the knowledge that no challenge is insurmountable, no obstacle too great to overcome. With each new day comes a fresh opportunity to push the boundaries of what is possible, to explore new horizons and chart a course towards a future shaped by the boundless power of automation.


![IMG_2042](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/10602e68-7151-418c-9ef3-9136fc7f6830)
TADAAAA😭😹

![IMG_2043](https://github.com/23W-GBAC/AmaAdusei/assets/148862738/463cf264-5224-4c34-9659-134d3fd06425)
I am definately going into the ocean.🤩

(SIRI, PLAY ME,'IT'S A GOOD DAY TINEE NE'😭😹)
Final Solution:

The automation project embarked upon to schedule motivational and inspirational quotes has evolved into a transformative endeavor. After meticulous planning, experimentation, and implementation, the final solution encapsulates a Python script integrated with GitHub workflows to deliver motivational quotes at regular intervals.

Utilizing the Zen Quotes API, the Python script fetches random quotes, ensuring a diverse selection of inspirational content. The GitHub workflow orchestrates the execution of the Python script, ensuring seamless dissemination of motivational messages to users.

Reflection on Potential Advantages:

Enhanced Efficiency: The automation eliminates the need for manual intervention, streamlining the process of generating and sharing motivational quotes.
Consistency and Reliability: By automating the workflow, the project ensures consistent delivery of inspirational content, fostering engagement and trust among users.
Time Savings: The automation project saves significant time and effort by reducing repetitive tasks, allowing users to focus on more strategic initiatives.
Scalability: The automation solution is scalable, capable of accommodating increased demand and user engagement without compromising performance.
Reflection on Potential Disadvantages:

Technical Complexity: The integration of Python scripts with GitHub workflows requires a certain level of technical expertise, posing a barrier to entry for individuals with limited programming knowledge.
Dependency on External APIs: The reliance on external APIs, such as the Zen Quotes API, introduces a degree of vulnerability to service disruptions or changes in API functionality.
Maintenance and Updates: Continuous monitoring and maintenance are essential to ensure the smooth operation of the automation project, including addressing potential issues and updating dependencies.
In conclusion, while the automation project offers numerous advantages in terms of efficiency, consistency, and scalability, it is not without its challenges and considerations. By carefully weighing the potential advantages and disadvantages, and implementing robust maintenance and monitoring practices, the automation project stands poised to deliver lasting value and impact to users and stakeholders alike.

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
Initial Investment:
The initial investment of time and resources into the automation project was considerable. It involved research, learning, experimentation, and troubleshooting, spanning several weeks. Additionally, setting up the workflow on GitHub and writing the Python script required significant effort and dedication.

Time and Resources Saved:
Over the next five years, the automation project is poised to yield substantial time and resource savings. By automating the process of generating and disseminating inspirational quotes, the project eliminates the need for manual intervention, thus reducing the time and effort required to perform repetitive tasks. Furthermore, the automation ensures consistency and reliability in delivering motivational content to users, enhancing overall efficiency and productivity.

Economic Benefit:
The economic benefit of the automation project becomes evident when considering the long-term savings and efficiency gains it affords. While the initial investment may have been significant, the anticipated savings and benefits over the next five years far outweigh the costs incurred during the development phase.

By streamlining processes, reducing manual labor, and improving productivity, the automation project enables the efficient allocation of resources and maximizes return on investment. Additionally, the project contributes to enhanced user experience, engagement, and satisfaction, further bolstering its economic value.

In conclusion, the automation project represents a sound economic investment, characterized by a favorable cost-benefit ratio and the potential for long-term value creation. While the initial investment may have been substantial, the anticipated time and resource savings, coupled with the tangible benefits derived from enhanced efficiency and productivity, validate the project's economic viability.

As the project evolves and matures, continued optimization and refinement will further enhance its economic impact, underscoring the transformative power of automation in driving sustainable growth and prosperity.

[Link to File 1]()
