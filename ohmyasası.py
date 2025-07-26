#Bu program elektronikçilerin ohm yasası ile son değeri hesaplaması içindir.
print("Ota60 tarafından yazılmıştır,Tüm hakları saklıdır. ©")
print("Ticari amaçlarla kullanımı yasaktır.Sadece ücretsiz eğitim veren siteler,kişiler vs. kullanabilir.İş birliği için:ota6018@gmail.com @otaarktik")
print()
while True:
 print("Ohm yasası hesaplama programı: Lütfen seçeneğinizi seçin:")
 print()
 print()
 print()
 print("1.Voltaj hesaplama.")
 print("2.Akım (Amper) hesaplama.")
 print("3.Direnç hesaplama.")
 print("4.Çıkış.")

 secenek = input("Lütfen seçeneğinizi (sayı olarak) giriniz: ")
 if (secenek == '1'):
      akim = float(input("Lütfen akımı (amper cinsinden) giriniz: "))
      direnc = float(input("Lütfen direnç değerini (ohm cinsinden) giriniz: "))
      cevap = akim*direnc
      print("Voltaj: ",cevap,"v")
      

     
 elif (secenek == '2'):
      voltaj = float(input("Lütfen voltaj (volt cinsinden) giriniz: "))
      direnc = float(input("Lütfen direnç değerini (ohm cinsinden) giriniz: "))
      cevap = voltaj/direnc
      print("Akım (Amper): ",cevap,"A")
      


 elif (secenek == '3'):
      akim = float(input("Lütfen akımı (amper cinsinden) giriniz: "))
      voltaj = float(input("Lütfen voltaj değerini (volt cinsinden) giriniz: "))
      cevap = voltaj/akim
      print("Direnç: ",cevap,"Ω")
      


 elif (secenek == '4'):
      print("İyi günler.")
      exit()
