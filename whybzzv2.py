import discord
from discord.ext import commands
import youtube_dl

class whybzzv2(commands.Cog):
    def __init__(self , client):
        self.client = client
    
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:    # vc not joined
            await ctx.send("You need to join a voice channel first.")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def dc(self,ctx):
        await ctx.voice_client.disconnect()
        
    @commands.command()
    async def play(self,ctx,url):
        try:
            ctx.voice_client.stop()
        except:
            pass
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' , 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            vcc = ctx.author.voice.channel
            try:
                await vcc.connect()
            except:
                pass
            
            source = discord.FFmpegPCMAudio(executable="H:\/FFmpeg\/bin\/ffmpeg.exe", source=url2) #streams audio
            ctx.voice_client.play(source)
            
    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Player paused")

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Player resumed")
        
def setup(client):
    client.add_cog(whybzzv2(client))
