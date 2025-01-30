# This script is a simple example of how to use the Gemini API to generate content.

import os

import google.generativeai as genai

my_api_key=os.getenv("GOOGLE_API_KEY")
if my_api_key is None:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

genai.configure(api_key=my_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Compare DeepSeek-R1 and OpenAI-o1.")
print(response.text)


