import requests

client_id = "782388lsq8ewaf"
client_secret = "WPL_AP1.pfA8DEEG31hKHJG7.+l1+ng=="
redirect_uri = "http://localhost:3000/callback"
authorization_code = "AQT1-QFTGcE-dyL6zHTfJZ5zcwgu4l6L0bR1gkY-uAZKsJrOPXwZcvsteovxpphSDOmmb6K1BorvXGinMLuRiMuzzU_ky-AbUUOpa-jMrYRFzD-T6K3Wx0KM7LEzq3KZ9g5v8zHOfFDVYYkZV89sL2XmD4VfKvfUucOGqrQJ-T83oa0tX9zYgCwG27RvA8lHarD_biPjFSfKWGdXjKc"

token_url = "https://www.linkedin.com/oauth/v2/accessToken"

response = requests.post(token_url, data={
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri,
    "client_id": client_id,
    "client_secret": client_secret
})

print(response.status_code)
print(response.json())