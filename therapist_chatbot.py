import openai
import os
import streamlit as st

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_chatbot_response(prompt):
    try:
        # Send the user's message to the GPT model
        # response = openai.Completion.create(
        #     engine="gpt-3.5-turbo",  # You can use "gpt-3.5-turbo" or "gpt-4" based on your subscription
        #     prompt=prompt,
        #     max_tokens=150,  # Limit the length of the response
        #     temperature=0.7,  # Controls the randomness of the output
        #     n=1,  # Number of responses to generate
        #     stop=None  # Define stop sequences if necessary
        # )

        response = openai.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Pretend you are a therapist, and now answer this query: " + str(prompt),
                }
            ],
            model="gpt-3.5-turbo"
            # model="gpt-4o-mini"
            # model="text-embedding-3-small"
            # model="gpt-4"
        )
        
        # Extract the chatbot's response
        
        # return response.choices[0].text.strip()
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {e}"

def chat():
    st.write("Hello! I am your therapy chatbot! Please, speak your mind.")
    
    prompt = st.chat_input("You: ", key="chat_input")
    if prompt:
        st.write(get_chatbot_response(prompt))

    # i = 1
    # while True:
    #     i += 1
    #     # user_input = input("You: ")
    #     user_input = st.text_input("You: ", key="chat_input" + str(i))
    #     # user_input = st.chat_input("You: ", key="chat_input" + str(i))    
    #     # if user_input.lower() == "exit":
    #     if user_input:
    #         if user_input == "exit":
    #             print("Goodbye! Have a great day!")
    #             break
    #         st.write(f"User has sent the following prompt: {user_input}")
    #         # Generate the chatbot response
    #         # bot_response = get_chatbot_response(user_input)
        
    #         # print(f"Bot: {bot_response}")

if __name__ == "__main__":
    chat()
