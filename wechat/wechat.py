from wxpy import *

bot = Bot(cache_path=True)

xiaoai = XiaoI('open_d6xyBRGYChlm', 't1IaFMpAutsgUsaSTFy1')
tuling = Tuling(api_key='b9e22cd228304e6bb17913a5b3cc7ebe')


@bot.register(['Text'])
def reply_my_friend(msg: bot.messages):
    xiaoai.do_reply(msg)
    # tuling.do_reply(msg)


bot.join()
