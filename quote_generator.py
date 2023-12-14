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
