# задание №2
Text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
hour = Text.copy()
hour[1] = '"05"'
air = hour.copy()
air[8] = '"+05"'
minute = air.copy()
minute[3] = '"17"'
Text_copy = ' '.join(minute)
print(Text_copy)