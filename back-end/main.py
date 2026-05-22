from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from sqlalchemy import create_engine, text

app = FastAPI(title="API Obra Social")

# Habilitar CORS para que React se comunique de forma segura
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción se puede restringir al dominio de tu React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "ok",
        "message": "API de Python (FastAPI) funcionando correctamente"
    }

@app.get("/db-test")
def test_db():
    # Variables de entorno proveídas localmente (.env) o por Dokploy
    db_user = os.getenv("DB_USER", "root")
    db_password = os.getenv("DB_PASSWORD", "")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "obra_social")
    
    # URL de conexión SQLAlchemy para MySQL/MariaDB
    database_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    
    try:
        # Intentamos conectar con un timeout de 5 segundos
        engine = create_engine(database_url, connect_args={"connect_timeout": 5})
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return {
                "status": "connected",
                "message": "¡Conexión a MySQL exitosa desde Python!",
                "database": db_name,
                "host": db_host
            }
    except Exception as e:
        return {
            "status": "error",
            "message": "No se pudo conectar a la base de datos MySQL. Revisa tus credenciales o si el servicio está activo.",
            "error": str(e)
        }
