import vertexai
from vertexai.generative_models import GenerativeModel, Part

import vertexai
from vertexai.generative_models import GenerativeModel, Part

# Use your project ID and the correct location (one 'l', number 1)
vertexai.init(project="project-450e81d6-945c-48ed-b6e", location="us-central1")

# Use the Gemini 2.0 Flash model you just tested
model = GenerativeModel("gemini-2.0-flash-001")

with open("document.pdf", "rb") as f:
    pdf_data = f.read()

pdf_file = Part.from_data(data=pdf_data, mime_type="application/pdf")
prompt = "Please summarize this document in 3 bullet points."

print("--- Running script... ---")
response = model.generate_content([pdf_file, prompt])
print("\nAI Summary:")
print(response.text)
