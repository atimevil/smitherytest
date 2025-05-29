# server.py
from fastmcp import FastMCP, Context
import os
import logging
import asyncio # asyncio 임포트 추가

# Configure logging for detailed output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create FastMCP object
mcp = FastMCP(
    "Simple Test MCP",
    path="/mcp",
    lazy_load=True,
    session_management=False # 세션 관리 비활성화 (더 간단하게)
)

# A very simple tool that just returns a message
@mcp.tool()
async def hello_world() -> dict:
    """Returns a simple greeting message."""
    logger.info("hello_world tool called.")
    # asyncio.to_thread는 동기 함수를 비동기 컨텍스트에서 실행할 때 사용합니다.
    # 여기서는 간단한 문자열 반환이므로, 사실 필요 없지만,
    # FastMCP의 tool 데코레이터가 async 함수를 기대하므로 형식상 유지하거나 제거할 수 있습니다.
    # 이 예시에서는 필요 없으므로 직접 반환합니다.
    return {"message": "Hello from Simple Test MCP!"}

@mcp.tool()
async def ping() -> dict:
    """Responds with 'pong' to check server responsiveness."""
    logger.info("ping tool called.")
    return {"message": "pong"}

# Main execution block
if __name__ == "__main__":
    logger.info("Starting Simple Test MCP server...")
    
    # Get port from environment variable (as Smithery.ai provides it)
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0" # Listen on all network interfaces

    # Run FastMCP server
    mcp.run(
        transport="streamable-http",
        host=host,
        port=port,
        lazy_load=True,
        session_management=False, # 세션 관리 비활성화
        stream_resumable=True,
        error_handling=True
    )
    logger.info("Simple Test MCP server started successfully.")
