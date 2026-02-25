import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def urgencia(ctx):
    await ctx.send("📋 **Formulario de Urgencias / Emergency Form**")
    
    preguntas = [
        "👤 Nombre del paciente / Patient Name:",
        "🎂 Edad / Age:",
        "🩺 Síntomas / Symptoms:",
        "📍 Ubicación / Location:",
        "⏰ Hora del incidente / Time:"
    ]

    respuestas = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for pregunta in preguntas:
        await ctx.send(pregunta)
        msg = await bot.wait_for("message", check=check)
        respuestas.append(msg.content)

    canal_id = 147296442101428571  # CAMBIA ESTO SI QUIERES
    canal = bot.get_channel(canal_id)

    if canal:
        embed = discord.Embed(title="🚨 NUEVA URGENCIA", color=discord.Color.red())
        for i in range(len(preguntas)):
            embed.add_field(name=preguntas[i], value=respuestas[i], inline=False)
        await canal.send(embed=embed)

    await ctx.send("✅ Formulario enviado correctamente.")

bot.run(os.getenv("TOKEN"))
