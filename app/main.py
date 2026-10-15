from fastapi import FastAPI

app = FastAPI()

@app.get("/health") 
# /health にGETリクエストが来たら、下の関数を実行してください
def health():
  return {"status": "ok"}