import random
def primary():
    #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd = random.randint(0, last)
  print(quotes[rnd])

  rnd = random.randint(0, last)
  print(quotes[rnd])

  fd = open("quotes.txt","a")
  newQuote = input("Input a Qoute:")
  fd.write(newQuote)
      
if __name__== "__main__":
  primary()
