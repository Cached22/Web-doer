# review_bot/config/settings.py

# Global settings for the review bot application

# URLs where reviews will be posted
WEBSITE_URLS = [
    'http://example-website1.com/review',
    'http://example-website2.com/review',
    # Add more URLs as needed
]

# Configuration for proxy or VPN services
PROXY_DETAILS = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080',
    # Add more proxy configurations as needed
}

# Boolean to indicate if the browser should run in headless mode
HEADLESS_BROWSER = True

# List of email accounts to be used by the bot
ACCOUNT_LIST = [
    {'email': 'user1@example.com', 'password': 'password123'},
    {'email': 'user2@example.com', 'password': 'password456'},
    # Add more accounts as needed
]

# API key for CAPTCHA solving service
CAPTCHA_API_KEY = 'YOUR_CAPTCHA_API_KEY_HERE'

# Other global parameters can be added here as needed
# For example, user agent strings, browser preferences, etc.