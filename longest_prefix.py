# function which returns the shortest element of the list of strings
def min_list(c):
    shortest = c[0]
    for i in range(1, len(c)):
        if len(c[i]) < len(shortest):
            shortest = c[i]
    return shortest

# finds the common prefix by comparing the strings one by one 
def prefix(input_list):
  prefix = min_list(input_list)
  for j in range(0, len(input_list)):
      for i in range(0, len(shortest)):
          if shortest[i] != input_list[j][i]:
              prefix = shortest[:i]
              break
  return prefix

print(" To enter custom list :1")
print("\n")
print(" To use sample lists mentioned below: 2")
print("\n")
IN=input("Enter the option: ")
print("\n")
if (IN==1):
  input_list = input('Enter elements of a list separated by space ')
  print("\n")
  input_list = input_list.split()
  print("Input list: ",input_list)
  print("longest prefix:-",prefix(input_list))
else:
  print("flower,flow,flight: A/a")
  print("\n")
  print("light,racecar,car: B/b")
  print("\n")
  in_put = input("Enter the option: ")
  if(in_put=="a"or in_put=="A"):
    input_list = ["flower","flow","flight"]
  elif(in_put=="b"or in_put=="B"):
    input_list = ["light","racecar","car"]
  print("Input list: ",input_list)
  print("longest prefix:",prefix(input_list))
