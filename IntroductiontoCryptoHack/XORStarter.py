print("crypto{%s}" % "".join([chr(x^13) for x in [ord(x) for x in list("label")]]))
