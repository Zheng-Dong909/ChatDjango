import openai

SK = "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"

# Load your API key from an environment variable or secret management service
openai.api_key = SK


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt
    )
    return response['choices'][0]['message']['content'].strip()


if __name__ == '__main__':
    generate_response()
