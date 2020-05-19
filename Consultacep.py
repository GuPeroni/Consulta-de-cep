import requests

def main():
	print('####################')
	print('### Consulta CEP ###')
	print('####################')
	print()

	cep = input('Digite o CEP para a consulta: ')

	if len(cep) != 8:
		print('Quantidade de dígitos inválida!')
		exit()

	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

	endereço = request.json()

	if 'erro' not in endereço:
		print('==> CEP ENCONTRADO <==')
		
		print('CEP: {}'.format(endereço['cep']))
		print('Logradouro: {}'.format(endereço['logradouro']))
		print('Complemento: {}'.format(endereço['complemento']))
		print('Bairro: {}'.format(endereço['bairro']))
		print('Cidade: {}'.format(endereço['localidade']))
		print('Estado: {}'.format(endereço['uf']))
		
	else:
		print('{}: CEP inválido.'.format(cep))

	print('---------------------------------')
	option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\nDigite o número : \n'))
	if option == 1:
		main()
	else:
		print('Saindo...')

if __name__ == '__main__':
	main()