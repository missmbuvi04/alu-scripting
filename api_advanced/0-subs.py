#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import json
import requests

def number_of_subscribers(subreddit):
	# Define the URL for the subreddit's about endpoint
       	url = "https://api.reddit.com/r/{}/about".format(subreddit)
        
        # Set a custom User-Agent to avoid Too Many Requests error
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        try:
            # Make a GET request to the Reddit API
            response = requests.get(url,headers=headers,allow_redirects=False)
            
            # Check if the status code indicates a successful request
            if response.status_code == 200:
                try:
                    # Parse the JSON response
                    data = response.json()
                    # Check if the key 'data' exists in the JSON response
                    if 'data' in data and 'subscribers' in data['data']:
                        # Return the number of subscribers
                        return data['data']['subscribers']
                    else:
                        # If the 'data' or 'subscribers' key is not present, return 0
                        return 0
                except ValueError:
                    # If there is a JSON decoding error, return 0
                    return 0
            else:
                # If the subreddit does not exist or any other error, return 0
                return 0
        except requests.RequestException:
            # In case of a network error or any other issue, return 0
            return 0
