def contar_palavras(texto):
 texto = texto.lower()
 palavras = texto.split()
 return len(palavras)

def contar_caracteres(texto, incluir_espacos=True):
 if incluir_espacos:
  return len(texto)
 else:
  return len(texto.replace(" ", ""). replace("\n", "").replace("\t", ""))

def exibir_menu():
 print("Escolha uma opção:")
 print("1. Contar palavras")
 print("2. Contar caracteres (com espaços)")
 print("3. Contar caracteres (sem espaços)")
 print("4. Todos")
 print("5. Sair")
 
if __name__ == "__main__":
 while True:
    texto = input("Digite o texto (ou 'Enter' para encerrar): ")
    if texto == "":
        print("Encerrando o programa...")
        break
    exibir_menu()
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
       num_palavras = contar_palavras(texto)
       print(f"Número de palavras: {num_palavras}")
    elif opcao == "2":
       num_caracteres_com_espacos = contar_caracteres(texto, incluir_espacos=True)
       print(f"Número de caracteres (com espaços): {num_caracteres_com_espacos}")
    elif opcao == "3":
       num_caracteres_sem_espacos = contar_caracteres(texto, incluir_espacos=False)
       print(f"Número de caracteres (sem espaços): {num_caracteres_sem_espacos}")
    elif opcao == "4":
       num_palavras = contar_palavras(texto)
       num_caracteres_com_espacos = contar_caracteres(texto, incluir_espacos=True)
       num_caracteres_sem_espacos = contar_caracteres(texto, incluir_espacos=False)
       print(f"Número de palavras: {num_palavras}")
       print(f"Número de caracteres (com espaços): {num_caracteres_com_espacos}")
       print(f"Número de caracteres (sem espaços): {num_caracteres_sem_espacos}")
    elif opcao == "5":
       print("Encerrando o programa...")
    else:
       print("Opção inválida. Por favor, escolha uma opção válida.")

def perguntar_repetir():
    repetir = input("Deseja analisar outro texto? (S/N): ")
    if repetir.strip().upper() == "S":
        return True
    elif repetir.strip().upper() == "N":
        print("Encerrando o programa...")
        return False
    else:
        print("Opção inválida. Por favor, digite S para SIM ou N para NÃO.")
        return perguntar_repetir()