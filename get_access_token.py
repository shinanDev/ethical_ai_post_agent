import requests

client_id = "782388lsq8ewaf"
client_secret = "WPL_AP1.pfA8DEEG31hKHJG7.+l1+ng=="
redirect_uri = "http://localhost:3000/callback"
authorization_code = "AQRncWCnmNlZwqR8z7OPIFOhKiV29mhFWe53XgtPIpDGAkaQbY8ptex_JZzt4-gGRwlZa3avMDmd8FagtziZJeJNLp42-vM_Yox98B2rDr8VEqu4wZm0xkEgDMzIfewq1iYvpCBzqLXUU-arMPSR4adDCyY2JExm1pEIU8E6xNtsHkrByrNFQHZsHk-_bNOOEXeDn9p4O4EhZ8yWM6I"

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