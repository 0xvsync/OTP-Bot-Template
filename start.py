import sys
import discord, requests, os, time, random, sys
from discord.ext import commands
from Commands.OTPCommands import *

class BotConfig:
    def __init__(self) -> None:
        self.author     = "vSync#7348"
        self.AuthDiscID = 953100704363474954
        self.botToken   = "bot_token"
        self.prefix     = ">"
        self.dbFile     = "db.txt"
        self.Services   = ['PAYPAL','VENMO']
        self.Sensitive_Chars = ['"', '@','#','{','}',';','-','>','<','`','*','=','+','curl','\\']
        try:    self.PhoneLen = int(sys.argv[1])
        except: self.PhoneLen = 10

class Commands:
    client = commands.Bot(command_prefix=">",case_insensitive=True)
    
    @client.command(name="checkplan")
    async def CheckUserPlan (ctx):  await OTPCommands.CheckPlan(ctx)

    @client.command(name="call")
    async def otpSend (ctx, PhoneNumber, Name, Service):    await OTPCommands.SendOTP(ctx, PhoneNumber, Name, Service)
    
    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument): await ctx.send(" Please provide arguments.")
    
if __name__ == '__main__':
    Commands().client.run(BotConfig().botToken)
