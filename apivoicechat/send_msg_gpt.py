# import openai
# import pyttsx3
# import speech_recognition as sr

# # Set up your OpenAI API key
# openai.api_key = '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'

# # Initialize the Text-to-Speech engine
# engine = pyttsx3.init()

# # Initialize the speech recognizer
# recognizer = sr.Recognizer()

# print("Voice Chatbot: Hello! How can I assist you today?")

# while True:
#     # Listen for user's voice input
#     with sr.Microphone() as source:
#         print("You: Listening...")
#         audio = recognizer.listen(source)

#     try:
#         # Recognize the user's speech
#         user_input = recognizer.recognize_google(audio)
#         print(f"You: {user_input}")

#         # Send the user's input to the chatbot
#         response = openai.Completion.create(
#             engine="davinci", prompt=f"You: {user_input}", max_tokens=50
#         )

#         # Get the chatbot's response
#         chatbot_response = response.choices[0].text
#         print(f"Voice Chatbot: {chatbot_response}")

#         # Convert the chatbot's response to speech and play it
#         engine.say(chatbot_response)
#         engine.runAndWait()

#     except sr.UnknownValueError:
#         print("Voice Chatbot: Sorry, I didn't catch that. Can you please repeat?")
#     except sr.RequestError as e:
#         print(f"Voice Chatbot: Error: {e}")
#     except Exception as e:
#         print(f"Voice Chatbot: An error occurred: {e}")


# import openai
# from gtts import gTTS
# import pyttsx3
# import speech_recognition as sr
#####################################################################
# # Set up your OpenAI API key
# openai.api_key = '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'

# # Initialize the Text-to-Speech engine
# # engine = pyttsx3.init()

# # Initialize the speech recognizer
# # recognizer = sr.Recognizer()

# # print("Voice Chatbot: Hello! How can I assist you today?")

# # while True:
# #     # Listen for user's voice input
# #     with sr.Microphone() as source:
# #         print("You: Listening...")
# #         audio = recognizer.listen(source)

# #     try:
# #         # Recognize the user's speech
# #         user_input = recognizer.recognize_google(audio)
# #         print(f"You: {user_input}")

# #         # Send the user's input to the chatbot
# #         response = openai.Completion.create(
# #             engine="davinci", prompt=f"You: {user_input}", max_tokens=50
# #         )

# #         # Get the chatbot's response
# #         chatbot_response = response.choices[0].text
# #         print(f"Voice Chatbot: {chatbot_response}")

# #         # Convert the chatbot's response to speech and play it
# #         tts = gTTS(text=chatbot_response, lang='en')
# #         tts.save("chatbot_response.mp3")
# #         engine.say(chatbot_response)
# #         engine.runAndWait()

# #     except sr.UnknownValueError:
# #         print("Voice Chatbot: Sorry, I didn't catch that. Can you please repeat?")
# #     except sr.RequestError as e:
# #         print(f"Voice Chatbot: Error: {e}")
# #     except Exception as e:
# #         print(f"Voice Chatbot: An error occurred: {e}")

# def speaktext(command):
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()

# r = sr.Recognizer()

# def record_text():
#     while(1):
#         try:
#             with sr.Microphone() as source2:
#                 r.adjust_for_ambient_noise(source2, duration=0.2)
#                 print("i am listening")

#                 audio2 = r.listen(source2)

#                 mytest = r.recognize_google(audio2)

#                 return mytest
#         except sr.RequestError as e:
#             print("could not request results: {0}".format(e))

#         except sr.UnknownValueError:
#             print("unknown error occured")
# def send_to_chatgpt(message, model="gpt-3.5-turbo"):

#     response = openai.ChatCompletion.create(
#         model = model,
#         message = message,
#         max_token = 100,
#         n = 1,
#         stop = None,
#         temperature=0.5,
#     )

#     message = response.choice[0].message.content
#     message.append(response.choices[0].message)
#     return response

# message = []
# while(1):
#     text = record_text()
#     message.append({"role":"user", "content":"please act like jarvice from iron man."})
#     response = send_to_chatgpt(message)
#     speaktext(response)

#     print(response)
################################################
# import re

# text = "Hello, my name is John Smith and I work at XYZ Corp."
# name_pattern = r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)?\b'  # Matches names like "John Smith" or "Jane Doe"

# names = re.findall(name_pattern, text)
# print(names)  # Output: ['John Smith']

###############################################################################
# import openai

# # Set your OpenAI API key
# api_key = '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'
# openai.api_key = api_key

# # Define a conversation with multiple tasks
# conversation = [
#     {"role": "user", "content": "Translate the following English text to French: 'Hello, how are you?'"},
# ]

# # Send the conversation to the GPT-3 model
# response = openai.Completion.create(
#     engine="gpt-3.5-turbo-0613",
#     messages=conversation,
# )

# # Extract and print the model's responses
# for message in response['choices']:
#     print(f"{message['role']}: {message['content']}")
