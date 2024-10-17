import requests

class DexScreener:
    def get_pair_address(token_address) -> str:
        url = f"https://api.dexscreener.com/latest/dex/search?q={token_address}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['pairs'][0]['pairAddress']
        else:
            return None