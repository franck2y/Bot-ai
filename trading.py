from PocketOptionClient import PocketOptionClient
from config import POCKET_OPTION_EMAIL, POCKET_OPTION_PASSWORD

client = PocketOptionClient()
client.connect(POCKET_OPTION_EMAIL, POCKET_OPTION_PASSWORD)

def execute_trade(asset: str, direction: str, amount: float):
    try:
        result = client.buy(asset, amount, direction.lower())
        return {
            "success": True,
            "asset": asset,
            "direction": direction,
            "amount": amount,
            "server_response": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def get_account_info():
    try:
        balance = client.get_balance()
        return {
            "email": POCKET_OPTION_EMAIL,
            "balance": balance
        }
    except Exception as e:
        return {
            "error": str(e)
        }
