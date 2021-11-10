removeVogais str = [ x | x <- str , not $ elem x "aeiouAEIOU"]

tamanhoComVogal str = length str

tamanhoSemVogal str = length (removeVogais str)

replaces str = (removeVogais str,tamanhoComVogal str,tamanhoSemVogal str)