import json
import webbrowser
import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构造 tools.json 文件的路径
json_path = os.path.join(current_dir, 'tools.json')

# 读取 tools.json 文件
with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 遍历工具列表并打开每个 downUrl
for tool in data['tools']:
    url = tool['downUrl']
    print(f"Opening URL: {url}")
    webbrowser.open(url)
