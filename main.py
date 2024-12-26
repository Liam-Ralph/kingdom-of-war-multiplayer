#IMPORTS
import os
import time
import random

#GLOBAL VARIABLES
#Player 1
player1=0
player1ExtraSoldiers=0
player1Countries=[]
player1StartingCountry=0
player1TotalArmies=0

#Player 2
player2=0
player2ExtraSoldiers=0
player2Countries=[]
player2StartingCountry=0
player2TotalArmies=0

#Player 3
player3=0
player3ExtraSoldiers=0
player3Countries=[]
player3StartingCountry=0
player3TotalArmies=0

#Player 4
player4=0
player4ExtraSoldiers=0
player4Countries=[]
player4StartingCountry=0
player4TotalArmies=0

#Countries
countriesMorditir=["Moriatir", "Ardtir", "Desich", "Fadtir"]
countriesSentenos=["Magnollis", "Emptos", "Teracies", "Teramus"]
countriesMonelle=["Uchelle", "Dwylle", "Iselle", "Canolle"]
countriesKyorchi=["Kitashi", "Kitazai", "Nanseshu", "Nantshu"]
countriesSurlugar=["Desiar", "Esteplana", "Arenar", "Cenrodad"]
countries=[]
countries.extend(countriesMorditir)
countries.extend(countriesSentenos)
countries.extend(countriesMonelle)
countries.extend(countriesKyorchi)
countries.extend(countriesSurlugar)
neutralCountries=[]
neutralCountries.extend(countries)

#Armies
armiesMoriatir=750
armiesArdtir=250
armiesDesich=500
armiesFadtir=500

armiesMagnollis=1000
armiesEmptos=250
armiesTeracies=500
armiesTeramus=500

armiesUchelle=750
armiesDwylle=750
armiesIselle=750
armiesCanolle=1000

armiesKitashi=750
armiesKitazai=500
armiesNanseshu=500
armiesNantshu=500

armiesDesiar=250
armiesEsteplana=500
armiesArenar=750
armiesCenrodad=500

#Adjacent Countries
adjacentMoriatir=["Ardtir", "Fadtir", "Desich"]
adjacentArdtir=["Moriatir"]
adjacentDesich=["Moriatir", "Fadtir", "Uchelle", "Iselle", "Kitashi"]
adjacentFadtir=["Moriatir", "Desich", "Teracies", "Uchelle"]

adjacentMagnollis=["Teracies", "Emptos", "Teramus"]
adjacentEmptos=["Magnollis"]
adjacentTeracies=["Fadtir", "Uchelle", "Dwylle", "Magnollis"]
adjacentTeramus=["Magnollis", "Desiar", "Esteplana"]

adjacentUchelle=["Desich", "Fadtir", "Iselle", "Teracies", "Dwylle", "Canolle"]
adjacentDwylle=["Uchelle", "Canolle", "Iselle", "Desiar", "Teracies"]
adjacentIselle=["Kitazai", "Nantshu", "Uchelle", "Canolle", "Dwylle", "Desich"]
adjacentCanolle=["Uchelle", "Iselle", "Dwylle"]

adjacentKitashi=["Desich", "Nanseshu"]
adjacentKitazai=["Nantshu", "Iselle"]
adjacentNanseshu=["Kitashi", "Nantshu"]
adjacentNantshu=["Nanseshu", "Kitazai", "Iselle", "Arenar"]

adjacentDesiar=["Dwylle", "Teramus", "Esteplana", "Cenrodad"]
adjacentEsteplana=["Teramus", "Desiar", "Cenrodad"]
adjacentArenar=["Nantshu", "Cenrodad"]
adjacentCenrodad=["Arenar", "Desiar", "Esteplana"]

adjacentCountriesDict={"Moriatir":adjacentMoriatir, "Ardtir":adjacentArdtir,
					   "Desich":adjacentDesich, "Fadtir":adjacentFadtir,
					   "Magnollis":adjacentMagnollis, "Emptos":adjacentEmptos,
					   "Teracies":adjacentTeracies, "Teramus":adjacentTeramus,
					   "Uchelle":adjacentUchelle, "Dwylle":adjacentDwylle,
					   "Iselle":adjacentIselle, "Canolle":adjacentCanolle,
					   "Kitashi":adjacentKitashi, "Kitazai":adjacentKitazai,
					   "Nanseshu":adjacentNanseshu, "Nantshu":adjacentNantshu,
					   "Desiar":adjacentDesiar, "Esteplana":adjacentEsteplana,
					   "Arenar":adjacentArenar, "Cenrodad":adjacentCenrodad}

#Special Event Lists
heroCountries=[]
heroCountries.extend(countries)
rebellionCountries=[]
rebellionCountries.extend(countries)
eruptionCountries=["Ardtir", "Desich", "Teracies", "Emptos",
				   "Dwylle", "Kitashi", "Arenar", "Kitazai"]
revolutionCountries=[]
revolutionCountries.extend(countries)
refugeesCountries=[]
refugeesCountries.extend(countries)

#Death Total
deathTotal=0

#Miscellaneous
neutralTotalArmies=0
turn=0

