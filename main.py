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
  if message.content.startswith('$$pcalc') and not message.content.startswith('$$pcalc nolimit'): # and message.author.id == 110463653261623296:
    try:
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
        # elif boughtDict[bestToBuy] >= 1001:
          # divDict[bestToBuy] = 0
          # bestToBuy = (max(divDict, key=divDict.get))
          # if all(value == 0 for value in divDict.values()):
            # break
        elif round(boughtDict[.05] * .05 + boughtDict[.15] * .15 + boughtDict[.3] * .3 + boughtDict[.5] * .5 + boughtDict[1] + 1, 3) >= 1000:
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
    except:
      await message.channel.send('Please send a valid number of prestige points. (ex: $$pcalc 100000)')
  elif message.content.startswith('$$pcalc nolimit'): # and message.author.id == 110463653261623296:
    if message.author.id == 110463653261623296:
      try:
        pPoints = message.content.split("$$pcalc nolimit ",1)[1]
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
          # elif boughtDict[bestToBuy] >= 1001:
            # divDict[bestToBuy] = 0
            # bestToBuy = (max(divDict, key=divDict.get))
            # if all(value == 0 for value in divDict.values()):
              # break
          elif pPoints - minDict[bestToBuy] >= 0:
            pPoints = pPoints - minDict[bestToBuy]
            minDict[bestToBuy] += beforeDict[bestToBuy]
            boughtDict[bestToBuy] += 1
            for i, v in minDict.items():
              divDict[i] = i/v
            bestToBuy = (max(divDict, key=divDict.get))
        totalMult = round(boughtDict[.05] * .05 + boughtDict[.15] * .15 + boughtDict[.3] * .3 + boughtDict[.5] * .5 + boughtDict[1] + 1, 3)
        await message.channel.send('5% Multipliers: ' + str(boughtDict.get(.05)) + '\n15% Multipliers: ' + str(boughtDict.get(.15)) + '\n30% Multipliers: ' + str(boughtDict.get(.30)) + '\n50% Multipliers: ' + str(boughtDict.get(.50)) + '\n100% Multipliers: ' + str(boughtDict.get(1)) + '\n\nYou will have a ' + str(totalMult) + 'x multiplier with ' + str(pPoints) + ' prestige points left over.')
      except:
        await message.channel.send('Please send a valid number of prestige points. (ex: $$pcalc 100000)')
    elif message.author.id != 110463653261623296:
              await message.channel.send('You are not authorized to use this command! This command is exclusive for developers and trusted friends!')
  elif message.content.startswith('$$help'):
    await message.channel.send('There are only two commands right now... \n\n$$pcalc (prestige points) - Will calculate the best multipliers to buy with your prestige points. \n$$mcalc (multiplier) - Will calculate the number of prestige points for a specific multiplier.')
  elif message.content.startswith('$$mcalc'): # and message.author.id == 110463653261623296:
    try:
      mult = message.content.split("$$mcalc ",1)[1]
      if float(mult) > 1000.95:
        await message.channel.send('The $$mcalc command is capped to only calculating multipliers of 1000.95x and below!')
      else:
        pPoints = 10000000000000
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
        mult = float(mult)
        while pPoints > 0:
          if round(boughtDict[.05] * .05 + boughtDict[.15] * .15 + boughtDict[.3] * .3 + boughtDict[.5] * .5 + boughtDict[1] + 1, 3) >= mult:
            divDict[bestToBuy] = 0
            bestToBuy = (max(divDict, key=divDict.get))
            if all(value == 0 for value in divDict.values()):
              break
          elif round(boughtDict[.05] * .05 + boughtDict[.15] * .15 + boughtDict[.3] * .3 + boughtDict[.5] * .5 + boughtDict[1] + 1 + bestToBuy, 3) > mult:
            divDict[bestToBuy] = 0
            bestToBuy = (max(divDict, key=divDict.get))
            if all(value == 0 for value in divDict.values()):
              break
          # elif boughtDict[bestToBuy] >= 1001:
            # divDict[bestToBuy] = 0
            # bestToBuy = (max(divDict, key=divDict.get))
            # if all(value == 0 for value in divDict.values()):
              # break
          elif pPoints - minDict[bestToBuy] >= 0:
            pPoints = pPoints - minDict[bestToBuy]
            minDict[bestToBuy] += beforeDict[bestToBuy]
            boughtDict[bestToBuy] += 1
            for i, v in minDict.items():
              divDict[i] = i/v
            bestToBuy = (max(divDict, key=divDict.get))
        totalMult = round(boughtDict[.05] * .05 + boughtDict[.15] * .15 + boughtDict[.3] * .3 + boughtDict[.5] * .5 + boughtDict[1] + 1, 3)
        await message.channel.send('5% Multipliers: ' + str(boughtDict.get(.05)) + '\n15% Multipliers: ' + str(boughtDict.get(.15)) + '\n30% Multipliers: ' + str(boughtDict.get(.30)) + '\n50% Multipliers: ' + str(boughtDict.get(.50)) + '\n100% Multipliers: ' + str(boughtDict.get(1)) + '\n\nYou will need ' + str(10000000000000 - pPoints) + ' prestige points to get a ' + str(totalMult) + 'x multiplier.')
    except:
      await message.channel.send('Please send a valid multiplier. (ex: $$mcalc 1000)')

keep_alive()
client.run(os.environ['TOKEN'])