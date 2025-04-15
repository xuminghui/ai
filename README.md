# LangChain Hello World 示例

这是一个简单的 LangChain Hello World 示例项目，展示了 LangChain 的基本用法。

## 环境要求

- Python 3.8+
- 智谱AI API 密钥

## 安装步骤

1. 创建并激活虚拟环境（推荐）：
```bash
python -m venv .venv
source .venv/bin/activate  # 在 Unix/macOS
# 或
.venv\Scripts\activate  # 在 Windows
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 创建 `.env` 文件并添加你的智谱AI API 密钥：
```
ZHIPUAI_API_KEY=你的智谱AI API密钥
```

## 运行示例

```bash
python langchain_hello.py
```

## 示例说明

这个示例展示了：
- 如何初始化智谱AI ChatGLM
- 如何创建提示模板
- 如何使用 LLMChain 处理输入并生成输出

## 获取智谱AI API密钥

1. 访问智谱AI官网：https://open.bigmodel.cn/
2. 注册账号并登录
3. 在控制台获取API密钥
4. 将API密钥添加到 `.env` 文件中 