from math import inf


def main():
  import random
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  n=len(quotes)
  i=random.randint(0,n)


  print(quotes[i])

if __name__== "__main__":
  main()
