def triangle(length):
  sum=0
  for i in range(length):
    sum+=(length-i)
  return sum
def tprism(layers):
  sum=0
  for i in range(layers):
    sum+=(triangle(layers-i))
    print("Layer "+str(layers-i)+": "+str(triangle(layers-i)))
  return sum
