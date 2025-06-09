import os
import random
import asyncio
from pyrogram import Client
from pyrogram.types import InputMediaPhoto
from datetime import datetime

API_ID = 29530163  # Substituir pelo seu API_ID (caso use sessão)
API_HASH = "6066497fd46d35ea3dac9a179e27047b"  # Substituir pelo seu API_HASH (caso use sessão)
BOT_TOKEN = "7871641813:AAGvgNQpRvWuM0N7BXHPEqhTiEKoIK9DxMo"

# IDs dos destinos
CANAL_USERNAME = "@Avontzzp"

# Caminhos das pastas
PASTA_PROVAS_SOCIAIS = "provas sociais"
PASTA_PROVAS_GANHOS = "provas de ganhos"

# Textos possíveis para os envios
TEXTOS = [
    "🔥 De novo?! Olha isso...\n👉 http://short.up.bet.br/AAFY0",
    "📸 Mais um print do grupo. Já são vários hoje.\n👉 http://short.up.bet.br/AAFY0",
    "💰 Não é sorte... é constância. Veja o resultado:\n👉 http://short.up.bet.br/AAFY0",
    "🚀 Começou com pouco e já tá assim!\n👉 http://short.up.bet.br/AAFY0",
    "📲 Prova de saque recebida agora no grupo.\n👉 http://short.up.bet.br/AAFY0",
    "🧲 Se você entende o jogo, isso aqui é pra você:\n👉 http://short.up.bet.br/AAFY0",
]

ultima_imagem = None

async def enviar_mensagem(app):
    global ultima_imagem

    while True:
        # Escolher aleatoriamente entre as pastas
        pasta_escolhida = random.choice([PASTA_PROVAS_SOCIAIS, PASTA_PROVAS_GANHOS])
        imagens = os.listdir(pasta_escolhida)

        # Remover a última imagem usada para evitar repetição
        if ultima_imagem in imagens and len(imagens) > 1:
            imagens.remove(ultima_imagem)

        imagem_escolhida = random.choice(imagens)
        ultima_imagem = imagem_escolhida

        caminho_completo = os.path.join(pasta_escolhida, imagem_escolhida)
        texto = random.choice(TEXTOS)

        try:
            await app.send_photo(chat_id=CANAL_USERNAME, photo=caminho_completo, caption=texto)
            print(f"[{datetime.now()}] Enviado: {imagem_escolhida} | Texto: {texto}")
        except Exception as e:
            print(f"Erro ao enviar imagem: {e}")

        await asyncio.sleep(7 * 60)  # Esperar 7 minutos


app = Client("avontz_bot", bot_token=BOT_TOKEN)

async def main():
    async with app:
        await enviar_mensagem(app)

if __name__ == "__main__":
    asyncio.run(main())
