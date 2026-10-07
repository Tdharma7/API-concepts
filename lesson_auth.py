import os
from dotenv import load_dotenv
load_dotenv()
token=os.getenv("fake_weather_api")

if not token:
    raise ValueError("No API token provided. Please set the 'fake_weather_api' environment variable.")
else:
    headers= {
        "Authorization": f"Bearer {token}"

    }

print("API token found and headers set successfully.")
    