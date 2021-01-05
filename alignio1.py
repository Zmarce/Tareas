from Bio import AlingIO
aligment = AlignIO.read("PF05371_seed.sth", "stockholm")

print ("Aligment length %i" % aligment.get_aligment_length())
