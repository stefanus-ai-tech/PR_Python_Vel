class Bulan:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def getMonthbefore(self):
        return self.prev

    def getThismonth(self):
        return self.value

    def getNextmonth(self):
        return self.next

    def setPrev(self, prev):
        self.prev = prev

    def setNext(self, next):
        self.next = next

class Hari(Bulan):
    def __init__(self, value, prev=None, next=None):
        super(Hari, self).__init__(Bulan)
        self.value = value
        self.prev = prev
        self.next = next

    def getYesterday(self):
        return self.prev

    def getToday(self):
        return self.value

    def getTomorrow(self):
        return self.next

class Tanggal(Bulan):
    def __init__(self, value, prev=None, next=None):
        super(Tanggal, self).__init__(Bulan)
        self.value = value
        self.prev = prev
        self.next = next

    def getYesterday(self):
        return self.prev

    def getToday(self):
        return self.value

    def getTomorrow(self):
        return self.next

def startMonth():
    listBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
                 "Agustus", "September", "Oktober", "November", "Desember"]
    firstMonth = Bulan(listBulan[0])
    thisMonth = firstMonth
    for i in range(len(listBulan) - 1):
        tmp = Bulan(listBulan[i + 1], thisMonth)
        thisMonth.setNext(tmp)
        thisMonth = tmp
    firstMonth.setPrev(thisMonth)
    thisMonth.setNext(firstMonth)
    thisMonth = thisMonth.getNextmonth()
    return thisMonth

def startDay():
    listHari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    firstDay = Hari(listHari[0])
    today = firstDay
    for i in range(len(listHari) - 1):
        tmp = Hari(listHari[i + 1], today)
        today.setNext(tmp)
        today = tmp
    firstDay.setPrev(today)
    today.setNext(firstDay)
    today = today.getTomorrow()
    return today

def startDate31():
    listTanggal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31]
    firstDate = Tanggal(listTanggal[0])
    tanggalsekarang31 = firstDate
    for i in range(len(listTanggal) - 1):
        tmp = Tanggal(listTanggal[i + 1], tanggalsekarang31)
        tanggalsekarang31.setNext(tmp)
        tanggalsekarang31 = tmp
    firstDate.setPrev(tanggalsekarang31)
    tanggalsekarang31.setNext(firstDate)
    tanggalsekarang31 = tanggalsekarang31.getTomorrow()
    return tanggalsekarang31

def startDate30():
    listTanggal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30]
    firstDate = Tanggal(listTanggal[0])
    tanggalsekarang30 = firstDate
    for i in range(len(listTanggal) - 1):
        tmp = Tanggal(listTanggal[i + 1], tanggalsekarang30)
        tanggalsekarang30.setNext(tmp)
        tanggalsekarang30 = tmp
    firstDate.setPrev(tanggalsekarang30)
    tanggalsekarang30.setNext(firstDate)
    tanggalsekarang30 = tanggalsekarang30.getTomorrow()
    return tanggalsekarang30

def startDate28():
    listTanggal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28]
    firstDate = Tanggal(listTanggal[0])
    tanggalsekarang28 = firstDate
    for i in range(len(listTanggal) - 1):
        tmp = Tanggal(listTanggal[i + 1], tanggalsekarang28)
        tanggalsekarang28.setNext(tmp)
        tanggalsekarang28 = tmp
    firstDate.setPrev(tanggalsekarang28)
    tanggalsekarang28.setNext(firstDate)
    tanggalsekarang28 = tanggalsekarang28.getTomorrow()
    return tanggalsekarang28

def getMonth(x):
    thisMonth = startMonth()
    for i in range(x):
        arrbulan.append(str(thisMonth.getThismonth()))
        thisMonth = thisMonth.getNextmonth()


