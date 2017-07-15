# -*- coding: utf-8 -*-
"""
Spyder Editor
@author flamecoil
"""

import os

"""
General Goal
Create general expressions that are able to be interpreted and reformatted to:
	Furaffinity
	Weasyl
	Inkbunny
Support for:
	URL
	Profile Links:
		Text
		Icon
		Text+Icon
	Character References
"""
DEFAULT_FILENAMEOUT 	= '_output.txt'
DEFAULT_FILENAMEIN 	= '_input.txt'
REFS_FILE 				= '_refs.txt'

INPUT_COMMAND 	= 'input!'
OUTPUT_COMMAND 	= 'output!'

CUSTOM_FILENAMEOUT = ''

SITE_NAMES = ['FURAFFINITY', 'INKBUNNY', 'WEASYL']
#Indeces to keep track of where each site lies. 
FA_INDEX = SITE_NAMES.index('FURAFFINITY')
IB_INDEX = SITE_NAMES.index('INKBUNNY')
W_INDEX = SITE_NAMES.index('WEASYL')
#EXPRESSION TYPES
FA_TEXT_PROFILE = 'fa!'
FA_ICON_PROFILE = 'faicon!'
FA_BOTH_PROFILE = 'faboth!'
FA_PROFILES = [FA_TEXT_PROFILE, FA_ICON_PROFILE, FA_BOTH_PROFILE]

IB_TEXT_PROFILE = 'ib!'
IB_ICON_PROFILE = 'ibicon!'
IB_BOTH_PROFILE = 'ibboth!'
IB_PROFILES = [IB_TEXT_PROFILE, IB_ICON_PROFILE, IB_BOTH_PROFILE]

W_TEXT_PROFILE = 'w!'
W_ICON_PROFILE = 'wicon!'
W_BOTH_PROFILE = 'wboth!'
W_PROFILES = [W_TEXT_PROFILE, W_ICON_PROFILE, W_BOTH_PROFILE]

GEN_TEXT_PROFILE = 'gen!'
GEN_ICON_PROFILE = 'genicon!'
GEN_BOTH_PROFILE = 'genboth!'
GEN_PROFILES = [GEN_TEXT_PROFILE, GEN_ICON_PROFILE, GEN_BOTH_PROFILE]

GEN_LINK 		= 'link!' 			#Don't store any reference, just use the link.
FA_REF_LINK 	= 'faref!' 		#Use/Store a link to an FA page.
IB_REF_LINK 	= 'ibref!' 		#Use/Store a link to an IB page
W_REF_LINK 	= 'wref!' 		#Use/Store a link to a Weasyl page.
GEN_REF_LINK 	= 'genref!' 	#Use the reference based on the website
NAME_REF 		= 'name!'
REF_CHANGE 	= False

REF_LINKS = [GEN_REF_LINK, FA_REF_LINK, IB_REF_LINK, W_REF_LINK]
REF_LOG = [NAME_REF, FA_REF_LINK, W_REF_LINK, IB_REF_LINK, GEN_REF_LINK]

#TEST VARIABLES

charReference = {}
"""
Profile Link Expectation
"""
"""
faProfileLink:
	Take in Text
	Output the appropriate link that will guide to an FA page:
		FA - :icon<Name>:
		Weasyl & IB - URL:
			Weasyl - 	<fa:<Name>>
			Inkbunny - fa!name
"""
def faProfileLink(inText, website='FURAFFINITY'):
	
	splitExpr = inText.split('!')
	linkVariant = splitExpr[0]
	profileName = splitExpr[1]
	
	profileLink = 'UNDETERMINED-FALINK'
	
	#FA Replacement
	if website == 'FURAFFINITY':
		if linkVariant == 'fa':
			profileLink = '@{}'.format(profileName)
		elif linkVariant == 'faicon':
			profileLink = ':{}icon:'.format(profileName)
		elif linkVariant == 'faboth':
			profileLink = ':icon{}:'.format(profileName)
		else:
			print("faProfileLink ----- No valid linkVariant input | ({}).".format(linkVariant))
		
	elif website == 'INKBUNNY':
		profileLink = 'fa!{}'.format(profileName)
		
	elif website == 'WEASYL':
		profileLink = '<fa:{}>'.format(profileName)
		
	else:
		print("faProfileLink ----- No valid website input.")
	
	return profileLink


