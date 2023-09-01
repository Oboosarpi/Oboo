import gradio
import openai

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a Counseling expert that specializes in giving good counsels to students facing challenges"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "VConsellor KNUST")

demo.launch()

