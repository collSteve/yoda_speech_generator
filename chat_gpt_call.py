# from openai import OpenAI
import json
import os
from dotenv import load_dotenv
from pydantic import BaseModel

import asyncio
from openai import AsyncOpenAI

class CalendarEvent(BaseModel):
    normal_english: str
    mapping: list[int]


# Load the .env file
load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

client = AsyncOpenAI(
  api_key=api_key, 
)


async def generate_normal_english_and_mapping(yoda_sentence):

    prompt = (
        "Convert the following Yoda sentence into its normal English equivalent. "
        "Reorder the words without adding or removing any words. Then, provide a mapping "
        "that indicates which word in the normal English sentence corresponds to which word "
        "in the original Yoda sentence. Provide the result in JSON format with two keys: "
        "\"normal_english\" and \"mapping\". The mapping should be a dictionary where the keys "
        "are word indices (starting from 0) of the normal English sentence and the values are "
        "lists of corresponding word indices from the Yoda sentence. For example, for the Yoda sentence:\n"
        "\"Your father he is.\"\n"
        "A valid output might be:\n"
        "{\n"
        "  \"normal_english\": \"He is your father.\",\n"
        "  \"mapping\": [2, 3, 0, 1]}\n // this means that the index 0 of the normal English sentence (He) corresponds to the index 2 of the Yoda sentence (he), and so on.\n" 
        "}\n"
        f"Now process the following sentence:\n\"{yoda_sentence}\"\n"
    )

    response = await client.beta.chat.completions.parse(
        model="o3-mini-2025-01-31",  
        # model="gpt-4o-mini-2024-07-18",  
        messages=[{"role": "user", "content": prompt}],
        # temperature=0,     # Lower temperature for deterministic output
        response_format=CalendarEvent,
    )
    
    return response.choices[0].message.parsed

# Example usage:
if __name__ == "__main__":
    yoda_sentence = "Your father he is."
    
    result = generate_normal_english_and_mapping(yoda_sentence)
    print(result)