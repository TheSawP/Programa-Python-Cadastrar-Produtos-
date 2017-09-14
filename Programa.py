i = 0
nome = []
codigo =[]
preco = []
total =  int(input("Quantos produtos deseja cadastrar ?" ))
while (i < total):
	
	n = input("Digite o nome do produto: ")
	nome.append(n)
	c = int(input("Digite o codigo do produto: "))
	codigo.append(c)
	p = int(input("Digite o preco do produto: "))
	preco.append(p)
	i = i+ 1
dec = float(input("Digite 1 para listar o produto cadastrado ou qualquer tecla para finalizar: "))
contador = 0	
if dec == 1:	
		while ( contador < total):
			print("============================="
			,"\nO nome do produto é",nome[contador],
			 "\nO seu codigo é:", codigo[contador],
			  "\nO seu valor é:",preco[contador],
			   )
			contador = contador +1
else:
		exit(0)
	


