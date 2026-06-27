from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool
def multiply(a: float, b: float) -> float:
    return a * b
@mcp.tool
def add(a: int, b: int) -> int:
    return a + b
if __name__ == "__main__":
    mcp.run()