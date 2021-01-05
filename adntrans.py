nucleotides = ["A", "C", "T", "G"]

nucl_complement = {
	"A":"T",
	"C":"G",
	"T":"A",
	"G":"C"
	}

rna_complement = {
	 "A":"U",
	 "C":"G",
         "T":"A",
         "G":"C"
	 }

nucl_codon = [];

dna = "ACCGTT"
dna_complement = ""
rna = ""

# complementary seq 
#
for x in dna:
  dna_complement = dna_complement + nucl_complement[x]
x# files
# dna example
#

nucleotides = ["A", "C", "T", "G"]

nucl_complement = {
               "A":"T",
               "C":"G",
               "T":"A",
               "G":"C"
              }

rna_transcription = {
               "A":"A",
               "C":"C",
               "T":"U",
               "G":"G"
              }


nucl_codon = [];

dna = "ACCGTT"
dna_complement = ""
rna = ""

# complementary seq 
#
for x in dna:
  dna_complement = dna_complement + nucl_complement[x]
n = len(dna)
print " dna length  = ", n

n = len(dna_complement)
print " dna length complementary  = ", n


for i in range(0, n):
  print i, dna[i], dna_complement[i]

print "dna, dna complementary : "
print dna
print dna_complement

for x in dna:
	rna = rna + rna_transcription[x]

print "rna"
print rna[::-1]

codons = {
  "UUU": "Fenilalanina",
  "UUC": "Fenilalanina",
  "UUA": "Leucina",
  "UUG": "Leucina",
  "UCU": "Serina",
  "UCC": "Serina",
  "UCA": "Serina",
  "UCG": "Serina",
  "UAU": "Tirosina",
  "UAC": "Tirosina",
  "UAA": "Codon de terminacion ocre",
  "UAG": "Codon de terminacin Ambar",
  "UGU": "Cisteina",
  "UGC": "Cisteina",
  "UGA": "Codon de terminacion Opalo",
  "UGG": "Triptofano",
  "CUU": "Leucina",
  "CUC": "Leucina",
  "CUA": "Leucina",
  "CUG": "Leucina",
  "CCU": "Prolina",
  "CCC": "Prolina",
  "CCA": "Prolina",
  "CCG": "Prolina",
  "CAU": "Histidina",
  "CAC": "Histidina",
  "CAA": "Glutamina",
  "CAG": "Glutamina",
  "CGU": "Arginina",
  "CGC": "Arginina",
  "CGA": "Arginina",
  "CGG": "Arginina",
  "AUU": "Isoleucina",
  "AUC": "Isoleucina",
  "AUA": "Isoleucina",
  "AUG": "Metionina",
  "ACU": "Treonina",
  "ACC": "Treonina",
  "ACA": "Treonina",
  "ACG": "Treonina",
  "AAU": "Asparagina",
  "AAC": "Asparagina",
  "AAA": "Lisina",
  "AAG": "Lisina",
  "AGU": "Serina",
  "AGC": "Serina",
  "AGA": "Arginina",
  "AGG": "Arginina",
  "GUU": "Valina",
  "GUC": "Valina",
  "GUA": "Valina",
  "GUG": "Valina",
  "GCU": "Alanina",
  "GCC": "Alanina",
  "GCA": "Alanina",
  "GCG": "Alanina",
  "GAU": "acido asartico",
  "GAC": "acido asartico",
  "GAA": "acido glutamico",
  "GAG": "acido glutamico",
  "GGU": "Glicina",
  "GGC": "Glicina",
  "GGA": "Glicina",
  "GGG": "Glicina"
}

rna = rna[::-1]
n = len(rna)
for i in range(0, n, 3):
	nucl_codon.append(rna[i:i+3])

n = len(nucl_codon)
print "total codons ", n

for i in range(0,n):
	print i, nucl_codon[i], codons[nucl_codon[i]]






















