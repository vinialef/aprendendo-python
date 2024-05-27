consumo = float(input())    

def recomendar_plano (digite=consumo):
        if digite <= 10:
           print("Plano Essencial Fibra - 50Mbps")
        elif digite > 10 and digite <= 20:
           print("Plano Prata Fibra - 100Mbps")
        elif digite > 20:
           print("Plano Premium Fibra - 300Mbps")
recomendar_plano()
    




