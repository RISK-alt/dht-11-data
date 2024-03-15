from discord_webhook import DiscordWebhook, DiscordEmbed
import main

def alert(temp, humidity):
    webhook = embed = discord.Embed(title="La température es trop élevé !",
                        url="insérez l'url zabbix",
                        description="Il faut régulez la température.",
                        colour=0xb51a00,
                        timestamp=datetime.now())

    embed.set_author(name="Batiment 5 - Baie D3 - 4",
                    url="https://github.com/RISK-alt",
                    icon_url="https://cdn.discordapp.com/attachments/1216431298680324199/1216431366552551544/logo-white.png?ex=66005cfd&is=65ede7fd&hm=53913e65aa835bd837d4dd7e1172bd549893e0b1665529a8d0f392d1d8424a54&")

    embed.add_embed_field(name="Température", value=temp)
    embed.add_embed_field(name="Humidité", value=humidity)

    embed.set_image(url="https://cdn.discordapp.com/attachments/1216431298680324199/1217894977112379412/high-temperature-icon.webp?ex=6605b015&is=65f33b15&hm=89f1f88adb300246c6a43a0d5a71fbd421cf7335cbcc285a7764018a433665f1&")

    embed.set_footer(text="MESSAGE AUTOMATIQUE",
                    icon_url="https://cdn.discordapp.com/attachments/1216431298680324199/1217894977112379412/high-temperature-icon.webp?ex=6605b015&is=65f33b15&hm=89f1f88adb300246c6a43a0d5a71fbd421cf7335cbcc285a7764018a433665f1&")

    webhook.add_embed(embed)
    response = webhook.execute()