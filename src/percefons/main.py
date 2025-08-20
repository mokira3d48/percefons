import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from percefons.core import settings
from datetime import datetime

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=(
        "Enterprise Agentic RAG System with FastAPI"
    ),
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

def main():
    """Main function to start asynchronous server."""

    # Global exception handler

    uvicorn.run(
        app="percefons.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )


if __name__ == '__main__':
    main()
