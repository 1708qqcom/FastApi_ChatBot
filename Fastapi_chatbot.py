import logging
from sys import exc_info
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from langchain.chat_models import init_chat_model
from pydantic import BaseModel

app=FastAPI()

# 配置日志
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

# 错误映射
error_mapping={
    400:"Bad Request",
    404:"Not Found",
    500:"Internal Server Error"
}

# 全局错误处理中间件-对所有接口生效
@app.middleware("http") #对每个进入的 HTTP 请求都会执行
async def error_handler(request,call_next):
    try:
        response=await call_next(request)
        return response
    except Exception as e:
        logger.error(f"Error: {request.url}:{e}",exc_info=True)
        error_type=type(e) # 输出错误类型
        print(error_type)
        status_code=error_mapping.get(error_type,500)
        return JSONResponse( # 返回 JSON 响应
            content={f"detail":f"{e}"},
            
            status_code=status_code
        )

# 定义数据对象
class ChatRequest(BaseModel): # 继承BaseModel，规范请求数据格式
    message:str
    model_name:str="deepseek-chat"

# 获取模型名称
def get_model_name(model_name:str):
    if model_name=="deepseek-chat":
        return init_chat_model(
        model="deepseek-chat",
    api_key="xxx"  # input your deepseek key
    )
    elif model_name=="chatgpt":
        return init_chat_model(
        model="gpt-5-nano",
        api_key="" # input your gpt-key 
)
    else:
        raise ValueError("Invalid model name") # 自定义异常，提示用户输入正确的模型名称
    

@app.post("/chat")
async def chat(request:ChatRequest): # 创建实例（FastAPI 自动完成）
    llm_model=get_model_name(request.model_name) # 获取实例化对象request的model_name属性
    response=llm_model.invoke(request.message)
    return response.content
