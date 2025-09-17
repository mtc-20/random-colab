from fastmcp import FastMCP

# Initialize
mcp = FastMCP("math-me")


@mcp.tool
async def multiply(nums:list[int|float]) -> int|float:
  """Multiple numbers
  
  Args:
    nums: A list of numbers to be multiplied.
  """
  if 0 in nums:
    return 0
  res = 1
  for val in nums:
    res = res*val
  
  return res

if __name__ == "__main__":
  mcp.run(transport="stdio")  
