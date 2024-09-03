import requests

# Replace with your actual bearer token (obtained after OTP confirmation)
bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIzNmFiYmJjYi1mMWZiLTRiYWYtODZlZS0wZGVmZjU0ZjA3MzAiLCJ1c2VyX2lkIjoiMzZhYmJiY2ItZjFmYi00YmFmLTg2ZWUtMGRlZmY1NGYwNzMwIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo4NDAxMjk2NDg2LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjYxOTcxNzcwMzQ0OTAwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwic291cmNlIjoiY293aW4iLCJ1YSI6Ik1vemlsbGEvNS4wIiwiZGF0ZV9tb2RpZmllZCI6IjIwMjQtMDgtMjlUMTI6Mjc6MjYuNTE4WiIsImlhdCI6MTcyNDkzNDQ0NiwiZXhwIjoxNzI0OTM1MzQ2fQ.j7nsPs9v-PsO3BPmGobaff1hloN7D2BvG5SLQRq15sk"

# The beneficiary reference ID (you need to provide this ID)
beneficiary_reference_id = "82507374275130"  # Replace with the actual ID

# API endpoint for downloading the certificate
url = f"https://cdn-api.co-vin.in/api/v2/registration/certificate/public/download?beneficiary_reference_id={beneficiary_reference_id}"

# Headers with the authorization token
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "User-Agent": "Mozilla/5.0"
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Save the certificate to a file (e.g., certificate.pdf)
    with open("certificate.pdf", "wb") as file:
        file.write(response.content)
    print("Certificate downloaded successfully.")
else:
    print("Failed to download certificate:", response.status_code, response.text)
