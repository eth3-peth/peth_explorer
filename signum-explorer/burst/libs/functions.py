
from config import settings


#def calc_block_reward(height: int) -> int:
#    if height >= settings.BLOCK_REWARD_LIMIT_HEIGHT:
#        return settings.BLOCK_REWARD_LIMIT_AMOUNT
#    month = int(height / 10800)
#    return int(pow(0.95, month) * 10000)


import requests


def calc_block_reward(height: int) -> int:
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
    }
    url = f'http://mainnet.peth.world:6876/burst?requestType=getBlock&height={height}'
    response = requests.get(url=url, headers=headers, timeout=30).json()
    #print(height, '    ', response['generatorRS'], '    ', response['blockRewardNQT'])
    return int(response['blockRewardNQT'])

