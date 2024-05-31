def RondadeGrupos(equipos):
  resultados=np.zeros((4,4))
  consolidador=np.array([])
  for i in range(len(equipos)):
    for j in range(len(equipos)):
      if i!=j:
        golesLocal=random.randint(0,5)
        golesVisitante=random.randint(0,5)
        resultados[i][j]=golesLocal
        resultados[j][i]=golesVisitante
  print(resultados)
  for i in range(len(equipos)):
    for j in range(len(equipos)):
      if i!=j:
        print(f'{equipos[i]} {round(resultados[i][j])} {equipos[j]} {round(resultados[j][i])}')
        if resultados[i][j]>resultados[j][i]:
          consolidador=np.append(consolidador,equipos[i])
          consolidador=np.append(consolidador,3)
          consolidador=np.append(consolidador,round(resultados[i][j]))
          consolidador=np.append(consolidador,equipos[j])
          consolidador=np.append(consolidador,0)
          consolidador=np.append(consolidador,round(resultados[j][i]))

          print(f'{equipos[i]} Gano el Partido y Tiene 3 pts')
        elif resultados[j][i]>resultados[i][j]:
          consolidador=np.append(consolidador,equipos[j])
          consolidador=np.append(consolidador,3)
          consolidador=np.append(consolidador,round(resultados[j][i]))
          consolidador=np.append(consolidador,equipos[i])
          consolidador=np.append(consolidador,0)
          consolidador=np.append(consolidador,round(resultados[i][j]))
          print(f'{equipos[j]} Gano el Partido y Tiene 3 pts')
        elif resultados[i][j]==resultados[j][i]:
          consolidador=np.append(consolidador,equipos[j])
          consolidador=np.append(consolidador,1)
          consolidador=np.append(consolidador,round(resultados[j][i]))
          consolidador=np.append(consolidador,equipos[i])
          consolidador=np.append(consolidador,1)
          consolidador=np.append(consolidador,round(resultados[i][j]))
          print(f'{equipos[i]} y {equipos[j]} Empataron el Partido y cada uno tiene 1 pt')
  for equipo in equipos:
    for puntos in np.where(consolidador==equipo):
      ganados=np.sum(np.int64(consolidador[puntos+1]))
      goles=np.sum(np.int64(consolidador[puntos+2]))
    print(f'{equipo} {ganados} pts {goles} goles')
  print(consolidador)

import numpy as np
import random
equipos=np.array(['Bolivar','Millonarios','Flamengo','Palestino'])
print(RondadeGrupos(equipos))
