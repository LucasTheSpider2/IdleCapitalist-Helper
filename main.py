import os
import discord
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Successful log in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  #if message.content.startswith('$$pcalc') and message.author.id != 110463653261623296:
  #  await message.channel.send("You are not authorized to use this bot!")
  if message.content.startswith('$$pcalc'): # and message.author.id == 110463653261623296:
    pPoints = message.content.split("$$pcalc ",1)[1]
    minDict = {
      .05: 10,
      .15: 50,
      .3: 250,
      .5: 750,
      1: 2500
    }
    beforeDict = {
      .05: 10,
      .15: 50,
      .3: 250,
      .5: 750,
      1: 2500
    }
    boughtDict = {
      .05: 0,
      .15: 0,
      .3: 0,
      .5: 0,
      1: 0
    }
    divDict = {
      .05: 0,
      .15: 0,
      .3: 0,
      .5: 0,
      1: 0
    }
    bestToBuy = .05
    pPoints = int(pPoints)
    while pPoints > 0:
      if pPoints - minDict[bestToBuy] < 0:
        divDict[bestToBuy] = 0
        bestToBuy = (max(divDict, key=divDict.get))
        if all(value == 0 for value in divDict.values()):
          break
      elif pPoints - minDict[bestToBuy] >= 0:
        pPoints = pPoints - minDict[bestToBuy]
        minDict[bestToBuy] += beforeDict[bestToBuy]
        boughtDict[bestToBuy] += 1
        for i, v in minDict.items():
          divDict[i] = i/v
        bestToBuy = (max(divDict, key=divDict.get))
    totalMult = round(boughtDict[.05] * .05 + boughtDict[.15] * .15 + boughtDict[.3] * .3 + boughtDict[.5] * .5 + boughtDict[1] + 1, 3)
    await message.channel.send('5% Multipliers: ' + str(boughtDict.get(.05)) + '\n15% Multipliers: ' + str(boughtDict.get(.15)) + '\n30% Multipliers: ' + str(boughtDict.get(.30)) + '\n50% Multipliers: ' + str(boughtDict.get(.50)) + '\n100% Multipliers: ' + str(boughtDict.get(1)) + '\n\nYou will have a ' + str(totalMult) + 'x multiplier with ' + str(pPoints) + ' prestige points left over.')

keep_alive()
client.run(os.environ['TOKEN'])