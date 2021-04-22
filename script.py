import pyyoutube
from microdotphat import write_string, set_decimal, clear, show
import config as cfg
import math
import datetime
import time


# Calls the YouTube API and returns the subscribers count.
def get_subscribers():
    api = pyyoutube.Api(api_key=cfg.API_KEY)
    result = api.get_channel_info(channel_id=cfg.CHANNEL_ID)
    channel_info = result.items[0]
    subcount = channel_info.statistics.subscriberCount
    return subcount


# Parses and formats the input to a safe number.
def safe_num(num):
    if isinstance(num, str):
        num = float(num)
    return float('{:.3g}'.format(abs(num)))


# Formats the number.
def format_number(num):
    num = safe_num(num)
    sign = ''

    metric = {'T': 1000000000000, 'B': 1000000000, 'M': 1000000, 'K': 1000, '': 1}

    for index in metric:
        num_check = num / metric[index]

        if num_check >= 1:
            num = num_check
            sign = index
            break

    return f"{str(num).rstrip('0').rstrip('.')}{sign}"


while True:
    clear()
    sub_count = get_subscribers()
    print(datetime.datetime.now() + " Sub count: " + sub_count)
    write_string(format_number(sub_count), kerning=False)
    show()
    time.sleep(30)
