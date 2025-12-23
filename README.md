# Overview
用Fastapi搭建的一个简单的AI应用Demo，简单模拟后端暴露Api，前端调用执行的过程。
# Quick Start
## 填写自己的APIKey
分别在Chatbot.py和Fastapi_chatbot.py填写对应的api_key
<img width="1130" height="541" alt="image" src="https://github.com/user-attachments/assets/a546fb6f-fdce-4e3e-9ae1-636fb762723a" />
<img width="1169" height="504" alt="image" src="https://github.com/user-attachments/assets/b87c4355-f7cf-46c2-9708-2180dcdcdfb3" />

## 启动FastApi
```
uvicorn Fastapi_chatbot:app --port 8080 --reload  
```
访问 docs 路由，测试接口/chat的功能
```
http://127.0.0.1:8080/docs
```
 <img width="1107" height="368" alt="image" src="https://github.com/user-attachments/assets/ec1cc744-e184-4ec7-bcce-ce0807814313" />
测试效果如下
<img width="1094" height="394" alt="image" src="https://github.com/user-attachments/assets/30b2bfe3-020b-4e7e-aeba-2dabd50f6f31" />
