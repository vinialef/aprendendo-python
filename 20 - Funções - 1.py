#def exibir_mensagem():
#    print("Oi")
#exibir_mensagem()


digite_o_nome=input("\nDigite o nome aqui: ")

def exibir_mensagem2(nome=digite_o_nome):
    print(f"\nOi,{nome}!")

exibir_mensagem2()

def exibir_poema(data,*versos,**rodape):
    texto= "\n".join(versos)
    fim_do_texto= "\n".join(f"{chave.title()}:{valor}" for chave,valor in rodape.items())
    poema=f"\n\n{data}\n\n{texto}\n\n{fim_do_texto}\n"
    print(poema)

print(exibir_poema("Hoje, Dia do Trabalhador - Ano de mudança","Água mole","Pedra Dura","Tanto bate","Até que fura",autor="Eu",ano=2024))
