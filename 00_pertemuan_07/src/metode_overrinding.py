class Induk:
    def my_method(self):
        print("Memanggil metode induk")

class Anak(Induk):
    def my_method(self):
        print("Memanggil metode anak")

c = Anak()
c.my_method()