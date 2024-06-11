# Import necessary libraries
import openai

# Set up OpenAI API client
openai.api_key = "YOUR_API_KEY"

# Define a prompt
prompt = "Generate a summary of AI applications in psychology"

# Use the OpenAI API to generate a response
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5
)

# Print the response
print(response.choices[0].text)