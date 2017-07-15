README - USING THE MULTISITE TEXT GENERATOR

THIS PROGRAM IS INTENDED TO USE IT'S OWN SYNTAX IN ORDER
TO PRODUCE THE STYLES OF BBCODE AND MARKDOWN TO EASILY
POST ON FURAFFINITY, INKBUNNY AND WEASYL.
NOTE: THE SYNTAX USED BORROWS FROM INKBUNNY'S FORMAT. 

THERE ARE 2 TYPES OF COMMANDS THAT THIS PROGRAM UNDERSTANDS.
- PROFILE LINKS
- REFERENCE LINKS

	=== PROFILE LINKS ===
Profile links indicate the insertion of a link out to a specific website.
- Websites: Furaffinity (fa), Inkbunny(ib), and Weasyl(w)

Each website has multiple types of links that are available, involving
text and the icon of the user.
- Link Types:
	Text-Only - Only the text of the username appears.
	Icon-Only - Only the icon of the username appears.
	Both	  - The text and icon of the username appears. 

*NOTE: The specific link types are interpreted for each 

=== HOW TO USE PROFILE LINKS

Each profile link is made up of two components: the site being directed to,
and the type of link that you wish to use.

FORMAT: <website+type>!<username>
	website 	- fa, ib, w, gen
	variants	- icon, both
	NOTE: 

USAGE: 
	INPUT: 		fa!flamecoil	faicon!flamecoil	genboth!flamecoil
	OUTPUT:
		FA:	@flamecoil 	:flamecoilicon: 	:iconflamecoil:
		IB:	fa!flamecoil 	fa!flamecoil		@flamecoil 
		W:	<fa:flamecoil> 	<fa:flamecoil>		<!~flamecoil> 
NOTES
- Even if there is no ability to utilize an icon from one site to another (i.e. FA to a Weasyl
profile), the program will produce a link properly. Yet, 

	=== REFERENCE LINKS ===
    
Reference links are for providing a link 