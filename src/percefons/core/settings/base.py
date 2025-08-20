import os
import logging
import logging.config

LOGGING_CONFIG = "logging.conf"

if os.path.isfile(LOGGING_CONFIG):
    logging.config.fileConfig(LOGGING_CONFIG)

APP_NAME: str = os.getenv('APP_NAME', "PERCEFON'S SERVER" )
VERSION: str = os.getenv('VERSION', '0.1.0')
API_PREFIX: str = os.getenv('API_PREFIX', "/api/v1")
DEBUG: bool = bool(os.getenv('DEBUG', 'True'))

DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@db:5432/agentic_rag"

JWT_SECRET: str = os.getenv('JWT_SECRET', "change-me")
JWT_ALG: str = os.getenv('JWT_ALG', "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 1  # 60 min x 1 -> 1h

# CORS
CORS_ORIGINS: str = os.getenv('CORS_ORIGINS', "*")

# Vector store & embeddings
# CHROMA_PERSIST_DIR: str = "/data/chroma"
# EMBEDDINGS_PROVIDER: str = "sentence_transformers"  # or "openai"
# SENTENCE_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"

# LLM
# LLM_PROVIDER: str = "openai"  # or "transformers"
# OPENAI_API_KEY: Optional[str] = None
# OPENAI_MODEL: str = "gpt-4o-mini"
# HF_MODEL: str = "gpt2"  # Fallback tiny model
