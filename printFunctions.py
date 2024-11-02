def showTeams(teams):
  for i in range(len(teams)):
    print('-----------------------------------------------------------------------')
    printSatisfationLaners([teams[i][0][0], teams[i][1][0]], 0)
    printSatisfationLaners([teams[i][0][1], teams[i][1][1]], 1)
    printSatisfationLaners([teams[i][0][2], teams[i][1][2]], 2)
    printSatisfationLaners([teams[i][0][3], teams[i][1][3]], 3)
    printSatisfationLaners([teams[i][0][4], teams[i][1][4]], 4)
    print(f"Diferença:{teams[i][2]}")
    print('-----------------------------------------------------------------------')

def printSatisfationLaners(laners, index):
  RED   = "\033[1;31m"
  RESET = "\033[0;0m"
  lane = ['Top', 'Jg', 'Mid', 'Adc', 'Sup']
  if laners[0].getBanVector(index) == 1 and laners[1].getBanVector(index) == 1:
    print(f"{RED}{lane[index]}:{laners[0].getName()} \t {lane[index]}:{laners[1].getName()}{RESET}")
  elif laners[0].getBanVector(index) == 1:
    print(f"{RED}{lane[index]}:{laners[0].getName()}{RESET} \t {lane[index]}:{laners[1].getName()}")
  elif laners[1].getBanVector(index) == 1:
    print(f"{lane[index]}:{laners[0].getName()} \t {RED}{lane[index]}:{laners[1].getName()}{RESET}")
  else:
    print(f"{lane[index]}:{laners[0].getName()} \t {lane[index]}:{laners[1].getName()}")