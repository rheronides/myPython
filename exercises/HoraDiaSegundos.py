x = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(x)


dias = total_segs // 86400
total_segs2 = total_segs % 86400
horas = total_segs2 // 3600
segs_restantes = total_segs2 % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60


print (dias,"dias,", horas,"horas,", minutos,"minutos e",segs_restantes_final,"segundos.")
