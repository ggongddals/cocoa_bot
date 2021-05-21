import discord
from discord import message
from discord import channel
import time
print("=======봇을 시작하는중=======")
client = discord.Client()

@client.event
async def on_ready():
    print("NAME :",client.user.name)
    print("ID :",client.user.id)
    print("======로그인 성공======")
    game = discord.Game("코코아야 (할말)")
    await client.change_presence(status=discord.Status.online,activity=game)

@client.event
async def on_message(massage):
    if massage.content.startswith("코코아야 애교"): #입력 메세지(첫글자)
        await massage.channel.send("좆까 안해")#반응
    elif massage.content.startswith("코코아야 뭐해"):#메세지(첫글자)
        await massage.channel.send("알거없어 ㅗㅗ")#반응
    elif massage.content.startswith("코코아야 ㅎㅇ"):#메세지(첫글자)
        await massage.channel.send("?? 시발 누구세요?")#반응
    elif massage.content.startswith("코코아야 안녕"):#메세지(첫글자)
        await massage.channel.send("뭔데 인사를 걸고 지랄이야")#반응
    elif massage.content.startswith("코코아야 도움말"):#메세지(첫글자)
        await massage.channel.send("그딴 거 없어")#반응
    elif massage.content.startswith("코코아야 바보"):#메세지(첫글자)
        await massage.channel.send("네 다음 바보가 하는 말이었고요")#반응
    elif massage.content.startswith("코코아야 코코아"):#메세지(첫글자)
        await massage.channel.send("왜 불러 시발아")#반응
    elif massage.content.startswith("코코아야 크시"):#메세지(첫글자)
        await massage.channel.send("수인 새끼")#반응
    elif massage.content.startswith("코코아야 슷칼"):#메세지(첫글자)
        await massage.channel.send("나보다 못생긴 놈")#반응
    elif massage.content.startswith("코코아야 배추"):#메세지(첫글자)
        await massage.channel.send("배추는 먹는거고 멍청아")#반응
    elif massage.content.startswith("코코아야 지랄"):#메세지(첫글자)
        await massage.channel.send("니 면상이 지랄이다")#반응
    elif massage.content.startswith("코코아야 병신"):#메세지(첫글자)
        await massage.channel.send("그게 너야")#반응
    elif massage.content.startswith("코코아야 뒤져"):#메세지(첫글자)
        await massage.channel.send("너나 뒤져")#반응
    elif massage.content.startswith("코코아야 인성"):#메세지(첫글자)
        await massage.channel.send("니 인성이 더 쓰레기같다")#반응
    elif massage.content.startswith("코코아야 호감도"):#메세지(첫글자)
        await massage.channel.send("일단 너한텐 호감이 없어")#반응
    elif massage.content.startswith("코코아야 죽어"):#메세지(첫글자)
        await massage.channel.send("싫은데?")#반응
    elif massage.content.startswith("코코아야 민트초코"):#메세지(첫글자)
        await massage.channel.send("너나 처먹어")#반응
    elif massage.content.startswith("코코아야 ㅋ"):#메세지(첫글자)
        await massage.channel.send("왜 실실 처웃고 지랄이야")#반응
    elif massage.content.startswith("코코아야 나가뒤져"):#메세지(첫글자)
        await massage.channel.send("좆까 안나갈거야")#반응
    elif massage.content.startswith("코코아야 무한"):#메세지(첫글자)
        await massage.channel.send("도전이라고 할 줄 알았냐?")#반응
    elif massage.content.startswith("코코아야 컴퓨터"):#메세지(첫글자)
        await massage.channel.send("박살났어 씨발")#반응
    elif massage.content.startswith("코코아야 마우스"):#메세지(첫글자)
        await massage.channel.send("생쥐 빡대가리 새꺄")#반응
    elif massage.content.startswith("코코아야 ㅅㅂ"):#메세지(첫글자)
        await massage.channel.send("시발")#반응
    elif massage.content.startswith("코코아야 ㅆㅂ"):#메세지(첫글자)
        await massage.channel.send("씨발")#반응
    elif massage.content.startswith("코코아야 ㅈㄹ"):#메세지(첫글자)
        await massage.channel.send("지랄")#반응
    elif massage.content.startswith("코코아야 시발"):#메세지(첫글자)
        await massage.channel.send("시발?")#반응
    elif massage.content.startswith("코코아야 좆까"):#메세지(첫글자)
        await massage.channel.send("니 면상이 좆같다")#반응
    elif massage.content.startswith("코코아야 씨발"):#메세지(첫글자)
        await massage.channel.send("씨발같은 소리하고 앉아있네 이새끼가")#반응
    elif massage.content.startswith("코코아야 친구"):#메세지(첫글자)
        await massage.channel.send("나는 많은데 넌 없어")#반응
    elif massage.content.startswith("코코아야 찐따"):#메세지(첫글자)
        await massage.channel.send("그러는 당신이 방구석 찐따새끼")#반응
    elif massage.content.startswith("코코아야 아싸"):#메세지(첫글자)
        await massage.channel.send("친구없는 니가 아싸")#반응
    elif massage.content.startswith("코코아야 인싸"):#메세지(첫글자)
        await massage.channel.send("너는 평생 아싸")#반응
    elif massage.content.startswith("코코아야 미친"):#메세지(첫글자)
        await massage.channel.send("미친;'")#반응
    elif massage.content.startswith("코코아야"):#메세지(첫글자)
        await massage.channel.send("왜")#반응
client.run("ODQ0OTIwMTI1NjUxMTU3MTA0.YKZbLw.YVC_Bc5kuDpKhMVIQTxA5XRzB8k")