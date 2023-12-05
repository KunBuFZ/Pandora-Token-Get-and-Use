from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r') as file:
        return file.read()

@app.route('/get_tokens', methods=['POST'])
def get_tokens():
    base_url = request.form['base_url']
    username = request.form['username']
    password = request.form['password']
    
    # 登录以获取 access token
    login_url = f"{base_url}/api/auth/login"
    data = {"username": username, "password": password}
    response = requests.post(login_url, data=data)
    if response.status_code == 200:
        access_token = response.json().get('access_token')

        # 使用 access token 获取 share token
        register_url = f"{base_url}/api/token/register"
        headers = {"Authorization": f"Bearer {access_token}"}
        data = {"unique_name": "unique_name_for_share_token", "access_token": access_token}
        response = requests.post(register_url, headers=headers, data=data)
        if response.status_code == 200:
            share_token = response.json().get('token_key')
            return f"Access Token: {access_token}<br>Share Token: {share_token}"
        else:
            return "Failed to get share token."
    else:
        return "Failed to log in and get access token."

if __name__ == '__main__':
    app.run(host='0.0.0.0')
