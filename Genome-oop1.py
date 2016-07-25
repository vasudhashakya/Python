

class Genome:
	x=0
	
	def __init__(self):
		print "I am constructed"
		
	def sequence(self):
		self.x +=1
		print "Sequence no.so far", self.x
		
	def __del__(self):
		print "destructed",self.x
gs=Genome()
print "\n\n/*****Info on genome class****\\\n\n"
print "Type",type(gs)
print "Dir",dir(gs)


gs.sequence()
gs.sequence()
gs.sequence()