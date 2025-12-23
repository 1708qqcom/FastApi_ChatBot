from langchain.chat_models import init_chat_model 


choose=input("Choose a model:deepseek or chatgpt\n")
if choose=="deepseek":
    llm_model=init_chat_model(
        model="deepseek-chat",
    api_key=""
    )
elif choose=="chatgpt":
    fllm_model=init_chat_model(
        model="gpt-5-nano",
        api_key=""
)
else:
    print("Invalid model,please choose deepseek or chatgpt or edit the model in Chatbot.py")

# llm_model=init_chat_model(
#         model="gpt-5-nano",
#         api_key=""
# )

response=llm_model.invoke("你好")
print(response.content)
