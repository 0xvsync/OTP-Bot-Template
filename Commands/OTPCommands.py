from Commands.database import DataBase
from start import BotConfig
import requests,discord
from datetime import datetime
from Commands.database import DataBase
from  Commands.algorithms import alg

class OTPCommands:
    async def CheckPlan(ctx):
        id = ctx.author.id
        Plan = {
            "MemberShip"  : "",
            "UserName"    : id,
            "Expiry Date" : ""
        }
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        try:
            id = (int(id))
            if DataBase.dbChecks(id) == True:
                # Get Membership
                GetPlan = DataBase.PlanCheck(id)
                if GetPlan == False:    Plan['MemberShip'] = 'Error with loading Membership.'
                else:   Plan['MemberShip'] = GetPlan

                #Get Expiry
                GetExpiry = DataBase.ExpiryCheck(id)
                if GetExpiry == False:  Plan['Expiry Date'] = 'Error with loading Expiry'
                else:   Plan['Expiry Date'] = GetExpiry
                embed = discord.Embed(title="Plan", description=f"Plan for {Plan['UserName']}")
                embed.add_field(name="Info",value=f"Membership  : {Plan['MemberShip']}\nExpires   : {Plan['Expiry Date']}")
                #embed.set_footer(name=f"{current_time}")
                await ctx.send(embed=embed)
                return
        except Exception as Error:
            await ctx.send(" Sorry, but your user ID is invalid. [{}]".format(Error))
            return
        
    async def SendOTP(ctx, PhoneNumber, Name, Service):
        try:
            if len(PhoneNumber) < BotConfig().PhoneLen:
                await ctx.send(" Please enter a valid phone number.")
                return
            elif len(PhoneNumber) >= 12:
                await ctx.send(" Please enter a valid phone number.")
                return
        except:
            await ctx.send(" Please enter a valid phone number.")
            return
        if (str(Service.upper())) not in BotConfig().Services:
            await ctx.send(" Sorry, but the service you've entered is invalid.")
            return
        if "+" in PhoneNumber:  PhoneNumber = PhoneNumber.strip("+")
        try:    PhoneNumber = (int(PhoneNumber))
        except:
            await ctx.send(" Please enter a valid phone number . ")
            return
        for x in Name:
            for f in range(0, len(BotConfig().Sensitive_Chars)):
                if x.upper() ==  BotConfig().Sensitive_Chars[f].upper():
                    await ctx.send(" Please us a appropriate name . ")
                    return
                else:   pass
        # SEND A REQUEST TO API HERE ! 
        # for here make a new file which will listen for GET requests from the API to send more embeds with the status of the call, use flask.
        if alg.algo(Service) == False:
            await ctx.send(" Please try again as the OTP bot is under load.")
            return
        else:   alg.algo(Service)
        return
