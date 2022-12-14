
#Para iniciar a estruturação do gráfico foi importada a biblioteca matplotlib.pyplot:   
from matplotlib import pyplot as plt

#Criando uma função de MENU que irá trazer o resultado de Y quando: A = 8, B = 1 e C podendo ser: X1 = 5, X2 = 7 e X3 = 9.
#Serão três resultados diferentes para cada resultado de Y pois há três valores para X. 
def menu(x, a, b, c):
  y = a*x + b*x - c
  return y

# Informando os valores para cada X, sendo X1 = 5, X2 = 7 e X3 = 9:
x1 = 5
x2 = 7
x3 = 9

# Informando qual será o valor de A, B e C usando os três últimos números do meu RU 3742819:
a = 8 
b = 1
c = 9

# Colocando título no gráfico e quadrados no gráfico:   
plt.title('Gráfico Representativo da Equação A*X + B*X - C',fontweight='black')
plt.grid()

#plot usado para definir os valores do eixo X, irá apresentar números de 1 a 0 no eixo.
plt.xlim(1, 10) 

# Plotando os resultados de x e y:
plt.plot(x1,menu(x1, a, b, c), marker="o", markersize=12, markerfacecolor='orange')
plt.plot(x2,menu(x2, a, b, c), marker="o", markersize=12, markerfacecolor='pink')
plt.plot(x3,menu(x3, a, b, c), marker="o", markersize=12, markerfacecolor='purple')


# Inserindo legenda no gráfico (ao lado superior esquerdo irá apresentar o valor para X e para Y):
plt.legend([f'x={x1} y={menu(x1, a, b, c)}', f'x={x2} y={menu(x2, a, b, c)}', f'x={x3} y={menu(x3, a, b, c)}'])

# Inserido nome para o eixo X e Y:
plt.xlabel('Valores de X',fontweight='black')
plt.ylabel('Valores de Y',fontweight='black')
plt.show()
