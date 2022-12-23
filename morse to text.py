print('Enter Code Example: ( ... --- ...  = SOS)')

while True:
	code = input('Morse Code:')
	codes = code.split()
	all = []
	
	for item in codes:
		if item == '.-':
			all.append('A')
		elif item == '-...':
			all.append('B')
		elif item == '-.-.':
			all.append('C')
		elif item == '-..':
			all.append('D')
		elif item == '.':
			all.append('E')
		elif item == '..-.':
			all.append('F')
		elif item == '--.':
			all.append('G')			
		elif item == '....':
			all.append('H')					
		elif item == '..':
			all.append('I')							
		elif item == '.---':
			all.append('J')									
		elif item == '-.-':
			all.append('K')											
		elif item == '.-..':
			all.append('L')
		elif item == '--':
			all.append('M')
		elif item == '-.':
			all.append('N')				
		elif item == '---':
			all.append('O')	
		elif item == '.--.':
			all.append('P')			
		elif item == '--.-':
			all.append('Q')										
		elif item == '.-.':
			all.append('R')
		elif item == '...':
			all.append('S')
		elif item == '-':
			all.append('T')
		elif item == '..-':
			all.append('U')
		elif item == '...-':
			all.append('V')
		elif item == '.--':
			all.append('W')
		elif item == '-..-':
			all.append('X')
		elif item == '-.--':
			all.append('Y')
		elif item == '--..':
			all.append('Z')		
		elif item == '-----':
			all.append('0')			
		elif item == '.----':
			all.append('1')				
		elif item == '..---':
			all.append('2')					
		elif item == '...--':
			all.append('3')
		elif item == '....-':
			all.append('4')
		elif item == '.....':
			all.append('5')
		elif item == '-....':
			all.append('6')			
		elif item == '--...':
			all.append('7')							
		elif item == '---..':
			all.append('8')								
		elif item == '----.':
			all.append('9')			
		elif item == '---...':
			all.append(':')
			
																			
	p = (''.join(map(str, all)))
	print(p.capitalize())