"""
ibProfileLink:
	Take in Text
	Output the appropriate link that will guide to an IB page:
		FA 	- fa!name
		W 	- w!name
		IB:
			name - ib!name
			icon - [icon]name[/icon]
			both - @name
		
"""
def ibProfileLink(inText, website='FURAFFINITY'):
	
	splitExpr = inText.split('!')
	linkVariant = splitExpr[0]
	profileName = splitExpr[1]
	
	profileLink = 'UNDETERMINED-IBLINK'
	
	#FA Replacement
	if website == 'FURAFFINITY':
		profileLink = "[url=https://inkbunny.net/{}]{}[/url]".format(profileName, profileName)
		
	elif website == 'INKBUNNY':
		if linkVariant == 'ib':
			profileLink = 'ib!{}'.format(profileName)
		elif linkVariant == 'ibicon':
			profileLink = '[icon]{}[/icon]'.format(profileName)
		elif linkVariant == 'ibboth':
			profileLink = '@{}'.format(profileName)
		else:
			print("faProfileLink ----- No valid linkVariant input | ({}).".format(linkVariant))
#		profileLink = 'fa!{}'.format(profileName)
		
	elif website == 'WEASYL':
		profileLink = '<ib:{}>'.format(profileName)
		
	else:
		print("ibProfileLink ----- No valid website input.")
	
	return profileLink


"""
weasylProfileLink:
	Take in Text
	Output the appropriate link that will guide to an IB page:
		FA - [url=https://www.weasyl.com/~name]name[/url]
		IB - w!name
		Weasyl:
			name - <~name>
			icon - <!name>
			both - <!~name>
"""
def wProfileLink(inText, website='FURAFFINITY'):
	
	splitExpr = inText.split('!')
	linkVariant = splitExpr[0]
	profileName = splitExpr[1]
	
	profileLink = 'UNDETERMINED-WEASYLLINK'
	
	#FA Replacement
	if website == 'FURAFFINITY':
		profileLink = "[url=https://www.weasyl.com/~{}]{}[/url]".format(profileName, profileName)
		
	elif website == 'INKBUNNY':
		profileLink = 'w!{}'.format(profileName)
		
	elif website == 'WEASYL':
		if linkVariant == 'w':
			profileLink = '<~{}>'.format(profileName)
		elif linkVariant == 'wicon':
			profileLink = '<!{}>'.format(profileName)
		elif linkVariant == 'wboth':
			profileLink = '<!~{}>'.format(profileName)
		else:
			print("faProfileLink ----- No valid linkVariant input | ({}).".format(linkVariant))
		
	else:
		print("ibProfileLink ----- No valid website input.")
	
	return profileLink

"""
General Profile Link
This special case is to be used in specific cases where the username of a profile
matches across each site. As such, the passed in username will be formatted to the proper website.
"""
def genProfileLink(inText, website='FURAFFINITY'):
	
	splitExpr = inText.split('!')
	linkVariant = splitExpr[0]
	profileName = splitExpr[1]
	
	profileLink = 'UNDETERMINED-GENLINK'
	
	if website == 'FURAFFINITY':
		if linkVariant == 'gen':
			profileLink = '@{}'.format(profileName)
		elif linkVariant == 'genicon':
			profileLink = ':{}icon:'.format(profileName)
		elif linkVariant == 'genboth':
			profileLink = ':icon{}:'.format(profileName)
		else:
			print("faProfileLink ----- No valid linkVariant input | ({}).".format(linkVariant))
	
	elif website == 'INKBUNNY':
		if linkVariant == 'gen':
			profileLink = 'ib!{}'.format(profileName)
		elif linkVariant == 'genicon':
			profileLink = '[icon]{}[/icon]'.format(profileName)
		elif linkVariant == 'genboth':
			profileLink = '@{}'.format(profileName)
		else:
			print("faProfileLink ----- No valid linkVariant input | ({}).".format(linkVariant))

	elif website == 'WEASYL':
		if linkVariant == 'gen':
			profileLink = '<~{}>'.format(profileName)
		elif linkVariant == 'genicon':
			profileLink = '<!{}>'.format(profileName)
		elif linkVariant == 'genboth':
			profileLink = '<!~{}>'.format(profileName)
		else:
			print("faProfileLink ----- No valid linkVariant input | ({}).".format(linkVariant))
			
	else:
		print("genProfileLink ----- No valid website input.")
	
	return profileLink

