import vertexai
from vertexai.generative_models import GenerativeModel
import csv

# 1. Initialize
vertexai.init(project="project-450e81d6-945c-48ed-b6e", location="global")
model = GenerativeModel("gemini-2.5-flash")

# 2. Your List of Reviews
reviews = [
    "The app crashed during checkout. Highly frustrating.",
    "Fast delivery to Tracy, but the box was damaged.",
    "The customer service agent was very rude and didn't help.",
    "I love the product! Best purchase of the year."
]

# 3. Create the CSV file and write the header
with open('ai_analysis_report.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Review Text", "AI Sentiment Analysis"])

    print("--- STARTING BATCH PROCESSING TO CSV ---")

    for review in reviews:
        prompt = f"Analyze this review: '{review}'. Give me a Sentiment and a Frustration Score (1-10)."
        response = model.generate_content(prompt)
        
        # Write the result to the spreadsheet
        writer.writerow([review, response.text.strip()])
        print(f"Processed: {review[:30]}...")

print("\n--- REPORT GENERATED: ai_analysis_report.csv ---")