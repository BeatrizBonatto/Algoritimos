import json
import os

class Times:
    local_data_time = r"C:\Users\biake\OneDrive - Fatec Centro Paula Souza\Documents\GitHub\desktop-tutorial\times.json"


def editTimes():
    times = Time.getDataTimes()

    print('\nEscolha um time para editar:\n')
    x = 1
    for time in times:
        print(f"{x} - {time['identificaçao']}")
        x = x + 1
    op = int(input("\nDigite aqui: "))

    time_selecionada = times[op - 1]

    id_time = time_selecionada['id_time']

    new_identificacao = input("\nEntre com a nova identificação: ")

    new_time = {'id_time': id_time,
                'identificaçao': new_identificacao}

    del (times[op - 1])

    times.append(new_time)

    Times.setDataTimes(times)

    return "Time editado!!!"