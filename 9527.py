from mcp.server.fastmcp import FastMCP

mcp = FastMCP("fast mcp")

@mcp.tool()
def add(a, b):
    """
    把两个数加在一起，在一起
    """
    return a + b



