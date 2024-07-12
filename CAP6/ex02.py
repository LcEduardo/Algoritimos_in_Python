# implementando fila

from collections import deque

fila = deque()

fila.append('A')
fila.append('B')
fila.append('C')

print("Fila após inserções:", fila)

primeiro = fila.popleft()
print("Elemento removido:", primeiro)
print("Fila após a remoção:", fila)

fila.append('D')
fila.append('E')

print("Fila após mais inserções:", fila)

segundo = fila.popleft()
terceiro = fila.popleft()

print("Elementos removidos:", segundo, terceiro)
print("Fila final:", fila)

