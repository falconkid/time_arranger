class Professor:
    def _init_(self, name):
        self.name = name
        self.available_time = [[0 for x in range(12)] for x in range(5)]
        self.count = 0
        self.day = -1
        self.time = -1
    
    def set_email(self, email):
        self.email = email

    def set_time(self,day,time):
        if time&1:
            for i in range(0,4):
                self.available_time[day][i] = 1
        if time&2:
            for i in range(4,8):
                self.available_time[day][i] = 1
        if time&4:
            for i in range(8,12):
                self.available_time[day][i] = 1
        self.count += 1

    def check_time(self,day,time):
        if self.available_time[day][time] == 1:
            return True

    def get_count(self):
        return self.count
    
    def set_exact_time(self,day,time):
        self.day = day
        self.time = time

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email
    
    def real_time(self): # 1. 更改當年日期 
        day = self.day
        time = self.time
        time_string = ""
        if day == 0:
            time_string = "1/18(一)"
        elif day == 1:
            time_string = "1/19(二)"
        elif day == 2:
            time_string = "1/20(三)"
        elif day == 3:
            time_string = "1/21(四)"
        elif day == 4:
            time_string = "1/22(五)"

        if time == 0:
            time_string = time_string + " 10:00~10:30"
        elif time == 1:
            time_string = time_string + " 10:30~11:00"
        elif time == 2:
            time_string = time_string + " 11:00~11:30"
        elif time == 3:
            time_string = time_string + " 11:30~12:00"
        elif time == 4:
            time_string = time_string + " 13:00~13:30"
        elif time == 5:
            time_string = time_string + " 13:30~14:00"
        elif time == 6:
            time_string = time_string + " 14:00~14:30"
        elif time == 7:
            time_string = time_string + " 14:30~15:00"
        elif time == 8:
            time_string = time_string + " 15:00~15:30"
        elif time == 9:
            time_string = time_string + " 15:30~16:00"
        elif time == 10:
            time_string = time_string + " 16:00~16:30"
        elif time == 11:
            time_string = time_string + " 16:30~17:00"
        return time_string


    def print_available_time(self):
        for x in range(5):
            for y in range(12):
                print (self.available_time[x][y])

    def check_error(self):
        if self.count > 0 and self.day == -1:
            return True
        else:
            return False

    def check_day(self): 
        only_day = ""
        for y in range(5):
            for w in range(12):
                if self.available_time[y][w] == 1 and not only_day :
                    only_day = str(y+1)
                    break
                elif self.available_time[y][w] == 1:
                    return True
        if only_day:
            print (self.name + " " + only_day)                    
        return False