def getDay(n):
    x=1
    getMonth(x)
    today = startDay()
    tanggalsekarang31 = startDate31()
    tanggalsekarang30 = startDate30()
    tanggalsekarang28 = startDate28()
    for i in range(n):
        arrhari.append(str(today.getToday()))
        today = today.getTomorrow()
        arrtanggal31.append(str(tanggalsekarang31.getToday()))
        arrtanggal30.append(str(tanggalsekarang30.getToday()))
        arrtanggal28.append(str(tanggalsekarang28.getToday()))
        if len(arrtanggal31) == 1:
            tanggalsekarang31 = tanggalsekarang31.getTomorrow()
            tanggalsekarang30 = tanggalsekarang30.getTomorrow()
            tanggalsekarang28 = tanggalsekarang28.getTomorrow()
        elif arrtanggal31[len(arrtanggal31) - 1] == arrtanggal31[0]:
            x+=1
            getMonth(x)
            if (str(arrbulan[len(arrbulan) - 1]) == "Februari"):
                tanggalsekarang28 = tanggalsekarang28.getTomorrow()
            elif (str(arrbulan[len(arrbulan) - 1]) in ["April", "Juni", "September", "November"]):
                tanggalsekarang30 = tanggalsekarang30.getTomorrow()
            else:
                tanggalsekarang31 = tanggalsekarang31.getTomorrow()
        elif len(arrtanggal31) > 1:
            tanggalsekarang31 = tanggalsekarang31.getTomorrow()
            tanggalsekarang30 = tanggalsekarang30.getTomorrow()
            tanggalsekarang28 = tanggalsekarang28.getTomorrow()



    if (str(arrbulan[len(arrbulan) - 1]) == "Februari"):
        print(str(arrhari[len(arrhari) - 1]), ", ", str(arrtanggal28[len(arrtanggal28) - 1]),
              str(arrbulan[len(arrbulan) - 1]))
    elif (str(arrbulan[len(arrbulan) - 1]) in ["April", "Juni", "September", "November"]):
        print(str(arrhari[len(arrhari) - 1]), ", ", str(arrtanggal30[len(arrtanggal30) - 1]),
              str(arrbulan[len(arrbulan) - 1]))
    else:
        print(str(arrhari[len(arrhari) - 1]), ", ", str(arrtanggal31[len(arrtanggal31) - 1]),
              str(arrbulan[len(arrbulan) - 1]))

    print("arrtanggal 31 = ", arrtanggal31)
    print("arrtanggal 30 = ", arrtanggal30)
    print("arrtanggal 28 = ", arrtanggal28)
    print(arrbulan)
    print(arrhari)



if __name__ == "__main__":
    arrbulan = []
    arrhari = []
    arrtanggal31 = []
    arrtanggal30 = []
    arrtanggal28 = []
    x = 1
    getDay(31)

"""""
if (str(arrbulan[len(arrbulan) - 1]) == "Februari"):
#arrtanggal.remove(29)
#arrtanggal.remove(30)
#arrtanggal.remove(31)
elif (str(arrbulan[len(arrbulan) - 1]) in ["April", "Juni", "September", "November"]):
#arrtanggal.remove(31)
#else:
#continue
i += 1
arrbulan.append(str(thisMonth.getThismonth()))
        thisMonth = thisMonth.getNextmonth()
        
def getDate(x):
tanggalsekarang = startDate()
for i in range(x):
    arrtanggal.append(str(tanggalsekarang.getToday()))
    tanggalsekarang = tanggalsekarang.getTomorrow()
    
def getMonth(x):
    thisMonth = startMonth()
    for i in range(x):
        arrbulan.append(str(thisMonth.getThismonth()))
        thisMonth = thisMonth.getNextmonth()


def startDate():
    listTanggal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31]
    firstDate = Tanggal(listTanggal[0])
    tanggalsekarang = firstDate
    if (str(arrbulan[len(arrbulan) - 1]) == "Februari"):
        for i in range(len(listTanggal) - 4):
            tmp = Tanggal(listTanggal[i + 1], tanggalsekarang)
            tanggalsekarang.setNext(tmp)
            tanggalsekarang = tmp
    elif (str(arrbulan[len(arrbulan) - 1]) in ["April", "Juni", "September", "November"]):
        for i in range(len(listTanggal) - 2):
            tmp = Tanggal(listTanggal[i + 1], tanggalsekarang)
            tanggalsekarang.setNext(tmp)
            tanggalsekarang = tmp
    else:
        for i in range(len(listTanggal) - 1):
            tmp = Tanggal(listTanggal[i + 1], tanggalsekarang)
            tanggalsekarang.setNext(tmp)
            tanggalsekarang = tmp
    firstDate.setPrev(tanggalsekarang)
    tanggalsekarang.setNext(firstDate)
    tanggalsekarang = tanggalsekarang.getTomorrow()
    return tanggalsekarang
    
    
    #print(str(arrtanggaly[len(arrtanggaly) - 1]))

    #print(str(arrhari[len(arrhari)-1]), ", ",str(arrtanggalx[len(arrtanggalx) - 1]),
          #str(arrbulan[len(arrbulan)-1]))
          
"""""









