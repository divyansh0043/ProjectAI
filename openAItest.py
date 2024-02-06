from openai import OpenAI
from config import apikey
client = OpenAI(api_key=apikey)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write a tagline for ice cream shopwrite a tagline for ice cream shop\n\n\"Scoop up happiness in every cone!\"",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)