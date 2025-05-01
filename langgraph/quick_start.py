#https://langchain-ai.github.io/langgraph/tutorials/introduction/
from csv import DictReader
from langgraph.graph import START,END
from langgraph.graph import StateGraph
def supermarket(state):
    return {"ingredients":state["ingredients"],"ret":"{}买到了".format(state["ingredients"])}

def recipe(state):
    print("recipe")
    return {"ingredients":state["ingredients"],"ret":"搜索到了红烧{}菜谱".format(state["ingredients"])}

def cooking(state):
    print("cooking")
    return {"ingredients":state["ingredients"],"ret":"做了一道红烧{}菜".format(state["ingredients"])}


if __name__ == "__main__":
    #参考源码：type[Any] 表示接受任何类型的类对象（如 dict 本身，而不是 dict 的实例）
    #- *, 星号后的参数必须通过关键字方式传递（keyword-only arguments）
    # 这是Python 3的特性，强制调用者显式指定参数名
    sg=StateGraph(dict)   #python中dict是一个内置类型，不需要导入，直接使用。
    #节点
    #(method) def add_node(
    #node: str,
    #action: RunnableLike,注意这里action类型，查看源码的定义，python的duck typing

    sg.add_node("supermarket",supermarket)
    sg.add_node("recipe",recipe)
    sg.add_node("cooking",cooking)
    #起点
    sg.add_edge(START,"supermarket")
    #定义普通边
    sg.add_edge("supermarket","recipe")
    sg.add_edge("recipe","cooking")
    #终点
    sg.add_edge("cooking",END)
    graph=sg.compile()
    ret=graph.invoke({"ingredients":"羊排"})
    print(graph.get_graph().draw_ascii())
    print(ret)
