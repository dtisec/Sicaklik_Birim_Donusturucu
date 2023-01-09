# SICAKLIK BİRİM DÖNÜŞTÜRÜCÜ - PYTHON3

print("Hangi sıcaklık birimini gireceksiniz: ")
print("Celcius için 1'e basınız: ")
print("Fahrenheit için 2'e basınız: ")
print("Kelvin için 3'e basınız: ")

a = int(input("Seçim yapınız: "))

if a == 1:
     b = int(input("Sıcaklık değerini giriniz: "))
     c = float((b*5-38)/9)
     d = float(b+273)
     print('%d derece %.2f Fahrenheit ve %.2f Kelvindir' % (b,c,d))
if a == 2:
     e = float(input("Sıcaklık değerini giriniz:"))
     f = float(((e-32)*5)/9)
     g = float((((e-32)*5)/9)+273)
     print('%.1f Fahrenheit %d derece %.2f Kelvindir'% (e,f,g))
if a == 3:
     h = int("Sıcaklık değerini giriniz:")
     j = float(h-273)
     k = float((9*j)/5)+32
     print('%.1f Fahrenheit %d derece %.2f Kelvindir'% (h,j,k))
