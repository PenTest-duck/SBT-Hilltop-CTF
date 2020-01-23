line = "$@ sa4 sb6 se3 sg9 si1 so0 ss5 st7 sz2"
for i in range(16):
  prefix = "c ^" + str(hex(i)[2:])
  for j in range(16):
    print(prefix, "$" + str(hex(j)[2:]), line)
