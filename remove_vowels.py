#badger
def remove_vowels(txt:str)->str:
	vowels:str="aeiou"
	ans:str=""
	for c in txt.lower():
		if c not in vowels:
			ans+=c
	return ans

def main()->None:
	txt:str=input("Enter a string: ")
	print("String without vowels:",remove_vowels(txt))

if __name__ == "__main__":
	main()