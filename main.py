import discord
from discord.ext import commands

import os
TOKEN = os.getenv(MTQ3NjAyNzY4MTI0NDk3MTA3NA.GTbwom.dSWo1DrDSyP2ybHFU0CipavenFtfozdQQNQ6_o) 
CANAL_REGISTRO_ID = 1472964421201428571  # PON AQUI EL ID DEL CANAL

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Cuando el bot esté listo
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# ==========================
# FORMULARIO DE URGENCIAS
# ==========================
@bot.command()
async def urgencia(ctx):
    await ctx.send("📋 **Formulario de Urgencias / Emergency Form**\n\nResponde las siguientes preguntas:")

    preguntas = [
        "👤 Nombre del paciente / Patient name:",
        "📅 Edad / Age:",
        "🩺 Síntomas / Symptoms:",
        "📍 Ubicación del incidente / Location:",
        "⏰ Hora del incidente / Time:"
    ]

    respuestas = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for pregunta in preguntas:
        await ctx.send(pregunta)
        msg = await bot.wait_for("message", check=check)
        respuestas.append(msg.content)

    canal = bot.get_channel(CANAL_REGISTRO_ID)

    embed = discord.Embed(
        title="🚨 Nuevo Registro de Urgencia / New Emergency Record",
        color=discord.Color.red()
    )

    for i in range(len(preguntas)):
        embed.add_field(name=preguntas[i], value=respuestas[i], inline=False)

    embed.set_footer(text=f"Atendido por / Attended by: {ctx.author}")

    await canal.send(embed=embed)
    await ctx.send("✅ Registro enviado correctamente / Record sent successfully.")

# ==========================
# FORMULARIO DE PARTO
# ==========================
@bot.command()
async def parto(ctx):
    await ctx.send("👶 **Formulario de Parto / Birth Form**\n\nResponde las siguientes preguntas:")

    preguntas = [
        "👩 Nombre de la madre / Mother's name:",
        "📅 Edad / Age:",
        "🏥 Lugar del parto / Birth location:",
        "👶 Nombre del bebé / Baby name:",
        "⚕ Complicaciones / Complications:"
    ]

    respuestas = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for pregunta in preguntas:
        await ctx.send(pregunta)
        msg = await bot.wait_for("message", check=check)
        respuestas.append(msg.content)

    canal = bot.get_channel(CANAL_REGISTRO_ID)

    embed = discord.Embed(
        title="👶 Nuevo Registro de Parto / New Birth Record",
        color=discord.Color.green()
    )

    for i in range(len(preguntas)):
        embed.add_field(name=preguntas[i], value=respuestas[i], inline=False)

    embed.set_footer(text=f"Atendido por / Attended by: {ctx.author}")

    await canal.send(embed=embed)
    await ctx.send("✅ Registro de parto enviado / Birth record sent.")

# ==========================
# COMANDO DE AYUDA
# ==========================
@bot.command()
async def medico(ctx):
    await ctx.send("""
🏥 **BOT MÉDICO RP**

Comandos disponibles:

!urgencia  → Formulario de emergencia
!parto     → Formulario de parto
!medico    → Ver comandos

""")

bot.run(TOKEN)
