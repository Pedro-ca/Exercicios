def soma_imposto(taxa, custo):
    taxa = taxa * custo / 100
    return taxa + custo

print(soma_imposto(5 , 20))
