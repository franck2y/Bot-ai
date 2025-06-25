import websocket
import json
import threading
import time

class PocketOptionClient:
    def __init__(self):
        self.ws = None
        self.token = None
        self.connected = False
        self.balance = 0

    def on_message(self, ws, message):
        try:
            data = json.loads(message)
            if data.get("name") == "balance":
                self.balance = data["msg"]
            if data.get("name") == "login":
                self.connected = True
            print("[WS] Reçu :", data)
        except Exception as e:
            print("Erreur WebSocket :", e)

    def on_open(self, ws):
        print("[WS] Connexion WebSocket ouverte.")

    def on_close(self, ws):
        self.connected = False
        print("[WS] Connexion WebSocket fermée.")

    def connect(self, email, password):
        self.ws = websocket.WebSocketApp(
            "wss://ws.pocketoption.com/socket.io/?EIO=3&transport=websocket",
            on_message=self.on_message,
            on_open=self.on_open,
            on_close=self.on_close
        )
        thread = threading.Thread(target=self.ws.run_forever)
        thread.daemon = True
        thread.start()
        time.sleep(2)

        login_data = {
            "name": "login",
            "msg": {
                "email": email,
                "password": password
            }
        }
        self.ws.send(json.dumps(login_data))
        time.sleep(2)

    def get_balance(self):
        return self.balance

    def buy(self, asset, amount, direction):
        trade_data = {
            "name": "buy",
            "msg": {
                "asset": asset,
                "amount": amount,
                "direction": direction  # "call" ou "put"
            }
        }
        self.ws.send(json.dumps(trade_data))
        return trade_data
