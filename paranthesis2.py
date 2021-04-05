strr = "{()[]}}"
if strr.count("(") == strr.count(")") and strr.count("[") == strr.count("]") and strr.count("{") == strr.count("}"):
    print("Balanced")
else:
    print("Unbalanced")    
