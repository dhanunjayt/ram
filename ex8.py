formatter = "%r %r %r %r %r"  

print formatter % (1, 2, 3, 4,5)
print formatter % ("one", "two", "three", "four", "five")
print formatter % (True, False, False, True, False)
print formatter % (formatter, formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I've said goodnight.",
"Tace Care."
  )
