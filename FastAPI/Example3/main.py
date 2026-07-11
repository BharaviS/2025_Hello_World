from app import create_app
from app.database.database import init_db

import uvicorn

app = create_app()

# Initialize database
init_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)