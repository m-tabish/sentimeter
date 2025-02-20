from google import genai
def sentiment_analysis(prompt, apiKey):  
    
    client = genai.Client(api_key="") 
    
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
    )
    print(response.text)
    
    
api_key = ""
prompt = """Analyze the following tweet and return a JSON object with 3-5 sentiment scores (out of 10) and a comment on what the model thinks the tweet implies (e.g., misleading, hatred, self-expression, etc.).

Tweet: "I can't believe the service at this restaurant! Absolutely terrible experience."

Return format:
{
    "sentiment_scores": {
        "anger": 8,
        "disgust": 7,
        "sadness": 5
    },
    "comment": "The tweet implies dissatisfaction and anger towards the service."
}
"""

print(sentiment_analysis(api_key, "1 mahine se class nahi gaya (involved in techfest) , ab kal se internal hai.1st paper COA ka"))