"""
Take a combo of a name and link to a reference and turn it into an appropriate
link and description.
Expected input: ref!description|link
Return Value: Formatted link
"""
def generateLink(inText, website=SITE_NAMES[0]):
	
	refCombo = inText.split('!')[1] 
	refCombo = refCombo.split('|')
	description = refCombo[0]
	link = refCombo[1]
	
	regularLink = 'UNDETERMINED REFERENCE LINK'
	
	if website == 'FURAFFINITY' or website == 'INKBUNNY':
		regularLink = '[url={}]{}[/url]'.format(link, description)
	elif website == 'WEASYL':
		regularLink = '[{}]({})'.format(description,link)
	
	return regularLink
	

"""
TODO: Make a way to store references from previous characters used.
When a reference is used for a specific site, pull it into a dictionary
of characters and store it properly. 
Declaration of each new dictionary should be the size of SITE_NAMES (the num
of sites that are supported.)
Key: charName
value: List of references, ordered by SITE_NAMES

RETURN VALUE: 
	Appropriate link to use.
"""
def siteReferenceLink(inText, website=SITE_NAMES[0]):
	
	textSplit = inText.split('!') #0 - which ref type #1 - Character + link
	refType = textSplit[0]
	#Store references when there're three parts.
	if '|' in textSplit[1]:
		refSplit = textSplit[1].split('|')
		charName = refSplit[0]
		link = refSplit[1]
		
		storeRef(refType, charName, link)
	#Fetch references when there's only 2. refType!Name
	else:
		charName = textSplit[1]
		link = fetchRef(refType, charName, website)
		
	if link == '':
		return link
	if website == 'FURAFFINITY' or website == 'INKBUNNY':
		refLink = '[url={}]{}[/url]'.format(link, charName)
	elif website == 'WEASYL':
		refLink = '[{}]({})'.format(charName,link)
	
	
	return refLink

"""
Takes and stores a link from the format of:
	referencetype!CharacterName|URL
	
Any characters that exist in the dictionary will have their links UPDATED.
GEN shouldn't work here.
"""
def storeRef (refType, charName, link):
	
	faRef 		= FA_REF_LINK.strip('!') 
	wRef 		= W_REF_LINK.strip('!')
	ibRef 		= IB_REF_LINK.strip('!')
	
	if charName not in charReference.keys():
		#Create a new entry in the reference list.
		charReference[charName] = [''] * len(SITE_NAMES)
		#Insert the link at the right spot.
	if refType == faRef:
		charReference[charName][FA_INDEX] = link
	elif refType == wRef:
		charReference[charName][W_INDEX] = link
	elif refType == ibRef:
		charReference[charName][IB_INDEX] = link
	else:
		print("useLink -- reference type not valid.")
		return
	
	REF_CHANGE = True
	
	return

"""
If a character is called upon, fetch the correct link to be used. 
"""
def fetchRef (refType, charName, website=SITE_NAMES[0]):
	
	if charName not in charReference.keys():
		return 'fetchRef_NOT_IN_USERS'
	
	faRef 		= FA_REF_LINK.strip('!') 
	wRef 		= W_REF_LINK.strip('!')
	ibRef 		= IB_REF_LINK.strip('!')
	genRef 	= GEN_REF_LINK.strip('!')
	
		#Insert the link at the right spot.
	refLink = 'fetchRef - INVALID'
		
	if refType == faRef:
		refLink = charReference[charName][FA_INDEX]
	elif refType == wRef:
		refLink = charReference[charName][W_INDEX]
	elif refType == ibRef:
		refLink = charReference[charName][IB_INDEX] 
	elif refType == genRef:
		websiteIndex = SITE_NAMES.index(website)
		refLink = charReference[charName][websiteIndex]
		if refLink == '':
			for site in SITE_NAMES:
				curRef = charReference[charName][SITE_NAMES.index(site)]
				if curRef != '':
					return curRef
			
	else:
		print('fetchRef -- no proper refType.')
		
	
	return refLink

