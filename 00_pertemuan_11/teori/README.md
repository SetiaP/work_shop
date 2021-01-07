Pemrograman Web
Flask

Pengenalan Python Flask Flask adalah kerangka (framework) Python untuk membuat aplikasi web. Dari situs aslinya,

Flask adalah microframework untuk Python berbasis Werkzeug, Jinja 2 dan "niat baik". Ketika kita memikirkan Python, kerangka de facto yang muncul di benak kita adalah framework Django. Tapi dari perspektif pemula Python, Flask lebih mudah, jika dibandingkan dengan Django.

Menyiapkan Flask Menyiapkan Flask sangat sederhana dan cepat. Dengan package manager pip, semua yang perlu kita lakukan adalah:

pip install flask

Setelah anda selesai meng-install Flask, buat folder dengan nama FlaskApp. Masuk ke folder FlaskApp dan buat sebuah file dengan nama app.py. Import modul flask dan buat aplikasi menggunakan Flask seperti ditunjukkan berikut:

from flask import Flask app = Flask(name) Sekarang tentukan basic route / dan handler yang sesuai:

@app.route("/") def main(): return "Welcome!" Berikutnya, periksa jika file yang dieksekusi adalah program utama dan jalankan app-nya

if name == "main": app.run() Simpan perubahan dan eksekusi app.py:

python app.py Arahkan browser Anda ke http://localhost: 5000/ dan Anda pasti memiliki pesan pembuka, "welcome".

Membuat Home Page Pertama, ketika aplikasi berjalan kita akan menampilkan home page dengan isi dari daftar keinginan terbaru yang ditambahkan oleh pengguna. Jadi, mari menambahkan home page ke folder aplikasi kita.

Flask mencari file template di dalam folder templates. Jadi, navigasi ke folder PythonApp dan buat folder dengan nama templates. Didalam templates, buat sebuah file dengan nama index.html. Buka index.html dan tambahkan HTML berikut:

<title>Python Flask Bucket List App</title>
<link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

<link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
<div class="container">
    <div class="header">
        <nav>
            <ul class="nav nav-pills pull-right">
                <li role="presentation" class="active"><a href="#">Home</a>
                </li>
                <li role="presentation"><a href="#">Sign In</a>
                </li>
                <li role="presentation"><a href="showSignUp">Sign Up</a>
                </li>
            </ul>
        </nav>
        <h3 class="text-muted">Python Flask App</h3>
    </div>

    <div class="jumbotron">
        <h1>Bucket List App</h1>
        <p class="lead"></p>
        <p><a class="btn btn-lg btn-success" href="showSignUp" role="button">Sign up today</a>
        </p>
    </div>

    <div class="row marketing">
        <div class="col-lg-6">
            <h4>Bucket List</h4>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h4>Bucket List</h4>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h4>Bucket List</h4>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
        </div>

        <div class="col-lg-6">
            <h4>Bucket List</h4>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h4>Bucket List</h4>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h4>Bucket List</h4>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
        </div>
    </div>

    <footer class="footer">
        <p>&copy; Company 2015</p>
    </footer>

</div>
Buka app.py dan import render_template, dimana kita akan menggunakan untuk me-render file-file template.

from flask import Flask, render_template Ubah metode utama untuk mengembalikan file template yang di-render.

def main(): return render_template('index.html')

Membuat Halaman Pendaftaran (Signup) Langkah 1: Menyiapkan Database Kita akan menggunakan MySQL sebagai back end. Jadi, masuk ke MySQL dari "command line", atau jika anda lebih suka GUI seperti MySQL work bench, Anda bisa menggunakannya. ertama, buat sebuah database dengan nama BucketList. Dari command line:

mysql -u -p

Masukkan password dan setelah masuk, eksekusi perintah berikut untuk membuat database:

CREATE DATABASE BucketList;

Setelah database telah jadi, buat sebuah table dengan nama tbl_user seperti berikut:

1 2 3 4 5 6 CREATE TABLE BucketList.tbl_user ( user_id BIGINT NULL AUTO_INCREMENT, user_name VARCHAR(45) NULL, user_username VARCHAR(45) NULL, user_password VARCHAR(45) NULL, PRIMARY KEY (user_id)); Kita akan menggunakan Stored procedures untuk aplikasi Python kita untuk berinteraksi dengan database MySQL. Jadi, saat table tbl_user telah jadi, buat sebuah "stored procedure" (prosedur penyimpanan) dengan nama sp_createUser untuk mendaftarkan pengguna.

Saat membuat storage procedure untuk membuat pengguna di table tbl_user, pertama kita harus memeriksa jika pengguna dengan username yang sama telah ada. Jika telah ada, kita akan menampilkan error ke pengguna tersebut, dan jika tidak kita akan menambahkan pengguna kedalam table. Berikut bagaimana storage procedure atau prosedur penyimpanan sp_createUser bekerja:

DELIMITER $$ CREATE DEFINER=root@localhost PROCEDURE sp_createUser( IN p_name VARCHAR(20), IN p_username VARCHAR(20), IN p_password VARCHAR(20) ) BEGIN if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN

    select 'Username Exists !!';
 
ELSE
 
    insert into tbl_user
    (
        user_name,
        user_username,
        user_password
    )
    values
    (
        p_name,
        p_username,
        p_password
    );
 
END IF;
END$$ DELIMITER ;

Step 2: Buat Interface (Antarmuka) Pendaftaran Masuk ke direktori PythonApp/templates dan buat file HTML dengan nama singup.html. Tambahkan code HTML berikut ke singup.html:

<title>Python Flask Bucket List App</title>
<link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

<link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
<link href="../static/signup.css" rel="stylesheet">
<div class="container">
  <div class="header">
    <nav>
      <ul class="nav nav-pills pull-right">
        <li role="presentation" ><a href="main">Home</a></li>
        <li role="presentation"><a href="#">Sign In</a></li>
        <li role="presentation" class="active"><a href="#">Sign Up</a></li>
      </ul>
    </nav>
    <h3 class="text-muted">Python Flask App</h3>
  </div>

  <div class="jumbotron">
    <h1>Bucket List App</h1>
    <form class="form-signin">
    <label for="inputName" class="sr-only">Name</label>
    <input type="name" name="inputName" id="inputName" class="form-control" placeholder="Name" required autofocus>
    <label for="inputEmail" class="sr-only">Email address</label>
    <input type="email" name="inputEmail" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
    <label for="inputPassword" class="sr-only">Password</label>
    <input type="password" name="inputPassword" id="inputPassword" class="form-control" placeholder="Password" required>
     
    <button id="btnSignUp" class="btn btn-lg btn-primary btn-block" type="button">Sign up</button>
  </form>
  </div>

   

  <footer class="footer">
    <p>&copy; Company 2015</p>
  </footer>

</div>
Juga tambahkan CSS berikut dengan nama singup.css ke folder statis didalam PythonApp.

body { padding-top: 40px; padding-bottom: 40px; }

.form-signin { max-width: 330px; padding: 15px; margin: 0 auto; } .form-signin .form-signin-heading, .form-signin .checkbox { margin-bottom: 10px; } .form-signin .checkbox { font-weight: normal; } .form-signin .form-control { position: relative; height: auto; -webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; padding: 10px; font-size: 16px; } .form-signin .form-control:focus { z-index: 2; } .form-signin input[type="email"] { margin-bottom: -1px; border-bottom-right-radius: 0; border-bottom-left-radius: 0; } .form-signin input[type="password"] { margin-bottom: 10px; border-top-left-radius: 0; border-top-right-radius: 0; }

Di app.py tambahkan metode lain yang disebut showSignUp untuk membuat halaman pendaftaran begitu sebuah permintaan datang ke /showSignUp:

@app.route('/showSignUp') def showSignUp(): return render_template('signup.html')

Simpan perubahan dan restart server.

Step 3: Mengimplementasikan Metode Pendaftaran (Signup) Berikutnya, kita membutuhkan metode server-side untuk UI agar berinteraksi dengan database MySQL. Jadi masuk ke PythonApp dan buka app.py. Buat metode baru dengan nama singUp dan juga tambahkan route /signUp.

@app.route('/signUp') def signUp(): # create user code will be here !!

Kita akan menggunakan jQuery AJAX untuk mengirim data signup Anda ke metode signUp, jadi kami akan menentukan metode dalam definisi rute.

