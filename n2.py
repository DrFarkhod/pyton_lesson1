#2

time = int(input("Введите много-много секунды, Я их переведу в часы, минуты и секунды: "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")