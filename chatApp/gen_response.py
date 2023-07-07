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
