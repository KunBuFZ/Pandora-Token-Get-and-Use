# Pandora-Token-Get-and-Use

## 注意！所有涉及到登录的操作，消耗panduora额度为1:100 请小心使用！

## script版 (可获取access token,session token,share token。可自动生成tokens.json)

本项目需要配合 Pandora_Next 使用，请确保您的Pandora_Next已经配置妥当

tokens.py 利用账号密码获取时效更长的Session Token，并自动生成pandora_next所需的tokens.json (第二次生成时，需要清空tokens.json中的内容)

需要创建account.txt 并按照 账号,密码 的格式一行一个

share.py 用于获取access token和share token；配合定时计划运行可实现 share token 长期有效

test.py 是调用示例脚本

## web版(可获取access token,session_token，share token)

### Demo(自定URL版): https://auth.vnbest.eu.org/

### 部署指南

#### 安装 Flask

如果您还没有安装 Flask，您可以使用 pip 来安装它。在您的终端或命令提示符中运行以下命令：

```bash
pip install flask
```

#### 保存代码

将 app.py和index.html上传至服务器（或下载至本地）

#### 运行 Flask 应用

在包含 app.py 的目录中，运行以下命令来启动 Flask 应用：

```bash
python3 app.py
```

#### 访问应用

在浏览器中打开 http://127.0.0.1:5000 。您应该能看到您的前端页面，并能够提交表单以获取 tokens。


