from datetime import datetime

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from percefons.core import settings
from percefons.interfaces.api.routes.auth import router as auth_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description=(
        "Agentic Retrieval-Augmented Generation server with JWT auth, PostgreSQL, Chroma vector store, "
        "and OpenAPI (Swagger) documentation."
    ),
    openapi_tags=[
        {
            "name": "Auth",
            "description": (
                "User registration and login (OAuth2 password)."
            )
        },
        # {"name": "documents", "description": "Upload and manage documents for retrieval."},
        # {"name": "query", "description": "Ask questions to the agentic RAG system."},
        # {"name": "health", "description": "Health check endpoint."},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        origin.strip() for origin in settings.CORS_ORIGINS.split(",")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix=settings.API_V1_PREFIX)


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
        port=8080,
        reload=settings.DEBUG
    )


if __name__ == '__main__':
    main()
