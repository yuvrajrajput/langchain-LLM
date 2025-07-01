from mcp.server import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """ _Summary_ add two numbers together"""
    return a + b

@mcp.tool()
def multiple(a: int, b: int) -> int:
    """ _Summary_ multiply two numbers together"""
    return a * b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """ _Summary_ subtract two numbers together"""
    return a - b

# the transport = 'studio' argument tell the server to: 
#use standard input/output (stdin and stdio) to receive and responnd to tool funcation calls
if __name__ == "__main__":
    mcp.run(transport="stdio")