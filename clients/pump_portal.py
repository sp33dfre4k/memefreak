import requests

class PumpPortalException(Exception):
    pass

class PumpPortal:
    BASE_API = "https://pumpportal.fun/api/"

    def build_transaction(
            self,
            public_key: str,
            action: str,
            mint: str,
            amount: float,
            denominated_in_sol: bool,
            slippage: int,
            priortiy_fee: float,
            pool: str,
    ):
        return self._post(
            "trade-local",
            {
                "publicKey": public_key,
                "action": action,
                "mint": mint,
                "amount": amount,
                "denominationInSol": denominated_in_sol,
                "slippage": slippage,
                "priortiyFe": priortiy_fee,
                "pool": pool,
            }
        )

    def _get(self, path: str, params: dict = None):
        response = requests.get(
            self.BASE_API + path,
        )

        return response
    
    def _post(self, path: str, payload: dict = None):
        response = requests.post(
            self.BASE_API + path,
        )

        return response


    @property
    def headers(self):
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }