from fastapi import FastAPI
from google import genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

client = genai.Client()

@app.get("/chat/{saludo}")
def llamar_ia(saludo):
    inferencia = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=saludo,
    )
    return {"Respuesta": inferencia.output_text }
       

