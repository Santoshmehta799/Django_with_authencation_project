import requests
import hashlib
import time

def generate_otp(mobile_number):
    print('3')
    url = "https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP"
    payload = {
        "mobile": mobile_number
    }
    response = requests.post(url, json=payload)
    return response.json().get("txnId")

def validate_otp(txn_id, otp):
    url = "https://cdn-api.co-vin.in/api/v2/auth/validateMobileOtp"
    hashed_otp = hashlib.sha256(otp.encode()).hexdigest()
    payload = {
        "otp": hashed_otp,
        "txnId": txn_id
    }
    response = requests.post(url, json=payload)
    return response.json().get("token")

def download_certificate(bearer_token, beneficiary_reference_id):
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    url = f"https://cdn-api.co-vin.in/api/v2/registration/certificate/download?beneficiary_reference_id={beneficiary_reference_id}"
    response = requests.get(url, headers=headers)
    return response

def main():
    print('2')
    mobile_number = input("Enter your mobile number: ")
    txn_id = generate_otp(mobile_number)
    print(f"OTP sent. Transaction ID: {txn_id}")
    
    otp = input("Enter the OTP you received: ")
    bearer_token = validate_otp(txn_id, otp)
    print(f"Bearer token: {bearer_token}")
    
    beneficiary_reference_id = int(input("Enter your beneficiary reference ID: "))
    print(beneficiary_reference_id,'bee')
    
    response = download_certificate(bearer_token, beneficiary_reference_id)
    
    if response.status_code == 200:
        with open("certificate.pdf", "wb") as file:
            file.write(response.content)
        print("Certificate downloaded successfully.")
    else:
        print(f"Failed to download certificate: {response.status_code} {response.text}")

if __name__ == "__main__":
    print('1')
    main()