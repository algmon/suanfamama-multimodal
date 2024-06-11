# design text argumentation module via the gpt4o model
# TODO: For current, USE wechat webui instead
"""
This module is developed by Suanfamama.

Authors:
- Wei Jiang (wei@suanfamama.com)
- Mama Xiao (mama.xiao@suanfamama.com)
"""

import os
import openai

# Set up the OpenAI API key (replace with your actual key)
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

def get_gpt4_response(prompt):
  """Sends a request to the OpenAI GPT-4 API and returns the response."""
  api_key = os.environ.get("OPENAI_API_KEY")
  if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

  response = openai.ChatCompletion.create(
    model="gpt-4-0613",  # Use the GPT-4 model
    messages=[
      {"role": "user", "content": prompt}
    ],
    temperature=0.7,  # Adjust for creativity
    max_tokens=256,  # Adjust for desired response length
  )
  return response.choices[0].message.content

def evaluate_design_request(text):
  """Evaluates the user's design request for clarity and completeness.

  Args:
    text: The user's raw design request.

  Returns:
    A tuple (is_ok, message), where is_ok is True if the request is 
    acceptable, False otherwise. The message provides feedback or 
    clarification requests. 
  """

  augment_design_request(text)

  # TODO: Implement more robust evaluation logic. 
  # This could involve checking for keywords, 
  # assessing sentence structure, etc.

  if len(text.split()) < 5:
    return False, "Please provide more details about your design."
  
  return True, "Request received!"

def augment_design_request(text):
  """Uses the GPT-4 model to augment the design request with 
  style, color, and material suggestions.

  Args:
    text: The user's initial design request.

  Returns:
    An augmented design request with additional details.
  """
  prompt = (
    f"The user provided this design request: '{text}'. "
    "As a fashion expert, please suggest additional details "
    "regarding style, color palette, and suitable materials. "
    "Provide your suggestions in a clear and concise list format."
  )
  response = get_gpt4_response(prompt)
  return f"{text}\n\nSuggestions:\n{response}"


def main():
  """Main function to interact with the user and process design requests."""
  print("Welcome to the AI Fashion Design Assistant!")
  design_request = input("Describe your desired clothing or decoration:\n")

  is_ok, message = evaluate_design_request(design_request)
  print(message)

  if not is_ok:
    augmented_request = augment_design_request(design_request)
    print("\nHere are some suggestions to improve your request:")
    print(augmented_request)

if __name__ == "__main__":
  main() 
