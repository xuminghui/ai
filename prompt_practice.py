from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

class MessagePractice:
    def __init__(self):
        self.messages = []
    
    def add_message(self, message_type, content):
        """
        添加消息到消息列表
        :param message_type: 消息类型 ('ai', 'human', 'system')
        :param content: 消息内容
        """
        if message_type == 'ai':
            self.messages.append(AIMessage(content=content))
        elif message_type == 'human':
            self.messages.append(HumanMessage(content=content))
        elif message_type == 'system':
            self.messages.append(SystemMessage(content=content))
    
    def build_prompt(self, user_input):
        """
        构建ChatPromptTemplate并处理用户输入
        :param user_input: 用户输入
        :return: 生成的最终提示词
        """
        # 添加用户输入到消息列表
        self.add_message('human', user_input)
        
        # 创建带有占位符的模板
        template_messages = []
        for msg in self.messages:
            if isinstance(msg, HumanMessage):
                template_messages.append(("human", "{input}"))
            else:
                template_messages.append((msg.type, msg.content))
        
        # 创建ChatPromptTemplate
        prompt = ChatPromptTemplate.from_messages(template_messages)
        
        # 格式化提示词
        formatted_prompt = prompt.format(input=user_input)
        
        return formatted_prompt

# 示例用法
if __name__ == "__main__":
    practice = MessagePractice()
    
    # 添加系统消息
    practice.add_message('system', '你是一个有帮助的AI助手')
    
    # 添加AI消息
    practice.add_message('ai', '你好！我是AI助手。')
    
    # 构建提示词并处理用户输入
    user_input = "请告诉我今天的天气"
    final_prompt = practice.build_prompt(user_input)
    
    print("最终提示词:")
    print(final_prompt)