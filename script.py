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

def human_format(num, precision=2, suffixes=['', 'K', 'M', 'G', 'T', 'P']):
    num = int(num)
    m = sum([abs(num/10000.0**x) >= 1 for x in range(1, len(suffixes))])

    if num <= 9999:
        return f'{num}'
    else:
        return f'{num/1000.0**m:.{precision}f}{suffixes[m]}'

while True:
    clear()
    write_string(human_format(get_subscribers()))
    show()
    time.sleep(30)