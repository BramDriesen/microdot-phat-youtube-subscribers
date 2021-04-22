import pyyoutube
from microdotphat import write_string, set_decimal, clear, show
import config as cfg
import math
import time

def get_subscribers():
    api = pyyoutube.Api(api_key=cfg.API_KEY)
    result = api.get_channel_info(channel_id=cfg.CHANNEL_ID)
    channel_info = result.items[0]
    subcount = channel_info.statistics.subscriberCount
    return subcount

def safe_num(num):
    if isinstance(num, str):
        num = float(num)
    return float('{:.3g}'.format(abs(num)))

def format_number(num):
    num = safe_num(num)
    sign = ''

    metric = {'T': 1000000000000, 'B': 1000000000, 'M': 1000000, 'K': 1000, '': 1}

    for index in metric:
        num_check = num / metric[index]

        if(num_check >= 1):
            num = num_check
            sign = index
            break

    return f"{str(num).rstrip('0').rstrip('.')}{sign}"

while True:
    clear()
    write_string(format_number(get_subscribers()), kerning=False)
    show()
    time.sleep(30)