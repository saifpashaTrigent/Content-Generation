import openai
import streamlit as st
from content_generation.pdfGenerator import generate_pdf_report
from dotenv import load_dotenv,find_dotenv
import os
import openai

_=load_dotenv(find_dotenv())
os.getenv("OPENAI_API_KEY")

openai.api_key="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"


class ArticleWriter:
    def __init__(self):
        self.template = """
        You are an expert article writer who will write beautiful and meaningful
        articles for the topic given by the user.
        Remember that your sole purpose is to write an article in any Language asked.

        The user can select the language from the gven et of languages and you will
        write the blog in that language.

        If asked for your name, always say "Ai Article and blog writer."

        If the user greets you, just greet them normally.

        If the user tells you something and asks a question on the same, 
        you will answer them correctly.

        Remeber that article should be a minimum of 600 words in any language that is given by the user
        .
        """

        self.conversation_history = []
        self.conversation_history.append({"role": "system", "content": self.template})

    def add_message_to_conversation(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, question,language):
        self.add_message_to_conversation("user", question)

        language_prompt = f"Language: {language}"
        self.add_message_to_conversation("system", language_prompt)

        self.add_message_to_conversation("user", question)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=self.conversation_history,
            max_tokens=1024,
            temperature=0,
        )
        ai_response = response['choices'][0]['message']['content']
        self.add_message_to_conversation("assistant", ai_response)
        return ai_response


articlewriter = ArticleWriter()



