

class Location():
	"""docstring for Location"""
	def __init__(self, area, room, rates = None):
		self.area = area
		self.north = None
		self.west = None
		self.east = None
		self.south = None
		self.room = room
		if area == 0:
			self.name = 'Heaven'
			if rates == None:
				self.rates = 30
			else:
				self.rates = rates

		if area == 1:
			self.name = 'Solstice Chambere'

	

			
Hgate = Location(0,'Heavens Gate',0)
Gthresh = Location(0,'Glistening Threshold')
Bopp = Location(0,'Bridge of Opportunity')
Donus = Location(0,'Depression of Onus')
Tonus = Location(0,'Terminus of Onus')
Cfate = Location(0,'Crossroads of Fate', 100)
FCS = Location(0,'Fates Coil: South')
FCSW = Location(0,'Fates Coil: South West')
FCW = Location(0,'Fates Coil: West')
FCNW = Location(0,'Fates Coil: North West')
FCN = Location(0,'Fates Coil: North')
FCNE = Location(0,'Fates Coil: North East')
FCE = Location(0,'Fates Coil: East')
Rpast = Location(0,'Realities Pasture')
Scham = Location(1,'Solstice Chambere', 0)

Hgate.north = Gthresh
Gthresh.south = Hgate
Gthresh.north = Bopp
Bopp.south = Gthresh
Bopp.east = Donus
Bopp.west = Cfate
Donus.west = Bopp
Donus.north = Tonus
Tonus.south = Donus
Cfate.east = Bopp
Cfate.north = FCE
Cfate.west = FCS
FCS.west = FCSW
FCS.east = Cfate
FCSW.east = FCS
FCSW.north = FCW
FCW.south = FCSW
FCW.north = FCNW
FCNW.south = FCW
FCNW.north = Scham
FCNW.east = FCN
Scham.south = FCNW
FCN.west = FCNW
FCN.east = FCNE
FCNE.west = FCN
FCNE.east = Rpast
FCNE.south = FCE
Rpast.west = FCNE
FCE.north = FCNE
FCE.south = Cfate


