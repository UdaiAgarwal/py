import getpass
import dotenv
import os

dotenv.load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint

# model = "meta-llama/Llama-3.1-8B-Instruct"
model = "mistralai/Mistral-7B-Instruct-v0.3"
from huggingface_hub import InferenceClient
def invoke_llm(prompt):
    messages = [{"role": "user", "content": prompt}]
    client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", api_key=os.environ["LLAMA_KEY"])
    output = client.chat.completions.create(messages)
    return output.choices[0].message.content
