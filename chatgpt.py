import openai

api_key = 'YOUR_API_KEY'

openai.api_key = api_key

def continue_conversation(prompt, history):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=50
    )
    return response.choices[0].text.strip()

print("Assistant: Hi! I'm here to chat with you. What's on your mind?")

while True:
    user_input = input("You: ")
    conversation_history = f"Assistant: {continue_conversation(user_input, conversation_history)}\nYou: {user_input}\n"

