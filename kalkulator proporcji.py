'''1. 

	Plese provide input of proportions A:B
	Let's start from proportion A
	> 1
	Now plese provide proportion B
	> 4
	
2. 
	
	Please provide density of ingrediend A - hardener (l/kg)
	> A 
	Please provide density of ingrediend B - base (l/kg)
	> B
	
3. 

	Please provide volume of radey to use mix that you wnat to achive (ml).
	>
	
	
4. 
	Your desired weight of substance A is xxx and B is XXX'''

while(True):
        
    print("Plese provide input of proportions A:B")
    A = float(input("Let's start from proportion A: "))
    B = float(input("Now plese provide proportion B: "))

    print ("Please provide density of ingrediend A - hardener (ml/g)")
    x = float(input("Provide density of ingrediend A - hardener: "))
    print ("Please provide density of ingrediend B - hardener (ml/g)")
    y = float(input("Provide density of ingrediend B - base: "))

    print("Please provide volume of radey to use mix that you wnat to achive (ml)")
    V = float(input("Please provide volume: "))

    weight_A = ((A*V)/(A+B))
    weight_B = ((B*V)/(A+B))

    desired_weight_A = weight_A*x
    desired_weight_B = weight_B*y

    print("Your desired weight of substance A is: ", desired_weight_A,
          "Your desired weight of substance B is: ", desired_weight_B)




