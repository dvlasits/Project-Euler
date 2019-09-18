ins = input("Enter x,y,z,n: ")

x,y,z,n = [int(i) for i in ins.split()]

def totSpaceTakenUp(x,y,z,n):
  if n != 0:
    return (x+2*n)*(y+2*n)*(z+2*n)-(4*(x+y+z+6*n-4))
  if n == 0:
    return x*y*z
  raise IndexError("Messed up n")

print(totSpaceTakenUp(x,y,z,n))
print(totSpaceTakenUp(x,y,z,n-1))
print(totSpaceTakenUp(x,y,z,n)-totSpaceTakenUp(x,y,z,n-1))
