import json
from . import gen_response
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.prompt = []

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user_input_dict = {"role": "user", "content": message}
        self.prompt.append(user_input_dict)

        response = gen_response.generate_response(self.prompt)
        response_dict = {"role": "assistant", "content": response}
        self.prompt.append(response_dict)
        self.send(text_data=json.dumps({"message": response}))
