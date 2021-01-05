nucleotidos = {"A":"Adenina", "C":"Citosina", "G":"Guanina", "T":"Timina"}
print len(nucleotidos)
print nucleotidos ["A"]
print nucleotidos ["C"]
print nucleotidos ["G"]
print nucleotidos ["T"]

nucleotidos ["A"] = "ADENINA"
nucleotidos ["C"] = "CITOSINA"
nucleotidos ["G"] = "GUANINA"
nucleotidos ["T"] = "TIMINA"

print nucleotidos
nucleotidos.pop("T", None)
print nucleotidos

nucleotidos.pop("T", None)
nucleotidos.pop("C", None)
nucleotidos.pop("G", None)
print nucleotidos

nucleotidos.pop("A", None)
nucleotidos.pop("T", None)
nucleotidos.pop("C", None)
nucleotidos.pop("G", None)
print nucleotidos

