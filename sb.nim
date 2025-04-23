import strutils

var bintang = "*"

for i in countup(1,5):
    for j in countup(1, i):
      echo bintang.repeat(i)
      break

      
