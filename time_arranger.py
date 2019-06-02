import professor
import csv

original_list = []
professor_list = []
error_professor_list = []
firstline = "星期一\t星期二\t星期三\t星期四\t星期五"

def professor_sort(professor_list):
    for x in range(len(professor_list)):
        y = x
        while y > 0:
            if professor_list[y].get_count() < professor_list[y-1].get_count():
                temp = professor_list[y]
                professor_list[y] = professor_list[y-1]
                professor_list[y-1] = temp
                y = y-1
            else:
                 break
            
f= open("reply.csv", "r", encoding="utf8") # 1.改教授時間資料表(參考2015夏的excel)
csv_f = csv.reader(f)

for row in csv_f:
    pro = professor.Professor()
    for x in range(len(row)-1): #讀csv,前兩個是教授跟教授信箱
        if x == 1:
            pro._init_(row[x])
        elif x == 2:
            pro.set_email(row[x])
        elif x < 9:
            day = x-4
            time = 0
            if "10:00～12:00" in row[x]:
                time += 1
            if "13:00～15:00" in row[x]:
                time += 2
            if "15:00～17:00" in row[x]:
                time += 4
            if time != 0:
                pro.set_time(day, time)
    professor_list.append(pro)
    original_list.append(pro)
f.close()

for x in professor_list:
    x.check_day()

professor_sort(professor_list)

final_time = [[0 for x in range(12)] for x in range(5)]



for x in professor_list:
    flag = 0
    for y in range(5):
        for w in range(12):
            if x.check_time(y,w) and final_time[y][w] == 0:
                final_time[y][w] = x  #.get_name()
                x.set_exact_time(y,w)
                flag = 1
                break
        if flag == 1:
            break
    if x.check_error() :
        error_professor_list.append(x)
        print (x.get_name()+"error")

for x in error_professor_list:
    temp_day = -1
    temp_time = -1
    flag = 0
    flag2 = 0
    for y in range(5):
        for w in range(12):
            if final_time[y][w] == 0:
                temp_day = y
                temp_time = w
                flag = 1
                break
        if flag == 1:
            break
    for y in range(5):
        for w in range(12):
            if final_time[y][w] != 0 and final_time[y][w] != 1 and final_time[y][w].check_time(temp_day,temp_time) and x.check_time(y,w):
                x.set_exact_time(y,w)
                final_time[y][w].set_exact_time(temp_day,temp_time)
                final_time[temp_day][temp_time] = final_time[y][w]
                final_time[y][w] = x
                flag2 = 1
                print( x.get_name()+"成功插入" )
                break
        if flag2 == 1:
            break
    if flag2 == 0:
        print( x.get_name()+"插入失敗" )

time_table = open("time_table.txt","w") # 2.輸出總體時間表
time_table.write(firstline)
time_table.write("\n")
for x in range(12):
    for y in range(5):
        if final_time[y][x] != 0 and final_time[y][x] != 1:
            time_table.write(str(final_time[y][x].get_name()))
        else:
            for w in range(6):
                time_table.write(" ")
        time_table.write("\t")
    time_table.write("\n")
time_table.close()

protime_list = open("mail_list_time","w") # 3.輸出教授個人時間
for x in original_list:
    if x.get_count() > 0:
        protime_list.write(x.get_name())
        protime_list.write("\t")
        protime_list.write(x.get_email())
        protime_list.write("\t")
        protime_list.write(x.real_time())
        protime_list.write("\n")

protime_list.close()