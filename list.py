adnseq = ["A", "C", "T", "G", "A", "T", "G", "T", "A", "C"]
adnseq2 = ["T", "G", "A", "T", "G"]

n = len(adnseq)

#print adnseq
#print " length = ",n

#print " First position = ", adnseq[0]
#print " Last position = ", adnseq[n-1]
#print " First 3 position = ", adnseq[0:3]
#print " Last 5 position = ", adnseq[-5:]

#print "insert one item..."
#adnseq.append ("T")
#n = len(adnseq)
#print adnseq
#print " Length ",n

#print " Replace first position with T "
adnseq[0] = "T"
#print adnseq

#print "Delete last position"
adnseq.pop(n-1)
#print adnseq

print "newadnseq = seq1 + seq2"
newadnseq = adnseq + adnseq2
print adnseq
print adnseq2
print newadnseq
print "Length = ", len(newadnseq)
