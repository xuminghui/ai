import requests

# FastAPI服务的基础URL
BASE_URL = "http://localhost:8000"

def greet(name: str):
    """
    调用/greet端点获取问候语
    
    参数:
        name: 要问候的名字
    
    返回:
        dict: 包含问候消息的字典
    """
    response = requests.post(f"{BASE_URL}/greet", params={"name": name})
    return response.json()

def greet_with_prefix(name: str, prefix: str = "尊敬的"):
    """
    调用/greet_with_prefix端点获取带前缀的问候语
    
    参数:
        name: 要问候的名字
        prefix: 名字前缀，默认为"尊敬的"
    
    返回:
        dict: 包含问候消息的字典
    """
    response = requests.post(
        f"{BASE_URL}/greet_with_prefix", 
        params={"name": name, "prefix": prefix}
    )
    return response.json()

if __name__ == "__main__":
    # 示例用法
    print(greet("小明"))
    print(greet_with_prefix("小明", "亲爱的"))