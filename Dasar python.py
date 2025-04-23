#if else
#loop (conditional loop)
#operasi string (setiap bahasa beda2)
#array (2D) kalau AI bisa aja array (3D)
#object (kayak class, def)
#oop (object oriented programming) (class, def, dsb.)
#algoritma dasar (binary search, quick search, bubble search)


# framework = a layered structure indicating what kind of programs can or should be built
#             and how they would interrelate. (alat bantu bahasa programming)


#CONTOH LOOP ANJAI
print("hello world")
for i in range (10):
    if i %2==0:
        print("genap cok")
    else:
        print("ada yang ganjil di hubungan kita")
    print (i)
print("selesai")

#contoh while
print("hello world")
stop=False
i = 0
while(stop==False):
    print (i)
    if i %2==0:
        print("genap cok")
    else:
        print("ada yang ganjil di hubungan kita")
        print("lo gue end")
        stop=True
    i = i+1
print("selesai")

#contoh lain while
print("hello world")
stop = False
i = 1
while (stop == False):
    i = (i + 1) * 3
    print(i)
    if i % 2 == 0:
        print("lantjar")
    else:
        print("ada yang ganjil di hubungan kita")
        print("lo gue end")
        stop = True

print("selesai")

#contoh duplikasi string
for i in range (10):
    print("-"*i)
print("selesai")

#PR 1 vel
a="+-"
i=0
for i in range (10):
    print((a[1]*i)+(a[0]*(9-i)))
    i = i+1

#jawaban vel
n = 10
for i in range(n):
    print("-" * i + "+" * (n - i - 1))

#PR 2 vel
a = "Januari"
b = "Februari"
c = "Maret"
d = "April"
e = "Mei"
f = "Juni"
g = "Juli"
h = "Agustus"
i = "September"
j = "Oktober"
k = "November"
l = "Desember"
x = 0
y = 31
print(a)
for x in range(y):
    print(x + 1)
    x = x + 1

print(b)
for x in range(y - 3):
    print(x + 1)
    x = x + 1

print(c)
for x in range(y):
    print(x + 1)
    x = x + 1

print(d)
for x in range(y - 1):
    print(x + 1)
    x = x + 1

print(e)
for x in range(y):
    print(x + 1)
    x = x + 1

print(f)
for x in range(y - 1):
    print(x + 1)
    x = x + 1

print(g)
for x in range(y):
    print(x + 1)
    x = x + 1

print(h)
for x in range(y):
    print(x + 1)
    x = x + 1

print(i)
for x in range(y - 1):
    print(x + 1)
    x = x + 1

print(j)
for x in range(y):
    print(x + 1)
    x = x + 1

print(k)
for x in range(y - 1):
    print(x + 1)
    x = x + 1

print(l)
for x in range(y):
    print(x + 1)
    x = x + 1

# PR 2 vel ver 2
a = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November",
     "Desember"]
