import discord
import asyncio
import random
import os
import datetime
from time import sleep
import arrow
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope1 = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #정책시트
scope2 = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #재고시트
creds1 = ServiceAccountCredentials.from_json_keyfile_name('gjhelper-cc7069273059.json', scope1) #정책시트
creds2 = ServiceAccountCredentials.from_json_keyfile_name('gjhelper-cc7069273059.json', scope2) #재고시트
client1 = gspread.authorize(creds1) #정책시트
client2 = gspread.authorize(creds2) #재고시트
doc1 = client1.open_by_url('https://docs.google.com/spreadsheets/d/1MVKpRP5UFV6OX4whUsFr7qp_K_zGa8JLDw0HUbjzY8I') #정책시트
doc2 = client2.open_by_url('https://docs.google.com/spreadsheets/d/1PA2WP-aQ-d8TlGubOSpUJwHoH8VZfiTwIFPO3eYGnIs') #재고시트




client = discord.Client()


@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='업무지원', type=1))

@client.event
async def on_member_join(member):
    sleep(1)	
    fmt = '{1.name} 에 오신것을 환영합니다.\n{0.mention} 님!! \n매장이름/직급/성함/연락처 이렇게 남겨주시면 \n확인후 권한을 승인해드리겠습니다. '
    channel = member.server.get_channel("679365866000875602")
    return await client.send_message(channel, fmt.format(member, member.server))


