def toh(n, source, auxiliary, destination):
  # base case
  if n == 1:
    print('Disk', n, 'FROM:', source, '-->', destination)
  else:
    toh(n-1, source, destination, auxiliary) # recursive call (source to auxiliary, destination is temporary)
    print('Disk', n, 'FROM:', source, '-->', destination)
    toh(n-1, auxiliary, source, destination) # recursive call (auxiliary to destination, source is temporary)

# example use
n = 3
toh(n, 'Source', 'Auxiliary', 'Destination')