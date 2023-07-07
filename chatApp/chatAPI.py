import os
import openai
SK = "sk-HIKqpLXuC7amEm4cGjJMT3BlbkFJcwgTvvxg60vhHHzB"

# Load your API key from an environment variable or secret management service
openai.api_key = SK

prompt = []


def generate_response(prompt):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=prompt
    )
    return response['choices'][0]['message']['content'].strip()

while True:
    user_input = input("You: ")
    user_input_dict = {"role": "user", "content": user_input}
    prompt.append(user_input_dict)
    response_content = generate_response(prompt)
    # if response['choice'][0]['message']['finish_reason'] == 'stop':
    #     print('respones finished')
    # response_content = response['choices'][0]['message']['content'].strip()
    response_dict = {"role": "assistant", "content": response_content}
    prompt.append(response_dict)
    print(response_content)