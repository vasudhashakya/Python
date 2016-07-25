

class Genome:
	x=0
	name=""
	def __init__(self,category):
		self.name=category
		print "constructed: in category",self.name
		
		
	def sequence(self):
		self.x +=1
		print "Sequence no.so far", self.x
		
	def __del__(self):
		print "destructed",self.x

		
gs=Genome("category1")
print "\n\n/*****Info on genome class****\\\n\n"
print "Type",type(gs)
print "Dir",dir(gs)

gs.sequence()
gs.sequence()
gs.sequence()

gs=Genome("category2")
gs.sequence()
gs.sequence()
gs.sequence()