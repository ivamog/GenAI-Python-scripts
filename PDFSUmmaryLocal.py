# PDFSUmmaryLocal.py
# This script reads a local PDF file, encodes it, and sends it to the Generative AI model to generate a summary of the document.

import os
import time
from google.api_core.exceptions import ServiceUnavailable

def PDFOverview():
   
    print("Start")

    import base64
    import google.generativeai as genai
    from google.api_core.exceptions import DeadlineExceeded
    
    retries = 3  # Number of retries
    delay = 1  # Initial delay in seconds

    # Retreive API Key from the environment variable
    my_api_key=os.getenv("GOOGLE_API_KEY")
    if my_api_key is None:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")

    genai.configure(api_key=my_api_key)
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    doc_path = "/Users/ivamo/DropBox/AIScripts/Python/From-Similia-to-Synergy.pdf" # Replace with the actual path to your local PDF
   
    print(doc_path)

    if doc_path is None:
        raise ValueError("doc_path variable is not set")
    
    # Read and encode the local file
    with open(doc_path, "rb") as doc_file:
        doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")

    prompt = "Summarize this document by writing a paragraph on each chapter of the document."

    # response = model.generate_content([{'mime_type': 'application/pdf', 'data': doc_data}, prompt])  
    # print(response.text)
    
    for i in range(retries):
        try:
            response = model.generate_content([{'mime_type': 'application/pdf', 'data': doc_data}, prompt])  # API call here
            print(response.text)  # Success!
            break  # Exit the loop
        except ServiceUnavailable as e:
            print(f"Model overloaded. Retrying in {delay} seconds... (Attempt {i+1}/{retries})")
            time.sleep(delay)
            delay *= 2  # Exponential backoff
    else:  # If the loop completes without success
        raise Exception("Model still unavailable after multiple retries.")


print("End")

#Call function to execute
if __name__ == "__main__":
   print("This code runs when the script is executed directly.")
   PDFOverview()

 
#Running from the Windows command line (cmd):
# py -m PDFSUmmaryLocal  






