import time
import random
import datetime

version = "v1.0"

# Sorry for the messy code :P

print("Welcome to Discord Nitro Codes Generator v1.0")
print("Brought to you by wraithM17")
print("\n\n")
time.sleep(2)
print("How many codes would you like to generate ?")
num = int(input("-->"))
print("So you've decided to generate "+str(num)+" nitro codes.")
time.sleep(2)
print("In order to claim the nitro codes, use this link [https://discord.gift/(CODE)]")
print("The percentage of getting a working one is very low but you're getting it for free and can atleast try!")
print("")
time.sleep(1)
print("In what format would you like to recieve the codes ?\n")
print("1. Codes with the links        [ Example : https://discord.gift/HR4U5NR6KI5GIQCD ] [Recommended]")
print("2. Raw codes without links     [ Example : HR4U5NR6KI5GIQCD ]")
print("\n Please type either 1 or 2")
code_format = str(input("-->"))
time.sleep(1)


def generate():
	chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
	'1','2','3','4','5','6','7','8','9','0'
	]
	char1 = random.choice((chars))
	char2 = random.choice((chars))
	char3 = random.choice((chars))
	char4 = random.choice((chars))
	char5 = random.choice((chars))
	char6 = random.choice((chars))
	char7 = random.choice((chars))
	char8 = random.choice((chars))
	char9 = random.choice((chars))
	char10 = random.choice((chars))
	char11 = random.choice((chars))
	char12 = random.choice((chars))
	char13 = random.choice((chars))
	char14 = random.choice((chars))
	char15 = random.choice((chars))
	char16 = random.choice((chars))

	code = char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16

	if code_format == "1":
		linked_code = "https://discord.gift/"+code
		file.write(linked_code+"\n")
	else:
		raw_code = code
		file.write(raw_code+"\n")





def main():
	print("Please enter the name of the file in which you'd like to generate the accounts.  [Example: results.txt]")
	file_name = str(input("-->"))
	time.sleep(1)
	print("\n\n Generating the accounts...")
	time.sleep(2)
	date_time = str(datetime.datetime.now())
	global file
	file = open(file_name,'w')
	file.write("File name : "+file_name)
	
	file.write("\nTime generated : "+date_time+"\n")
	file.write("Number of codes in this file : "+str(num)+"\n")
	file.write(f"Codes generated using Discord Nitro Code Generator {version} by wraithM17")
	file.write("\nGithub for support : https://github.com/wraithM17\n")
	file.write("\n  GENERATED CODES ARE GIVEN BELOW :\n\n")
	generated = 0
	while generated != num:
		generated += 1
		generate()

main()
print(f"\n{num} codes have been generated successfully!")
print(f"Thanks for using Discord Nitro Code Generator {version} by wraithM17 ")
print("Have a nice day and good luck with the codes! :3 \n\n")
print("Github : https://github.com/wraithM17")
time.sleep(10)

