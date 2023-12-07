import requests

# 设置PandoraNext代理API的基本URL和你的API前缀
base_url = "https://pandora/prefix"

# 登录以获取 access token
def get_access_token(base_url, username, password):
    login_url = f"{base_url}/api/auth/login"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(login_url, data=data)
    if response.status_code == 200:
        return response.json().get('session_token')
    else:
        raise Exception("Failed to log in and get access token.")

# 读取账号密码
def read_accounts(filename):
    accounts = []
    with open(filename, 'r') as file:
        for line in file:
            if ' ' in line:
                username, password = line.strip().split(' ')
                accounts.append((username, password))
    return accounts

# 将tokens写入文件
def write_tokens(filename, tokens):
    with open(filename, 'w') as file:
        file.write("{\n")
        for idx, (key, token) in enumerate(tokens.items(), 1):
            file.write(f'    "test-{idx}": {{\n')
            file.write(f'        "token": "{token}",\n')
            file.write(f'        "shared": true,\n')
            file.write(f'        "show_user_info": true\n')
            file.write('    }' + (',\n' if idx < len(tokens) else '\n'))
        file.write("}\n")

# 主程序
try:
    accounts = read_accounts('account.txt')
    tokens = {}
    for idx, (username, password) in enumerate(accounts, 1):
        access_token = get_access_token(base_url, username, password)
        tokens[f'test-{idx}'] = access_token
        print(f"Access Token for {username}: {access_token}")s

    write_tokens('tokens.json', tokens)

except Exception as e:
    print(str(e))
