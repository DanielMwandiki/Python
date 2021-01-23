print('This program will take several numbers and sum them')
sum = 0.0

count = int(input('How Many Numbers : '))
current_count = 0

while current_count < count :
    print("Number" , current_count)
    number = float(input("Enter Number :"))
    sum = sum + number
    current_count +=1
    
print(sum/count)
