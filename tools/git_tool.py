from langchain_core.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field
import subprocess
import os

class GitCommitSchema(BaseModel):
    commit_message: str = Field(..., description="提交信息")
    remote_url: Optional[str] = Field(default=None, description="Git远程仓库地址，默认为当前配置的origin")


class GitCommitTool(BaseTool):
    name: str = "git_commit"  # 添加类型注解
    description: str = "将当前项目目录下的所有修改提交到Git仓库并推送到远程"  # 添加类型注解
    args_schema: Type[BaseModel] = GitCommitSchema

    def _run(self, commit_message: str, remote_url: str = None):
        try:
            # 执行Git操作
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            
            #查看git remote url的 命令
            if remote_url:
                subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)
            
            subprocess.run(["git", "push"], check=True)
            return "代码提交成功"
        except subprocess.CalledProcessError as e:
            return f"Git操作失败: {str(e)}"

if __name__ == "__main__":
    # 本地验证代码
    tool = GitCommitTool()
    try:
        # 示例提交（可修改参数测试）
        result = tool._run(
            commit_message="测试提交"        )
        print("执行结果:", result)
    except Exception as e:
        print("验证失败:", str(e))
    print("提示：请确保：")
    print("1. 当前目录是git仓库")
    print("2. 已配置git用户信息（user.name/user.email）")
    print("3. 有网络连接和仓库写入权限")
