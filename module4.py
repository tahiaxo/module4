#problem1
from datetime import datetime

current_datetime = datetime.now()

print("Current Date and Time:", current_datetime)


#problem2 
import json

student = {
    "name": "Rahim",
    "age": 20,
    "department": "CSE"
}

json_string = json.dumps(student)

print(json_string)