@app.route('/signUp',methods=['POST']) def signUp(): # create user code will be here !!

Untuk membaca nilai yang dikirim, kita harus mengimpor request dari Flask.

from flask import Flask, render_template, request

Dengan menggunakan request kita bisa membaca nilai yang diposting seperti berikut:

@app.route('/signUp',methods=['POST']) def signUp():

# read the posted values from the UI
_name = request.form['inputName']
_email = request.form['inputEmail']
_password = request.form['inputPassword']
Setelah nilainya terbaca, kita akan memeriksa apakah datanya "valid" dan untuk sementara kita akan menampilkan pesan sederhana:

@app.route('/signUp',methods=['POST']) def signUp():

# read the posted values from the UI
_name = request.form['inputName']
_email = request.form['inputEmail']
_password = request.form['inputPassword']

# validate the received values
if _name and _email and _password:
    return json.dumps({'html':'<span>All fields good !!</span>'})
else:
    return json.dumps({'html':'<span>Enter the required fields</span>'})
Juga, import json dari Flask, karena kita menggunakannya di code sebelumnya untuk mengembalikan data json.

from flask import Flask, render_template, json, request

Langkah 4: Buat permintaan Signup Kita akan menggunakan jQuery AJAX untuk mengirim permintaan singup ke metode Python. Download dan tempatkan jQuery didalam PythonApp/static/js dan tambahkan link dari halaman singup. Setelah jQuery disertakan, kami akan menambahkan permintaan JQuery POST saat pengguna mengklik tombol Sign Up.

$(function() { $('#btnSignUp').click(function() {

    $.ajax({
        url: '/signUp',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
});
});

Simpan semua perubahan dan restart server. Dari halaman Sign Up, isi rinciannya dan klik Sign Up. Periksa konsol browser dan Anda pasti memiliki pesan di bawah ini:

{"html": "All fields good !!"}

Step 5: Panggil Prosedur Penyimpanan MySQL Setelah kita memiliki name, email address dan password, kita bisa langsung memanggil prosedur tersimpan MySQL untuk membuat pengguna baru.

Untuk terhubung dengan MySQL, kita akan menggunakan Flask-MySQL, yang merupakan ekstensi Flask. Untuk memulai dengan Flask-MySQL, instal dengan menggunakan manajer paket pip:

pip install flask-mysql Import MySQL kedalam app.py:

from flask.ext.mysql import MySQL Sebelumnya kita mendefinisikan aplikasi kita seperti berikut:

app = Flask(name) Bersaat dengan itu masukka konfigurasi MySQL berikut:

mysql = MySQL()

MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'jay' app.config['MYSQL_DATABASE_PASSWORD'] = 'jay' app.config['MYSQL_DATABASE_DB'] = 'BucketList' app.config['MYSQL_DATABASE_HOST'] = 'localhost' mysql.init_app(app) Pertama, mari buat koneksi MySQL:

conn = mysql.connect() Setelah koneksi dibuat, kita akan meminta cursor untuk memeriksa prosedur peyimpanan kita. Jadi, gunakan koneksi conn, buat sebuah cursor (kursos).

cursor = conn.cursor() Sebelum memanggil pengguna membuat prosedur tersimpan, mari membuat password salted menggunakan bantuan yang disediakan oleh Werkzeug. Import modul kedalam app.py:

from werkzeug import generate_password_hash, check_password_hash Gunakan modul salting untuk membuat pasword ber-hash

_hashed_password = generate_password_hash(_password) Sekarang, buat prosedur sp_createUser:

cursor.callproc('sp_createUser',(_name,_email,_hashed_password)) Jika prosedur berhasil dijalankan, maka kita akan melakukan perubahan dan menampilkan pesan sukses.

data = cursor.fetchall()

if len(data) is 0: conn.commit() return json.dumps({'message':'User created successfully !'}) else: return json.dumps({'error':str(data[0])}) Simpan perubahan dan restart server. Buka halaman pendaftaran dan masukkan name, email address dan password dan klik tombol Sign Up. Pada pembuatan pengguna yang sukses, Anda dapat melihat pesan di konsol browser Anda.

{"message": "User created successfully !"}