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
messages = [{"role": "user", "content": "What is the capital of France?"}]
client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", api_key=os.environ["LLAMA_KEY"])
output = client.chat.completions.create(messages)
print(output)
print(output.choices[0].message.content)
# llm = HuggingFaceEndpoint(
#     repo_id=model,
#     max_length=128,
#     temperature=0.5,
#     huggingfacehub_api_token=os.environ["LLAMA_KEY"],
# )
# # llm = ChatHuggingFace(llm = llm)
# # messages = [{"role": "User", "message": "Hey"}]
# # result = openai.chat.completions.create(
# #     messages=messages, model=model, temperature=0, api_key = os.environ["LLAMA_KEY"]
# # )
# # result.choices[0].message.model_dump()

# output = llm.invoke("Hey, who's the president of india?")
# print("=========== output ================")
# print(output)
# model = init_chat_model(model, model_provider="huggingface", key = os.environ["LLAMA_KEY"])