#badger
import sys

def help()->None:
	print("Usage: \"python ./remove_vowels.py word\" or \"python ./remove_vowels.py\"")
	exit(0)

def remove_vowels(txt:str)->str:
	vowels:str="aeiou"
	ans:str=""
	for c in txt.lower():
		if c not in vowels:
			ans+=c
	return ans

def main()->None:
	txt:str=''
	if len(sys.argv)<=1:
		txt=input("Enter a string: ")
	elif len(sys.argv)>2:
		help()
	else:
		txt=sys.argv[1]

	print("String without vowels:",remove_vowels(txt))

if __name__ == "__main__":
	main()