<<<<<<< HEAD
=======
import openpyxl
import pandas as pd
import io
>>>>>>> c1c9e59edf6b2693c24fe282c3276d12ea48dc47
import os
import glob
import sqlite3
import json
from . import createQR
from pathlib import Path
from sqlite3.dbapi2 import ProgrammingError
from plyer import notification
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from PIL import Image
import qrcode

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer


from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest.forms import workerForm, authPerForm, regHForm, workerUpdateForm, authPerUpdateForm, regHUpdateForm
from rest.models import workerModel


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    
def index(request):
    title = 'Plan Vacacional 2024'
    return render(request, 'index.html', {'title': title})


def registro(request):
    title = " Registro"
    form = workerForm()
    if request.method == 'POST':
        form = workerForm(request.POST)
        if form.is_valid():
            app = form.cleaned_data['app']
            apm = form.cleaned_data['apm'] 
            nombres = form.cleaned_data['nombres'] 
            edad = form.cleaned_data['edad'] 
            matricula = form.cleaned_data['matricula'] 
            adscripcion = form.cleaned_data['adscripcion'] 
            horario = form.cleaned_data['horario']
            categoria = form.cleaned_data['categoria'] 
            n_afil = form.cleaned_data['n_afil'] 
            calle = form.cleaned_data['calle'] 
            num = form.cleaned_data['num'] 
            colonia = form.cleaned_data['colonia'] 
            cp = form.cleaned_data['cp'] 
            mcpio = form.cleaned_data['mcpio'] 
            tel_t = form.cleaned_data['tel_t'] 
            tel_p = form.cleaned_data['tel_p'] 
            tel_c = form.cleaned_data['tel_c'] 
            createdat = datetime.now()
            entRec = form.cleaned_data['entRec']
            try:
                with sqlite3.connect("") as cnx:
                    cur = cnx.cursor()
                    worker = cur.execute("INSERT INTO worker(app,apm,nombres,edad,matricula,adscripcion,horario,categoria,n_afil,calle,num,colonia,cp,mcpio,tel_t,tel_p,tel_c,createdat, entRec)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                                (app.upper(),apm.upper(),nombres.upper(),edad,matricula,adscripcion.upper(),horario,categoria.upper(),n_afil,calle.upper(),num,colonia.upper(),cp,mcpio.upper(),tel_t,tel_p,tel_c,entRec.upper(),createdat)) 
                    cnx.commit()
                    nt = notification.notify(title='Registro', message="Registro Realizado con éxito", timeout=10)
                    return redirect('listado')
            except sqlite3.ProgrammingError as e:
                raise e
            if worker is None:
                nt = notification.notify(title='Error', message='Error al guardar los datos', timeout=15)

    else:
        form = workerForm()
    return render(request, 'worker/registro.html', {'form': form, 'title': title})


def listado(request):
    title = 'Listado General'
    if request.method == 'GET':
        try:
            with sqlite3.connect('') as cnx:
                cur = cnx.cursor()
                cur.execute("SELECT * FROM worker")
                ctx = cur.fetchall()
                cnx.commit()
        except sqlite3.ProgrammingError as e:
            return e
    return render(request, 'worker/listado.html', {'ctx': ctx, 'title': title})


def delete(request, id):
    id = id
    print(id)
    title = 'Eliminar Registro'
    if request.method == 'POST':
        print(request.method)
        try:
            with sqlite3.connect('') as cnx:
                cur = cnx.cursor()
                cur.execute("DELETE FROM worker WHERE id=?",(id))
                cnx.commit()
                return redirect('listado')
            nt = notification.notify(title='Eliminar', message='Registro Eliminado', timeout=10)
        except sqlite3.ProgrammingError as e:
            print(e)
    response = HttpResponse("Registro ELiminado", content_type="application/json")
    return response
                
                
                
   
   
def regauthper(request, id):
    id = id
    print(id)
    title = 'Registro Persona Autorizada'
    form = authPerForm()
    if request.method == 'POST':
        form = authPerForm(request.POST)
        if form.is_valid():
            app = form.cleaned_data['app']
            apm = form.cleaned_data['apm']
            nombre = form.cleaned_data['nombre']
            parentesco = form.cleaned_data['parentesco']
            tel = form.cleaned_data['tel']
            createdat = datetime.now()
            try:
                with sqlite3.connect('') as cnx:
                    cur = cnx.cursor()
                    cur.execute("INSERT INTO authPer(app,apm,nombre,parentesco,tel,createdat,authPer_id_id)VALUES(?,?,?,?,?,?,?)", (app.upper(),apm.upper(),nombre.upper(),parentesco.upper(),tel,createdat,id))
                    cnx.commit()
                    nt = notification.notify(title='Registro', message="Registro Realizado con éxito", timeout=10)
                    return redirect('listado')
            except sqlite3.ProgrammingError as e:
                return e
    return render(request, 'authper/registro.html', {'title': title, 'form': form})


def listadoP(request):
    title = 'Listado Personas Autorizadas'
    if request.method == 'GET':
        ctx = None
        try:
            with sqlite3.connect('') as cnx:
                cur = cnx.cursor()
                cur.execute('SELECT * FROM authPer')
                ctx = cur.fetchall()
                cnx.commit()
        except sqlite3.ProgrammingError as e:
            raise e    
    return render(request, 'authper/listado.html', {'ctx': ctx, 'title': title})


def regh(request, id):
    id = id
    title = 'Registro Hijo(a)'
    form = regHForm()
    if request.method == 'POST':
        form = regHForm(request.POST)
        if form.is_valid():
            app = form.cleaned_data['app']
            apm = form.cleaned_data['apm']
            nombre = form.cleaned_data['nombre']
            f_nac = form.cleaned_data['f_nac']
            edad = form.cleaned_data['edad']
            t_sangre = form.cleaned_data['t_sangre']
            alergias = form.cleaned_data['alergias']
            createdat = datetime.now()
            print(app,apm,nombre)
            try:
                with sqlite3.connect('') as cnx:
                    cur = cnx.cursor()
                    cur.execute("INSERT INTO registerH(app,apm,nombre,f_nac,edad,t_sangre,alergias,createdat,worker_id_id)VALUES(?,?,?,?,?,?,?,?,?)", \
                        (app.upper(),apm.upper(),nombre.upper(),f_nac,edad,t_sangre,alergias.upper(),createdat,id))
                    cnx.commit()
                    nt = notification.notify(title='Registro Hijo', message='Registro Realizado con éxito', timeout=10)
                    return redirect('listado')
            except sqlite3.ProgrammingError as e:
                raise e
    return render(request, 'hijos/registro.html', {'form': form, 'title': title})


def listadoH(request):
    title = 'Listado Hijos Registrados'
    ctx = None
    if request.method == 'GET':
        try:
            with sqlite3.connect('') as cnx:
                cur = cnx.cursor()
                cur.execute("SELECT * FROM registerH")
                ctx = cur.fetchall()
                cnx.commit()
                if ctx == None:
                    nt = notification.notify(title='Error', message='Error, no se encontraton resultados', timeout=10)
        except sqlite3.ProgrammingError as e:
            raise e
    return render(request, 'hijos/listado.html', {'title': title, 'ctx': ctx})

    
def editar(request, id):
    id = id
    title = "Editar Datos"
    form = workerUpdateForm()
    if request.method == 'GET':
        try:
            with sqlite3.connect('') as cnx:
                cur = cnx.cursor()
                cur.execute("SELECT * FROM worker WHERE id={0}".format(id))
                ctx = cur.fetchone()
                cnx.commit()
        except sqlite3.ProgrammingError as e:
            raise e
    return render(request, 'worker/editar.html', {'title': title, 'form': form, 'ctx': ctx})


def save_edit(request, id):
    id = id
    title = 'Guardar Edicion'
    if request.method == 'POST':
        form = workerUpdateForm(request.POST)
        if form.is_valid():
            app = form.cleaned_data['app']
            apm = form.cleaned_data['apm'] 
            nombres = form.cleaned_data['nombres'] 
            edad = form.cleaned_data['edad'] 
            matricula = form.cleaned_data['matricula'] 
            adscripcion = form.cleaned_data['adscripcion'] 
            horario = form.cleaned_data['horario']
            categoria = form.cleaned_data['categoria'] 
            n_afil = form.cleaned_data['n_afil'] 
            calle = form.cleaned_data['calle'] 
            num = form.cleaned_data['num'] 
            colonia = form.cleaned_data['colonia'] 
            cp = form.cleaned_data['cp'] 
            mcpio = form.cleaned_data['mcpio'] 
            tel_t = form.cleaned_data['tel_t'] 
            tel_p = form.cleaned_data['tel_p'] 
            tel_c = form.cleaned_data['tel_c'] 
            entRec = form.cleaned_data['entRec']
            createdat = datetime.now()
            try:
                with sqlite3.connect('') as cnx:
                    cur = cnx.cursor()
                    cur.execute("UPDATE worker SET app=?,apm=?,nombres=?,edad=?,matricula=?,adscripcion=?,horario=?,categoria=?,n_afil=?,calle=?,num=?,colonia=?,\
                                cp=?,mcpio=?,tel_t=?,tel_p=?,tel_c=?,entRec=?,createdat=? WHERE id=?", (app.upper(),apm.upper(),nombres.upper(),edad,matricula,adscripcion.upper(),horario,categoria.upper(),n_afil,calle.upper(),num,\
                                colonia.upper(),cp,mcpio.upper(),tel_t,tel_p,tel_c,entRec,createdat,id))
                nt = notification.notify(title='Actualizacion', message='Datos actualizados', timeout=10)
                return redirect('listado')
            except sqlite3.ProgrammingError as e:
                raise e
    return render(request, 'index.html', {'title': title}) 



def editar_authPer(request, id):
    id = id
    title = "Editar Datos"
    form = authPerUpdateForm()
    if request.method == 'GET':
        try:
            with sqlite3.connect('') as cnx:
                cur = cnx.cursor()
                cur.execute("SELECT * FROM authPer WHERE id={0}".format(id))
                ctx = cur.fetchone()
                cnx.commit()
        except sqlite3.ProgrammingError as e:
            raise e
    return render(request, 'authper/editPer.html', {'title': title, 'form': form, 'ctx': ctx})



def save_edit_p(request, id):
    id = id
    title = 'Editar Datos Personas Autorizadas'
    if request.method == 'POST':
        form = authPerUpdateForm(request.POST)
        if form.is_valid():
            app = form.cleaned_data['app']
            apm = form.cleaned_data['apm']
            nombre = form.cleaned_data['nombre']
            parentesco = form.cleaned_data['parentesco']
            tel = form.cleaned_data['tel']
            createdat = datetime.now()
            try:
                with sqlite3.connect('') as cnx:
                    cur = cnx.cursor()
                    cur.execute("UPDATE authPer SET app=?,apm=?,nombre=?,parentesco=?,tel=?,createdat=?,authPer_id_id=? WHERE id=?", (app.upper(),apm.upper(), nombre.upper(),parentesco.upper(),tel,createdat,id, id))
                    cnx.commit()
                nt = notification.notify(title='Actualizar Datos', message='Datos actualizados', timeout=10)
                return redirect('listadop')
            except sqlite3.ProgrammingError as e:
                raise e
    return render(request, 'authPer/editPer.html', {'title': title})


def edit_h(request, id):
    id = id
    title = 'Editar Datos Hijo(a)'
    form = regHUpdateForm()
    if request.method == 'GET':
        try:
            with sqlite3.connect('') as cnx:
                cur = cnx.cursor()
                cur.execute("SELECT * FROM registerH WHERE id={0}".format(id))
                ctx = cur.fetchone()
                cnx.commit()
        except sqlite3.Error as e:
            print(e)
    return render(request, 'hijos/editar.html', {'title': title, 'ctx': ctx})
                    
            
def save_edit_h(request, id):
    id = id
    title = 'Editar Datos de Hijo(a)'
    if request.method == 'POST':
        form = regHUpdateForm(request.POST)
        if form.is_valid():
            app = form.cleaned_data['app']
            apm = form.cleaned_data['apm']
            nombre = form.cleaned_data['nombre']
            f_nac = form.cleaned_data['f_nac']
            edad = form.cleaned_data['edad']
            t_sangre = form.cleaned_data['t_sangre']
            alergias = form.cleaned_data['alergias']
            try:
                with sqlite3.connect('') as cnx:
                    cur = cnx.cursor()
                    cur.execute("UPDATE registerH SET app=?, apm=?, nombre=?, f_nac=?, edad=?, t_sangre=?, alergias=? WHERE id=?", (app.upper(),apm.upper(),nombre.upper(),f_nac,edad,t_sangre.upper(),alergias.upper(),id))
                    cnx.commit()
                nt = notification.notify(title='Actualizar hijos', message='Datos Actualizados', timeout=10)
                return redirect('listadoH')
            except sqlite3.Error as e:
                print(e) 
    return render(request, 'hijos/editar.html', {'title': title})


def datos(request, id):
    id = id
    title = 'Mostrar Datos'
    if request.method == 'GET':
        try:
            with sqlite3.connect('') as cnx:
                cur = cnx.cursor()
                cur.execute("select * from worker inner join authPer on worker.id=authPer.authPer_id_id inner join registerH on authPer.authPer_id_id=registerH.worker_id_id and worker.id={0}".format(id))
                result = cur.fetchall()
                print(result)
                print(len(result))
                cnx.commit()
        except sqlite3.ProgrammingError as e:
            print(e)
    return JsonResponse(result, safe=False)
    #response = HttpResponse(result, 'application/json')
    #return response
    #return render(request, 'worker/datos.html', {'ctx': result})

def create_cred(request, id):
    id = id
    title = 'Crear Credencial'                      
    try:
<<<<<<< HEAD
        path = Path.cwd()
        qrimg = path.joinpath('qrcode.png')

        path1 = Path.cwd()
        path_static = path1.joinpath('static')
        img_cred = path_static.joinpath('cred.png')
        
        with sqlite3.connect('db.sqlite3') as cnx:
=======
       ()
        with sqlite3.connect('') as cnx:
>>>>>>> c1c9e59edf6b2693c24fe282c3276d12ea48dc47
            #cnx.row_factory = sqlite3.Row
            cur = cnx.cursor()
            cur.execute("""select * from worker inner join authPer on worker.id=authPer_id_id inner join registerH on authPer_id_id=registerH.worker_id_id and registerH.id={0}""".format(id))
            ctx = cur.fetchall()
            cnx.commit()
<<<<<<< HEAD
            qr = createQR.QRCODE
            qr.createqr_code(ctx)
        with sqlite3.connect('') as cnx:
            cur1 = cnx.cursor()
            cur1.execute("SELECT * FROM registerH WHERE id={0}".format(id))
            result = cur1.fetchone()
            print(result)
            cnx.commit()
            name = result[1] + ' ' + result[2] + ' ' + result[3]
            c = canvas.Canvas("Credencial.pdf")
            c.drawImage(img_cred, x=10, y=450, width=570, height=350)
            c.drawImage(image='qrcode.png', x=450 , y=540, width=90, height=90)
            c.setFont('Helvetica', size=10)
            c.drawString(x=55, y=490, text=str(name))
=======
            nombre = ctx[0][29] + ' ' + ctx[0][30] + ' ' + ctx[0][31]
            print(f'La longituf es: ' + str(len(ctx)))
            image = qrcode.make(ctx)
            image.save('qrimage.png')
            #create_qr(id)
            #qrImage = qrcode.make(i)
            #qrImage.save("qrcodeImage.png")
            #print(nombre)
            cred_name = 'credencial' + nombre + '.pdf'
            c = canvas.Canvas(cred_name)
            c.drawImage('cred.png', x=10, y=400, width=575, height=400)
            #c.drawImage('C:/Users/jazyi/Dev/planv/restExample/static/cred.png', x=10, y=400, width=575, height=400)
            c.setFont('Helvetica', size=10)
            c.drawString(x=47, y=450, text=nombre)
            c.drawImage('qrimage.png', x=450, y=510, width=100, height=100)
            #c.drawImage('C:/Users/jazyi/Dev/planv/restExample/qrimage.png', x=450, y=510, width=100, height=100)
>>>>>>> c1c9e59edf6b2693c24fe282c3276d12ea48dc47
            c.showPage()
            c.save()
            
    except OSError as e:
        print(e)
    latest_file = glob.glob('C:/Users/jazyi/Dev/sysplanv/restExample/credencial*.pdf')
    last = max(latest_file, key=os.path.getctime)
    file = open(last, "rb")
    response = HttpResponse(file)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename="cred.pdf"'
    return response
#esponse = HttpResponse('Credencial Generada', 'application/json')
#    return response


def create_sheet(request, id):
    id = id
    title = 'Crear hoja de Registro'
    if request.method == 'GET':
        try:
            with sqlite3.connect('') as cnx:
                cur = cnx.cursor()
                cur.execute("""select * from worker inner join authPer on worker.id=authPer_id_id inner join registerH on authPer_id_id=registerH.worker_id_id and worker.id={0}""".format(id))
                ctx = cur.fetchall()
                cnx.commit()
                print(len(ctx))
                name = ctx[0][1] + ctx[0][2] + ctx[0][3]
                name_reg = 'hojaRegistro' + name + '.pdf'
                c = canvas.Canvas(name_reg)
                c.setPageSize(landscape(letter))
                c.drawImage('/home/catsis/restExample/qrimage.png', x=10, y=400, width=575, height=400)
                #c.drawImage('/Users/k3nsh1n/Dev/planv/restExample/qrimage.png', x=450, y=510, width=100, height=100)
                #c.drawImage('C:/Users/jazyi/Dev/planv/restExample/static/PORTADA.jpg', x=5, y=0, width=770, height=620)
                
                c.drawImage('/home/catsis/restExample/static/PORTADA.jpg', x=5, y=0, width=770, height=620)
                #c.drawImage('/Users/k3nsh1n/Dev/planv/restExample/static/PORTADA.jpg', x=5, y=0, width=770, height=620)
                #c.drawImage('/Users/k3nsh1n/Dev/planv/restExample/static/CONTRAPORTADA.jpg', x=5, y=0, width=770, height=620)
                c.setFont('Helvetica', size=8)
                if len(ctx) == 1:
                #Una per aut--> 1 hijo
                    c.drawString(x=80, y=495, text=ctx[0][1])
                    c.drawString(x=180, y=495, text=ctx[0][2])
                    c.drawString(x=310, y=495, text=ctx[0][3])
                    c.drawString(x=520, y=495, text=ctx[0][4])
                    c.drawString(x=110, y=465, text=ctx[0][5])
                    c.drawString(x=287, y=465, text=ctx[0][6])
                    c.drawString(x=445, y=465, text=ctx[0][18])
                    c.drawString(x=88, y=435, text=ctx[0][7])
                    c.drawString(x=400, y=435, text=ctx[0][8])

                    c.drawString(x=120, y=405, text=ctx[0][9])
                    c.drawString(x=260, y=405, text=ctx[0][10])
                    c.drawString(x=320, y=405, text=ctx[0][11])
                    c.drawString(x=470, y=405, text=ctx[0][12])

                    c.drawString(x=50, y=380, text=ctx[0][13])
                    c.drawString(x=200, y=380, text=ctx[0][14])
                    c.drawString(x=350, y=380, text=ctx[0][15])
                    c.drawString(x=470, y=380, text=ctx[0][16])

                    c.drawString(x=200, y=355, text=ctx[0][19])

                    per1 = ctx[0][21] + '  ' + ctx[0][22] + '  ' + ctx[0][23]
                    c.drawString(x=45, y=285, text=per1)
                    c.drawString(x=380, y=285, text=ctx[0][24])
                    c.drawString(x=480, y=285, text=ctx[0][25])

                    h1 = ctx[0][29] + '  ' + ctx[0][30] + '  ' + ctx[0][31]
                    c.drawString(x=45, y=203, text=h1)
                    c.drawString(x=400, y=203, text=str(ctx[0][33]))
                    c.drawString(x=500, y=203, text=ctx[0][32])
                    c.drawString(x=600, y=203, text=ctx[0][37])
                    c.drawString(x=645, y=203, text=ctx[0][34])

                
                elif len(ctx) == 2:
                    c.drawString(x=80, y=495, text=ctx[0][1])
                    c.drawString(x=180, y=495, text=ctx[0][2])
                    c.drawString(x=310, y=495, text=ctx[0][3])
                    c.drawString(x=520, y=495, text=ctx[0][4])
                    c.drawString(x=110, y=465, text=ctx[0][5])
                    c.drawString(x=287, y=465, text=ctx[0][6])
                    c.drawString(x=445, y=465, text=ctx[0][18])
                    c.drawString(x=88, y=435, text=ctx[0][7])
                    c.drawString(x=400, y=435, text=ctx[0][8])

                    c.drawString(x=120, y=405, text=ctx[0][9])
                    c.drawString(x=260, y=405, text=ctx[0][10])
                    c.drawString(x=320, y=405, text=ctx[0][11])
                    c.drawString(x=470, y=405, text=ctx[0][12])

                    c.drawString(x=50, y=380, text=ctx[0][13])
                    c.drawString(x=200, y=380, text=ctx[0][14])
                    c.drawString(x=350, y=380, text=ctx[0][15])
                    c.drawString(x=470, y=380, text=ctx[0][16])

                    c.drawString(x=200, y=355, text=ctx[0][17])

                    per1 = ctx[0][21] + '  ' + ctx[0][22] + '  ' + ctx[0][23]
                    c.drawString(x=45, y=285, text=per1)
                    c.drawString(x=380, y=285, text=ctx[0][24])
                    c.drawString(x=480, y=285, text=ctx[0][25])
                    
                    per2 = ctx[1][21] + '  ' + ctx[1][22] + '  ' + ctx[1][23]
                    c.drawString(x=45, y=270, text=per2)
                    c.drawString(x=380, y=270, text=ctx[1][24])
                    c.drawString(x=480, y=270, text=ctx[1][25])
                    
                    h1 = ctx[0][29] + '  ' + ctx[0][30] + '  ' + ctx[0][31]
                    c.drawString(x=45, y=203, text=h1)
                    c.drawString(x=400, y=203, text=str(ctx[0][33]))
                    c.drawString(x=500, y=203, text=ctx[0][32])
                    c.drawString(x=600, y=203, text=ctx[0][37])
                    c.drawString(x=645, y=203, text=ctx[0][34])
                    
                    h2 = ctx[1][29] + '  ' + ctx[1][30] + '  ' + ctx[1][31]
                    c.drawString(x=45, y=188, text=h2)
                    c.drawString(x=400, y=188, text=str(ctx[1][33]))
                    c.drawString(x=500, y=188, text=ctx[1][32])
                    c.drawString(x=600, y=188, text=ctx[1][37])
                    c.drawString(x=645, y=188, text=ctx[1][34])

                elif len(ctx) == 3:
                    print(ctx)
                    print(ctx[2][32])
                    print(ctx[2][33])
                    print(ctx[2][34])
                    print(ctx[2][35])
                    print(ctx[2][37])
                    c.drawString(x=80, y=495, text=ctx[0][1])
                    c.drawString(x=180, y=495, text=ctx[0][2])
                    c.drawString(x=310, y=495, text=ctx[0][3])
                    c.drawString(x=520, y=495, text=ctx[0][4])
                    c.drawString(x=110, y=465, text=ctx[0][5])
                    c.drawString(x=287, y=465, text=ctx[0][6])
                    c.drawString(x=445, y=465, text=ctx[0][18])
                    c.drawString(x=88, y=435, text=ctx[0][7])
                    c.drawString(x=400, y=435, text=ctx[0][8])
                    c.drawString(x=120, y=405, text=ctx[0][9])
                    c.drawString(x=260, y=405, text=ctx[0][10])
                    c.drawString(x=320, y=405, text=ctx[0][11])
                    c.drawString(x=470, y=405, text=ctx[0][12])
                    c.drawString(x=50, y=380, text=ctx[0][13])
                    c.drawString(x=200, y=380, text=ctx[0][14])
                    c.drawString(x=350, y=380, text=ctx[0][15])
                    c.drawString(x=470, y=380, text=ctx[0][16])
                    
                    c.drawString(x=200, y=355, text=ctx[0][19])

                    per1 = ctx[0][21] + '  ' + ctx[0][22] + '  ' +ctx[0][23]
                    c.drawString(x=45, y=285, text=per1)
                    c.drawString(x=380, y=285, text=ctx[0][24])
                    c.drawString(x=480, y=285, text=ctx[0][25])

                    h1 = ctx[0][29] + '  ' + ctx[0][30] + '  ' + ctx[0][31]
                    c.drawString(x=45, y=203, text=h1)
                    c.drawString(x=400, y=203, text=str(ctx[0][33]))
                    c.drawString(x=500, y=203, text=ctx[0][32])
                    c.drawString(x=600, y=203, text=ctx[0][37])
                    c.drawString(x=645, y=203, text=ctx[0][34])
                    
                    h2 = ctx[1][29] + '  ' + ctx[1][30] + '  ' + ctx[1][31]
                    c.drawString(x=45, y=186, text=h2)
                    c.drawString(x=400, y=186, text=str(ctx[1][33]))
                    c.drawString(x=500, y=186, text=ctx[1][32])
                    c.drawString(x=600, y=186, text=ctx[1][37])
                    c.drawString(x=645, y=186, text=ctx[1][34]) 
                    
<<<<<<< HEAD
                    h3 = ctx[2][31] + '  ' + ctx[2][30] + '  ' + ctx[2][31]
=======
                    h3 = ctx[2][29] + '  ' + ctx[2][30] + '  ' + ctx[2][31]
>>>>>>> c1c9e59edf6b2693c24fe282c3276d12ea48dc47
                    c.drawString(x=45, y=169, text=h3)
                    c.drawString(x=400, y=169, text=str(ctx[2][33]))
                    c.drawString(x=500, y=169, text=ctx[2][32])
                    c.drawString(x=600, y=169, text=ctx[2][37])
                    c.drawString(x=645, y=169, text=ctx[2][34])
                
                elif len(ctx) == 4:
                    print(ctx)
                    c.drawString(x=80, y=495, text=ctx[0][1])
                    c.drawString(x=180, y=495, text=ctx[0][2])
                    c.drawString(x=310, y=495, text=ctx[0][3])
                    c.drawString(x=520, y=495, text=ctx[0][4])
                    c.drawString(x=110, y=465, text=ctx[0][5])
                    c.drawString(x=287, y=465, text=ctx[0][6])
                    c.drawString(x=445, y=465, text=ctx[0][18])
                    c.drawString(x=88, y=435, text=ctx[0][7])
                    c.drawString(x=400, y=435, text=ctx[0][8])
                    c.drawString(x=120, y=405, text=ctx[0][9])
                    c.drawString(x=260, y=405, text=ctx[0][10])
                    c.drawString(x=320, y=405, text=ctx[0][11])
                    c.drawString(x=470, y=405, text=ctx[0][12])
                    c.drawString(x=50, y=380, text=ctx[0][13])
                    c.drawString(x=200, y=380, text=ctx[0][14])
                    c.drawString(x=350, y=380, text=ctx[0][15])
                    c.drawString(x=470, y=380, text=ctx[0][16])
                    
                    c.drawString(x=200, y=355, text=ctx[0][19])

                    per1 = ctx[0][21] + '  ' + ctx[0][22] + '  ' +ctx[0][23]
                    c.drawString(x=45, y=285, text=per1)
                    c.drawString(x=380, y=285, text=ctx[0][24])
                    c.drawString(x=480, y=285, text=ctx[0][25])
                    
                    per2 = ctx[1][21] + '  ' + ctx[1][22] + '  ' +ctx[1][23]
                    c.drawString(x=45, y=270, text=per2)
                    c.drawString(x=380, y=270, text=ctx[1][24])
                    c.drawString(x=480, y=270, text=ctx[1][25])

                    h1 = ctx[0][29] + '  ' + ctx[0][30] + '  ' + ctx[0][31]
                    c.drawString(x=45, y=203, text=h1)
                    c.drawString(x=400, y=203, text=str(ctx[0][33]))
                    c.drawString(x=500, y=203, text=ctx[0][32])
                    c.drawString(x=600, y=203, text=ctx[0][37])
                    c.drawString(x=645, y=203, text=ctx[0][34])
                    
                    h2 = ctx[2][29] + '  ' + ctx[2][30] + '  ' + ctx[2][31]
                    c.drawString(x=45, y=186, text=h2)
                    c.drawString(x=400, y=186, text=str(ctx[2][33]))
                    c.drawString(x=500, y=186, text=ctx[2][32])
                    c.drawString(x=600, y=186, text=ctx[2][37])
                    c.drawString(x=645, y=186, text=ctx[2][34]) 
                    
                    """
                    h3 = ctx[3][29] + '  ' + ctx[3][30] + '  ' + ctx[3][31]
                    c.drawString(x=45, y=169, text=h3)
                    c.drawString(x=400, y=169, text=str(ctx[3][3]))
                    c.drawString(x=500, y=169, text=ctx[3][32])
                    c.drawString(x=600, y=169, text=ctx[3][37])
                    c.drawString(x=645, y=169, text=ctx[3][34])
                    
                    h4 = ctx[3][29] + '  ' + ctx[3][30] + '  ' + ctx[3][31]
                    c.drawString(x=45, y=151, text=h4)
                    c.drawString(x=400, y=151, text=str(ctx[3][3]))
                    c.drawString(x=500, y=151, text=ctx[3][32])
                    c.drawString(x=600, y=151, text=ctx[3][37])
                    c.drawString(x=645, y=151, text=ctx[3][34])
                    """
                
                elif len(ctx) == 6:
                    # 1 worker --> 2 authPer --> 3 registerH
                    c.drawString(x=80, y=495, text=ctx[0][1])
                    c.drawString(x=180, y=495, text=ctx[0][2])
                    c.drawString(x=310, y=495, text=ctx[0][3])
                    c.drawString(x=520, y=495, text=ctx[0][4])
                    c.drawString(x=110, y=465, text=ctx[0][5])
                    c.drawString(x=287, y=465, text=ctx[0][6])
                    c.drawString(x=445, y=465, text=ctx[0][18])
                    c.drawString(x=88, y=435, text=ctx[0][7])
                    c.drawString(x=400, y=435, text=ctx[0][8])
                    c.drawString(x=120, y=405, text=ctx[0][9])
                    c.drawString(x=260, y=405, text=ctx[0][10])
                    c.drawString(x=320, y=405, text=ctx[0][11])
                    c.drawString(x=470, y=405, text=ctx[0][12])
                    c.drawString(x=50, y=380, text=ctx[0][13])
                    c.drawString(x=200, y=380, text=ctx[0][14])
                    c.drawString(x=350, y=380, text=ctx[0][15])
                    c.drawString(x=470, y=380, text=ctx[0][16])
                    
                    c.drawString(x=200, y=355, text=ctx[0][19])

                    per1 = ctx[0][21] + '  ' + ctx[0][22] + '  ' +ctx[0][23]
                    c.drawString(x=45, y=285, text=per1)
                    c.drawString(x=380, y=285, text=ctx[0][24])
                    c.drawString(x=480, y=285, text=ctx[0][25])
                    
                    per2 = ctx[1][21] + '  ' + ctx[1][22] + '  ' +ctx[1][23]
                    c.drawString(x=45, y=270, text=per2)
                    c.drawString(x=380, y=270, text=ctx[1][24])
                    c.drawString(x=480, y=270, text=ctx[1][25])

                    h1 = ctx[0][29] + '  ' + ctx[0][30] + '  ' + ctx[0][31]
                    c.drawString(x=45, y=203, text=h1)
                    c.drawString(x=400, y=203, text=str(ctx[0][33]))
                    c.drawString(x=500, y=203, text=ctx[0][32])
                    c.drawString(x=600, y=203, text=ctx[0][37])
                    c.drawString(x=645, y=203, text=ctx[0][34])
                    
                    h2 = ctx[2][29] + '  ' + ctx[2][30] + '  ' + ctx[2][31]
                    c.drawString(x=45, y=186, text=h2)
                    c.drawString(x=400, y=186, text=str(ctx[2][33]))
                    c.drawString(x=500, y=186, text=ctx[2][32])
                    c.drawString(x=600, y=186, text=ctx[2][37])
                    c.drawString(x=645, y=186, text=ctx[2][34]) 
                    
                    h3 = ctx[4][29] + '  ' + ctx[4][30] + '  ' + ctx[4][31]
                    c.drawString(x=45, y=169, text=h3)
                    c.drawString(x=400, y=169, text=str(ctx[5][33]))
                    c.drawString(x=500, y=169, text=ctx[5][32])
                    c.drawString(x=600, y=169, text=ctx[5][37])
                    c.drawString(x=645, y=169, text=ctx[5][34])

                elif len(ctx) == 8:
                    # 1 worker  --> 2 authPer --> 4 registerH
                    c.drawString(x=80, y=495, text=ctx[0][1])
                    c.drawString(x=180, y=495, text=ctx[0][2])
                    c.drawString(x=310, y=495, text=ctx[0][3])
                    c.drawString(x=520, y=495, text=ctx[0][4])
                    c.drawString(x=110, y=465, text=ctx[0][5])
                    c.drawString(x=287, y=465, text=ctx[0][6])
                    c.drawString(x=445, y=465, text=ctx[0][18])
                    c.drawString(x=88, y=435, text=ctx[0][7])
                    c.drawString(x=400, y=435, text=ctx[0][8])
                    c.drawString(x=120, y=405, text=ctx[0][9])
                    c.drawString(x=260, y=405, text=ctx[0][10])
                    c.drawString(x=320, y=405, text=ctx[0][11])
                    c.drawString(x=470, y=405, text=ctx[0][12])
                    c.drawString(x=50, y=380, text=ctx[0][13])
                    c.drawString(x=200, y=380, text=ctx[0][14])
                    c.drawString(x=350, y=380, text=ctx[0][15])
                    c.drawString(x=470, y=380, text=ctx[0][16])
                    
                    c.drawString(x=200, y=355, text=ctx[0][19])

                    per1 = ctx[0][21] + '  ' + ctx[0][22] + '  ' +ctx[0][23]
                    c.drawString(x=45, y=285, text=per1)
                    c.drawString(x=380, y=285, text=ctx[0][24])
                    c.drawString(x=480, y=285, text=ctx[0][25])
                    
                    per2 = ctx[1][21] + '  ' + ctx[1][22] + '  ' +ctx[1][23]
                    c.drawString(x=45, y=270, text=per2)
                    c.drawString(x=380, y=270, text=ctx[1][24])
                    c.drawString(x=480, y=270, text=ctx[1][25])

                    h1 = ctx[0][29] + '  ' + ctx[0][30] + '  ' + ctx[0][31]
                    c.drawString(x=45, y=203, text=h1)
                    c.drawString(x=400, y=203, text=str(ctx[0][33]))
                    c.drawString(x=500, y=203, text=ctx[0][32])
                    c.drawString(x=600, y=203, text=ctx[0][37])
                    c.drawString(x=645, y=203, text=ctx[0][34])
                    
                    h2 = ctx[2][29] + '  ' + ctx[2][30] + '  ' + ctx[2][31]
                    c.drawString(x=45, y=186, text=h2)
                    c.drawString(x=400, y=186, text=str(ctx[2][33]))
                    c.drawString(x=500, y=186, text=ctx[2][32])
                    c.drawString(x=600, y=186, text=ctx[2][37])
                    c.drawString(x=645, y=186, text=ctx[2][34]) 
                    
                    h3 = ctx[4][29] + '  ' + ctx[4][30] + '  ' + ctx[4][31]
                    c.drawString(x=45, y=169, text=h3)
                    c.drawString(x=400, y=169, text=str(ctx[5][33]))
                    c.drawString(x=500, y=169, text=ctx[5][32])
                    c.drawString(x=600, y=169, text=ctx[5][37])
                    c.drawString(x=645, y=169, text=ctx[5][34])
                    
                    h4 = ctx[6][29] + '  ' + ctx[6][30] + '  ' + ctx[6][31]
                    c.drawString(x=45, y=151, text=h4)
                    c.drawString(x=400, y=151, text=str(ctx[6][33]))
                    c.drawString(x=500, y=151, text=ctx[6][32])
                    c.drawString(x=600, y=151, text=ctx[6][37])
                    c.drawString(x=645, y=151, text=ctx[6][34])
                
                    c.showPage()
                
<<<<<<< HEAD
                #c.drawImage('/Users/k3nsh1n/Dev/planv/restExample/static/CONTRAPORTADA.jpg', x=5, y=0, width=770, height=620)
                c.drawImage('/home/catsis/restExample/static/CONTRAPORTADA.png', x=0, y=0, width=770, height=620)
                c.showPage()
                c.save()
        except sqlite3.Error as e:
            print(e)
    latest_file = glob.glob('/home/catsis/restExample/hojaRegistro*.pdf')
    last = max(latest_file, key=os.path.getctime)
    file = open(last, "rb")
=======
                    c.drawImage('/Users/k3nsh1n/Dev/planv/restExample/static/CONTRAPORTADA.jpg', x=5, y=0, width=770, height=620)
                    c.showPage()
                    c.drawImage('C:/Users/jazyi/Dev/planv/restExample/static/CONTRAPORTADA.jpg')
                    c.showPage()
                    c.save()
        except sqlite3.Error as e:
            print(e)
    latest_file = glob.glob('C:/Users/jazyi/Dev/planv/restExample/hojaRegistro*.pdf')
    last = max(latest_file, key=os.path.getctime)
    file =open(last, 'rb')
>>>>>>> c1c9e59edf6b2693c24fe282c3276d12ea48dc47
    response = HttpResponse(file)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename="port.pdf"'
    return response



def create_excel(ctx):
    df = pd.DataFrame(ctx)
    df.to_excel('exportDB.xlsx', sheet_name='totales')


def export_toExcel(request):
    title = 'Export Excel'
    try:
        with sqlite3.connect('db.sqlite3') as cnx:
            cur = cnx.cursor()
            cur.execute("SELECT * FROM worker, authPer, registerH WHERE worker.id=authPer.authPer_id_id AND worker.id=registerH.worker_id_id")
            ctx = cur.fetchall()
            cnx.commit()
            create_excel(ctx)
    except sqlite3.Error as e:
        print(e)
    latest_file = glob.glob('C:/Users/jazyi/Dev/planv/restExample/*.xlsx')
    last = max(latest_file, key=os.path.getctime)
    file =open(last, 'rb')
    response = HttpResponse(file)
    response.headers['Content-Type'] = 'application/vnd.ms-excel'
    response.headers['Content-Disposition'] = 'attachment; filename="resume.xlsx"'
    return response
