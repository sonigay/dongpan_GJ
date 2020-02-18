import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('dongpan-699a93059b16.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1hL4uvq2On11zp-_JWoWMG0Gyyuty5Lhvp_gQkfTYsOI')




client = discord.Client()


@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='정책 전달', type=1))




@client.event
async def on_message(message):
	global gc #정산
	global creds	#정산
    
          
	if message.content.startswith('!동판'):
		SearchID = message.content[len('!동판')+1:]
		gc = gspread.authorize(creds)
		wks = gc.open('정책표수정').worksheet('동판출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		embed1 = discord.Embed(
			title = ' :globe_with_meridians:  ' + SearchID + ' 안내 ',
			description= '**```css\n' + SearchID + '  오늘 정책입니다. ' + result + ' ```**',
			color=0x00ffff
			)
		embed2 = discord.Embed(
			title = ' :globe_with_meridians: 동판 ' + SearchID + ' 정책조회!! ',
			description= '```' "출력자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
			color=0x00ffff
			)
		await client.send_message(client.get_channel("674653007132229632"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
		
	if message.content.startswith('!공짜폰'):
		SearchID = message.content[len('!공짜폰')+1:]
		gc = gspread.authorize(creds)
		wks = gc.open('정책표수정').worksheet('무선공짜출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		
		embed1 = discord.Embed(
			title = ' 오늘의 ' + SearchID + ' 공짜폰 안내 ',
			description= '**```css\n' + SearchID + '  정책입니다. ' + result + ' ```**',
			color=0x4BAF4B
			)
		embed2 = discord.Embed(
			title = SearchID + ' 공짜폰 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + '```',
			color=0x4BAF4B
			)
		await client.send_message(client.get_channel("674652501693300737"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
		
		
	if message.content.startswith('!외국인공짜폰'):
		SearchID = message.content[len('!외국인공짜폰')+1:]
		gc = gspread.authorize(creds)
		wks = gc.open('정책표수정').worksheet('외국인공짜출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		
		embed1 = discord.Embed(
			title = ' 오늘의 ' + SearchID + ' 외국인공짜폰 안내 ',
			description= '**```css\n' + SearchID + '  정책입니다. ' + result + ' ```**',
			color=0xFF848F
			)
		embed2 = discord.Embed(
			title = SearchID + ' 외국인공짜폰 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
			color=0xFF848F
			)
		await client.send_message(client.get_channel("674654114592063498"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
	if message.content == '!정책표':
		command_list = ''
		command_list += '\n'
		command_list += '📌 공지사항\n'
		command_list += '```diff\n-2020-02-18기준 금일부터\n-방x위 지시사항으로 정책표상에 시간기재가 금지됩니다.\n-정책적용기준은 폰클 상에 작성된 기준시간과\n-"!정책표" 명령시 테이블 상단 적용일시 확인바랍니다.```'
		command_list += '\n'
		command_list += '웹사이트 링크\n'
		command_list += 'https://docs.google.com/spreadsheets/d/1gGOqkMcSau3lXHnP5_UZfEW1rbJOi5czd3w-22QX2j4/pubhtml# \n'     #!링크
		command_list += '\n'
		command_list += '엑셀다운 링크\n'
		command_list += 'https://docs.google.com/spreadsheets/d/1gGOqkMcSau3lXHnP5_UZfEW1rbJOi5czd3w-22QX2j4/pub?output=xlsx \n'     #!링크
		gc = gspread.authorize(creds)
		wks = gc.open('정책표수정').worksheet('무선구두')
		result = wks.acell('E3').value
		embed1 = discord.Embed(
			title = ':bar_chart: 정책 적용일시: ' + result + '',
			description= command_list,
			color=0xf29886
			)
		embed1.add_field(
			name="❗ 주의사항 ",
			value= '```diff\n-위 엔드정책은 참고용입니다. \n-정산은 폰클 정책표에서 그레이드 합산후 날짜별로 구두추가하시고 \n-맞추셔야하십니다.감사합니다.\n-폰클단가표 보는법은 앞자리 2빼고 뒷두자리 입니다.\n-그레이드확인은 "!그레이드" 로 확인 가능하십니다..```'
			)
		embed2 = discord.Embed(
			title = ':bar_chart: 적용일시: ' + result + ' 출력!',
			description= '```' "출력자:" + message.author.display_name +"\n거래처:" + message.channel.name + '```',
			color=0xf29886
			)
		await client.send_message(client.get_channel("672022974223876096"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)	


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