def textReplacement(textIn, sitename=SITE_NAMES[0]):
	
	text = textIn.split()	
	
	newText = ''
	
	#iterate through 
	for word in text:
		#Iterate through the FA Profile formats
		if '!' in word:
			exprFound = False
			
			if exprFound == False:
				for genProfile in GEN_PROFILES:
					if genProfile in word:
						newText+= '{} '.format(genProfileLink(word, sitename))
						exprFound = True
						break
			
			if exprFound == False:
				for faProfile in FA_PROFILES:											#check word against profiles
					if faProfile in word:												
	#					print(faProfileLink(word, "INKBUNNY"))
						newText+= '{} '.format(faProfileLink(word, sitename))		#run FA link
						exprFound = True 												# Halt later checks.
						break
			
			if exprFound == False:
				for ibProfile in IB_PROFILES:
					if ibProfile in word:
						newText+= '{} '.format(ibProfileLink(word, sitename))
						exprFound = True
						break
			
			if exprFound == False:
				for wProfile in W_PROFILES:
					if wProfile in word:
						newText+= '{} '.format(wProfileLink(word, sitename))
						exprFound = True
						break
					
			if exprFound == False:
				if GEN_LINK in word:
					newText += '{} '.format(generateLink(word, sitename))
					exprFound = True
				
			
			if exprFound == False:
				newText += '{} '.format(word)
				
			
			
		else:
			newText += '{} '.format(word)	
	
	return newText

def fileTextReplacement(fileIn, sitename=SITE_NAMES[0]):
	
#	text = textIn.split()	
	
	newText = ''
	outputFilename = ''
	
	fileIn.seek(0,0)
	
	#iterate through
	for text in fileIn: 

		words = text.split()
		for word in words:
			#Iterate through the FA Profile formats
			if '!' in word:
				exprFound = False
				
				if exprFound == False:
					if OUTPUT_COMMAND in word:
						outputFilename = changeOutputFile(word)
#						print("OUTPUT FILE: {}".format(outputFilename)
						exprFound = True
						continue
				
				if exprFound == False:
					for genProfile in GEN_PROFILES:
						if genProfile in word:
							newText+= '{} '.format(genProfileLink(word, sitename))
							exprFound = True
							continue
				
				if exprFound == False:
					for faProfile in FA_PROFILES:											#check word against profiles
						if faProfile in word:												
		#					print(faProfileLink(word, "INKBUNNY"))
							newText+= '{} '.format(faProfileLink(word, sitename))		#run FA link
							exprFound = True 												# Halt later checks.
							continue
				
				if exprFound == False:
					for ibProfile in IB_PROFILES:
						if ibProfile in word:
							newText+= '{} '.format(ibProfileLink(word, sitename))
							exprFound = True
							continue
				
				if exprFound == False:
					for wProfile in W_PROFILES:
						if wProfile in word:
							newText+= '{} '.format(wProfileLink(word, sitename))
							exprFound = True
							continue
						
				if exprFound == False:
					if GEN_LINK in word:
						newText += '{} '.format(generateLink(word, sitename))
						exprFound = True
						continue
						
				if exprFound == False:
					for linkExpr in REF_LINKS:
						if linkExpr in word:
							link = siteReferenceLink(word, sitename)
							if link != '':
								newText += '{} '.format(link)
							exprFound = True 
							continue
					
				
				if exprFound == False:
					newText += '{} '.format(word)
				
			else:
				newText += '{} '.format(word)	
				
			if '\n' in word:
				print("ENDLINE HERE")
			
		newText += '\n'
		
	return newText, outputFilename

def allSiteTexts(inText):
	
	for site in SITE_NAMES:
		print('\t====={}====='.format(site))
#		print(textReplacement("Hey! The time is now for me to go talk to genboth!flamecoil -- he's ref!Charkol's|https://inkbunny.net/submissionview.php?id=1129778 creator.\n", sitename=site)
		print(textReplacement("genboth!flamecoil",sitename=site))
		print()
	
	return

def fileAllSiteTexts(inFile):
	texts = []
#	for site in SITE_NAMES:
#		outFile.write('\t===== {} ====='.format(site))
#	#	print(textReplacement("Hey! The time is now for me to go talk to genboth!flamecoil -- he's ref!Charkol's|https://inkbunny.net/submissionview.php?id=1129778 creator.\n", sitename=site)
#		outFile.write(fileTextReplacement(inFile,sitename=site))
#		outFile.write('\n')
	outputFilename = ''
	curText = ''
	for site in SITE_NAMES:
		curText = '\t===== {} =====\n'.format(site)
		curSiteText, tempOutputFilename = fileTextReplacement(inFile, sitename=site)
		if tempOutputFilename != '':
			outputFilename = tempOutputFilename
		curText += curSiteText
		curText += '\n\n'
		texts.append(curText)	
	
	return texts, outputFilename