@client.event
async def on_message(message):
    
          
	if message.content.startswith('!동판'):
		SearchID = message.content[len('!동판')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('GJ정책표관리').worksheet('동판출력')
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
		await client.send_message(client.get_channel("679370962927616030"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
		
	if message.content.startswith('!공짜폰'):
		SearchID = message.content[len('!공짜폰')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('GJ정책표관리').worksheet('무선공짜출력')
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
		await client.send_message(client.get_channel("679370756735369274"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
		
		
	if message.content.startswith('!외국인공짜폰'):
		SearchID = message.content[len('!외국인공짜폰')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('GJ정책표관리').worksheet('외국인공짜출력')
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
		await client.send_message(client.get_channel("679370924440551424"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
	if message.content == '!정책표':
		command_list = ''
		command_list += '\n'
		command_list += '📌 공지사항\n'
		command_list += '```diff\n-2020-02-18기준 금일부터\n-방x위 지시사항으로 정책표상에 시간기재가 금지됩니다.\n-정책적용기준은 폰클 상에 작성된 기준시간과\n-"!정책표" 명령시 테이블 상단 적용일시 확인바랍니다.```'
		command_list += '\n'
		command_list += '웹사이트 링크\n'
		command_list += 'https://docs.google.com/spreadsheets/d/1iA-tAgT6BpoQjiuTgimPvdQgoCysJ028088RtCa0078/pubhtml# \n'     #!링크
		command_list += '\n'
		command_list += '엑셀다운 링크\n'
		command_list += 'https://docs.google.com/spreadsheets/d/1iA-tAgT6BpoQjiuTgimPvdQgoCysJ028088RtCa0078/pub?output=xlsx \n'     #!링크
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('GJ정책표관리').worksheet('무선구두')
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
		await client.send_message(client.get_channel("679370172007579668"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
	if message.content.startswith('!그레이드'):
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('GJ재고관리').worksheet('그레이드')
		result = wks.acell('B1').value
		embed1 = discord.Embed(
			title = ' 파트너 그레이드 안내!! ',
			description= '**```css\n' + result + ' ```**',
			color=0x7fffd4
			)
		embed2 = discord.Embed(
			title = ' 파트너 그레이드 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
			color=0x00ffff
			)
		await client.send_message(message.channel, embed=embed1)
		await client.send_message(client.get_channel("679369629172498474"), embed=embed2)
		
	if message.content.startswith('!주문'):
		curruntTime = datetime.datetime.now() + datetime.timedelta(hours = 9)
		krnow = curruntTime.strftime('%Y/%m/%d %H:%M')
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('GJ재고관리').worksheet('디스코드주문내역')
		wks.insert_row([krnow, message.channel.name, message.author.display_name, message.content[4:]], 3)
		embed1 = discord.Embed(
			title = message.author.display_name + "님 의 주문 ",
			description= '```fix\n' + message.content[4:] + '```',
			color=0xCBFF75
			)
		embed1.add_field(
			name=" 주문접수 확인... ",
			value= '```diff\n!주문내용이 전달되어 정상적으로\n!접수되었습니다. 부득이한경우\n!개인답변 드리겠습니다.```'
			)
		embed2 = discord.Embed(
			title = message.author.display_name + "님 의 주문내용 ",
			description= '```' + message.content[4:] + '```',
			color=0xCBFF75
			)
		embed2.add_field(
			name=" 주문 접수처... ",
			value= '```' "거래처:"+ message.channel.name +"\n채널아이디:" + message.channel.id + '```'
			)
		await client.send_message(message.channel, embed=embed1)
		await client.send_message(client.get_channel("679376089885310997"), embed=embed2)
		
	if message.content.startswith('!답변'):
		member = discord.utils.get(client.get_all_channels(), id=message.content[4:22])
		neyongdabtotal = message.content[23:]
		neyongdab = neyongdabtotal.split("/")
		neyong = neyongdab[0]
		dab = neyongdab[1]
		
		embed = discord.Embed(
			title = "주문내용",
			description= '```fix\n' + neyong + '```',
			color=0xFF0000
			)
		embed.add_field(
			name = message.author.display_name + "님 답변",
			value= '```Tex\n' + '$' + dab + '```'
			)
		await client.send_message(member, embed=embed)
		

	if message.content.startswith('!공지'):
		if message.author.id == '315237238940106754' :
			embed = discord.Embed(    
				title = "📌 공지사항",
				description= '```' + message.content[4:] + '```',
				color=0xFF0000	
				)
			await client.send_message(client.get_channel("679379752318009352"), embed=embed)
			await client.send_message(client.get_channel("679402498607546398"), embed=embed)
			await client.send_message(client.get_channel("680081617083170818"), embed=embed)
			await client.send_message(client.get_channel("680081729452507193"), embed=embed)
			await client.send_message(client.get_channel("680081795349217303"), embed=embed)
			await client.send_message(client.get_channel("680081829029609521"), embed=embed)
			await client.send_message(client.get_channel("680081863255130121"), embed=embed)
			await client.send_message(client.get_channel("680081902295580728"), embed=embed)
			await client.send_message(client.get_channel("680081929671933972"), embed=embed)
			await client.send_message(client.get_channel("680081956171808788"), embed=embed)
			await client.send_message(client.get_channel("680081978116014110"), embed=embed)
			await client.send_message(client.get_channel("680082009976209444"), embed=embed)
			await client.send_message(client.get_channel("680082046282104863"), embed=embed)
			await client.send_message(client.get_channel("680082075352825992"), embed=embed)
			await client.send_message(client.get_channel("680082122270179361"), embed=embed)
			await client.send_message(client.get_channel("680082158261633025"), embed=embed)
			await client.send_message(client.get_channel("680082168483020800"), embed=embed)
			await client.send_message(client.get_channel("680082314901979226"), embed=embed)
			await client.send_message(client.get_channel("680082355666681889"), embed=embed)
			await client.send_message(client.get_channel("680082398498783249"), embed=embed)
			await client.send_message(client.get_channel("680082433307050009"), embed=embed)
			await client.send_message(client.get_channel("680082468761632774"), embed=embed)
			await client.send_message(client.get_channel("680082525028089879"), embed=embed)
			await client.send_message(client.get_channel("680082555080540231"), embed=embed)
			await client.send_message(client.get_channel("680082578228772864"), embed=embed)
			await client.send_message(client.get_channel("680082598206505015"), embed=embed)
			await client.send_message(client.get_channel("680082619484209409"), embed=embed)
			await client.send_message(client.get_channel("680082641269424128"), embed=embed)
			await client.send_message(client.get_channel("680082664069660821"), embed=embed)
			await client.send_message(client.get_channel("680082711733338120"), embed=embed)
			await client.send_message(client.get_channel("680082735603384366"), embed=embed)
			await client.send_message(client.get_channel("680082759892729856"), embed=embed)
			await client.send_message(client.get_channel("680082802875695151"), embed=embed)
			await client.send_message(client.get_channel("680082833464623106"), embed=embed)
			await client.send_message(client.get_channel("680082853941608530"), embed=embed)
			await client.send_message(client.get_channel("680082876246786130"), embed=embed)
			await client.send_message(client.get_channel("680082896434102300"), embed=embed)
			await client.send_message(client.get_channel("680082919007584261"), embed=embed)
			await client.send_message(client.get_channel("680082938762756096"), embed=embed)
			await client.send_message(client.get_channel("680082967284285537"), embed=embed)
			await client.send_message(client.get_channel("680082990973583364"), embed=embed)
			await client.send_message(client.get_channel("680083018932813825"), embed=embed)
			await client.send_message(client.get_channel("680083045398741038"), embed=embed)
			await client.send_message(client.get_channel("680083066353352748"), embed=embed)
			await client.send_message(client.get_channel("680083086872281276"), embed=embed)
			await client.send_message(client.get_channel("680083109181652998"), embed=embed)
			await client.send_message(client.get_channel("680083128831836210"), embed=embed)
			await client.send_message(client.get_channel("680083167457443897"), embed=embed)
			await client.send_message(client.get_channel("680083575793778828"), embed=embed)
			await client.send_message(client.get_channel("680083622300352588"), embed=embed)
			await client.send_message(client.get_channel("680083653245534324"), embed=embed)
			await client.send_message(client.get_channel("680083686460620871"), embed=embed)
			await client.send_message(client.get_channel("680083730349555789"), embed=embed)
			await client.send_message(client.get_channel("680083754768662594"), embed=embed)
			await client.send_message(client.get_channel("680083782870761513"), embed=embed)
			await client.send_message(client.get_channel("680083809928216682"), embed=embed)
			await client.send_message(client.get_channel("680083836465446939"), embed=embed)
			await client.send_message(client.get_channel("680083862365274160"), embed=embed)
			await client.send_message(client.get_channel("680083887720103976"), embed=embed)
			await client.send_message(client.get_channel("680083926382936073"), embed=embed)
			await client.send_message(client.get_channel("680083970624323618"), embed=embed)
			await client.send_message(client.get_channel("680084002148843520"), embed=embed)
			await client.send_message(client.get_channel("680084027872510002"), embed=embed)
			await client.send_message(client.get_channel("680084054644883476"), embed=embed)
			await client.send_message(client.get_channel("680084082830737459"), embed=embed)
			await client.send_message(client.get_channel("680084108050956289"), embed=embed)
			await client.send_message(client.get_channel("680084134223413273"), embed=embed)
			await client.send_message(client.get_channel("680084156398829574"), embed=embed)
			await client.send_message(client.get_channel("680084191450365961"), embed=embed)
			await client.send_message(client.get_channel("680084278604070949"), embed=embed)
			await client.send_message(client.get_channel("680084325475024932"), embed=embed)
			await client.send_message(client.get_channel("680084419901522029"), embed=embed)
			await client.send_message(client.get_channel("680084446241882119"), embed=embed)
			await client.send_message(client.get_channel("680084470958784556"), embed=embed)
			await client.send_message(client.get_channel("680084501501968386"), embed=embed)
			await client.send_message(client.get_channel("680084528957620396"), embed=embed)
			await client.send_message(client.get_channel("680084563438993439"), embed=embed)
			await client.send_message(client.get_channel("680084633458835554"), embed=embed)
			await client.send_message(client.get_channel("680084662210920478"), embed=embed)
			await client.send_message(client.get_channel("680084689234821198"), embed=embed)
			await client.send_message(client.get_channel("680084713347743792"), embed=embed)
			await client.send_message(client.get_channel("680084738702311545"), embed=embed)
			await client.send_message(client.get_channel("680084763712946256"), embed=embed)
			await client.send_message(client.get_channel("680084786815303913"), embed=embed)
			await client.send_message(client.get_channel("680084809166749706"), embed=embed)
			await client.send_message(client.get_channel("680084834798010417"), embed=embed)
			await client.send_message(client.get_channel("680084861054222348"), embed=embed)
			await client.send_message(client.get_channel("680084887771938817"), embed=embed)
			await client.send_message(client.get_channel("680084913730748423"), embed=embed)
			await client.send_message(client.get_channel("680084946408439827"), embed=embed)
			await client.send_message(client.get_channel("680085001706274881"), embed=embed)
			await client.send_message(client.get_channel("680085026288828426"), embed=embed)
			await client.send_message(client.get_channel("680085050255081475"), embed=embed)
			await client.send_message(client.get_channel("680085077417525302"), embed=embed)
			await client.send_message(client.get_channel("680085105976672311"), embed=embed)
			await client.send_message(client.get_channel("680085132228558964"), embed=embed)
			await client.send_message(client.get_channel("680085156358258708"), embed=embed)
			await client.send_message(client.get_channel("680085181922803737"), embed=embed)
			await client.send_message(client.get_channel("680085206358818853"), embed=embed)
			await client.send_message(client.get_channel("680085231419785216"), embed=embed)
			await client.send_message(client.get_channel("680475870938529834"), embed=embed)
			await client.send_message(client.get_channel("680476192281067520"), embed=embed)
			await client.send_message(client.get_channel("680476223066996945"), embed=embed)
			await client.send_message(client.get_channel("680476264242348050"), embed=embed)
			await client.send_message(client.get_channel("680476288603127831"), embed=embed)
			await client.send_message(client.get_channel("680476310853910529"), embed=embed)
			await client.send_message(client.get_channel("680476332089671689"), embed=embed)
			await client.send_message(client.get_channel("680476363030921320"), embed=embed)
			await client.send_message(client.get_channel("680476384283590659"), embed=embed)
			await client.send_message(client.get_channel("680476421201985585"), embed=embed)
			await client.send_message(client.get_channel("680476494199259172"), embed=embed)
			await client.send_message(client.get_channel("680476524427870218"), embed=embed)
			await client.send_message(client.get_channel("680476545382481940"), embed=embed)
			await client.send_message(client.get_channel("680476566689808582"), embed=embed)
			await client.send_message(client.get_channel("680476586591780961"), embed=embed)
			await client.send_message(client.get_channel("680476609190690888"), embed=embed)
			await client.send_message(client.get_channel("680476629318762566"), embed=embed)
			await client.send_message(client.get_channel("680476653536673910"), embed=embed)
			await client.send_message(client.get_channel("680476683618353193"), embed=embed)
			await client.send_message(client.get_channel("680476708864131150"), embed=embed)
			await client.send_message(client.get_channel("680476762463141918"), embed=embed)
			await client.send_message(client.get_channel("680476786974261258"), embed=embed)
			await client.send_message(client.get_channel("680476806934953999"), embed=embed)
			await client.send_message(client.get_channel("680476825180438623"), embed=embed)
			await client.send_message(client.get_channel("680476846336507911"), embed=embed)
			await client.send_message(client.get_channel("680476874706649097"), embed=embed)
			await client.send_message(client.get_channel("680476529998037180"), embed=embed)
			await client.send_message(client.get_channel("680478520568578091"), embed=embed)
			await client.send_message(client.get_channel("680478561504722944"), embed=embed)
			await client.send_message(client.get_channel("680478588981870592"), embed=embed)
			await client.send_message(client.get_channel("680478614290038926"), embed=embed)
			await client.send_message(client.get_channel("680478645995044909"), embed=embed)
			await client.send_message(client.get_channel("680478666643341352"), embed=embed)
			await client.send_message(client.get_channel("680478688617300018"), embed=embed)
			await client.send_message(client.get_channel("680478765402685446"), embed=embed)
			await client.send_message(client.get_channel("680478787108208661"), embed=embed)
			await client.send_message(client.get_channel("680478819945152586"), embed=embed)
			await client.send_message(client.get_channel("680478855437484161"), embed=embed)
			await client.send_message(client.get_channel("680478881488437254"), embed=embed)
			await client.send_message(client.get_channel("680478909611245627"), embed=embed)
			await client.send_message(client.get_channel("680478934047260724"), embed=embed)
			await client.send_message(client.get_channel("680478953751969829"), embed=embed)
			await client.send_message(client.get_channel("680478974392270884"), embed=embed)
			await client.send_message(client.get_channel("680478992968581201"), embed=embed)
			await client.send_message(client.get_channel("680479013600362513"), embed=embed)
			await client.send_message(client.get_channel("680479033707986997"), embed=embed)
			await client.send_message(client.get_channel("680479063504322561"), embed=embed)
			await client.send_message(client.get_channel("680479082768760870"), embed=embed)
			await client.send_message(client.get_channel("680479103778029592"), embed=embed)
			await client.send_message(client.get_channel("680479149944602732"), embed=embed)

	if message.content == '!명령어':
		command_list = ''
		command_list += '!명령어\n'     #!명령어
		command_list += '!모델명\n'     #!모델명
		
		embed = discord.Embed(
			title = ":keyboard: 기본명령어",
			description= '```fix\n' + command_list + '```',
			color=0xFFD5B4
			)
		embed.add_field(
			name="📶 정책관련 명령어 ",
			value= '```diff\n- !정책표\n- !그레이드\n- !비하인드\n---< 비하인드 명령어는 음성지원만 확인가능합니다. >\n+ !단가 모델명 요금제군 유형\n---< ex)!단가 N976 A군 MNP >\n+ !외국인단가 모델명 요금제군 유형\n---< ex)!외국인단가 N976 A군 MNP >\n+ !공짜폰 요금제군 유형\n---< ex)!공짜폰 C군 MNP >\n+ !외국인공짜폰 요금제군 유형\n---< ex)!외국인공짜폰 A군 신규 > ```',
			inline = False
			)
		embed.add_field(
			name="📲 재고관련 명령어 ",
			value= '```diff\n- !주문\n---< ex)!주문 N976 화이트 1대 보내주세요 >\n+ !재고 모델명\n---< ex)!재고 N976 >\n+ !재고 [구단위]\n---< ex)!재고 남동구 >\n+ !퀵비 [동단위/동단위]\n---< ex)!퀵비 논현동/가좌동 >\n\n퀵비 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="🌐 동판관련 명령어 ",
			value= '```Cs\n# !동판 동판\n'+'@ !동판 소호신규\n@ !동판 소호기변\n@ !동판 후결합\n@ !동판 재약정\n@ !동판 재약정단독\n@ !동판 단독\n\n\n\n ```',
			inline = True
			)
		embed.add_field(
			name="🎲 기타 명령어 ",
			value= '```diff\n= !영화순위\n= !주사위\n= !복권\n+ !나이 생년-월-일 \n---< ex)!나이 2002-02-01 >\n+ !유지기간 개통일\n---< ex)!유지기간 2020-01-01 >\n+ !사다리 뽑을인원수 인원1 인원2 인원3...\n---< ex)!사다리 2 홍길동 갑돌이 갑순이 >\n+ !타이머 초시간\n---< ex)!타이머 5 >```',
			inline = True
			)
		await client.send_message(message.channel, embed=embed)
        
	if message.content == '!영업명령어':
		command_list = ''
		command_list += '!영업명령어\n'     #!명령어        
		command_list += '!모델명\n'     #!모델명
		command_list += '!거래처\n'     #!모델명
		
		embed = discord.Embed(
			title = "🚗 영업부 기본명령어",
			description= '```fix\n' + command_list + '```',
			color=0xFFD5B4
			)
		embed.add_field(
			name="📈 실적관련 명령어 ",
			value= '```diff\n- !전월실적\n---< 전월 전체실적 >\n+ !전월실적 영업사원이름\n---< ex)!전월실적 홍길동 >\n- !당월실적\n---< 데이터 입력일까지 당월 전체실적 >\n+ !당월실적 영업사원이름\n---< ex)!당월실적 홍길동 >\n\n실적 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="📶 정책관련 명령어 ",
			value= '```diff\n- !정책표\n- !그레이드\n- !비하인드\n---< 비하인드 명령어는 음성지원만 확인가능합니다. >\n+ !단가 모델명 요금제군 유형\n---< ex)!단가 N976 A군 MNP >\n+ !외국인단가 모델명 요금제군 유형\n---< ex)!외국인단가 N976 A군 MNP >\n+ !공짜폰 요금제군 유형\n---< ex)!공짜폰 C군 MNP >\n+ !외국인공짜폰 요금제군 유형\n---< ex)!외국인공짜폰 A군 신규 > ```',
			inline = False
			)
		embed.add_field(
			name="📲 재고관련 명령어 ",
			value= '```diff\n- !주문\n---< ex)!주문 A305 A505 배정부탁드립니다. >\n+ !재고 모델명\n---< ex)!재고 N976 >\n+ !재고 거래처코드\n---< ex)!재고 A34 >\n- !불량\n---< 전체불량현황 >\n+ !불량 거래처코드\n---< ex)!불량 A34 >\n- !유심\n---< 10개 미만 유심현황 >\n+ !유심 전체\n---< 거래처 총 유심현황 >\n+ !퀵비 [동단위/동단위]\n---< ex)!퀵비 논현동/가좌동 >\n\n퀵비 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="🌐 동판관련 명령어 ",
			value= '```Cs\n# !동판 동판\n'+'@ !동판 소호신규\n@ !동판 소호기변\n@ !동판 후결합\n@ !동판 재약정\n@ !동판 재약정단독\n@ !동판 단독\n\n\n\n ```',
			inline = True
			)
		embed.add_field(
			name="🎲 기타 명령어 ",
			value= '```diff\n= !영화순위\n= !주사위\n= !복권\n+ !나이 생년-월-일 \n---< ex)!나이 2002-02-01 >\n+ !유지기간 개통일\n---< ex)!유지기간 2020-01-01 >\n+ !사다리 뽑을인원수 인원1 인원2 인원3...\n---< ex)!사다리 2 홍길동 갑돌이 갑순이 >\n+ !타이머 초시간\n---< ex)!타이머 5 >```',
			inline = True
			)
		await client.send_message(message.channel, embed=embed)		
		
	if message.content.startswith('!나이'):
		SearchID = message.content[len('!나이')+1:]
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('GJ재고관리').worksheet('만나이계산기')
		
		wks.update_acell('C8', SearchID)
		result1 = wks.acell('H8').value
		result2 = wks.acell('J8').value
		
		embed = discord.Embed(
			title = ' 오늘기준 ' + SearchID + ' 나이! ',
			description= '```md\n' + SearchID + result1 + result2 + '```',
			color=0x5ABEFF
			)
		await client.send_message(message.channel, embed=embed)
		
		
	if message.content.startswith('!유지기간'):
		SearchID = message.content[len('!유지기간')+1:]
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('오전재고').worksheet('유지기간')
		wks.update_acell('a1', SearchID)
		result = wks.acell('b1').value
		
		embed = discord.Embed(
			title = ' 오늘기준 ' + SearchID + ' 개통자 남은 유지일수는 ',
			description= '```md\n' + SearchID + result + '```',
			color=0x5ABEFF
			)
		await client.send_message(message.channel, embed=embed)		
		
	if message.content.startswith('!영화순위'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx
		i1 = 0 # 랭킹 string값
		embed = discord.Embed(
			title = "영화순위",
			description = "영화순위입니다.",
			colour= discord.Color.red()
			)
		hdr = {'User-Agent': 'Mozilla/5.0'}
		url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
		print(url)
		req = Request(url, headers=hdr)
		html = urllib.request.urlopen(req)
		bsObj = bs4.BeautifulSoup(html, "html.parser")
		moviechartBase = bsObj.find('div', {'class': 'main_detail'})
		moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
		moviechart2 = moviechart1.find_all('li')

		for i in range(0, 20):
			i1 = i1+1
			stri1 = str(i1) # i1은 영화랭킹을 나타내는데 사용됩니다
			print()
			print(i)
			print()
			moviechartLi1 = moviechart2[i]  # ------------------------- 1등랭킹 영화---------------------------
			moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
			moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
			moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목
			print(moviechartLi1MovieName)

			moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
			moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
			moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점
			print(moviechartLi1Ratting)

			moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
			moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
			moviechartLi1openDay3 = moviechartLi1openDay2[0]
			moviechartLi1Yerating1 = moviechartLi1openDay2[1]
			moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
			print(moviechartLi1openDay)
			moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
			print(moviechartLi1Yerating)  # ------------------------- 1등랭킹 영화---------------------------
			print()
			embed.add_field(name='---------------랭킹'+stri1+'위---------------', value='\n영화제목 : '+moviechartLi1MovieName+'\n영화평점 : '+moviechartLi1Ratting+'점'+'\n개봉날짜 : '+moviechartLi1openDay+'\n예매율,랭킹변동 : '+moviechartLi1Yerating, inline=False) # 영화랭킹


		await client.send_message(message.channel, embed=embed)


	if message.content.startswith('!주사위'):
		randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
		print(randomNum)
		if randomNum == 1:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
		if randomNum == 2:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
		if randomNum ==3:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
		if randomNum ==4:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
		if randomNum ==5:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
		if randomNum ==6:
			await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))
			
			
			
			
	if message.content.startswith("!복권"):
		Text = ""
		number = [1, 2, 3, 4, 5, 6, 7]
		count = 0
		for i in range(0, 7):
			num = random.randrange(1, 46)
			number[i] = num
			if count >= 1:
				for i2 in range(0, i):
					if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
						numberText = number[i]
						print("작동 이전값 : " + str(numberText))
						number[i] = random.randrange(1, 46)
						numberText = number[i]
						print("작동 현재값 : " + str(numberText))
						if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
							numberText = number[i]
							print("작동 이전값 : " + str(numberText))
							number[i] = random.randrange(1, 46)
							numberText = number[i]
							print("작동 현재값 : " + str(numberText))
							if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
								numberText = number[i]
								print("작동 이전값 : " + str(numberText))
								number[i] = random.randrange(1, 46)
								numberText = number[i]
								print("작동 현재값 : " + str(numberText))

			count = count + 1
			Text = Text + "  " + str(number[i])
			
		print(Text.strip())
		embed = discord.Embed(
			title="복권 숫자!",
			description=Text.strip(),
			colour=discord.Color.red()
		)
		await client.send_message(message.channel, embed=embed)
		
		
	if message.content.startswith('!사다리'):
		ladder = []
		ladder = message.content[len('!사다리') + 1:].split(" ")
		num_cong = int(ladder[0])
		del (ladder[0])
		if num_cong < len(ladder):
			result_ladder = random.sample(ladder, num_cong)
			result_ladderSTR = ','.join(map(str, result_ladder))
			embed = discord.Embed(
				title="----- 당첨! -----",
				description='```' + result_ladderSTR + '```',
				color=0xff00ff
				)
			await client.send_message(message.channel, embed=embed, tts=False)
		else:
			await client.send_message(message.channel, '```추첨인원이 총 인원과 같거나 많습니다. 재입력 해주세요```', tts=False)

	if message.content.startswith('!타이머'):

		Text = ""
		learn = message.content.split(" ")
		vrsize = len(learn)  # 배열크기
		vrsize = int(vrsize)
		for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
			Text = Text + " " + learn[i]
			
		secint = int(Text)
		sec = secint
		
		for i in range(sec, 0, -1):
			print(i)
			await client.send_message(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
			sleep(1)

		else:
			print("땡")
			await client.send_message(message.channel, embed=discord.Embed(description='타이머 종료'))
		
		
		
		
		


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
