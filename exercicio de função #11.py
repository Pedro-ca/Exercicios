from datetime import datetime

def formatar_data(data_str):
    try:

        data = datetime.strptime(data_str, "%d/%m/%Y")


        meses = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]


        dia = data.day
        mes = meses[data.month - 1]
        ano = data.year


        return f"{dia} de {mes} de {ano}"

    except ValueError:
        return None


data = input("Digite uma data (DD/MM/AAAA): ")
resultado = formatar_data(data)

if resultado:
    print("Data formatada:", resultado)
else:
    print("Data inválida!")
