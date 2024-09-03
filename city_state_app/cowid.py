import requests

# mobile_number = "YOUR_MOBILE_NUMBER"
# url = "https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP"
# payload = {
#     "mobile": 8401296486
# }
# response = requests.post(url, json=payload)
# txn_id = response.json().get("txnId")
# print("=============>>",txn_id)


# =======================================================

# import hashlib
# txn_id="a33237f6-9049-4792-968e-ca9972a38e27"
# otp = "279362"
# hashed_otp = hashlib.sha256(otp.encode()).hexdigest()

# url = "https://cdn-api.co-vin.in/api/v2/auth/validateMobileOtp"
# payload = {
#     "otp": hashed_otp,
#     "txnId": txn_id
# }
# response = requests.post(url, json=payload)
# bearer_token = response.json().get("token")
# print("==========>>",bearer_token)








# ================================================================

import requests
bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIzNmFiYmJjYi1mMWZiLTRiYWYtODZlZS0wZGVmZjU0ZjA3MzAiLCJ1c2VyX2lkIjoiMzZhYmJiY2ItZjFmYi00YmFmLTg2ZWUtMGRlZmY1NGYwNzMwIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo4NDAxMjk2NDg2LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjYxOTcxNzcwMzQ0OTAwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwic291cmNlIjoiY293aW4iLCJ1YSI6InB5dGhvbi1yZXF1ZXN0cy8yLjMyLjMiLCJkYXRlX21vZGlmaWVkIjoiMjAyNC0wOC0yOVQxMjozNjoxOC4xMTBaIiwiaWF0IjoxNzI0OTM0OTc4LCJleHAiOjE3MjQ5MzU4Nzh9.nEFy2iNuSPRvQHliBgkJK6IvOctf1bZ6GJXpDUQt2rc"
# Use the bearer token obtained above
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "User-Agent": "Mozilla/5.0"
}

beneficiary_reference_id = "82507374275130"
url = f"https://cdn-api.co-vin.in/api/v2/registration/certificate/public/download?beneficiary_reference_id={beneficiary_reference_id}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open("certificate.pdf", "wb") as file:
        file.write(response.content)
    print("Certificate downloaded successfully.")
else:
    print("Failed to download certificate:", response.status_code, response.text)
