import sys

# Время запроса
h1, m1, s1 = map(int, sys.stdin.readline().strip().split(":"))
# Время получения запроса сервером SNTP
h2, m2, s2 = map(int, sys.stdin.readline().strip().split(":"))
# Время ответа
h3, m3, s3 = map(int, sys.stdin.readline().strip().split(":"))

# Время сетевой задержки
# round() округляет 10.5 в меньшую сторону, а по условию 10.5 => 11, поэтому просто добавляем 1/2 и берем целое int()
# math.ceil() всегда в большую
# math.floor() всегда в меньшую
s_lat =  int( ( (s3-s1) + (m3-m1)*60 + (h3-h1)*3600 ) / 2 + 0.5)

# До конца суток на сервере SNTP: от времени на SNTP до 86399 секунд (день без одной секунды)
s_end = (23*3600+59*60+59) - (h2*3600+m2*60+s2)

answer = ""

# Могут ли из-за сетевой задержки наступить новые сутки?
if s_lat > s_end:
    # Наступают новые сутки на SNTP
    s_lat -= s_end + 1
    hh = s_lat//3600
    s_lat -= hh*3600
    mm = s_lat//60
    s_lat -= mm*60
    ss = s_lat
else:
    # Не наступают новые сутки на SNTP
    hh = h2 + s_lat//3600
    s_lat -= s_lat//3600*3600
    mm = m2 + s_lat//60
    s_lat -= s_lat//60*60
    ss = s2 + s_lat

if (mm >= 59):
    hh += mm // 60
    mm = mm % 60

if (ss >= 59):
    mm += ss // 60
    ss = ss % 60

answer += "0{}:".format(hh) if hh//10 == 0 else "{}:".format(hh)
answer += "0{}:".format(mm) if mm//10 == 0 else "{}:".format(mm)
answer += "0{}".format(ss) if ss//10 == 0 else "{}".format(ss)

print(answer)
