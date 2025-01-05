from dotenv import load_dotenv
import gradio as gr

from chatbot_engine import chat


def respond(message, history):
    bot_message = chat(message, history)
    return bot_message

demo = gr.ChatInterface(
    fn=respond,
    title="Chatbot",
    type="messages",
)

if __name__ == "__main__":
    load_dotenv()
    demo.launch(server_name="0.0.0.0")
