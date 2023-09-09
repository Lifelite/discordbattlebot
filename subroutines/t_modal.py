class TextModal(ui.Modal, title="Build your Character"):

    def __init__(self, c_class):
        super().__init__()
        self.sp_move = ui.TextInput(
            label='Name Your Special Move',
            placeholder='Falcon Punch...'
        )
        self.name = ui.TextInput(
            label='Character Name',
            placeholder='Name your character....'
        )
        self.c_class = c_class

    async def on_submit(self, interaction: discord.Interaction):
        funct = Functions(self.name, self.sp_move, self.c_class)
        funct.toon_upload({interaction.user})

