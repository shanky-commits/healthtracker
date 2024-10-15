import requests
from datetime import datetime

GENDER = "MALE"  # Correctly defined as a string
WEIGHT_KG = 70
HEIGHT_CM = 170
AGE = 20

APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_APP_KEY"  # Check this key

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/01302e6b6fba081fdba60e88dffe11d2/workouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# if response.status_code == 200:
#     result = response.json()
#     print(result)
# else:
#     print(f"Error: {response.status_code} - {response.text}")

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
#
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
           "date": today_date,
            "time": now_time,
             "exercise": exercise["name"].title(),
             "duration": exercise["duration_min"],
             "calories": exercise["nf_calories"]
         }
      }
#
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"

    authorization_header = {
        'Authorization': "Basic YOURHEADER"
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD),
                             headers=authorization_header)
#
    print(sheet_response.text)
