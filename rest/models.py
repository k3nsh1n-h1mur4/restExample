import sqlite3
from datetime import datetime
from typing_extensions import Required
from django.db import models
from django.utils import timezone


class workerModel(models.Model):
    class Meta:
        db_table = 'worker'
    ENTREC = [
        ("CMNO","CMNO"),
        ("HGR 45","HGR 45"),
        ("HGR 46","HGR 46"),
        ("HGR 110","HGR 110"),
        ("HGR 180","HGR 180"),
        ("HGZ 14","HGZ 14"),
        ("HGZ 89","HGZ 89"),
        ("UMF 1","UMF 1"),
        ("UMF 2","UMF 2"),
        ("UMF 34","UMF 34"),
        ("UMF 39","UMF 39"),
        ("UMF 51","UMF 51"),
        ("UMF 52","UMF 52"),
        ("UMF 53","UMF 53"),
        ("UMF 54","UMF 54"),
        ("UMF 88","UMF 88"),
        ("UMF 93","UMF 93"),
        ("UMF 171","UMF 171"),
        ("UMF 178","UMF 178"),
        ("UMF 184","UMF 184"),
        ("SUB-DEL HIDALGO", "SUB-DEL HIDALGO"),
        ("SUB-DEL JUAREZ","SUB-DEL JUAREZ"),
        ("SNTSS","SNTSS"),
    ]   
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
    entRec = models.CharField(max_length=100, choices=ENTREC, blank=True, null=True, default='CMNO')
    createdat = models.DateTimeField(null=True, blank=True, default=datetime.now())
    
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
    worker_id = models.ForeignKey(workerModel, on_delete=models.CASCADE)
    createdat = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    