#FUNCTIONS
def sanitisedInput(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    expected = " or ".join((
                        ", ".join(str(x) for x in range_[:-1]),
                        str(range_[-1])
                    ))
                    print(template.format(expected))
        else:
            return ui


def clearScreen(): 
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

def intro():
	bannerFile=open("banner.txt", "r")
	if bannerFile.mode=="r":
		banner=bannerFile.read()
		print(banner)
	time.sleep(1.5)
	clearScreen()
	print(banner)
	print()
	print("Tip: Invade with 0 armies to stall...")
	time.sleep(1.5)
	clearScreen()
	print(banner)
	print()
	print("Choose your country wisely...")
	time.sleep(1.5)
	clearScreen()
	print(banner)
	print()
	print("Contact me with questions or comments.")
	time.sleep(1.5)
	clearScreen()

	print("Would you like an introduction to the game?")
	print("Recommended for first-time players.")
	print("Yes (1)")
	print("No (0)")
	answer=sanitisedInput("", int, range_=(0, 1))
	if(answer==1):
		clearScreen()
		introduction()
	clearScreen()
    
def introduction():
	print("""Welcome to Kingdom of War - Multiplayer!
This is a strategy-based war game,
similar to my other game, 
Kingdom of War.""")
	input("Press Enter")
	clearScreen()

	print("Here is the map:")
	print()
	print(map)
	print("Morditir, Sentenos - Monelle - Kyorchi - Surlugar")
	input("Press Enter")
	clearScreen()

	print("""As you can see, there are
some words at the bottom. These are the
names of the regions on this map. There
are also these symbols ^ , which are
mountains. Mountain ranges are borders
your armies cannot cross.""")
	input("Press Enter")
	clearScreen()

	print("""Goal of the Game

Each and every one of you has a singular goal:
Be the last one standing.
Eliminate every other player by
conquering all of their countries.""")
	input("Press Enter")
	clearScreen()

	print("""Your Opponent(s)

This is a LOCAL multiplayer game.
You cannot play people on the other
side of the world. You can play
yourself if you have no one else to
play with. There can be 2-4 players
in this game.""")
	input("Press Enter")
	clearScreen()

	print("""Turns
		  
During their turn, a player can
gain soldiers, deploy said soldiers,
and invade other countries.""")
	input("Press Enter")
	clearScreen()

	print("""Gaining Soldiers

• 100 soldiers/country each turn.
• 800 for eliminating another player
or capturing the last neutral country.
• You can also get soldiers for
controlling every country in a region.
Here are the regions""")
	input("Press Enter")
	clearScreen()

	print("Morditir")
	morditirFile=open("Regions/Morditir.txt", "r")
	if morditirFile.mode=="r":
		morditir=morditirFile.read()
		print(morditir)
		print("750 soldiers/turn")
	input("Press Enter")
	clearScreen()

	print("Sentenos")
	sentenosFile=open("Regions/Sentenos.txt", "r")
	if sentenosFile.mode=="r":
		sentenos=sentenosFile.read()
		print(sentenos)
		print("850 soldiers/turn")
	input("Press Enter")
	clearScreen()

	print("Monelle")
	monelleFile=open("Regions/Monelle.txt", "r")
	if monelleFile.mode=="r":
		monelle=monelleFile.read()
		print(monelle)
		print("1200 soldiers/turn")
	input("Press Enter")
	clearScreen()

	print("Kyorchi")
	kyorchiFile=open("Regions/Kyorchi.txt", "r")
	if kyorchiFile.mode=="r":
		kyorchi=kyorchiFile.read()
		print(kyorchi)
		print("850 soldiers/turn")
	input("Press Enter")
	clearScreen()

	print("Surlugar")
	surlugarFile=open("Regions/Surlugar.txt", "r")
	if surlugarFile.mode=="r":
		surlugar=surlugarFile.read()
		print(surlugar)
		print("750 soldiers/turn")
	input("Press Enter")
	clearScreen()

	print("""Invading Countries

This is how you win and control new
countries. You can also invade your
own countries to move your soldiers.
**Note, you only have a 100% chance
of success if your army is at
least 50% larger than the one you
are invading.
Ex.
150 soldiers invading 100 - Guaranteed success
130 soldiers invading 100 - May win may not
90 soldiers invading 100 - Cannot win""")
	input("Press Enter")
	clearScreen()

	print("""Special Events
		  
There are also certain special
events that can take place after
the opponent's turn.""")
	input("Press Enter")
	clearScreen()

	print("""That's all!
Please contact the creator
Liam Ralph
with any questions or suggestions.
Have fun playing!""")
	input("Press Enter")

def createPlayers(numPlayers=None):
	global player1
	global player1StartingCountry
	global player2
	global player2StartingCountry
	global player3
	global player3StartingCountry
	global player4
	global player4StartingCountry
	global armiesMoriatir
	global armiesArdtir
	global armiesDesich
	global armiesFadtir
	global armiesMagnollis
	global armiesEmptos
	global armiesTeracies
	global armiesTeramus
	global armiesUchelle
	global armiesDwylle
	global armiesCanolle
	global armiesIselle
	global armiesKitashi
	global armiesKitazai
	global armiesNanseshu
	global armiesNantshu
	global armiesDesiar
	global armiesEsteplana
	global armiesArenar
	global armiesCenrodad

	armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
				"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
				"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
				"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
				"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
	startingCountryOptions=[]
	startingCountryOptions.extend(countries)
	print("When choosing a country, you cannot")
	print("choose a country beside another player's")
	print("country.")
	input("Press Enter")
	clearScreen()

	print(map)
	player1=input("Player 1 (name): ")
	player1StartingCountry=sanitisedInput("Choose your country: ", str, range_=startingCountryOptions)
	startingCountryOptions.remove(player1StartingCountry)
	for country in adjacentCountriesDict[player1StartingCountry]:
		if(country in startingCountryOptions):
			startingCountryOptions.remove(country)
	player1Countries.append(player1StartingCountry)
	neutralCountries.remove(player1StartingCountry)
	armiesDict[player1StartingCountry]=500
	clearScreen()

	print(map)
	player2=input("Player 2: ")
	player2StartingCountry=sanitisedInput("Choose your country: ", str, range_=startingCountryOptions)
	startingCountryOptions.remove(player2StartingCountry)
	for country in adjacentCountriesDict[player2StartingCountry]:
		if(country in startingCountryOptions):
			startingCountryOptions.remove(country)
	player2Countries.append(player2StartingCountry)
	neutralCountries.remove(player2StartingCountry)
	armiesDict[player2StartingCountry]=500
	clearScreen()
	
	if(numPlayers>=3):
		print(map)
		player3=input("Player 3: ")
		player3StartingCountry=sanitisedInput("Choose your country: ", str, range_=startingCountryOptions)
		startingCountryOptions.remove(player3StartingCountry)
		for country in adjacentCountriesDict[player3StartingCountry]:
			if(country in startingCountryOptions):
				startingCountryOptions.remove(country)
		player3Countries.append(player3StartingCountry)
		neutralCountries.remove(player3StartingCountry)
		armiesDict[player3StartingCountry]=500
		clearScreen()
	
	if(numPlayers==4):
		print(map)
		player4=input("Player 4: ")
		player4StartingCountry=sanitisedInput("Choose your country: ", str, range_=startingCountryOptions)
		startingCountryOptions.remove(player4StartingCountry)
		for country in adjacentCountriesDict[player3StartingCountry]:
			if(country in startingCountryOptions):
				startingCountryOptions.remove(country)
		player4Countries.append(player4StartingCountry)
		neutralCountries.remove(player4StartingCountry)
		armiesDict[player4StartingCountry]=500
		clearScreen()

	armiesMoriatir=armiesDict["Moriatir"]
	armiesArdtir=armiesDict["Ardtir"]
	armiesFadtir=armiesDict["Fadtir"]
	armiesDesich=armiesDict["Desich"]
	armiesMagnollis=armiesDict["Magnollis"]
	armiesEmptos=armiesDict["Emptos"]
	armiesTeracies=armiesDict["Teracies"]
	armiesTeramus=armiesDict["Teramus"]
	armiesUchelle=armiesDict["Uchelle"]
	armiesCanolle=armiesDict["Canolle"]
	armiesIselle=armiesDict["Iselle"]
	armiesDwylle=armiesDict["Dwylle"]
	armiesKitashi=armiesDict["Kitashi"]
	armiesNanseshu=armiesDict["Nanseshu"]
	armiesNantshu=armiesDict["Nantshu"]
	armiesKitazai=armiesDict["Kitazai"]
	armiesDesiar=armiesDict["Desiar"]
	armiesEsteplana=armiesDict["Esteplana"]
	armiesCenrodad=armiesDict["Cenrodad"]
	armiesArenar=armiesDict["Arenar"]

def printMap():
	global mapPiece1
	global mapPiece2
	global mapPiece3
	global mapPiece4
	global mapPiece5
	global mapPiece6
	global mapPiece7
	global mapPiece8
	global mapPiece9
	global mapPiece10
	global mapPiece11
	global mapPiece12
	global mapPiece13
	global mapPiece14
	global mapPiece15
	global mapPiece16
	global mapPiece17
	global mapPiece18
	global mapPiece19
	global mapPiece20
	global mapPiece21
	global mapPiece22
	global mapPiece23
	global mapPiece24
	global mapPiece25
	global mapPiece26
	global mapPiece27
	global mapPiece28
	global mapPiece29
	global mapPiece30
	global mapPiece31
	global mapPiece32
	global mapPiece33
	global mapPiece34
	global mapPiece35
	global mapPiece36
	global mapPiece37
	global mapPiece38
	global mapPiece39
	global mapPiece40
	global mapPiece41
	global mapPiece42
	global armiesMoriatir
	global armiesArdtir
	global armiesDesich
	global armiesFadtir
	global armiesMagnollis
	global armiesEmptos
	global armiesTeracies
	global armiesTeramus
	global armiesUchelle
	global armiesDwylle
	global armiesCanolle
	global armiesIselle
	global armiesKitashi
	global armiesKitazai
	global armiesNanseshu
	global armiesNantshu
	global armiesDesiar
	global armiesEsteplana
	global armiesArenar
	global armiesCenrodad
	
	print("\033[0;37;49m", mapPiece1, sep="", end="")
	if("Ardtir" in player1Countries):
		print("\033[0;31;49mArdtir", end="")
	elif("Ardtir" in player2Countries):
		print("\033[0;32;49mArdtir", end="")
	elif("Ardtir" in neutralCountries):
		print("\033[0;37;49mArdtir", end="")
	elif("Ardtir" in player3Countries):
		print("\033[0;34;49mArdtir", end="")
	elif("Ardtir" in player4Countries):
		print("\033[0;35;49mArdtir", end="")

	print("\033[0;37;49m", mapPiece2, sep="", end="")
	if(armiesArdtir<100):
		print(" ", end="")
	if("Ardtir" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Ardtir" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Ardtir" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Ardtir" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Ardtir" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesArdtir, end="")
	if(armiesArdtir<1000):
		print(" ", end="")
	if(armiesArdtir<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece3, sep="", end="")
	if("Moriatir" in player1Countries):
		print("\033[0;31;49mMoriatir", end="")
	elif("Moriatir" in player2Countries):
		print("\033[0;32;49mMoriatir", end="")
	elif("Moriatir" in neutralCountries):
		print("\033[0;37;49mMoriatir", end="")
	elif("Moriatir" in player3Countries):
		print("\033[0;34;49mMoriatir", end="")
	elif("Moriatir" in player4Countries):
		print("\033[0;35;49mMoriatir", end="")

	print("\033[0;37;49m", mapPiece4, sep="", end="")
	if("Magnollis" in player1Countries):
		print("\033[0;31;49mMagnollis", end="")
	elif("Magnollis" in player2Countries):
		print("\033[0;32;49mMagnollis", end="")
	elif("Magnollis" in neutralCountries):
		print("\033[0;37;49mMagnollis", end="")
	elif("Magnollis" in player3Countries):
		print("\033[0;34;49mMagnollis", end="")
	elif("Magnollis" in player4Countries):
		print("\033[0;35;49mMagnollis", end="")

	print("\033[0;37;49m", mapPiece5, sep="", end="")
	if(armiesMoriatir<100):
		print(" ", end="")
	if("Moriatir" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Moriatir" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Moriatir" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Moriatir" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Moriatir" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesMoriatir, end="")
	if(armiesMoriatir<1000):
		print(" ", end="")
	if(armiesMoriatir<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece6, sep="", end="")
	if(armiesMagnollis<100):
		print(" ", end="")
	if("Magnollis" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Magnollis" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Magnollis" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Magnollis" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Magnollis" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesMagnollis, end="")
	if(armiesMagnollis<1000):
		print(" ", end="")
	if(armiesMagnollis<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece7, sep="", end="")
	if("Emptos" in player1Countries):
		print("\033[0;31;49mEmptos", end="")
	elif("Emptos" in player2Countries):
		print("\033[0;32;49mEmptos", end="")
	elif("Emptos" in neutralCountries):
		print("\033[0;37;49mEmptos", end="")
	elif("Emptos" in player3Countries):
		print("\033[0;34;49mEmptos", end="")
	elif("Emptos" in player4Countries):
		print("\033[0;35;49mEmptos", end="")

	print("\033[0;37;49m", mapPiece8, sep="", end="")
	if(armiesEmptos<100):
		print(" ", end="")
	if("Emptos" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Emptos" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Emptos" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Emptos" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Emptos" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesEmptos, end="")
	if(armiesEmptos<1000):
		print(" ", end="")
	if(armiesEmptos<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece9, sep="", end="")
	if("Fadtir" in player1Countries):
		print("\033[0;31;49mFadtir", end="")
	elif("Fadtir" in player2Countries):
		print("\033[0;32;49mFadtir", end="")
	elif("Fadtir" in neutralCountries):
		print("\033[0;37;49mFadtir", end="")
	elif("Fadtir" in player3Countries):
		print("\033[0;34;49mFadtir", end="")
	elif("Fadtir" in player4Countries):
		print("\033[0;35;49mFadtir", end="")

	print("\033[0;37;49m", mapPiece10, sep="", end="")
	if(armiesFadtir<100):
		print(" ", end="")
	if("Fadtir" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Fadtir" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Fadtir" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Fadtir" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Fadtir" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesFadtir, end="")
	if(armiesFadtir<1000):
		print(" ", end="")
	if(armiesFadtir<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece11, sep="", end="")
	if("Teracies" in player1Countries):
		print("\033[0;31;49mTeracies", end="")
	elif("Teracies" in player2Countries):
		print("\033[0;32;49mTeracies", end="")
	elif("Teracies" in neutralCountries):
		print("\033[0;37;49mTeracies", end="")
	elif("Teracies" in player3Countries):
		print("\033[0;34;49mTeracies", end="")
	elif("Teracies" in player4Countries):
		print("\033[0;35;49mTeracies", end="")

	print("\033[0;37;49m", mapPiece12, sep="", end="")
	if("Desich" in player1Countries):
		print("\033[0;31;49mDesich", end="")
	elif("Desich" in player2Countries):
		print("\033[0;32;49mDesich", end="")
	elif("Desich" in neutralCountries):
		print("\033[0;37;49mDesich", end="")
	elif("Desich" in player3Countries):
		print("\033[0;34;49mDesich", end="")
	elif("Desich" in player4Countries):
		print("\033[0;35;49mDesich", end="")

	print("\033[0;37;49m", mapPiece13, sep="", end="")
	if(armiesTeracies<100):
		print(" ", end="")
	if("Teracies" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Teracies" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Teracies" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Teracies" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Teracies" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesTeracies, end="")
	if(armiesTeracies<1000):
		print(" ", end="")
	if(armiesTeracies<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece14, sep="", end="")
	if(armiesDesich<100):
		print(" ", end="")
	if("Desich" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Desich" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Desich" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Desich" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Desich" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesDesich, end="")
	if(armiesDesich<1000):
		print(" ", end="")
	if(armiesDesich<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece15, sep="", end="")
	if("Uchelle" in player1Countries):
		print("\033[0;31;49mUchelle", end="")
	elif("Uchelle" in player2Countries):
		print("\033[0;32;49mUchelle", end="")
	elif("Uchelle" in neutralCountries):
		print("\033[0;37;49mUchelle", end="")
	elif("Uchelle" in player3Countries):
		print("\033[0;34;49mUchelle", end="")
	elif("Uchelle" in player4Countries):
		print("\033[0;35;49mUchelle", end="")

	print("\033[0;37;49m", mapPiece16, sep="", end="")
	if("Teramus" in player1Countries):
		print("\033[0;31;49mTeramus", end="")
	elif("Teramus" in player2Countries):
		print("\033[0;32;49mTeramus", end="")
	elif("Teramus" in neutralCountries):
		print("\033[0;37;49mTeramus", end="")
	elif("Teramus" in player3Countries):
		print("\033[0;34;49mTeramus", end="")
	elif("Teramus" in player4Countries):
		print("\033[0;35;49mTeramus", end="")

	print("\033[0;37;49m", mapPiece17, sep="", end="")
	if(armiesUchelle<100):
		print(" ", end="")
	if("Uchelle" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Uchelle" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Uchelle" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Uchelle" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Uchelle" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesUchelle, end="")
	if(armiesUchelle<1000):
		print(" ", end="")
	if(armiesUchelle<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece18, sep="", end="")
	if("Dwylle" in player1Countries):
		print("\033[0;31;49mDwylle", end="")
	elif("Dwylle" in player2Countries):
		print("\033[0;32;49mDwylle", end="")
	elif("Dwylle" in neutralCountries):
		print("\033[0;37;49mDwylle", end="")
	elif("Dwylle" in player3Countries):
		print("\033[0;34;49mDwylle", end="")
	elif("Dwylle" in player4Countries):
		print("\033[0;35;49mDwylle", end="")

	print("\033[0;37;49m", mapPiece19, sep="", end="")
	if(armiesTeramus<100):
		print(" ", end="")
	if("Teramus" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Teramus" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Teramus" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Teramus" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Teramus" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesTeramus, end="")
	if(armiesTeramus<1000):
		print(" ", end="")
	if(armiesTeramus<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece20, sep="", end="")
	if(armiesDwylle<100):
		print(" ", end="")
	if("Dwylle" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Dwylle" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Dwylle" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Dwylle" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Dwylle" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesDwylle, end="")
	if(armiesDwylle<1000):
		print(" ", end="")
	if(armiesDwylle<10):
		print(" ", end="")
	
	print("\033[0;37;49m", mapPiece21, sep="", end="")
	if("Iselle" in player1Countries):
		print("\033[0;31;49mIselle", end="")
	elif("Iselle" in player2Countries):
		print("\033[0;32;49mIselle", end="")
	elif("Iselle" in neutralCountries):
		print("\033[0;37;49mIselle", end="")
	elif("Iselle" in player3Countries):
		print("\033[0;34;49mIselle", end="")
	elif("Iselle" in player4Countries):
		print("\033[0;35;49mIselle", end="")

	print("\033[0;37;49m", mapPiece22, sep="", end="")
	if("Canolle" in player1Countries):
		print("\033[0;31;49mCanolle", end="")
	elif("Canolle" in player2Countries):
		print("\033[0;32;49mCanolle", end="")
	elif("Canolle" in neutralCountries):
		print("\033[0;37;49mCanolle", end="")
	elif("Canolle" in player3Countries):
		print("\033[0;34;49mCanolle", end="")
	elif("Canolle" in player4Countries):
		print("\033[0;35;49mCanolle", end="")

	print("\033[0;37;49m", mapPiece23, sep="", end="")
	if("Kitashi" in player1Countries):
		print("\033[0;31;49mKitashi", end="")
	elif("Kitashi" in player2Countries):
		print("\033[0;32;49mKitashi", end="")
	elif("Kitashi" in neutralCountries):
		print("\033[0;37;49mKitashi", end="")
	elif("Kitashi" in player3Countries):
		print("\033[0;34;49mKitashi", end="")
	elif("Kitashi" in player4Countries):
		print("\033[0;35;49mKitashi", end="")

	print("\033[0;37;49m", mapPiece24, sep="", end="")
	if(armiesIselle<100):
		print(" ", end="")
	if("Iselle" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Iselle" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Iselle" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Iselle" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Iselle" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesIselle, end="")
	if(armiesIselle<1000):
		print(" ", end="")
	if(armiesIselle<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece25, sep="", end="")
	if(armiesCanolle<100):
		print(" ", end="")
	if("Canolle" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Canolle" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Canolle" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Canolle" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Canolle" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesCanolle, end="")
	if(armiesCanolle<1000):
		print(" ", end="")
	if(armiesCanolle<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece26, sep="", end="")
	if("Esteplana" in player1Countries):
		print("\033[0;31;49mEsteplana", end="")
	elif("Esteplana" in player2Countries):
		print("\033[0;32;49mEsteplana", end="")
	elif("Esteplana" in neutralCountries):
		print("\033[0;37;49mEsteplana", end="")
	elif("Esteplana" in player3Countries):
		print("\033[0;34;49mEsteplana", end="")
	elif("Esteplana" in player4Countries):
		print("\033[0;35;49mEsteplana", end="")

	print("\033[0;37;49m", mapPiece27, sep="", end="")
	if(armiesKitashi<100):
		print(" ", end="")
	if("Kitashi" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Kitashi" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Kitashi" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Kitashi" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Kitashi" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesKitashi, end="")
	if(armiesKitashi<1000):
		print(" ", end="")
	if(armiesKitashi<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece28, sep="", end="")
	if(armiesEsteplana<100):
		print(" ", end="")
	if("Esteplana" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Esteplana" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Esteplana" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Esteplana" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Esteplana" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesEsteplana, end="")
	if(armiesEsteplana<1000):
		print(" ", end="")
	if(armiesEsteplana<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece29, sep="", end="")
	if("Kitazai" in player1Countries):
		print("\033[0;31;49mKitazai", end="")
	elif("Kitazai" in player2Countries):
		print("\033[0;32;49mKitazai", end="")
	elif("Kitazai" in neutralCountries):
		print("\033[0;37;49mKitazai", end="")
	elif("Kitazai" in player3Countries):
		print("\033[0;34;49mKitazai", end="")
	elif("Kitazai" in player4Countries):
		print("\033[0;35;49mKitazai", end="")

	print("\033[0;37;49m", mapPiece30, sep="", end="")
	if("Desiar" in player1Countries):
		print("\033[0;31;49mDesiar", end="")
	elif("Desiar" in player2Countries):
		print("\033[0;32;49mDesiar", end="")
	elif("Desiar" in neutralCountries):
		print("\033[0;37;49mDesiar", end="")
	elif("Desiar" in player3Countries):
		print("\033[0;34;49mDesiar", end="")
	elif("Desiar" in player4Countries):
		print("\033[0;35;49mDesiar", end="")

	print("\033[0;37;49m", mapPiece31, sep="", end="")
	if(armiesKitazai<100):
		print(" ", end="")
	if("Kitazai" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Kitazai" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Kitazai" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Kitazai" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Kitazai" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesKitazai, end="")
	if(armiesKitazai<1000):
		print(" ", end="")
	if(armiesKitazai<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece32, sep="", end="")
	if(armiesDesiar<100):
		print(" ", end="")
	if("Desiar" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Desiar" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Desiar" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Desiar" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Desiar" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesDesiar, end="")
	if(armiesDesiar<1000):
		print(" ", end="")
	if(armiesDesiar<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece33, sep="", end="")
	if("Nanseshu" in player1Countries):
		print("\033[0;31;49mNanseshu", end="")
	elif("Nanseshu" in player2Countries):
		print("\033[0;32;49mNanseshu", end="")
	elif("Nanseshu" in neutralCountries):
		print("\033[0;37;49mNanseshu", end="")
	elif("Nanseshu" in player3Countries):
		print("\033[0;34;49mNanseshu", end="")
	elif("Nanseshu" in player4Countries):
		print("\033[0;35;49mNanseshu", end="")

	print("\033[0;37;49m", mapPiece34, sep="", end="")
	if("Cenrodad" in player1Countries):
		print("\033[0;31;49mCenrodad", end="")
	elif("Cenrodad" in player2Countries):
		print("\033[0;32;49mCenrodad", end="")
	elif("Cenrodad" in neutralCountries):
		print("\033[0;37;49mCenrodad", end="")
	elif("Cenrodad" in player3Countries):
		print("\033[0;34;49mCenrodad", end="")
	elif("Cenrodad" in player4Countries):
		print("\033[0;35;49mCenrodad", end="")

	print("\033[0;37;49m", mapPiece35, sep="", end="")
	if(armiesNanseshu<100):
		print(" ", end="")
	if("Nanseshu" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Nanseshu" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Nanseshu" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Nanseshu" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Nanseshu" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesNanseshu, end="")
	if(armiesNanseshu<1000):
		print(" ", end="")
	if(armiesNanseshu<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece36, sep="", end="")
	if("Nantshu" in player1Countries):
		print("\033[0;31;49mNantshu", end="")
	elif("Nantshu" in player2Countries):
		print("\033[0;32;49mNantshu", end="")
	elif("Nantshu" in neutralCountries):
		print("\033[0;37;49mNantshu", end="")
	elif("Nantshu" in player3Countries):
		print("\033[0;34;49mNantshu", end="")
	elif("Nantshu" in player4Countries):
		print("\033[0;35;49mNantshu", end="")

	print("\033[0;37;49m", mapPiece37, sep="", end="")
	if("Arenar" in player1Countries):
		print("\033[0;31;49mArenar", end="")
	elif("Arenar" in player2Countries):
		print("\033[0;32;49mArenar", end="")
	elif("Arenar" in neutralCountries):
		print("\033[0;37;49mArenar", end="")
	elif("Arenar" in player3Countries):
		print("\033[0;34;49mArenar", end="")
	elif("Arenar" in player4Countries):
		print("\033[0;35;49mArenar", end="")

	print("\033[0;37;49m", mapPiece38, sep="", end="")
	if(armiesCenrodad<100):
		print(" ", end="")
	if("Cenrodad" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Cenrodad" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Cenrodad" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Cenrodad" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Cenrodad" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesCenrodad, end="")
	if(armiesCenrodad<1000):
		print(" ", end="")
	if(armiesCenrodad<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece39, sep="", end="")
	if(armiesNantshu<100):
		print(" ", end="")
	if("Nantshu" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Nantshu" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Nantshu" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Nantshu" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Nantshu" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesNantshu, end="")
	if(armiesNantshu<1000):
		print(" ", end="")
	if(armiesNantshu<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece40, sep="", end="")
	if(armiesArenar<100):
		print(" ", end="")
	if("Arenar" in player1Countries):
		print("\033[0;31;49m", end="")
	elif("Arenar" in player2Countries):
		print("\033[0;32;49m", end="")
	elif("Arenar" in neutralCountries):
		print("\033[0;37;49m", end="")
	elif("Arenar" in player3Countries):
		print("\033[0;34;49m", end="")
	elif("Arenar" in player4Countries):
		print("\033[0;35;49m", end="")
	print(armiesArenar, end="")
	if(armiesArenar<1000):
		print(" ", end="")
	if(armiesArenar<10):
		print(" ", end="")

	print("\033[0;37;49m", mapPiece41, sep="")

def loadMapPieces():
	mapPiece1File=open("Map Pieces 1-9/mapPiece1.txt", "r")
	if mapPiece1File.mode=="r":
		global mapPiece1
		mapPiece1=mapPiece1File.read()
	mapPiece2File=open("Map Pieces 1-9/mapPiece2.txt", "r")
	if mapPiece2File.mode=="r":
		global mapPiece2
		mapPiece2=mapPiece2File.read()
	mapPiece3File=open("Map Pieces 1-9/mapPiece3.txt", "r")
	if mapPiece3File.mode=="r":
		global mapPiece3
		mapPiece3=mapPiece3File.read()
	mapPiece4File=open("Map Pieces 1-9/mapPiece4.txt", "r")
	if mapPiece4File.mode=="r":
		global mapPiece4
		mapPiece4=mapPiece4File.read()
	mapPiece5File=open("Map Pieces 1-9/mapPiece5.txt", "r")
	if mapPiece5File.mode=="r":
		global mapPiece5
		mapPiece5=mapPiece5File.read()
	mapPiece6File=open("Map Pieces 1-9/mapPiece6.txt", "r")
	if mapPiece6File.mode=="r":
		global mapPiece6
		mapPiece6=mapPiece6File.read()
	mapPiece7File=open("Map Pieces 1-9/mapPiece7.txt", "r")
	if mapPiece7File.mode=="r":
		global mapPiece7
		mapPiece7=mapPiece7File.read()
	mapPiece8File=open("Map Pieces 1-9/mapPiece8.txt", "r")
	if mapPiece8File.mode=="r":
		global mapPiece8
		mapPiece8=mapPiece8File.read()
	mapPiece9File=open("Map Pieces 1-9/mapPiece9.txt", "r")
	if mapPiece9File.mode=="r":
		global mapPiece9
		mapPiece9=mapPiece9File.read()

	mapPiece10File=open("Map Pieces 10-19/mapPiece10.txt", "r")
	if mapPiece10File.mode=="r":
		global mapPiece10
		mapPiece10=mapPiece10File.read()
	mapPiece11File=open("Map Pieces 10-19/mapPiece11.txt", "r")
	if mapPiece11File.mode=="r":
		global mapPiece11
		mapPiece11=mapPiece11File.read()
	mapPiece12File=open("Map Pieces 10-19/mapPiece12.txt", "r")
	if mapPiece12File.mode=="r":
		global mapPiece12
		mapPiece12=mapPiece12File.read()
	mapPiece13File=open("Map Pieces 10-19/mapPiece13.txt", "r")
	if mapPiece13File.mode=="r":
		global mapPiece13
		mapPiece13=mapPiece13File.read()
	mapPiece14File=open("Map Pieces 10-19/mapPiece14.txt", "r")
	if mapPiece14File.mode=="r":
		global mapPiece14
		mapPiece14=mapPiece14File.read()
	mapPiece15File=open("Map Pieces 10-19/mapPiece15.txt", "r")
	if mapPiece15File.mode=="r":
		global mapPiece15
		mapPiece15=mapPiece15File.read()
	mapPiece16File=open("Map Pieces 10-19/mapPiece16.txt", "r")
	if mapPiece16File.mode=="r":
		global mapPiece16
		mapPiece16=mapPiece16File.read()
	mapPiece17File=open("Map Pieces 10-19/mapPiece17.txt", "r")
	if mapPiece17File.mode=="r":
		global mapPiece17
		mapPiece17=mapPiece17File.read()
	mapPiece18File=open("Map Pieces 10-19/mapPiece18.txt", "r")
	if mapPiece18File.mode=="r":
		global mapPiece18
		mapPiece18=mapPiece18File.read()
	mapPiece19File=open("Map Pieces 10-19/mapPiece19.txt", "r")
	if mapPiece19File.mode=="r":
		global mapPiece19
		mapPiece19=mapPiece19File.read()

	mapPiece20File=open("Map Pieces 20-29/mapPiece20.txt", "r")
	if mapPiece20File.mode=="r":
		global mapPiece20
		mapPiece20=mapPiece20File.read()
	mapPiece21File=open("Map Pieces 20-29/mapPiece21.txt", "r")
	if mapPiece21File.mode=="r":
		global mapPiece21
		mapPiece21=mapPiece21File.read()
	mapPiece22File=open("Map Pieces 20-29/mapPiece22.txt", "r")
	if mapPiece22File.mode=="r":
		global mapPiece22
		mapPiece22=mapPiece22File.read()
	mapPiece23File=open("Map Pieces 20-29/mapPiece23.txt", "r")
	if mapPiece23File.mode=="r":
		global mapPiece23
		mapPiece23=mapPiece23File.read()
	mapPiece24File=open("Map Pieces 20-29/mapPiece24.txt", "r")
	if mapPiece24File.mode=="r":
		global mapPiece24
		mapPiece24=mapPiece24File.read()
	mapPiece25File=open("Map Pieces 20-29/mapPiece25.txt", "r")
	if mapPiece25File.mode=="r":
		global mapPiece25
		mapPiece25=mapPiece25File.read()
	mapPiece26File=open("Map Pieces 20-29/mapPiece26.txt", "r")
	if mapPiece26File.mode=="r":
		global mapPiece26
		mapPiece26=mapPiece26File.read()
	mapPiece27File=open("Map Pieces 20-29/mapPiece27.txt", "r")
	if mapPiece27File.mode=="r":
		global mapPiece27
		mapPiece27=mapPiece27File.read()
	mapPiece28File=open("Map Pieces 20-29/mapPiece28.txt", "r")
	if mapPiece28File.mode=="r":
		global mapPiece28
		mapPiece28=mapPiece28File.read()
	mapPiece29File=open("Map Pieces 20-29/mapPiece29.txt", "r")
	if mapPiece29File.mode=="r":
		global mapPiece29
		mapPiece29=mapPiece29File.read()
	
	mapPiece30File=open("Map Pieces 30-39/mapPiece30.txt", "r")
	if mapPiece30File.mode=="r":
		global mapPiece30
		mapPiece30=mapPiece30File.read()
	mapPiece31File=open("Map Pieces 30-39/mapPiece31.txt", "r")
	if mapPiece31File.mode=="r":
		global mapPiece31
		mapPiece31=mapPiece31File.read()
	mapPiece32File=open("Map Pieces 30-39/mapPiece32.txt", "r")
	if mapPiece32File.mode=="r":
		global mapPiece32
		mapPiece32=mapPiece32File.read()
	mapPiece33File=open("Map Pieces 30-39/mapPiece33.txt", "r")
	if mapPiece33File.mode=="r":
		global mapPiece33
		mapPiece33=mapPiece33File.read()
	mapPiece34File=open("Map Pieces 30-39/mapPiece34.txt", "r")
	if mapPiece34File.mode=="r":
		global mapPiece34
		mapPiece34=mapPiece34File.read()
	mapPiece35File=open("Map Pieces 30-39/mapPiece35.txt", "r")
	if mapPiece35File.mode=="r":
		global mapPiece35
		mapPiece35=mapPiece35File.read()
	mapPiece36File=open("Map Pieces 30-39/mapPiece36.txt", "r")
	if mapPiece36File.mode=="r":
		global mapPiece36
		mapPiece36=mapPiece36File.read()
	mapPiece37File=open("Map Pieces 30-39/mapPiece37.txt", "r")
	if mapPiece37File.mode=="r":
		global mapPiece37
		mapPiece37=mapPiece37File.read()
	mapPiece38File=open("Map Pieces 30-39/mapPiece38.txt", "r")
	if mapPiece38File.mode=="r":
		global mapPiece38
		mapPiece38=mapPiece38File.read()
	mapPiece39File=open("Map Pieces 30-39/mapPiece39.txt", "r")
	if mapPiece39File.mode=="r":
		global mapPiece39
		mapPiece39=mapPiece39File.read()

	mapPiece40File=open("Map Pieces 40-41/mapPiece40.txt", "r")
	if mapPiece40File.mode=="r":
		global mapPiece40
		mapPiece40=mapPiece40File.read()
	mapPiece41File=open("Map Pieces 40-41/mapPiece41.txt", "r")
	if mapPiece41File.mode=="r":
		global mapPiece41
		mapPiece41=mapPiece41File.read()

def playerTurns():
	global turn
	turn+=1
	print("Turn", turn)
	playersGainSoldiers()
	input("\033[0;37;49mPress Enter")
	clearScreen()
	playersDeploySoldiers()
	playersAttack()
	randomChance=random.randint(1, 3)
	if(randomChance==1):
		specialEvent()
	printStats()

def playersGainSoldiers():
	global player1
	global player2
	global player3
	global player4
	global player1ExtraSoldiers
	global player2ExtraSoldiers
	global player3ExtraSoldiers
	global player4ExtraSoldiers
	morditirBonus=500
	sentenosBonus=600
	monelleBonus=1000
	kyorchiBonus=600
	surlugarBonus=500
	#Player 1
	if(player1!=0):
		player1OwnsMorditir=False
		player1OwnsSentenos=False
		player1OwnsMonelle=False
		player1OwnsKyorchi=False
		player1OwnsSurlugar=False
		player1Placeholder=player1ExtraSoldiers
		for country in player1Countries:
			player1ExtraSoldiers+=100
		if set(countriesMorditir).issubset(player1Countries):
			player1ExtraSoldiers+=morditirBonus
			player1OwnsMorditir=True
		if set(countriesSentenos).issubset(player1Countries):
			player1ExtraSoldiers+=sentenosBonus
			player1OwnsSentenos=True
		if set(countriesMonelle).issubset(player1Countries):
			player1ExtraSoldiers+=monelleBonus
			player1OwnsMonelle=True
		if set(countriesKyorchi).issubset(player1Countries):
			player1ExtraSoldiers+=kyorchiBonus
			player1OwnsKyorchi=True
		if set(countriesSurlugar).issubset(player1Countries):
			player1ExtraSoldiers+=surlugarBonus
			player1OwnsSurlugar=True
		gained=player1ExtraSoldiers-player1Placeholder
		print("\033[0;31;49m", player1, " gained ", gained, " soldiers.", sep="")
		print("-"+str(len(player1Countries))+" countries * 100 = "+str(len(player1Countries)*100)+" soldiers.")
		if(player1OwnsMorditir==True):
			print("-Owns Morditir = "+str(morditirBonus)+" soldiers.")
		if(player1OwnsSentenos==True):
			print("-Owns Sentenos = "+str(sentenosBonus)+" soldiers.")
		if(player1OwnsMonelle==True):
			print("-Owns Monelle = "+str(monelleBonus)+" soldiers.")
		if(player1OwnsKyorchi==True):
			print("-Owns Kyorchi = "+str(kyorchiBonus)+" soldiers.")
		if(player1OwnsSurlugar==True):
			print("-Owns Surlugar = "+str(surlugarBonus)+" soldiers.")

	#Player 2
	if(player2!=0):
		player2OwnsMorditir=False
		player2OwnsSentenos=False
		player2OwnsMonelle=False
		player2OwnsKyorchi=False
		player2OwnsSurlugar=False
		player2Placeholder=player2ExtraSoldiers
		for country in player2Countries:
			player2ExtraSoldiers+=100
		if set(countriesMorditir).issubset(player2Countries):
			player2ExtraSoldiers+=morditirBonus
			player2OwnsMorditir=True
		if set(countriesSentenos).issubset(player2Countries):
			player2ExtraSoldiers+=sentenosBonus
			player2OwnsSentenos=True
		if set(countriesMonelle).issubset(player2Countries):
			player2ExtraSoldiers+=monelleBonus
			player2OwnsMonelle=True
		if set(countriesKyorchi).issubset(player2Countries):
			player2ExtraSoldiers+=kyorchiBonus
			player2OwnsKyorchi=True
		if set(countriesSurlugar).issubset(player2Countries):
			player2ExtraSoldiers+=surlugarBonus
			player2OwnsSurlugar=True
		gained=player2ExtraSoldiers-player2Placeholder
		print("\033[0;32;49m", player2, " gained ", gained, " soldiers.", sep="")
		print("-"+str(len(player2Countries))+" countries * 100 = "+str(len(player2Countries)*100)+" soldiers.")
		if(player2OwnsMorditir==True):
			print("-Owns Morditir = "+str(morditirBonus)+" soldiers.")
		if(player2OwnsSentenos==True):
			print("-Owns Sentenos = "+str(sentenosBonus)+" soldiers.")
		if(player2OwnsMonelle==True):
			print("-Owns Monelle = "+str(monelleBonus)+" soldiers.")
		if(player2OwnsKyorchi==True):
			print("-Owns Kyorchi = "+str(kyorchiBonus)+" soldiers.")
		if(player2OwnsSurlugar==True):
			print("-Owns Surlugar = "+str(surlugarBonus)+" soldiers.")

	#Player 3
	if(player3!=0):
		player3OwnsMorditir=False
		player3OwnsSentenos=False
		player3OwnsMonelle=False
		player3OwnsKyorchi=False
		player3OwnsSurlugar=False
		player3Placeholder=player3ExtraSoldiers
		for country in player3Countries:
			player3ExtraSoldiers+=100
		if set(countriesMorditir).issubset(player3Countries):
			player3ExtraSoldiers+=morditirBonus
			player3OwnsMorditir=True
		if set(countriesSentenos).issubset(player3Countries):
			player3ExtraSoldiers+=sentenosBonus
			player3OwnsSentenos=True
		if set(countriesMonelle).issubset(player3Countries):
			player3ExtraSoldiers+=monelleBonus
			player3OwnsMonelle=True
		if set(countriesKyorchi).issubset(player3Countries):
			player3ExtraSoldiers+=kyorchiBonus
			player3OwnsKyorchi=True
		if set(countriesSurlugar).issubset(player3Countries):
			player3ExtraSoldiers+=surlugarBonus
			player3OwnsSurlugar=True
		gained=player3ExtraSoldiers-player3Placeholder
		print("\033[0;34;49m", player3, " gained ", gained, " soldiers.", sep="")
		print("-"+str(len(player3Countries))+" countries * 100 = "+str(len(player3Countries)*100)+" soldiers.")
		if(player3OwnsMorditir==True):
			print("-Owns Morditir = "+str(morditirBonus)+" soldiers.")
		if(player3OwnsSentenos==True):
			print("-Owns Sentenos = "+str(sentenosBonus)+" soldiers.")
		if(player3OwnsMonelle==True):
			print("-Owns Monelle = "+str(monelleBonus)+" soldiers.")
		if(player3OwnsKyorchi==True):
			print("-Owns Kyorchi = "+str(kyorchiBonus)+" soldiers.")
		if(player3OwnsSurlugar==True):
			print("-Owns Surlugar = "+str(surlugarBonus)+" soldiers.")

	#Player 4
	if(player4!=0):
		player4OwnsMorditir=False
		player4OwnsSentenos=False
		player4OwnsMonelle=False
		player4OwnsKyorchi=False
		player4OwnsSurlugar=False
		player4Placeholder=player4ExtraSoldiers
		for country in player4Countries:
			player4ExtraSoldiers+=100
		if set(countriesMorditir).issubset(player4Countries):
			player4ExtraSoldiers+=morditirBonus
			player4OwnsMorditir=True
		if set(countriesSentenos).issubset(player4Countries):
			player4ExtraSoldiers+=sentenosBonus
			player4OwnsSentenos=True
		if set(countriesMonelle).issubset(player4Countries):
			player4ExtraSoldiers+=monelleBonus
			player4OwnsMonelle=True
		if set(countriesKyorchi).issubset(player4Countries):
			player4ExtraSoldiers+=kyorchiBonus
			player4OwnsKyorchi=True
		if set(countriesSurlugar).issubset(player4Countries):
			player4ExtraSoldiers+=surlugarBonus
			player4OwnsSurlugar=True
		gained=player4ExtraSoldiers-player4Placeholder
		print("\033[0;35;49m", player4, " gained ", gained, " soldiers.", sep="")
		print("-"+str(len(player4Countries))+" countries * 100 = "+str(len(player4Countries)*100)+" soldiers.")
		if(player4OwnsMorditir==True):
			print("-Owns Morditir = "+str(morditirBonus)+" soldiers.")
		if(player4OwnsSentenos==True):
			print("-Owns Sentenos = "+str(sentenosBonus)+" soldiers.")
		if(player4OwnsMonelle==True):
			print("-Owns Monelle = "+str(monelleBonus)+" soldiers.")
		if(player4OwnsKyorchi==True):
			print("-Owns Kyorchi = "+str(kyorchiBonus)+" soldiers.")
		if(player4OwnsSurlugar==True):
			print("-Owns Surlugar = "+str(surlugarBonus)+" soldiers.")

def playersDeploySoldiers():
	global player1
	global player2
	global player3
	global player4
	global player1ExtraSoldiers
	global player2ExtraSoldiers
	global player3ExtraSoldiers
	global player4ExtraSoldiers
	global armiesMoriatir
	global armiesArdtir
	global armiesDesich
	global armiesFadtir
	global armiesMagnollis
	global armiesEmptos
	global armiesTeracies
	global armiesTeramus
	global armiesUchelle
	global armiesDwylle
	global armiesCanolle
	global armiesIselle
	global armiesKitashi
	global armiesKitazai
	global armiesNanseshu
	global armiesNantshu
	global armiesDesiar
	global armiesEsteplana
	global armiesArenar
	global armiesCenrodad

	#Player 1
	if(player1!=0):
		done=False
		while(done==False and player1ExtraSoldiers>0):
			printMap()
			print("\033[0;31;49m", player1, ", you have ", player1ExtraSoldiers, " soldiers to deploy.", sep="")
			print("\033[0;37;49mPlease note your army in one country ")
			print("cannot be greater than 9999.")
			print("Deploy soldiers?")
			print("Yes (1)")
			print("No (0)")
			answer=sanitisedInput("", int, range_=(0, 1))
			if(answer==0):
				print("You have finished deploying soldiers.")
				done=True
				input("Press Enter")
				clearScreen()
			else:
				where=sanitisedInput("Where? ", str, range_=(player1Countries))
				number=sanitisedInput("How many? ", int, 1, player1ExtraSoldiers)
				armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
							"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
							"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
							"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
							"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
				armiesDict[where]+=number
				if(armiesDict[where]>9999):
					armiesDict[where]=9999
					print("Your army is too large.")
					time.sleep(1)
				player1ExtraSoldiers-=number
				clearScreen()
				armiesMoriatir=armiesDict["Moriatir"]
				armiesArdtir=armiesDict["Ardtir"]
				armiesFadtir=armiesDict["Fadtir"]
				armiesDesich=armiesDict["Desich"]
				armiesMagnollis=armiesDict["Magnollis"]
				armiesEmptos=armiesDict["Emptos"]
				armiesTeracies=armiesDict["Teracies"]
				armiesTeramus=armiesDict["Teramus"]
				armiesUchelle=armiesDict["Uchelle"]
				armiesCanolle=armiesDict["Canolle"]
				armiesIselle=armiesDict["Iselle"]
				armiesDwylle=armiesDict["Dwylle"]
				armiesKitashi=armiesDict["Kitashi"]
				armiesNanseshu=armiesDict["Nanseshu"]
				armiesNantshu=armiesDict["Nantshu"]
				armiesKitazai=armiesDict["Kitazai"]
				armiesDesiar=armiesDict["Desiar"]
				armiesEsteplana=armiesDict["Esteplana"]
				armiesCenrodad=armiesDict["Cenrodad"]
				armiesArenar=armiesDict["Arenar"]

	#Player 2
	if(player2!=0):
		done=False
		while(done==False and player2ExtraSoldiers>0):
			printMap()
			print("\033[0;32;49m", player2, ", you have ", player2ExtraSoldiers, " soldiers to deploy.", sep="")
			print("\033[0;37;49mPlease note your army in one country ")
			print("cannot be greater than 9999.")
			print("Deploy soldiers?")
			print("Yes (1)")
			print("No (0)")
			answer=sanitisedInput("", int, range_=(0, 1))
			if(answer==0):
				print("You have finished deploying soldiers.")
				done=True
				input("Press Enter")
				clearScreen()
			else:
				where=sanitisedInput("Where? ", str, range_=(player2Countries))
				number=sanitisedInput("How many? ", int, 1, player2ExtraSoldiers)
				armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
							"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
							"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
							"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
							"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
				armiesDict[where]+=number
				if(armiesDict[where]>9999):
					armiesDict[where]=9999
					print("Your army is too large.")
					time.sleep(1)
				player2ExtraSoldiers-=number
				clearScreen()
				armiesMoriatir=armiesDict["Moriatir"]
				armiesArdtir=armiesDict["Ardtir"]
				armiesFadtir=armiesDict["Fadtir"]
				armiesDesich=armiesDict["Desich"]
				armiesMagnollis=armiesDict["Magnollis"]
				armiesEmptos=armiesDict["Emptos"]
				armiesTeracies=armiesDict["Teracies"]
				armiesTeramus=armiesDict["Teramus"]
				armiesUchelle=armiesDict["Uchelle"]
				armiesCanolle=armiesDict["Canolle"]
				armiesIselle=armiesDict["Iselle"]
				armiesDwylle=armiesDict["Dwylle"]
				armiesKitashi=armiesDict["Kitashi"]
				armiesNanseshu=armiesDict["Nanseshu"]
				armiesNantshu=armiesDict["Nantshu"]
				armiesKitazai=armiesDict["Kitazai"]
				armiesDesiar=armiesDict["Desiar"]
				armiesEsteplana=armiesDict["Esteplana"]
				armiesCenrodad=armiesDict["Cenrodad"]
				armiesArenar=armiesDict["Arenar"]
	
	#Player 3
	if(player3!=0):
		done=False
		while(done==False and player3ExtraSoldiers>0):
			printMap()
			print("\033[0;34;49m", player3, ", you have ", player3ExtraSoldiers, " soldiers to deploy.", sep="")
			print("\033[0;37;49mPlease note your army in one country ")
			print("cannot be greater than 9999.")
			print("Deploy soldiers?")
			print("Yes (1)")
			print("No (0)")
			answer=sanitisedInput("", int, range_=(0, 1))
			if(answer==0):
				print("You have finished deploying soldiers.")
				done=True
				input("Press Enter")
				clearScreen()
			else:
				where=sanitisedInput("Where? ", str, range_=(player3Countries))
				number=sanitisedInput("How many? ", int, 1, player3ExtraSoldiers)
				armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
							"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
							"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
							"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
							"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
				armiesDict[where]+=number
				if(armiesDict[where]>9999):
					armiesDict[where]=9999
					print("Your army is too large.")
					time.sleep(1)
				player3ExtraSoldiers-=number
				clearScreen()
				armiesMoriatir=armiesDict["Moriatir"]
				armiesArdtir=armiesDict["Ardtir"]
				armiesFadtir=armiesDict["Fadtir"]
				armiesDesich=armiesDict["Desich"]
				armiesMagnollis=armiesDict["Magnollis"]
				armiesEmptos=armiesDict["Emptos"]
				armiesTeracies=armiesDict["Teracies"]
				armiesTeramus=armiesDict["Teramus"]
				armiesUchelle=armiesDict["Uchelle"]
				armiesCanolle=armiesDict["Canolle"]
				armiesIselle=armiesDict["Iselle"]
				armiesDwylle=armiesDict["Dwylle"]
				armiesKitashi=armiesDict["Kitashi"]
				armiesNanseshu=armiesDict["Nanseshu"]
				armiesNantshu=armiesDict["Nantshu"]
				armiesKitazai=armiesDict["Kitazai"]
				armiesDesiar=armiesDict["Desiar"]
				armiesEsteplana=armiesDict["Esteplana"]
				armiesCenrodad=armiesDict["Cenrodad"]
				armiesArenar=armiesDict["Arenar"]

	#Player 4
	if(player4!=0):
		done=False
		while(done==False and player4ExtraSoldiers>0):
			printMap()
			print("\033[0;35;49m", player4, ", you have ", player4ExtraSoldiers, " soldiers to deploy.", sep="")
			print("\033[0;37;49mPlease note your army in one country ")
			print("cannot be greater than 9999.")
			print("Deploy soldiers?")
			print("Yes (1)")
			print("No (0)")
			answer=sanitisedInput("", int, range_=(0, 1))
			if(answer==0):
				print("You have finished deploying soldiers.")
				done=True
				input("Press Enter")
				clearScreen()
			else:
				where=sanitisedInput("Where? ", str, range_=(player4Countries))
				number=sanitisedInput("How many? ", int, 1, player4ExtraSoldiers)
				armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
							"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
							"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
							"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
							"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
				armiesDict[where]+=number
				if(armiesDict[where]>9999):
					armiesDict[where]=9999
					print("Your army is too large.")
					time.sleep(1)
				player4ExtraSoldiers-=number
				clearScreen()
				armiesMoriatir=armiesDict["Moriatir"]
				armiesArdtir=armiesDict["Ardtir"]
				armiesFadtir=armiesDict["Fadtir"]
				armiesDesich=armiesDict["Desich"]
				armiesMagnollis=armiesDict["Magnollis"]
				armiesEmptos=armiesDict["Emptos"]
				armiesTeracies=armiesDict["Teracies"]
				armiesTeramus=armiesDict["Teramus"]
				armiesUchelle=armiesDict["Uchelle"]
				armiesCanolle=armiesDict["Canolle"]
				armiesIselle=armiesDict["Iselle"]
				armiesDwylle=armiesDict["Dwylle"]
				armiesKitashi=armiesDict["Kitashi"]
				armiesNanseshu=armiesDict["Nanseshu"]
				armiesNantshu=armiesDict["Nantshu"]
				armiesKitazai=armiesDict["Kitazai"]
				armiesDesiar=armiesDict["Desiar"]
				armiesEsteplana=armiesDict["Esteplana"]
				armiesCenrodad=armiesDict["Cenrodad"]
				armiesArenar=armiesDict["Arenar"]

def playersAttack():
	global player1
	global player2
	global player3
	global player4
	global armiesMoriatir
	global armiesArdtir
	global armiesDesich
	global armiesFadtir
	global armiesMagnollis
	global armiesEmptos
	global armiesTeracies
	global armiesTeramus
	global armiesUchelle
	global armiesDwylle
	global armiesCanolle
	global armiesIselle
	global armiesKitashi
	global armiesKitazai
	global armiesNanseshu
	global armiesNantshu
	global armiesDesiar
	global armiesEsteplana
	global armiesArenar
	global armiesCenrodad
	global deathTotal
	global player1TotalArmies
	global player2TotalArmies
	global player3TotalArmies
	global player4TotalArmies
	global neutralTotalArmies
	global player1ExtraSoldiers
	global player2ExtraSoldiers
	global player3ExtraSoldiers
	global player4ExtraSoldiers

	player1Done=False
	player2Done=False
	player3Done=False
	player4Done=False
	if(player1==False):
		player1Done=True
	if(player2==False):
		player2Done=True
	if(player3==False):
		player3Done=True
	if(player4==False):
		player4Done=True

	checkTotalArmies()
	while(player1Done==False or player2Done==False or player3Done==False or player4Done==False):
		#Player 1
		checkTotalArmies()
		if(player1TotalArmies==0):
			player1Done=True
		if(player1Done==False):
			armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
						"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
						"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
						"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
						"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
			clearScreen()
			printMap()
			print("\033[0;31;49m", player1, ", would you like to start an invasion?", sep="")
			print("\033[0;37;49mYes (1)")
			print("No (0)")
			answer=sanitisedInput("", int, range_=(0, 1))
			if(answer==0):
				print("You have finished invading.")
				player1Done=True
			else:
				attacker=sanitisedInput("Invade from: ", str, range_=(player1Countries))
				while(armiesDict[attacker]==0):
					print(attacker, "has no armies. Try again.")
					attacker=sanitisedInput("Invade from: ", str, range_=(player1Countries))
				defender=sanitisedInput("Invade: ", str, range_=(adjacentCountriesDict[attacker]))
				attackingArmies=sanitisedInput("Invading armies: ", int, min_=0, max_=armiesDict[attacker])
				armiesDict[attacker]-=attackingArmies
				if(defender in player1Countries):
					print("\033[0;33;49m", player1, " transferred ", attackingArmies, " soldiers from ", attacker, " to ", defender, ".", sep="")
					armiesDict[defender]+=attackingArmies
				else:
					attArmiesPlaceholder=attackingArmies
					attLossPercentage=random.randint(0, 50)
					attLossPercentage=attLossPercentage/100
					attLoss=round(armiesDict[defender]*attLossPercentage)
					attackingArmies-=attLoss
					if(attackingArmies<0):
						attackingArmies=0
					deathTotal+=attArmiesPlaceholder-attackingArmies
					if(attackingArmies>armiesDict[defender]):
						print("\033[0;32;49m", player1, " succeeded.", sep="")
						deathTotal+=armiesDict[defender]*2
						player1Countries.append(defender)
						attackingArmies-=armiesDict[defender]
						armiesDict[defender]=0
						armiesDict[defender]+=attackingArmies
						if(defender in player2Countries):
							player2Countries.remove(defender)
							if(len(player2Countries)==0):
								print("\033[0;31;49m", player1, "\033[0;37;49m elminated ", "\033[0;32;49m", player2, "\033[0;37;49m!", sep="")
								player1ExtraSoldiers+=800
								print("\033[0;31;49m", player1, "\033[0;37;49m gained 800 soldiers.", sep="")
								player2=0
						elif(defender in player3Countries):
							player3Countries.remove(defender)
							if(len(player3Countries)==0):
								print("\033[0;31;49m", player1, "\033[0;37;49m elminated ", "\033[0;34;49m", player3, "\033[0;37;49m!", sep="")
								player1ExtraSoldiers+=800
								print("\033[0;31;49m", player1, "\033[0;37;49m gained 800 soldiers.", sep="")
								player3=0
						elif(defender in player4Countries):
							player4Countries.remove(defender)
							if(len(player4Countries)==0):
								print("\033[0;31;49m", player1, "\033[0;37;49m elminated ", "\033[0;35;49m", player4, "\033[0;37;49m!", sep="")
								player1ExtraSoldiers+=800
								print("\033[0;31;49m", player1, "\033[0;37;49m gained 800 soldiers.", sep="")
								player4=0
						elif(defender in neutralCountries):
							neutralCountries.remove(defender)
							if(len(neutralCountries)==0):
								print("\033[0;31;49m", player1, "\033[0;37;49m captured the last neutral country!", sep="")
								player1ExtraSoldiers+=800
								print("\033[0;31;49m", player1, "\033[0;37;49m gained 800 soldiers.", sep="")
					elif(armiesDict[defender]>attackingArmies):
						print("\033[0;31;49m", player1, " failed.", sep="")
						deathTotal+=attackingArmies*2
						armiesDict[defender]-=attackingArmies
					elif(armiesDict[defender]==attackingArmies):
						print("\033[0;33;49m", player1, " drew a stalemate.", sep="")
						deathTotal+=attackingArmies*2
						armiesDict[defender]=0
			armiesMoriatir=armiesDict["Moriatir"]
			armiesArdtir=armiesDict["Ardtir"]
			armiesFadtir=armiesDict["Fadtir"]
			armiesDesich=armiesDict["Desich"]
			armiesMagnollis=armiesDict["Magnollis"]
			armiesEmptos=armiesDict["Emptos"]
			armiesTeracies=armiesDict["Teracies"]
			armiesTeramus=armiesDict["Teramus"]
			armiesUchelle=armiesDict["Uchelle"]
			armiesCanolle=armiesDict["Canolle"]
			armiesIselle=armiesDict["Iselle"]
			armiesDwylle=armiesDict["Dwylle"]
			armiesKitashi=armiesDict["Kitashi"]
			armiesNanseshu=armiesDict["Nanseshu"]
			armiesNantshu=armiesDict["Nantshu"]
			armiesKitazai=armiesDict["Kitazai"]
			armiesDesiar=armiesDict["Desiar"]
			armiesEsteplana=armiesDict["Esteplana"]
			armiesCenrodad=armiesDict["Cenrodad"]
			armiesArenar=armiesDict["Arenar"]
			input("\033[0;37;49mPress Enter")
			clearScreen()

		#Player 2
		checkTotalArmies()
		if(player2TotalArmies==0):
			player2Done=True
		if(player2Done==False):
			armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
						"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
						"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
						"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
						"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
			clearScreen()
			printMap()
			print("\033[0;32;49m", player2, ", would you like to start an invasion?", sep="")
			print("\033[0;37;49mYes (1)")
			print("No (0)")
			answer=sanitisedInput("", int, range_=(0, 1))
			if(answer==0):
				print("You have finished invading.")
				player2Done=True
			else:
				attacker=sanitisedInput("Invade from: ", str, range_=(player2Countries))
				while(armiesDict[attacker]==0):
					print(attacker, "has no armies. Try again.")
					attacker=sanitisedInput("Invade from: ", str, range_=(player2Countries))
				defender=sanitisedInput("Invade: ", str, range_=(adjacentCountriesDict[attacker]))
				attackingArmies=sanitisedInput("Invading armies: ", int, min_=0, max_=armiesDict[attacker])
				armiesDict[attacker]-=attackingArmies
				if(defender in player2Countries):
					print("\033[0;33;49m", player2, " transferred ", attackingArmies, " soldiers from ", attacker, " to ", defender, ".", sep="")
					armiesDict[defender]+=attackingArmies
				else:
					attArmiesPlaceholder=attackingArmies
					attLossPercentage=random.randint(0, 50)
					attLossPercentage=attLossPercentage/100
					attLoss=round(armiesDict[defender]*attLossPercentage)
					attackingArmies-=attLoss
					if(attackingArmies<0):
						attackingArmies=0
					deathTotal+=attArmiesPlaceholder-attackingArmies
					if(attackingArmies>armiesDict[defender]):
						print("\033[0;32;49m", player2, " succeeded.", sep="")
						deathTotal+=armiesDict[defender]*2
						player2Countries.append(defender)
						attackingArmies-=armiesDict[defender]
						armiesDict[defender]=0
						armiesDict[defender]+=attackingArmies
						if(defender in player1Countries):
							player1Countries.remove(defender)
							if(len(player1Countries)==0):
								print("\033[0;32;49m", player2, "\033[0;37;49m elminated ", "\033[0;31;49m", player1, "\033[0;37;49m!", sep="")
								player2ExtraSoldiers+=800
								print("\033[0;32;49m", player2, "\033[0;37;49m gained 800 soldiers.", sep="")
								player1=0
						elif(defender in player3Countries):
							player3Countries.remove(defender)
							if(len(player3Countries)==0):
								print("\033[0;32;49m", player2, "\033[0;37;49m elminated ", "\033[0;34;49m", player3, "\033[0;37;49m!", sep="")
								player2ExtraSoldiers+=800
								print("\033[0;32;49m", player2, "\033[0;37;49m gained 800 soldiers.", sep="")
								player3=0
						elif(defender in player4Countries):
							player4Countries.remove(defender)
							if(len(player4Countries)==0):
								print("\033[0;32;49m", player2, "\033[0;37;49m elminated ", "\033[0;35;49m", player4, "\033[0;37;49m!", sep="")
								player2ExtraSoldiers+=800
								print("\033[0;32;49m", player2, "\033[0;37;49m gained 800 soldiers.", sep="")
								player4=0
						elif(defender in neutralCountries):
							neutralCountries.remove(defender)
							if(len(neutralCountries)==0):
								print("\033[0;32;49m", player2, "\033[0;37;49m captured the last neutral country!", sep="")
								player2ExtraSoldiers+=800
								print("\033[0;32;49m", player2, "\033[0;37;49m gained 800 soldiers.", sep="")
					elif(armiesDict[defender]>attackingArmies):
						print("\033[0;31;49m", player2, " failed.", sep="")
						deathTotal+=attackingArmies*2
						armiesDict[defender]-=attackingArmies
					elif(armiesDict[defender]==attackingArmies):
						print("\033[0;33;49m", player2, " drew a stalemate.", sep="")
						deathTotal+=attackingArmies*2
						armiesDict[defender]=0
			armiesMoriatir=armiesDict["Moriatir"]
			armiesArdtir=armiesDict["Ardtir"]
			armiesFadtir=armiesDict["Fadtir"]
			armiesDesich=armiesDict["Desich"]
			armiesMagnollis=armiesDict["Magnollis"]
			armiesEmptos=armiesDict["Emptos"]
			armiesTeracies=armiesDict["Teracies"]
			armiesTeramus=armiesDict["Teramus"]
			armiesUchelle=armiesDict["Uchelle"]
			armiesCanolle=armiesDict["Canolle"]
			armiesIselle=armiesDict["Iselle"]
			armiesDwylle=armiesDict["Dwylle"]
			armiesKitashi=armiesDict["Kitashi"]
			armiesNanseshu=armiesDict["Nanseshu"]
			armiesNantshu=armiesDict["Nantshu"]
			armiesKitazai=armiesDict["Kitazai"]
			armiesDesiar=armiesDict["Desiar"]
			armiesEsteplana=armiesDict["Esteplana"]
			armiesCenrodad=armiesDict["Cenrodad"]
			armiesArenar=armiesDict["Arenar"]
			input("\033[0;37;49mPress Enter")
			clearScreen()

		#Player 3
		checkTotalArmies()
		if(player3TotalArmies==0):
			player3Done=True
		if(player3Done==False):
			armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
						"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
						"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
						"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
						"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
			clearScreen()
			printMap()
			print("\033[0;34;49m", player3, ", would you like to start an invasion?", sep="")
			print("\033[0;37;49mYes (1)")
			print("No (0)")
			answer=sanitisedInput("", int, range_=(0, 1))
			if(answer==0):
				print("You have finished invading.")
				player3Done=True
			else:
				attacker=sanitisedInput("Invade from: ", str, range_=(player3Countries))
				while(armiesDict[attacker]==0):
					print(attacker, "has no armies. Try again.")
					attacker=sanitisedInput("Invade from: ", str, range_=(player3Countries))
				defender=sanitisedInput("Invade: ", str, range_=(adjacentCountriesDict[attacker]))
				attackingArmies=sanitisedInput("Invading armies: ", int, min_=0, max_=armiesDict[attacker])
				armiesDict[attacker]-=attackingArmies
				if(defender in player3Countries):
					print("\033[0;33;49m", player3, " transferred ", attackingArmies, " soldiers from ", attacker, " to ", defender, ".", sep="")
					armiesDict[defender]+=attackingArmies
				else:
					attArmiesPlaceholder=attackingArmies
					attLossPercentage=random.randint(0, 50)
					attLossPercentage=attLossPercentage/100
					attLoss=round(armiesDict[defender]*attLossPercentage)
					attackingArmies-=attLoss
					if(attackingArmies<0):
						attackingArmies=0
					deathTotal+=attArmiesPlaceholder-attackingArmies
					if(attackingArmies>armiesDict[defender]):
						print("\033[0;32;49m", player3, " succeeded.", sep="")
						deathTotal+=armiesDict[defender]*2
						player3Countries.append(defender)
						attackingArmies-=armiesDict[defender]
						armiesDict[defender]=0
						armiesDict[defender]+=attackingArmies
						if(defender in player1Countries):
							player1Countries.remove(defender)
							if(len(player1Countries)==0):
								print("\033[0;34;49m", player3, "\033[0;37;49m elminated ", "\033[0;31;49m", player1, "\033[0;37;49m!", sep="")
								player3ExtraSoldiers+=800
								print("\033[0;34;49m", player3, "\033[0;37;49m gained 800 soldiers.", sep="")
								player1=0
						elif(defender in player2Countries):
							player2Countries.remove(defender)
							if(len(player2Countries)==0):
								print("\033[0;34;49m", player3, "\033[0;37;49m elminated ", "\033[0;32;49m", player2, "\033[0;37;49m!", sep="")
								player3ExtraSoldiers+=800
								print("\033[0;34;49m", player3, "\033[0;37;49m gained 800 soldiers.", sep="")
								player2=0
						elif(defender in player4Countries):
							player4Countries.remove(defender)
							if(len(player4Countries)==0):
								print("\033[0;34;49m", player3, "\033[0;37;49m elminated ", "\033[0;35;49m", player4, "\033[0;37;49m!", sep="")
								player3ExtraSoldiers+=800
								print("\033[0;34;49m", player3, "\033[0;37;49m gained 800 soldiers.", sep="")
								player4=0
						elif(defender in neutralCountries):
							neutralCountries.remove(defender)
							if(len(neutralCountries)==0):
								print("\033[0;34;49m", player3, "\033[0;37;49m captured the last neutral country!", sep="")
								player3ExtraSoldiers+=800
								print("\033[0;34;49m", player3, "\033[0;37;49m gained 800 soldiers.", sep="")
					elif(armiesDict[defender]>attackingArmies):
						print("\033[0;31;49m", player3, " failed.", sep="")
						deathTotal+=attackingArmies*2
						armiesDict[defender]-=attackingArmies
					elif(armiesDict[defender]==attackingArmies):
						print("\033[0;33;49m", player3, " drew a stalemate.", sep="")
						deathTotal+=attackingArmies*2
						armiesDict[defender]=0
			armiesMoriatir=armiesDict["Moriatir"]
			armiesArdtir=armiesDict["Ardtir"]
			armiesFadtir=armiesDict["Fadtir"]
			armiesDesich=armiesDict["Desich"]
			armiesMagnollis=armiesDict["Magnollis"]
			armiesEmptos=armiesDict["Emptos"]
			armiesTeracies=armiesDict["Teracies"]
			armiesTeramus=armiesDict["Teramus"]
			armiesUchelle=armiesDict["Uchelle"]
			armiesCanolle=armiesDict["Canolle"]
			armiesIselle=armiesDict["Iselle"]
			armiesDwylle=armiesDict["Dwylle"]
			armiesKitashi=armiesDict["Kitashi"]
			armiesNanseshu=armiesDict["Nanseshu"]
			armiesNantshu=armiesDict["Nantshu"]
			armiesKitazai=armiesDict["Kitazai"]
			armiesDesiar=armiesDict["Desiar"]
			armiesEsteplana=armiesDict["Esteplana"]
			armiesCenrodad=armiesDict["Cenrodad"]
			armiesArenar=armiesDict["Arenar"]
			input("\033[0;37;49mPress Enter")
			clearScreen()

		#Player 4
		checkTotalArmies()
		if(player4TotalArmies==0):
			player4Done=True
		if(player4Done==False):
			armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
						"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
						"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
						"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
						"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
			clearScreen()
			printMap()
			print("\033[0;35;49m", player4, ", would you like to start an invasion?", sep="")
			print("\033[0;37;49mYes (1)")
			print("No (0)")
			answer=sanitisedInput("", int, range_=(0, 1))
			if(answer==0):
				print("You have finished invading.")
				player4Done=True
			else:
				attacker=sanitisedInput("Invade from: ", str, range_=(player4Countries))
				while(armiesDict[attacker]==0):
					print(attacker, "has no armies. Try again.")
					attacker=sanitisedInput("Invade from: ", str, range_=(player4Countries))
				defender=sanitisedInput("Invade: ", str, range_=(adjacentCountriesDict[attacker]))
				attackingArmies=sanitisedInput("Invading armies: ", int, min_=0, max_=armiesDict[attacker])
				armiesDict[attacker]-=attackingArmies
				if(defender in player4Countries):
					print("\033[0;33;49m", player4, " transferred ", attackingArmies, " soldiers from ", attacker, " to ", defender, ".", sep="")
					armiesDict[defender]+=attackingArmies
				else:
					attArmiesPlaceholder=attackingArmies
					attLossPercentage=random.randint(0, 50)
					attLossPercentage=attLossPercentage/100
					attLoss=round(armiesDict[defender]*attLossPercentage)
					attackingArmies-=attLoss
					if(attackingArmies<0):
						attackingArmies=0
					deathTotal+=attArmiesPlaceholder-attackingArmies
					if(attackingArmies>armiesDict[defender]):
						print("\033[0;32;49m", player4, " succeeded.", sep="")
						deathTotal+=armiesDict[defender]*2
						player4Countries.append(defender)
						attackingArmies-=armiesDict[defender]
						armiesDict[defender]=0
						armiesDict[defender]+=attackingArmies
						if(defender in player1Countries):
							player1Countries.remove(defender)
							if(len(player1Countries)==0):
								print("\033[0;35;49m", player4, "\033[0;37;49m elminated ", "\033[0;31;49m", player1, "\033[0;37;49m!", sep="")
								player4ExtraSoldiers+=800
								print("\033[0;35;49m", player4, "\033[0;37;49m gained 800 soldiers.", sep="")
								player1=0
						elif(defender in player2Countries):
							player2Countries.remove(defender)
							if(len(player2Countries)==0):
								print("\033[0;35;49m", player4, "\033[0;37;49m elminated ", "\033[0;32;49m", player2, "\033[0;37;49m!", sep="")
								player4ExtraSoldiers+=800
								print("\033[0;35;49m", player4, "\033[0;37;49m gained 800 soldiers.", sep="")
								player2=0
						elif(defender in player3Countries):
							player3Countries.remove(defender)
							if(len(player3Countries)==0):
								print("\033[0;35;49m", player4, "\033[0;37;49m elminated ", "\033[0;34;49m", player3, "\033[0;37;49m!", sep="")
								player4ExtraSoldiers+=800
								print("\033[0;35;49m", player4, "\033[0;37;49m gained 800 soldiers.", sep="")
								player3=0
						elif(defender in neutralCountries):
							neutralCountries.remove(defender)
							if(len(neutralCountries)==0):
								print("\033[0;35;49m", player4, "\033[0;37;49m captured the last neutral country!", sep="")
								player4ExtraSoldiers+=800
								print("\033[0;35;49m", player4, "\033[0;37;49m gained 800 soldiers.", sep="")
					elif(armiesDict[defender]>attackingArmies):
						print("\033[0;31;49m", player4, " failed.", sep="")
						deathTotal+=attackingArmies*2
						armiesDict[defender]-=attackingArmies
					elif(armiesDict[defender]==attackingArmies):
						print("\033[0;33;49m", player4, " drew a stalemate.", sep="")
						deathTotal+=attackingArmies*2
						armiesDict[defender]=0
			armiesMoriatir=armiesDict["Moriatir"]
			armiesArdtir=armiesDict["Ardtir"]
			armiesFadtir=armiesDict["Fadtir"]
			armiesDesich=armiesDict["Desich"]
			armiesMagnollis=armiesDict["Magnollis"]
			armiesEmptos=armiesDict["Emptos"]
			armiesTeracies=armiesDict["Teracies"]
			armiesTeramus=armiesDict["Teramus"]
			armiesUchelle=armiesDict["Uchelle"]
			armiesCanolle=armiesDict["Canolle"]
			armiesIselle=armiesDict["Iselle"]
			armiesDwylle=armiesDict["Dwylle"]
			armiesKitashi=armiesDict["Kitashi"]
			armiesNanseshu=armiesDict["Nanseshu"]
			armiesNantshu=armiesDict["Nantshu"]
			armiesKitazai=armiesDict["Kitazai"]
			armiesDesiar=armiesDict["Desiar"]
			armiesEsteplana=armiesDict["Esteplana"]
			armiesCenrodad=armiesDict["Cenrodad"]
			armiesArenar=armiesDict["Arenar"]
			input("\033[0;37;49mPress Enter")
			clearScreen()

def specialEvent():
	global heroCountries
	global refugeesCountries
	global eruptionCountries
	global rebellionCountries
	global revolutionCountries
	if(len(heroCountries)==0):
		heroCountries.extend(countries)
	if(len(rebellionCountries)==0):
		rebellionCountries.extend(countries)
	if(len(refugeesCountries)==0):
		refugeesCountries.extend(countries)
	if(len(eruptionCountries)==0):
		eruptionCountries=["Fadtir", "Moriatir", "Teramus",
				   		   "Nanseshu", "Nantshu", "Desiar", "Esteplana"]
	revolutionCountries=[]
	revolutionCountries.extend(countries)
	for country in neutralCountries:
		revolutionCountries.remove(country)
	if(len(player1Countries)==1):
		for country in player1Countries:
			revolutionCountries.remove(country)
	if(len(player2Countries)==1):
		for country in player2Countries:
			revolutionCountries.remove(country)
	if(len(player3Countries)==1):
		for country in player3Countries:
			revolutionCountries.remove(country)
	if(len(player4Countries)==1):
		for country in player4Countries:
			revolutionCountries.remove(country)
	if(len(revolutionCountries)<=1):
		maxNum=11
	else:
		maxNum=12
	
	randomChance=random.randint(1, 12)
	if(randomChance==1):
		refugees()
	elif(randomChance<=5):
		heroArises()
	elif(randomChance<=9):
		rebellion()
	elif(randomChance<=11):
		eruption()
	else:
		revolution()

	printMap()
	input("\033[0;37;49mPress Enter")
	clearScreen()

def heroArises():
	global armiesMoriatir
	global armiesArdtir
	global armiesDesich
	global armiesFadtir
	global armiesMagnollis
	global armiesEmptos
	global armiesTeracies
	global armiesTeramus
	global armiesUchelle
	global armiesDwylle
	global armiesCanolle
	global armiesIselle
	global armiesKitashi
	global armiesKitazai
	global armiesNanseshu
	global armiesNantshu
	global armiesDesiar
	global armiesEsteplana
	global armiesArenar
	global armiesCenrodad
	randomNumber=random.randint(0, len(heroCountries)-1)
	heroCountry=heroCountries[randomNumber]
	heroCountries.remove(heroCountry)
	armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
				"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
				"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
				"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
				"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
	armiesDict[heroCountry]+=200
	print("A hero convinces 200 to join the army of", heroCountry)
	armiesMoriatir=armiesDict["Moriatir"]
	armiesArdtir=armiesDict["Ardtir"]
	armiesFadtir=armiesDict["Fadtir"]
	armiesDesich=armiesDict["Desich"]
	armiesMagnollis=armiesDict["Magnollis"]
	armiesEmptos=armiesDict["Emptos"]
	armiesTeracies=armiesDict["Teracies"]
	armiesTeramus=armiesDict["Teramus"]
	armiesUchelle=armiesDict["Uchelle"]
	armiesCanolle=armiesDict["Canolle"]
	armiesIselle=armiesDict["Iselle"]
	armiesDwylle=armiesDict["Dwylle"]
	armiesKitashi=armiesDict["Kitashi"]
	armiesNanseshu=armiesDict["Nanseshu"]
	armiesNantshu=armiesDict["Nantshu"]
	armiesKitazai=armiesDict["Kitazai"]
	armiesDesiar=armiesDict["Desiar"]
	armiesEsteplana=armiesDict["Esteplana"]
	armiesCenrodad=armiesDict["Cenrodad"]
	armiesArenar=armiesDict["Arenar"]

def eruption():
	global armiesMoriatir
	global armiesArdtir
	global armiesDesich
	global armiesFadtir
	global armiesMagnollis
	global armiesEmptos
	global armiesTeracies
	global armiesTeramus
	global armiesUchelle
	global armiesDwylle
	global armiesCanolle
	global armiesIselle
	global armiesKitashi
	global armiesKitazai
	global armiesNanseshu
	global armiesNantshu
	global armiesDesiar
	global armiesEsteplana
	global armiesArenar
	global armiesCenrodad
	global deathTotal
	randomNumber=random.randint(0, len(eruptionCountries)-1)
	eruptionCountry=eruptionCountries[randomNumber]
	eruptionCountries.remove(eruptionCountry)
	armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
				"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
				"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
				"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
				"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
	if(armiesDict[eruptionCountry]>500):
		totalKilled=500
		armiesDict[eruptionCountry]-=500
	else:
		totalKilled=armiesDict[eruptionCountry]
		armiesDict[eruptionCountry]=0
	deathTotal+=totalKilled
	print("A volcano in ", eruptionCountry, " erupted and killed ", totalKilled, ".", sep="")
	armiesMoriatir=armiesDict["Moriatir"]
	armiesArdtir=armiesDict["Ardtir"]
	armiesFadtir=armiesDict["Fadtir"]
	armiesDesich=armiesDict["Desich"]
	armiesMagnollis=armiesDict["Magnollis"]
	armiesEmptos=armiesDict["Emptos"]
	armiesTeracies=armiesDict["Teracies"]
	armiesTeramus=armiesDict["Teramus"]
	armiesUchelle=armiesDict["Uchelle"]
	armiesCanolle=armiesDict["Canolle"]
	armiesIselle=armiesDict["Iselle"]
	armiesDwylle=armiesDict["Dwylle"]
	armiesKitashi=armiesDict["Kitashi"]
	armiesNanseshu=armiesDict["Nanseshu"]
	armiesNantshu=armiesDict["Nantshu"]
	armiesKitazai=armiesDict["Kitazai"]
	armiesDesiar=armiesDict["Desiar"]
	armiesEsteplana=armiesDict["Esteplana"]
	armiesCenrodad=armiesDict["Cenrodad"]
	armiesArenar=armiesDict["Arenar"]

def rebellion():
	global armiesMoriatir
	global armiesArdtir
	global armiesDesich
	global armiesFadtir
	global armiesMagnollis
	global armiesEmptos
	global armiesTeracies
	global armiesTeramus
	global armiesUchelle
	global armiesDwylle
	global armiesCanolle
	global armiesIselle
	global armiesKitashi
	global armiesKitazai
	global armiesNanseshu
	global armiesNantshu
	global armiesDesiar
	global armiesEsteplana
	global armiesArenar
	global armiesCenrodad
	global deathTotal
	randomNumber=random.randint(0, len(rebellionCountries)-1)
	rebellionCountry=rebellionCountries[randomNumber]
	rebellionCountries.remove(rebellionCountry)
	armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
				"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
				"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
				"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
				"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
	if(armiesDict[rebellionCountry]>300):
		totalKilled=300
		armiesDict[rebellionCountry]-=300
	else:
		totalKilled=armiesDict[rebellionCountry]
		armiesDict[rebellionCountry]=0
	deathTotal+=totalKilled
	print("A rebellion occured in", rebellionCountry, "and", totalKilled, "died.")
	armiesMoriatir=armiesDict["Moriatir"]
	armiesArdtir=armiesDict["Ardtir"]
	armiesFadtir=armiesDict["Fadtir"]
	armiesDesich=armiesDict["Desich"]
	armiesMagnollis=armiesDict["Magnollis"]
	armiesEmptos=armiesDict["Emptos"]
	armiesTeracies=armiesDict["Teracies"]
	armiesTeramus=armiesDict["Teramus"]
	armiesUchelle=armiesDict["Uchelle"]
	armiesCanolle=armiesDict["Canolle"]
	armiesIselle=armiesDict["Iselle"]
	armiesDwylle=armiesDict["Dwylle"]
	armiesKitashi=armiesDict["Kitashi"]
	armiesNanseshu=armiesDict["Nanseshu"]
	armiesNantshu=armiesDict["Nantshu"]
	armiesKitazai=armiesDict["Kitazai"]
	armiesDesiar=armiesDict["Desiar"]
	armiesEsteplana=armiesDict["Esteplana"]
	armiesCenrodad=armiesDict["Cenrodad"]
	armiesArenar=armiesDict["Arenar"]

def refugees():
	global armiesMoriatir
	global armiesArdtir
	global armiesDesich
	global armiesFadtir
	global armiesMagnollis
	global armiesEmptos
	global armiesTeracies
	global armiesTeramus
	global armiesUchelle
	global armiesDwylle
	global armiesCanolle
	global armiesIselle
	global armiesKitashi
	global armiesKitazai
	global armiesNanseshu
	global armiesNantshu
	global armiesDesiar
	global armiesEsteplana
	global armiesArenar
	global armiesCenrodad
	randomNumber=random.randint(0, len(refugeesCountries)-1)
	refugeesCountry=refugeesCountries[randomNumber]
	refugeesCountries.remove(refugeesCountry)
	print("A refugee crisis occured in ", refugeesCountry, ".", sep="")
	armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
				"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
				"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
				"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
				"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
	for country in adjacentCountriesDict[refugeesCountry]:
		if(armiesDict[refugeesCountry]>=50):
			armiesDict[refugeesCountry]-=50
			armiesDict[country]+=50
			print("50 people fled from ", refugeesCountry, " to ", country, ".", sep="")
	armiesMoriatir=armiesDict["Moriatir"]
	armiesArdtir=armiesDict["Ardtir"]
	armiesFadtir=armiesDict["Fadtir"]
	armiesDesich=armiesDict["Desich"]
	armiesMagnollis=armiesDict["Magnollis"]
	armiesEmptos=armiesDict["Emptos"]
	armiesTeracies=armiesDict["Teracies"]
	armiesTeramus=armiesDict["Teramus"]
	armiesUchelle=armiesDict["Uchelle"]
	armiesCanolle=armiesDict["Canolle"]
	armiesIselle=armiesDict["Iselle"]
	armiesDwylle=armiesDict["Dwylle"]
	armiesKitashi=armiesDict["Kitashi"]
	armiesNanseshu=armiesDict["Nanseshu"]
	armiesNantshu=armiesDict["Nantshu"]
	armiesKitazai=armiesDict["Kitazai"]
	armiesDesiar=armiesDict["Desiar"]
	armiesEsteplana=armiesDict["Esteplana"]
	armiesCenrodad=armiesDict["Cenrodad"]
	armiesArenar=armiesDict["Arenar"]

def revolution():
	global armiesMoriatir
	global armiesArdtir
	global armiesDesich
	global armiesFadtir
	global armiesMagnollis
	global armiesEmptos
	global armiesTeracies
	global armiesTeramus
	global armiesUchelle
	global armiesDwylle
	global armiesCanolle
	global armiesIselle
	global armiesKitashi
	global armiesKitazai
	global armiesNanseshu
	global armiesNantshu
	global armiesDesiar
	global armiesEsteplana
	global armiesArenar
	global armiesCenrodad
	global deathTotal
	randomNumber=random.randint(0, len(revolutionCountries)-1)
	revolutionCountry=revolutionCountries[randomNumber]
	revolutionCountries.remove(revolutionCountry)
	print("A revolution occured in ", revolutionCountry, ".", sep="")
	armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
				"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
				"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
				"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
				"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
	print(revolutionCountry, "is now neutral.")
	if(revolutionCountry in player1Countries):
		player1Countries.remove(revolutionCountry)
	elif(revolutionCountry in player2Countries):
		player2Countries.remove(revolutionCountry)
	elif(revolutionCountry in player3Countries):
		player3Countries.remove(revolutionCountry)
	elif(revolutionCountry in player4Countries):
		player4Countries.remove(revolutionCountry)
	neutralCountries.append(revolutionCountry)
	for country in adjacentCountriesDict[revolutionCountry]:
		if(country not in neutralCountries):
			if(armiesDict[country]>=50):
				armiesDict[country]-=50
				armiesDict[revolutionCountry]+=50
			else:
				armiesDict[revolutionCountry]+=armiesDict[country]
				armiesDict[country]=0
	armiesMoriatir=armiesDict["Moriatir"]
	armiesArdtir=armiesDict["Ardtir"]
	armiesFadtir=armiesDict["Fadtir"]
	armiesDesich=armiesDict["Desich"]
	armiesMagnollis=armiesDict["Magnollis"]
	armiesEmptos=armiesDict["Emptos"]
	armiesTeracies=armiesDict["Teracies"]
	armiesTeramus=armiesDict["Teramus"]
	armiesUchelle=armiesDict["Uchelle"]
	armiesCanolle=armiesDict["Canolle"]
	armiesIselle=armiesDict["Iselle"]
	armiesDwylle=armiesDict["Dwylle"]
	armiesKitashi=armiesDict["Kitashi"]
	armiesNanseshu=armiesDict["Nanseshu"]
	armiesNantshu=armiesDict["Nantshu"]
	armiesKitazai=armiesDict["Kitazai"]
	armiesDesiar=armiesDict["Desiar"]
	armiesEsteplana=armiesDict["Esteplana"]
	armiesCenrodad=armiesDict["Cenrodad"]
	armiesArenar=armiesDict["Arenar"]

def printStats():
	global player1
	global player1TotalArmies
	global player1ExtraSoldiers
	global player2
	global player2TotalArmies
	global player2ExtraSoldiers
	global player3
	global player3TotalArmies
	global player3ExtraSoldiers
	global player4
	global player4TotalArmies
	global player4ExtraSoldiers
	global deathTotal
	global neutralTotalArmies
	checkTotalArmies()
	if(player1!=0):
		print("\033[0;31;49m", player1, sep="")
		print("Total Armies:", player1TotalArmies)
		print("Countries:", len(player1Countries))
	if(player2!=0):
		print("\033[0;32;49m", player2, sep="")
		print("Total Armies:", player2TotalArmies)
		print("Countries:", len(player2Countries))
	if(player3!=0):
		print("\033[0;34;49m", player3, sep="")
		print("Total Armies:", player3TotalArmies)
		print("Countries:", len(player3Countries))
	if(player4!=0):
		print("\033[0;35;49m", player4, sep="")
		print("Total Armies:", player4TotalArmies)
		print("Countries:", len(player4Countries))
	if(len(neutralCountries)>0):
		print("\033[0;37;49mNeutral Countries")
		print("Total Armies:", neutralTotalArmies)
		print("Countries:", len(neutralCountries))
	print("\033[0;37;49mDeath Total:", deathTotal)
	input("Press Enter")
	clearScreen()

def checkTotalArmies():
	global player1TotalArmies
	global player2TotalArmies
	global player3TotalArmies
	global player4TotalArmies
	global neutralTotalArmies
	player1TotalArmies=0
	player2TotalArmies=0
	player3TotalArmies=0
	player4TotalArmies=0
	neutralTotalArmies=0
	armiesDict={"Moriatir":armiesMoriatir, "Ardtir":armiesArdtir, "Desich":armiesDesich, "Fadtir":armiesFadtir,
				"Magnollis":armiesMagnollis, "Emptos":armiesEmptos, "Teracies":armiesTeracies, "Teramus":armiesTeramus,
				"Uchelle":armiesUchelle, "Dwylle":armiesDwylle, "Iselle":armiesIselle, "Canolle":armiesCanolle,
				"Kitashi":armiesKitashi, "Kitazai":armiesKitazai, "Nanseshu":armiesNanseshu, "Nantshu":armiesNantshu,
				"Desiar":armiesDesiar, "Esteplana":armiesEsteplana, "Arenar":armiesArenar, "Cenrodad":armiesCenrodad}
	for country in countries:
		if(country in player1Countries):
			player1TotalArmies+=armiesDict[country]
		elif(country in player2Countries):
			player2TotalArmies+=armiesDict[country]
		elif(country in player3Countries):
			player3TotalArmies+=armiesDict[country]
		elif(country in player4Countries):
			player4TotalArmies+=armiesDict[country]
		else:
			neutralTotalArmies+=armiesDict[country]
	
#MAIN FUNCTION
def main():
	global player1
	global player1StartingCountry
	global player2
	global player2StartingCountry
	global player3
	global player3StartingCountry
	global player4
	global player4StartingCountry
	loadMapPieces()
	
	mapFile=open("map.txt", "r")
	if mapFile.mode=="r":
		global map
		map=mapFile.read()
	clearScreen()
	intro()
	
	global players
	players=sanitisedInput("How many players are playing: ", int, 2, 4)
	clearScreen()
	createPlayers(players)
	if(players==2):
		print("Welcome ", player1, " and ", player2, ",", sep="", end="")
	if(players==3):
		print("Welcome ", player1, ", ", player2, ", and ", player3, ",", sep="", end="")
	elif(players==4):
		print("Welcome ", player1, ", ", player2, ", ", player3, ", and ", player4, ",", sep="", end="")
	print(" to Kingdom of War.")
	print("\033[0;31;49m", player1, " : Red", sep="")
	print("\033[0;32;49m", player2, " : Green", sep="")
	if(players>=3):
		print("\033[0;34;49m", player3, " : Blue", sep="")
	if(players==4):
		print("\033[0;35;49m", player4, " : Purple", sep="")
	print("\033[0;37;49mNeutral : White")
	input("\033[0;37;49mPress Enter")
	clearScreen()

	printMap()
	input("Press Enter")
	clearScreen()

	ended=False
	while(ended==False):
		playerTurns()
		totIn=0
		if(player1!=0):
			totIn+=1
		if(player2!=0):
			totIn+=1
		if(player3!=0):
			totIn+=1
		if(player4!=0):
			totIn+=1
		if(totIn==1):
			ended=True
	printMap()
	if(player1!=0):
		print("\033[0;31;49m", player1, sep="", end=" ")
		farewellCountry=player1StartingCountry
	elif(player2!=0):
		print("\033[0;32;49m", player2, sep="", end=" ")
		farewellCountry=player2StartingCountry
	elif(player3!=0):
		print("\033[0;34;49m", player3, sep="", end=" ")
		farewellCountry=player3StartingCountry
	elif(player4!=0):
		print("\033[0;35;49m", player4, sep="", end=" ")
		farewellCountry=player4StartingCountry
	print("""won the game!!!
Congrats! Your hard work and superior abilities prevaled!
You vanquished your opponents, decimating their countries,
who stood no change against you!
""")
	print("Unfortuately, not all is well, as a total of", deathTotal, "soldiers died.")
	print("""These grave loses mark the tragedy of this war.
""")
	print("Farewell, and may the spirit of", farewellCountry, "forever be with you.")

#RUN MAIN FUNCTION
if __name__=="__main__":
	main()