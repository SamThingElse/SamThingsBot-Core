import discord

class MyClient(discord.Client):
    async def on_ready(self):
        self.apikey = ''
        print('Logged in as') # Just for Debug
        print(self.user.name) # Just for Debug
        print(self.user.id) # Just for Debug
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        if message.content.startswith('!help'): 
            await message.channel.send('```Hier folgt in Kürze eine (hoffentlich) ausführliche Hilfe-Sektion über alle möglichen Commands...```'.format(message))

    def apitokenreader(self, keyfile):
        '''
        Reads an API-Token from any file. Needs a file path as argument.

        Argument: Filepath as String.
        '''

        with open(keyfile, "r",encoding="UTF-8") as file:
            self.apikey = file.readline()
        return self.apikey

keyfile = "./settings/dc_api_token.key"

client = MyClient()
#client.apikeyreader(keyfile)
client.run(client.apitokenreader(keyfile))