p = [0, 3, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
for x in a:
    print(x)
    for q in p:
        m = 31 - q
        q += 1
        for z in range(m):
            z = z + 1
            print(z)
            z += 1

#Solusi Vel


month = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

for i in range(len(month)):
  maxDays = 31
  if (i == 1):
    # ubah nilai variabel
  elif (i in [3, 5, 8, 10]):
    # ubah nilai variabel
  for day in range(maxDays):
    # print tanggal


#PR 2 ver 3
month = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

for i in range(len(month)):
    maxDays = 31
    if (i == 1):
        for day in range(maxDays - 3):
            print(str(day+1)+ " " + month[i])
    elif (i in [0, 2, 4, 6, 7, 9, 11]):
        for day in range(maxDays):
            print(str(day+1)+ " " + month[i])
    else:
        for day in range(maxDays - 1):
            print(str(day+1)+ " " + month[i])

#PR 2 ver 4
month = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

for i in range(len(month)):
    print(month[i])
    maxDays = 31
    if (i == 1):
        for day in range(maxDays - 3):
            print(str(day+1))
    elif (i in [0, 2, 4, 6, 7, 9, 11]):
        for day in range(maxDays):
            print(str(day+1))
    else:
        for day in range(maxDays - 1):
            print(str(day+1))

# pengertian array
# jadi apa aja yg dianggap array?
# string: string adalah array of char
# array: murni array yg menyimpan tipe data tertentu

# string adalah array of char
message = "Hello World!" # ini adalah string
print(message[0]) # output: "H" # ini adalah char
print(message[len(message) - 1] # output: "!" # ini adalah char

# murni array
messageTwo = ["H", "e", "l" , "l", "o", " ", "W", "o", "r", "l", "d", "!"] # ini adalah array of string
print(messageTwo[0]) # output: "H" # ini adalah char
print(messageTwo[len(messageTwo) - 1] # output: "!" # ini adalah char

#Pelarajan next

def main():
  print("Hello World")

if __name__ == "__main__":
  main()

#metode looping tanpa for dan while
def doBackflips(n):
    if (n > 0):
        doBackflips(n - 1)
        print("Backflip ke-" + str(n))


def main():
    doBackflips(3)
    print("Beres")


if __name__ == "__main__":
    main()

#PR 3 <Bikin kalender dengan def>

month = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
"Juli", "Agustus", "September", "Oktober", "November", "Desember"]
maxDays = 31

def PrintBulan(n):
    if (n > -1):
        PrintBulan(n-1)
        print(month[n])
        if (n == 1):
            def Hari(x):
                if (x > 0):
                    Hari(x - 1)
                    print(str(x))

            def mainHari():
                Hari(maxDays-3)

            if __name__ == "__main__":
                mainHari()
        elif (n in [0, 2, 4, 6, 7, 9, 11]):
            def Hari(x):
                if (x > 0):
                    Hari(x - 1)
                    print(str(x))

            def mainHari():
                Hari(maxDays)

            if __name__ == "__main__":
                mainHari()
        else:
            def Hari(x):
                if (x > 0):
                    Hari(x - 1)
                    print(str(x))

            def mainHari():
                Hari(maxDays-1)

            if __name__ == "__main__":
                mainHari()
def main():
    PrintBulan(12)

if __name__ == "__main__":
     main()

#PR 3 <Bikin kalender dengan def> solusi Vel
month = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
         "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

def printDay(n, i):
    i += 1
    print(i)
    if (i < n):
        printDay(n, i)

def printMonth(n, i):
    print(month[i])
    maxDays = 31
    if (i == 1):
        maxDays = 28
    elif (i in [3, 5, 8, 10]):
        maxDays = 30
    printDay(maxDays, 0)
    if (i < n - 1):
        printMonth(n, i + 1)

def main():
    printMonth(len(month), 0)


if __name__ == "__main__":
    main()

#jadi ada syntax untuk bikin function/method di python, yaitu def
#syntax lengkapnya begini:

def <expression/function name>(parameter1, parameter2, ...parameterN):

#jadi kl gw jelasin parameter di bagian def itu:
#n = max value
#i = iterator

#PR 4
#Terdapat kelas Mahasiswa dan kelas Fakultas dgn atribut demikian:
#Mahasiswa
    #nama
    #tgl_lahir
    #jenis_kelamin

#Fakultas
    #nama

#buatlah agar ketika menjalankan perintah di bawah memiliki output seperti ini:
print(fakultas.getName()) # output: "Fakultas Kedokteran Cinta"
print(mahasiswa.getFakultas()) # output: "Fakultas Kedokteran Cinta"
print(mahasiswa.getName()) # output: "Ontohod"

#clue:
#gunakan inheritance

#Selamat mengerjakan, Tuhan memberkati

#PR 4 ver 1

class Fakultas:
    def __init__(fakultas, getName):
        fakultas.getName = getName

    def printname(fakultas):
        print(fakultas.getName)


class Mahasiswa(Fakultas):
    def __init__(mahasiswa, getName, getBD, getGender, getFakultas):
        mahasiswa.getName = getName
        mahasiswa.getBD = getBD
        mahasiswa.getGender = getGender
        mahasiswa.getFakultas = getFakultas

    def printname(mahasiswa):
        print(mahasiswa.getFakultas)
        print(mahasiswa.getName)


f = Fakultas("Fakultas Kedokteran Cinta")
m = Mahasiswa("Ontohod", "29 Februari 2099", "Non-binary genderfluid bigot", "Fakultas Kedokteran Cinta")

f.printname()
m.printname()

#PR 4 solusi Vel

# class fakultas
class Fakultas(object):
    # init method
    def __init__(self, nama):
        self.fakultas = nama

    def getName(self):
        return self.fakultas

    # class Mahasiswa inherit Fakultas


class Mahasiswa(Fakultas):
    # init Mahasiswa
    def __init__(self, nama, tgl_lahir, jenis_kelamin, fakultas):
        super(Mahasiswa, self).__init__(fakultas)
        self.nama = nama
        self.tgl_lahir = tgl_lahir
        self.jenis_kelamin = jenis_kelamin

    def getName(self):
        return self.nama

    def getFakultas(self):
        return super(Mahasiswa, self).getName()


f = Fakultas("Fakultas Kedokteran Cinta")  # object fakultas
m = Mahasiswa("Ontohod", "29 Februari 2099", "Non-binary genderfluid bigot",
              "Fakultas Kedokteran Cinta")  # object mahasiswa

print(f.getName())  # output: "Fakultas Kedokteran Cinta"
print(m.getName())  # output: "Ontohod"
print(m.getFakultas())  # output: "Fakultas Kedokteran Cinta"

"""""
#Contoh cara buat objek di javascript

// cara 1 (declare directly)
const orang = {
  nama: "John Doe",
  jenis_kelamin: "Non-binary genderfluid bigot"
}

// cara 2 (class instantiation)
class Orang {
  constructor(nama, jenis_kelamin) {
    this.nama = nama
    this.jenis_kelamin = jenis_kelamin
  }
  setNama(nama) {
    this.nama = nama
  }
  getNama() {
    return this.nama
  }
// ... name your functions
}
const orangDua = new Orang("Jane Doe", "Binary options binomo")
"""""

#contoh bikin print hari pakai class

class Hari:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def getYesterday(self):
        return self.prev

    def getToday(self):
        return self.value

    def getTomorrow(self):
        return self.next

    def setPrev(self, prev):
        self.prev = prev

    def setNext(self, next):
        self.next = next


def startADay():
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


def main():
    today = startADay()
    i = 0
    while i < 7:
        print("Today is " + today.getToday() + ", yesterday was " + today.getYesterday().getToday())
        today = today.getTomorrow()
        i += 1


if __name__ == "__main__":
    main()

#contoh bikin print hari pakai class ver 2 (lebih optimal) ver 1

class Hari:
    def __init__(self, value, prev=None, next=None):
        self.value = value #yang di-declare di dalem def itu atribut
        self.prev = prev
        self.next = next


def startADay():
    listHari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    start = today = Hari(listHari[0])
    for i in range(len(listHari) - 1):
        today.next = today = Hari(listHari[i + 1], today)
    today.next = start
    start.prev = today
    return start


def main():
    today = startADay()
    i = 0
    while i < 30:
        print("Today is " + today.value + ", yesterday was " + today.prev.value + ", see you tomorrow...")
        today = today.next
        i += 1
    print("See you next month...")


if __name__ == "__main__":
    main()

#contoh bikin print hari pakai class ver 2 (lebih optimal) ver 2

class Hari:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def setValue(self, value):
        self.value = value


def startADay():
    listHari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    start = today = Hari(listHari[0])
    for i in range(len(listHari) - 1):
        tomorrow = Hari(listHari[i + 1], today)
        today.next = tomorrow
        today = tomorrow
    today.next = start
    start.prev = today
    today = start
    return today


def main():
    today = startADay()
    i = 0
    while i < 30:
        print("Today is " + today.value + ", yesterday was " + today.prev.value + ", see you tomorrow...")
        today = today.next
        i += 1
    print("See you next month...")


if __name__ == "__main__":
    main()

#contoh loop javascript

const ids = [1 , 2, 3, 4, 5, 6, 7, null, 9, 10],
  data = []
for (let i = 0; i < ids.length; i++)
  if (ids[i]) data.push(await axios.get(`server_url/${ids[i]}`))
console.log(data)

#contoh loop javascript2

const ids = [1, 2, 3, 4, 5, 6, 7, null, 9, 10],
  data = await Promise.all(ids.reduce((arr, id) => {
    if (id) arr.push(axios.get(`server_url/${id}`))
    return arr
  }, []))
console.log(data)

#contoh bikin print bulan pakai class

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


def startAMonth():
    listBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September","Oktober","November","Desember"]
    firstMonth = Bulan(listBulan[0])
    thismonth = firstMonth
    for i in range(len(listBulan) - 1):
        tmp = Bulan(listBulan[i + 1], thismonth)
        thismonth.setNext(tmp)
        thismonth = tmp
    firstMonth.setPrev(thismonth)
    thismonth.setNext(firstMonth)
    thismonth = thismonth.getNextmonth()
    return thismonth


def main():
    thismonth = startAMonth()
    i = 0
    while i < 12:
        print("This month is " + thismonth.getThismonth() + ", last month was " + thismonth.getMonthbefore().getThismonth())
        thismonth = thismonth.getNextmonth()
        i += 1


if __name__ == "__main__":
    main()

#contoh bikin print bulan pakai class yang lebih optimal

class Bulan:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


def startAMonth():
    listBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September","Oktober","November","Desember"]
    start = thismonth = Bulan(listBulan[0])
    for i in range(len(listBulan) - 1):
        thismonth.next = thismonth = Bulan(listBulan[i + 1], thismonth)
    thismonth.next = start
    start.prev = thismonth
    return start


def main():
    thismonth = startAMonth()
    i = 0
    while i < 12:
        print("This month is " + thismonth.value + ", last month was " + thismonth.prev.value + ", see you tomorrow...")
        thismonth = thismonth.next
        i += 1
    print("See you next month...")


if __name__ == "__main__":
    main()

#contoh bikin kalender dengan class ( yang lebih optimal )

class Bulan:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


def startAMonth():
    listBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September","Oktober","November","Desember"]
    start = thismonth = Bulan(listBulan[0])
    for i in range(len(listBulan) - 1):
        thismonth.next = thismonth = Bulan(listBulan[i + 1], thismonth)
    thismonth.next = start
    start.prev = thismonth
    return start

def printDay(n, i):
    i += 1
    print(i)
    if (i < n):
        printDay(n, i)

def main():
    thismonth = startAMonth()
    i = 0
    while i < 12:
        print(thismonth.value)
        maxDays = 31
        if (i == 1):
            maxDays = 28
        elif (i in [3, 5, 8, 10]):
            maxDays = 30
        printDay(maxDays, 0)
        thismonth = thismonth.next
        i += 1


if __name__ == "__main__":
    main()

#contoh bikin kalender dengan class ( yang kurang optimal )

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


def startAMonth():
    listBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September","Oktober","November","Desember"]
    firstMonth = Bulan(listBulan[0])
    thismonth = firstMonth
    for i in range(len(listBulan) - 1):
        tmp = Bulan(listBulan[i + 1], thismonth)
        thismonth.setNext(tmp)
        thismonth = tmp
    firstMonth.setPrev(thismonth)
    thismonth.setNext(firstMonth)
    thismonth = thismonth.getNextmonth()
    return thismonth

def printDay(n, i):
    i += 1
    print(i)
    if (i < n):
        printDay(n, i)

def main():
    thismonth = startAMonth()
    i = 0
    while i < 12:
        print(thismonth.getThismonth())
        maxDays = 31
        if (i == 1):
            maxDays = 28
        elif (i in [3, 5, 8, 10]):
            maxDays = 30
        printDay(maxDays, 0)
        thismonth = thismonth.getNextmonth()
        i += 1


if __name__ == "__main__":
    main()


# assignment operator

a = 10
b = 5

#bitwise OR (|)
c = a | b
print('==============OR==============')
print('nilai :',a,'  , binary:',format(a,'08b'))
print('nilai :',b,'  , binary:',format(b,'08b'))
print('---------------------------------- (|)')
print('nilai :',c,' , binary:',format(c,'08b'))

#bitwise AND (&)
c = a & b
print('==============AND==============')
print('nilai :',a,'  , binary:',format(a,'08b'))
print('nilai :',b,'  , binary:',format(b,'08b'))
print('---------------------------------- (&)')
print('nilai :',c,'  , binary:',format(c,'08b'))

#bitwise XOR (^)
c = a ^ b
print('==============XOR==============')
print('nilai :',a,'  , binary:',format(a,'08b'))
print('nilai :',b,'  , binary:',format(b,'08b'))
print('---------------------------------- (^)')
print('nilai :',c,' , binary:',format(c,'08b'))

#bitwise NOT (~)
c = ~a
print('==============NOT==============')
print('nilai :',a,'  , binary:',format(a,'08b'))
print('---------------------------------- (~)')
print('nilai :',c,' , binary:',format(c,'08b'))
print('---------------------------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' , binary:',format(e^d,'08b'))

# shifting

# shift right (>>)

print('==============(>>)==============')

def printNext(n, i):
    i += 1
    c = a >> i
    print('<---------------------------------->')
    print('nilai a :', a, '  , binary:', format(a, '08b'))
    print('---------------------------------- (>>)',i)
    print('nilai c :',c,'  , binary:',format(c,'08b'))
    print('<---------------------------------->')
    if (i < n):
        printNext(n, i)

def main():

    printNext(a,0)

if __name__ == "__main__":
    main()


# shift left (<<)
print('')
print('==============(<<)==============')

def printNext(n, i):
    i += 1
    c = a << i
    print('<---------------------------------->' )
    print('nilai a :', a, '  , binary:', format(a, '08b'))
    print('---------------------------------- (<<)',i)
    print('nilai c :',c,'  , binary:',format(c,'08b'))
    print('<---------------------------------->')
    if (i < n):
        printNext(n, i)

def main():

    printNext(a,0)

if __name__ == "__main__":
    main()

# string operator
# String slicing operator “[]”

string1 = "helloworld"

print('string1[1] = ' + string1[1])
print('string1[-3] = ' + string1[-3])
print('string1[1:5] = ' + string1[1:5])
print('string1[1:6] = ' + string1[1:6])
print('string1[1:-3] = ' + string1[1:-3])
print('string1[2:] = ' + string1[2:])
print('string1[:5] = ' + string1[:5])
print('string1[:-2] = ' + string1[:-2])
print('string1[-2:] = ' + string1[-2:])
print('string1[::-1] = ' + string1[::-1])
print('string1[::8] = ' + string1[::8])

# String Formatting Operator “%.”

name = "india"
age = 19
marks = 20.56
string1 = 'Hey %s' % (name)
print(string1)
string2 = 'my age is %d' % (age)
print(string2)
string2 = 'my age is %u' % (age)
print(string2)
string3= 'Hey %s, my age is %d' % (name, age)
print(string3)
string3= 'Hey %d, my age is %s' % (age, name)
print(string3)
string3= 'Hey %s, my subject mark is %f' % (name, marks)
print(string3)
string3= 'Hey %s, my subject mark is %s' % (name, marks)
print(string3)
string3= 'Hey %s, my subject mark is %d' % (name, marks)
print(string3)
string3= 'Hey %s, my subject mark is %u' % (name, marks)
print(string3)

# Binary search tree
# Linked list
# Pop heap push
# Extension string operator

#PR 5
""""
Bikin bilangan prima 0-100
Pake pop heap push (khususnya yang push [append])
On^2
""""

def showFactor(x):
    f.clear()
    for i in range(1, x + 1):
        if x % i == 0:
            f.append(i)
    if len(f) == 2:
        print(x)

def printNum(n, i):
    i += 1
    showFactor(i)
    if i < n:
        printNum(n,i)

def main():
    printNum(100, 0)


if __name__ == "__main__":
    f = []
    main()

#PR 5 versi lebih optimal 1 (adri)

def showFactor(x):
    f.clear()
    for i in range(1, x + 1):
        if x % i == 0:
            f.append(i)
    if len(f) == 2:
        print(x)

def main():
    for i in range(100):
        showFactor(i)

if __name__ == "__main__":
    f = []
    main()

#PR 5 versi lebih optimal 2 (adri)

f = []
for i in range(100):
    f.clear()
    for j in range(1, i + 1):
        if i % j == 0:
            f.append(j)
    if len(f) == 2:
        print(i)

# PR 5 tapi ngitung jumlah bilangan prima
p = []
f = []
for i in range(10000):
    f.clear()
    for j in range(1, i + 1):
        if i % j == 0:
            f.append(j)
    if len(f) == 2:
        p.append(i)
print("Jumlah bilangan prima ada = ", len(p))
for k in range(len(p)+1):
    print(p[k])

# PR 5 tapi ngitung jumlah bilangan prima (solusi vel ver 1)
# Solusi amatir
def printPrimes(size):
    if size < 10:
        size = 10
    primes = [2, 3, 5, 7]
    for i in range(10, size):
        isPrime = True
        for j in range(len(primes)):
            if i % primes[j] == 0:
                isPrime = False
                break
        if isPrime == True:
            primes.append(i)
    return primes


def main():
    print(printPrimes(10000))
    print(len(printPrimes(10000)))




if __name__ == "__main__":
    main()

# PR 5 tapi ngitung jumlah bilangan prima (solusi vel ver 2)
# Solusi Sieve of Eratosthenes (tercepat di dunia)
# Solusi ini masih bisa dikembangkan lagi dengan memory segmentation

def printPrimes(size):
    if size < 10:
        size = 10
    arr = [True]*size
    arr[0] = arr[1] = False
    for i in range(2, int(len(arr)**(1/2))):
        if arr[i]:
            j = i * i
            while j < len(arr):
                arr[j] = False
                j += i
    prime = []
    for i in range(len(arr)):
        if arr[i]:
            prime.append(i)
    return prime

def main():
    print(printPrimes(1000))

if __name__ == "__main__":
    main()

# PR 5 eratosthenes prime number vel revisi adri
def printPrimes(size):
    if size < 10:
        size = 10
    arr = [True]*size
    arr[0] = arr[1] = False
    for i in range(2, int((len(arr)+10)**(1/2))):
        if arr[i]:
            j = i * i
            while j < len(arr):
                arr[j] = False
                j += i
    prime = []
    for i in range(len(arr)):
        if arr[i]:
            prime.append(i)
    print("Jumlah bilangan prima yang ada = ",len(prime))
    print(prime)

def main():
    printPrimes(10000)

if __name__ == "__main__":
    main()

# PR 5 eratosthenes prime number adri ver 1

def prime_eratosthenes(n):
    notprime_list = []
    prime_list = []
    for i in range(2, n+1):
        if i not in notprime_list:
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                notprime_list.append(j)
    print("Jumlah total bilangan prima = ",len(prime_list))
    for i in range(len(prime_list)+1):
        print(prime_list[i])
print(prime_eratosthenes(100000))

# PR 5 eratosthenes prime number adri ver 2

def prime_eratosthenes(n):
    notprime_list = []
    prime_list = []
    for i in range(2, n+1):
        if i not in notprime_list:
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                notprime_list.append(j)
    print("Jumlah total bilangan prima = ",len(prime_list))
    print(prime_list)

def main():
    prime_eratosthenes(10)

if __name__ == "__main__":
    main()

# PR 5 eratosthenes prime number (solusi vel ver 3 bug fixes)

def primeNumbers(size):
    # if size < 10: size = 10
    arr = [True] * size
    arr[0] = arr[1] = False
    for i in range(2, int(size ** .5) + 1):
        if arr[i]:
            for j in range(i * i, size, i):
                arr[j] = False
    for i in range(size):
        if arr[i]: p.append(i)


def main():
    primeNumbers(3)
    print(p)
    print("Jumlah bilangan prima = ", len(p))


if __name__ == "__main__":
    p = []
    main()

#PR 6

""""
Class Calendar:
    getDay(self,n)
    
getDay(300) # output : Kamis, dd, Oktober
""""

#PR 6 solusi gue 061122

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
    listTanggal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                   1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                   1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                   15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
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


# PR 6 versi dengan dialog box

from tkinter import *
from tkinter import simpledialog
root = Tk()

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
    listTanggal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                   1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                   1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                   15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6,
                   7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                   19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
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
    def get_me():
        n = simpledialog.askinteger("Input integer", "Enter number of days in integer")
        getDay(n)
    button = Button(root, text="Click here to input!", command=get_me)
    button.pack()
    root.geometry("300x200")
    root.mainloop()

# PR 6 versi lebih ringkas

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

























