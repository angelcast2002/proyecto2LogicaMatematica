import re
from itertools import product

def obtener_variables(formula):
    variables = []
    for caracter in formula:
        if caracter.isalpha() and caracter not in variables:
            variables.append(caracter)
    return variables

def transformar_formula(formula):
    
    nueva_formula = formula[1:-1]
    patron = re.compile(r'(\{.*?\})')
    nueva_formula = re.findall(patron, nueva_formula)
    for i in range(len(nueva_formula)):
        nueva_formula[i] = nueva_formula[i][1:-1]
        
    for i in range(len(nueva_formula)):
        nueva_formula[i] = nueva_formula[i].replace(",", " or ")
        nueva_formula[i] = nueva_formula[i].replace("!", " not ")
    
    return nueva_formula

def operar(formula):
        
    valores_regreso = []
    
    for i in range(len(formula)):
        if i < len(formula) - 1:
            if eval(formula[i]):
                valores_regreso.append("1,")
            else:
                valores_regreso.append("0,")
        else:
            if eval(formula[i]):
                valores_regreso.append("1")
            else:
                valores_regreso.append("0")
    valores_regreso = "".join(valores_regreso)
    valores_regreso = valores_regreso.replace("," , " and ")
    
    if(eval(valores_regreso)):
        valores_regreso = "1"
    else:
        valores_regreso = "0"
    
    return valores_regreso
    

def main():
    # la negacion se representara como ! debido a que no se puede colorar el simbolo encima de la literal
    # El and es una coma que no esta seguido por letras (variables)
    # El or es una coma que esta seguido por letras (variables)
    # Los parentesis se representan como llaves
    ejemplo1 = "{{q, p, !p}}"
    ejemplo2 = "{{p, q, !p}, {p, q, !q}, {p, q, !p, !q}}"
    ejemplo3 = "{{p, q, !p}, {p, q, !q}, {p, q, !p, !q}, {p, q, !p, !q, r}, {p, q, !p, !q, !r}}"
    ejemplo4 = "{{r}, {!q, !r}, {!p, q, !r}, {q}}"
    
    formula = ejemplo4
    
    variables = obtener_variables(formula)
    
    combinaciones = list(product([1, 0], repeat=len(variables)))
    
    print(variables)
    print(len(combinaciones))
    print(combinaciones)
    
    mensaje = "La formula no es satisfactible" , []
    
    for i in range(len(combinaciones)):
        for j in range(len(combinaciones[i])):
            formula = formula.replace(variables[j], str(combinaciones[i][j]))
        nueva_formula = transformar_formula(formula)
        resultado = operar(nueva_formula)
        if resultado == "1":
            mensaje = "La formula es satisfacible para la combinacion: " + str(combinaciones[i])
            break
    
    return mensaje


if __name__ == '__main__':
    print(main())
    