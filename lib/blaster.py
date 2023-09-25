import random
import string
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import concurrent.futures

# Define a list of words related to education, courses, and buying
education_words = [
    "education", "learning", "courses", "buying", "online", "study",
    "e-learning", "school", "university", "enroll", "knowledge", "class",
    "training", "certification", "program", "student", "instructor", "tuition"
]

# Define a list of menu options for "menu-860"
menu_options = [
    "Cloud Computing",
    "Android App Development",
    "UI/UX",
    "Data Structures and Algorithms",
    "Artificial Intelligence",
    "Data Science With Machine Learning",
    "Cyber Security",
    "Full Stack Web Development",
    "Automobile",
    "Hybrid Electric Vehicle",
    "Construction Planning",
    "Building Information",
    "AutoCAD- Civil"
]

# Define the URL for the POST request
url = "URL_OF_POST_REQUEST"

# Function to generate random string of given length
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Function to generate a random phone number starting with 6, 7, 8, or 9
def generate_random_phone_number():
    first_digit = random.choice(['6', '7', '8', '9'])
    rest_of_number = ''.join(random.choice(string.digits) for _ in range(9))
    print(first_digit + rest_of_number)
    return first_digit + rest_of_number

# Function to generate a random 100-word message
def generate_random_message():
    words = [random.choice(education_words) for _ in range(100)]
    return ' '.join(words)

# Function to send a single POST request
def send_post_request(url):
    payload = {
        "your-name": generate_random_string(5),
        "your-email": f"{generate_random_string(8)}@gmail.com",
        "your-phone": generate_random_phone_number(),
        "menu-860": random.choice(menu_options),
        "your-message": generate_random_message()
    }
    
    multipart_data = MultipartEncoder(fields=payload)
    headers = {'Content-Type': multipart_data.content_type}

    response = requests.post(url, data=multipart_data, headers=headers)

    if response.status_code == 200:
        print("success")
        return "Request was successful."
        
    else:
        return f"Request failed with status code: {response.status_code}"

# Number of requests to send
num_requests = 100

# Use multithreading for faster requests
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(send_post_request, [url] * num_requests))

# Count successful requests
successful_requests = sum(1 for result in results if "successful" in result)

print(f"Total Requests: {num_requests}")
print(f"Successful Requests: {successful_requests}")