def writeInputExample(inFile):
	
	inFile.write(inputExample)
	
	return

def changeOutputFile(inText):
	
	splitExpr = inText.split('!')
	outputFilename = splitExpr[1]
	if '.' not in outputFilename:
		outputFilename += '.txt'
	
	return outputFilename

def readReferencesFile(inFilename):
#	REF_LOG = [NAME_REF, FA_REF_LINK, W_REF_LINK, IB_REF_LINK]
	
	nameRef 	= NAME_REF.strip('!')
	faRef 		= FA_REF_LINK.strip('!') 
	wRef 		= W_REF_LINK.strip('!')
	ibRef 		= IB_REF_LINK.strip('!')	
	
	inFile = open(inFilename, 'r')
	curName = None
	
	for line in inFile:
		curLine = line.split()
		
		#Determine which type of reference it is.
		for word in curLine:
			if '!' in word:
				splitRef = word.split('!')
				typeRef = splitRef[0]
				link = splitRef[1]
				
				if typeRef == nameRef:
					curName = link
					if curName not in charReference.keys():
						charList = [''] * len(SITE_NAMES)
						charReference[curName] = charList
					continue
				elif typeRef == faRef and curName is not None:
					#If an FA Reference, take the link and insert it into the active Character.
					charReference[curName][FA_INDEX] = link					
					continue
				elif typeRef == wRef and curName is not None:
					charReference[curName][W_INDEX] = link	
					continue
				elif typeRef == ibRef and curName is not None:
					charReference[curName][IB_INDEX] = link	
					break
				else:
					curName = None
					break
	
	
	inFile.close()
	
	return

def writeReferencesFile(inDict=charReference):
	
	outFile = open(REFS_FILE, 'w')
	
	for entry in inDict:
		curRefList = charReference[entry]
		outFile.write('{}{}\n'.format(NAME_REF, entry))
		outFile.write(('{}{}\n'.format(FA_REF_LINK, curRefList[FA_INDEX])))
		outFile.write(('{}{}\n'.format(IB_REF_LINK, curRefList[IB_INDEX])))
		outFile.write(('{}{}\n'.format(W_REF_LINK, curRefList[W_INDEX])))
		outFile.write('\n')
	
	outFile.close()
	return

def main():
#	for site in SITE_NAMES:
#		print('\t====={}====='.format(site))
##		print(textReplacement("Hey! The time is now for me to go talk to genboth!flamecoil -- he's ref!Charkol's|https://inkbunny.net/submissionview.php?id=1129778 creator.\n", sitename=site)
#		print(textReplacement("genboth!flamecoil",sitename=site))
#		print()
	
	readReferencesFile(REFS_FILE)
	if os.path.isfile(DEFAULT_FILENAMEIN):
		inFile = open(DEFAULT_FILENAMEIN, 'r')
	else:
		inFile = open(DEFAULT_FILENAMEIN, 'w')
		inFile.write(inputExample)
		inFile.close()
		inFile = open(DEFAULT_FILENAMEIN, 'r')
	
#	allSiteTexts('genboth!flamecoil')
	texts, outputFilename = fileAllSiteTexts(inFile)
	
	if outputFilename == '':	
		outFile = open(DEFAULT_FILENAMEOUT, 'w')
	else:
		outFile = open(outputFilename, 'w')
		print("OUTPUT FILE: {}".format(outputFilename))

	for text in texts:
		outFile.write(text)
	
	
#	for entry in charReference:	
#		curRefList = charReference[entry]
#		
#		print('{}{}\n'.format(FA_REF_LINK, curRefList[FA_INDEX]))
#		print('{}{}\n'.format(IB_REF_LINK, curRefList[IB_INDEX]))
#		print('{}{}\n'.format(W_REF_LINK, curRefList[W_INDEX]))
#		
#		print(charReference[entry])
	
	if REF_CHANGE:
		writeReferencesFile()
	
	outFile.close()
	inFile.close()

	return




'''
INPUT EXAMPLE
'''
inputExample = """output!Introduction Hello there! genboth!Flamecoil here. Use this program to easily draft texts between FA, IB, and Weasyl! Instructions
are in the README. Replace all this text here and run the python script again to get you going!"""



main()

