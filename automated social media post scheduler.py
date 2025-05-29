
from instabot import Bot

# Authenticate
bot = Bot()
bot.login(username="ankita123, 123456")

# Post an image with a caption
bot.upload_photo("image.jpg", caption="🚀 Automated Instagram post!")

print("✅ Instagram post uploaded!")
import requests

# Facebook API
facebook_page_id = "ankita shrivastav"#facebook username
facebook_access_token = "ankita kumari"#facebook password
fb_post_url = f"https://graph.facebook.com/{facebook_page_id}/feed"
fb_payload = {"message": "Hello, Facebook!", "access_token": facebook_access_token}
fb_response = requests.post(fb_post_url, data=fb_payload)
print("Facebook Response:", fb_response.json())

# LinkedIn API
linkedin_access_token = "123456789"#password for linkedin app
linkedin_post_url = "https://api.linkedin.com/v2/shares"
linkedin_headers = {"Authorization": f"Bearer {linkedin_access_token}", "Content-Type": "application/json"}
linkedin_payload = {
    "content": {"contentEntities": [{"entityLocation": "https://example.com"}]},
    "text": {"text": "Hello, LinkedIn!"},
    "distribution": {"linkedInDistributionTarget": {}}
}
linkedin_response = requests.post(linkedin_post_url, headers=linkedin_headers, json=linkedin_payload)
print("LinkedIn Response:", linkedin_response.json())