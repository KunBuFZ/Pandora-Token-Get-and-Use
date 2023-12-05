import requests

# 设置PandoraNext代理API的基本URL和你的API前缀
base_url = "https://xxxx/xxxx"
access_token = "fk-xxxx"

# 创建请求头部
headers = {
    "Authorization": f"Bearer {access_token}"
}

# 设置聊天内容
payload = {
    "model": "gpt-3.5-turbo",  # 根据需要选择模型
    "messages": [{"role": "system", "content": "You are a helpful assistant."}, 
                 {"role": "user", "content": "Can you help me with my homework?"}]
}

# 发送请求到Chat to API接口
response = requests.post(f"{base_url}/v1/chat/completions", json=payload, headers=headers)

# 检查响应
if response.status_code == 200:
    print("Response from API:", response.json())
else:
    print("Error:", response.status_code, response.text)

