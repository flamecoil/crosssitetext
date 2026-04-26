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
QUICK_GUIDE_FILE 	 	= '__QUICKSTART.txt'

INPUT_COMMAND 	= 'input!'
OUTPUT_COMMAND 	= 'output!'

CUSTOM_FILENAMEOUT = ''

SITE_NAMES 	= ['FURAFFINITY', 'INKBUNNY', 'WEASYL', 'FURRYNETWORK', 'SOFURRY']
SITES_MD 		= ['FURRYNETWORK', 'WEASYL']
SITES_BBC 		= ['FURAFFINITY', 'INKBUNNY', 'SOFURRY']
#Indeces to keep track of where each site lies. 
FA_INDEX = SITE_NAMES.index('FURAFFINITY')
IB_INDEX = SITE_NAMES.index('INKBUNNY')
W_INDEX = SITE_NAMES.index('WEASYL')
FN_INDEX = SITE_NAMES.index('FURRYNETWORK')
SF_INDEX = SITE_NAMES.index('SOFURRY')

#URLS
URL_FA 	= "http://www.furaffinity.net/" 		#www.furaffinity.net/user/flamecoil/
URL_IB 	= "https://inkbunny.net/"  				#inkbunny.net/flamecoil
URL_W  	= "https://www.weasyl.com/~" 			#www.weasyl.com/~flamecoil
URL_FN 	= "https://furrynetwork.com/" 			#furrynetwork.com/flamecoil/
URL_SF 	= ".sofurry.com/" 						#flamecoil.sofurry.com


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

FN_TEXT_PROFILE = 'fn!'
FN_ICON_PROFILE = 'fnicon!'
FN_BOTH_PROFILE = 'fnboth!'
FN_PROFILES = [FN_TEXT_PROFILE, FN_ICON_PROFILE, FN_BOTH_PROFILE]

SF_TEXT_PROFILE = 'sf!'
SF_ICON_PROFILE = 'sficon!'
SF_BOTH_PROFILE = 'sfboth!'
SF_PROFILES = [SF_TEXT_PROFILE, SF_ICON_PROFILE, SF_BOTH_PROFILE]

GEN_TEXT_PROFILE = 'gen!'
GEN_ICON_PROFILE = 'genicon!'
GEN_BOTH_PROFILE = 'genboth!'
GEN_PROFILES = [GEN_TEXT_PROFILE, GEN_ICON_PROFILE, GEN_BOTH_PROFILE]


GEN_LINK 		= 'link!' 			#Don't store any reference, just use the link.
FA_REF_LINK 	= 'faref!' 		#Use/Store a link to an FA page.
IB_REF_LINK 	= 'ibref!' 		#Use/Store a link to an IB page
W_REF_LINK 	= 'wref!' 		 	#Use/Store a link to a Weasyl page.
FN_REF_LINK 	= 'fnref!' 		#Use/Store a link to a FurryNetwork page.
SF_REF_LINK 	= 'sfref!' 		#Use/Store a link to a SoFurry page.

GEN_REF_LINK 	= 'genref!' 	#Use the reference based on the website
NAME_REF 		= 'name!'
REF_CHANGE 	= False

REF_LINKS = [GEN_REF_LINK, FA_REF_LINK, IB_REF_LINK, W_REF_LINK, FN_REF_LINK, SF_REF_LINK]
REF_LOG = [NAME_REF, FA_REF_LINK, W_REF_LINK, IB_REF_LINK, GEN_REF_LINK]
