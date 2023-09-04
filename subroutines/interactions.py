from data import responses
from main import client


class Bot(client):

    def __init__(self):
        self.client = client


class Help(Bot):

    def __init__(self):
        super().__init__()
        self.client = client

    @client.event
    async def help_command(self, message):
        await message.channel.send(
            responses.response_dict["help"]
        )

    @client.event
    async def build_command(self, message):
        await message.channel.sent(

        )
