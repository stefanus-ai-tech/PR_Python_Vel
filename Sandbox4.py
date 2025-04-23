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

def startDate():
    listTanggal = []
    listBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
                 "Agustus", "September", "Oktober", "November", "Desember"]

    for j in range(3):
        for k in range(len(listBulan)):
            if (k == 1):
                for i in range(28):
                    i += 1
                    listTanggal.append(i)
            elif (k in [3, 5, 8, 10]):
                for i in range(30):
                    i += 1
                    listTanggal.append(i)
            else:
                for i in range(31):
                    i += 1
                    listTanggal.append(i)
    for k in range(len(listBulan)):
        if (k == 1):
            for i in range(29):
                i += 1
                listTanggal.append(i)
        elif (k in [3, 5, 8, 10]):
            for i in range(30):
                i += 1
                listTanggal.append(i)
        else:
            for i in range(31):
                i += 1
                listTanggal.append(i)

    firstDate = Tanggal(listTanggal[0])
    tanggalsekarang = firstDate
    for i in range(len(listTanggal) - 1):
        tmp = Tanggal(listTanggal[i + 1], tanggalsekarang)
        tanggalsekarang.setNext(tmp)
        tanggalsekarang = tmp
    firstDate.setPrev(tanggalsekarang)
    tanggalsekarang.setNext(firstDate)
    tanggalsekarang = tanggalsekarang.getTomorrow()
    return tanggalsekarang

def getMonth(x):
    thisMonth = startMonth()
    for i in range(x):
        arrbulan.append(str(thisMonth.getThismonth()))
        thisMonth = thisMonth.getNextmonth()

def getDay(n):
    x=1
    getMonth(x)
    today = startDay()
    tanggalsekarang = startDate()
    for i in range(n):
        arrhari.append(str(today.getToday()))
        today = today.getTomorrow()
        arrtanggal.append(str(tanggalsekarang.getToday()))
        if len(arrtanggal) == 1:
            tanggalsekarang = tanggalsekarang.getTomorrow()
        elif arrtanggal[len(arrtanggal) - 1] == arrtanggal[0]:
            x+=1
            getMonth(x)
            tanggalsekarang = tanggalsekarang.getTomorrow()
        elif len(arrtanggal) > 1:
            tanggalsekarang = tanggalsekarang.getTomorrow()

    print(str(arrhari[len(arrhari) - 1]), ", ", str(arrtanggal[len(arrtanggal) - 1]),
          str(arrbulan[len(arrbulan) - 1]))

if __name__ == "__main__":
    arrbulan = []
    arrhari = []
    arrtanggal = []
    x = 1
    print("Enter number of days = ")
    n = int(input())
    getDay(n)