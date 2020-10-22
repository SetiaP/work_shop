class Induk: # mendefinisikan kelas Induk
    parent_attr = 100

    def __init__(self):
        print ("Memanggil konstruktor induk")

    def parent_method(self):
        print ('Memanggil metode induk')

    def set_attr(self, attr):
        Induk.parent_attr = attr

    def get_attr(self):
        print ("Attribut induk :", Induk.parent_attr)

class Anak(Induk): # mendefinisikan kelas Anak
    def __init__(self):
        print ("Memanggil konstruktor Anak")

    def child_method(self):
        print ('Memanggil metode Anak')

c = Anak() # instansiasi kelas Anak
c.child_method() # Anak memanggil metodenya

c.parent_method() # memanggil metode Induk
c.set_attr(200) # kembali memanggil metode Induk
c.get_attr() # kembali memanggil metode Induk