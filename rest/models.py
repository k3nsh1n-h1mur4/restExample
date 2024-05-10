import sqlite3
from django.db import models

class workerModel(models.Model):
    class Meta:
        db_table = 'worker'
        
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=150)
    apm = models.CharField(max_length=150)
    nombres = models.CharField(max_length=150)
    edad = models.CharField(max_length=5)
    matricula = models.CharField(max_length=20)
    adscripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    n_afil = models.CharField(max_length=11)
    calle = models.CharField(max_length=100)
    num = models.CharField(max_length=10)
    colonia = models.CharField(max_length=100)
    cp = models.CharField(max_length=5)
    mcpio = models.CharField(max_length=150)
    tel_t = models.CharField(max_length=10)
    tel_p = models.CharField(max_length=10)
    tel_c = models.CharField(max_length=10)
    createdat = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    entRec = models.CharField(max_length=180)
    
    def __str__(self):
        return '%s' % nombres

    @classmethod
    def create_w(cls, app, apm, nombres, edad, matricula, adscripcion, categoria, n_afil, calle, num, colonia, cp, mcpio, tel_t, tel_p, tel_c):
        
        try:
            with sqlite3.connect('db.sqlite3') as cnx:
                cur = cnx.cursor()
                cur.execute("""INSERT INTO worker VALUES(),""")
                cnx.commit()
        except sqlite3.ProgrammingError as e:
            print(e)    
    
    
class authPer(models.Model):
    class Meta:
        db_table = 'authPer'
        
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=100)
    apm = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=100)
    tel = models.CharField(max_length=30)
    authPer_id = models.ForeignKey(workerModel, on_delete=models.CASCADE)
    createdat = models.DateTimeField(auto_now_add=True)
    
    def __repr__(self):
        return '%s' % nombre
    

class regH(models.Model):
    class Meta:
        db_table = 'registerH'
        
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=100)
    apm = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    f_nac = models.DateField()
    edad = models.FloatField()
    alergias = models.CharField(max_length=150)
    regp_id = models.ForeignKey(workerModel, on_delete=models.CASCADE)
    createdat = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    