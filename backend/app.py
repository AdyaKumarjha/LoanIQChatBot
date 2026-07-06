from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.data_routes import router as data_router
from routes.analytics_routes import router as analytics_router
from routes.chat_routes import router as chat_router
from routes.predict_routes import router as predict_router


app = FastAPI(
    title="Loan AI Chatbot",
    version="1.0.0"
)

# ----------------------------
# CORS Configuration
# ----------------------------
origins = [
    # Local development
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://localhost:8000",

    # Vercel Frontend
    "https://loan-iq-chat-bot-p13f.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Allowed frontend URLs
    allow_credentials=True,
    allow_methods=["*"],        # Allow GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],        # Allow all headers
)

# ----------------------------
# Include Routes
# ----------------------------
app.include_router(data_router)
app.include_router(analytics_router)
app.include_router(chat_router)
app.include_router(predict_router)

# ----------------------------
# Home Route
# ----------------------------
@app.get("/")
def home():
    return {
        "message": "Loan AI Chatbot API Running Successfully!"
    }