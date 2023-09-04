from data import responses


class Bot:

    def __init__(self, client, message, user):
        self.client = client
        self.user = user
        self.message = message


class Help(Bot):

    def __init__(self, client, message, user):
        super().__init__(client, message, user)

    # @client.event
    async def help_command(self):
        await self.message.reply(f"""
            {responses.response_dict["help"]}
            """
                                         )


class Build(Bot):

    def __init__(self, client, message, user):
        super().__init__(client, user, message)

    # @client.event

    async def build_command(self):
        await self.message.reply(f"""
            {responses.response_dict["class_build"]}
            """
                                        )

    # async def build_type_option(self):
    #     await self.message.



