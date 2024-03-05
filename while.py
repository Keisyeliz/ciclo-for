z = 1
sumatoria = 0

cantInt = int(input('¿Cantidad de lecturas? -> '))
while z <= cantInt:
   sumatoria += int((cantInt + 10000000) * (z * 10000))
   print(sumatoria)
   z += 1