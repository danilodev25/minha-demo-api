from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

class Mensagem(BaseModel):
    mensagem: str = Field(min_length=1)

app = FastAPI(
    title="Minha Primeira Api"
)

@app.get("/", response_class=HTMLResponse)
def pagina_inicial():
    return """
    <h1>API em execução</h1>
    <p> FIAP - Let's rock the future!</p>
    """

@app.get("/Health")
def health()-> dict[str, str]:
    return {"status": "ok"}

@app.get("/teste2")
def teste2()-> dict[str, str]:
    return {"status": "esta funcionando"}

@app.post("/mensagem")
def _receber_mensagem(mensagem: Mensagem):
    return {
        "mensagem_recebida": mensagem.mensagem
    }