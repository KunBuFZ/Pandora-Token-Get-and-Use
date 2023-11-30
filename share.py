import requests

# 设置PandoraNext代理API的基本URL和你的API前缀
base_url = "http://your-pandoranext-deployment.com/<your_api_prefix>"

# 账号密码
username = "xxxx"
password = "xxxx"

# 登录以获取 access token
def get_access_token(base_url, username, password):
    login_url = f"{base_url}/api/auth/login"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(login_url, data=data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception("Failed to log in and get access token.")

# 使用 access token 获取 share token
def get_share_token(base_url, access_token):
    register_url = f"{base_url}/api/token/register"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    data = {
        "unique_name": "123321",
        "access_token": access_token,
        "expires_in": 0

        # 更多参数根据您的需求进行配置
    }
    response = requests.post(register_url, data=data)
    if response.status_code == 200:
        return response.json().get('token_key')
    else:
        raise Exception("Failed to get share token.")

# 执行脚本
try:
    access_token = get_access_token(base_url, username, password)
    print("Access Token:", access_token)

    share_token = get_share_token(base_url, access_token)
    print("Share Token:", share_token)
except Exception as e:
    print(str(e))
