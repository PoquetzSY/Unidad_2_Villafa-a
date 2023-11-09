def imc(peso, altura, nombre):
    imc_p= peso/altura**2
    categorias = [
        (18.5, "Bajo peso"),
        (24.9, "Normal"),
        (29.9, "Sobrepeso"),
        (float('inf'),"Obesidad")
    ]
    
    for limite, descripcion in categorias:
        if imc_p <= limite:
            print(f"{nombre} estas {descripcion}: IMC {round(imc_p,1)}")
            break