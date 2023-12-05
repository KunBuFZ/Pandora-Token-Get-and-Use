# Pandora-Token-Get-and-Use

## script版

本项目需要配合 Pandora_Next 使用，请确保您的Pandora_Next已经配置妥当

tokens.py 利用账号密码获取时效更长的Session Token，并自动生成pandora_next所需的tokens.json (第二次生成时，需要清空tokens.json中的内容)

share.py 用于获取access token和share token；配合定时计划运行可实现 share token 长期有效

test.py 是调用示例脚本

## 新增web版，详见web目录下readme
