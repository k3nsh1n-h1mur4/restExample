import sqlite3
from sqlite3.dbapi2 import ProgrammingError
from plyer import notification
from datetime import datetime
from reportlab.pdfgen import canvas
from PIL import Image
import qrcode

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer


from django.shortcuts import render, redirect
from django.http import HttpResponse
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
                with sqlite3.connect("db.sqlite3") as cnx:
                    cur = cnx.cursor()
                    worker = cur.execute("INSERT INTO worker(app,apm,nombres,edad,matricula,adscripcion,categoria,n_afil,calle,num,colonia,cp,mcpio,tel_t,tel_p,tel_c,createdat, entRec)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                                (app.upper(),apm.upper(),nombres.upper(),edad,matricula,adscripcion.upper(),categoria.upper(),n_afil,calle.upper(),num,colonia.upper(),cp,mcpio.upper(),tel_t,tel_p,tel_c,entRec.upper(),createdat)) 
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
            with sqlite3.connect('db.sqlite3') as cnx:
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
            with sqlite3.connect('db.sqlite3') as cnx:
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
                with sqlite3.connect('db.sqlite3') as cnx:
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
            with sqlite3.connect('db.sqlite3') as cnx:
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
            alergias = form.cleaned_data['alergias']
            createdat = datetime.now()
            print(app,apm,nombre)
            try:
                with sqlite3.connect('db.sqlite3') as cnx:
                    cur = cnx.cursor()
                    cur.execute("INSERT INTO registerH(app,apm,nombre,f_nac,edad,alergias,createdat,worker_id_id)VALUES(?,?,?,?,?,?,?,?)", \
                        (app.upper(),apm.upper(),nombre.upper(),f_nac,edad,alergias.upper(),createdat,id))
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
            with sqlite3.connect('db.sqlite3') as cnx:
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
            with sqlite3.connect('db.sqlite3') as cnx:
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
                with sqlite3.connect('db.sqlite3') as cnx:
                    cur = cnx.cursor()
                    cur.execute("UPDATE worker SET app=?,apm=?,nombres=?,edad=?,matricula=?,adscripcion=?,categoria=?,n_afil=?,calle=?,num=?,colonia=?,\
                                cp=?,mcpio=?,tel_t=?,tel_p=?,tel_c=?,entRec=?,createdat=? WHERE id=?", (app,apm,nombres,edad,matricula,adscripcion,categoria,n_afil,calle,num,\
                                colonia,cp,mcpio,tel_t,tel_p,tel_c,entRec,createdat,id))
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
            with sqlite3.connect('db.sqlite3') as cnx:
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
                with sqlite3.connect('db.sqlite3') as cnx:
                    cur = cnx.cursor()
                    cur.execute("UPDATE authPer SET app=?,apm=?,nombre=?,parentesco=?,tel=?,createdat=?,authPer_id_id=? WHERE id=?", (app.upper(),apm.upper(), nombre.upper(),parentesco.upper(),tel,createdat,id, id))
                    cnx.commit()
                nt = notification.notify(title='Actualizar Datos', message='Datos actualizados', timeout=10)
                return redirect('listadop')
            except sqlite3.ProgrammingError as e:
                raise e
    return render(request, 'authPer/editPer.html', {'title': title})


def datos(request, id):
    id = id
    title = 'Mostrar Datos'
    if request.method == 'GET':
        try:
            with sqlite3.connect('db.sqlite3') as cnx:
                cur = cnx.cursor()
                cur.execute("""select * from worker inner join authPer on worker.id=authPer_id_id inner join registerH on authPer_id_id=registerH.worker_id_id and worker.id={0}""".format(id))
                result = cur.fetchall()
                print(result)
                cnx.commit()
                for i in result:
                    print(type(i))
        except sqlite3.ProgrammingError as e:
            print(e)
    return render(request, 'worker/datos.html', {'ctx': i})

def create_cred(request, id):
    id = id
    title = 'Crear Credencial'                      
    try:
        #img = Image.open('/Users/k3nsh1n/Dev/restExample/static/cred.png')
        #img.show()
        with sqlite3.connect('db.sqlite3') as cnx:
            #cnx.row_factory = sqlite3.Row
            cur = cnx.cursor() 
            cur.execute("SELECT * FROM worker,authPer,registerH on worker.id=authPer.authPer_id_id and worker.id=registerH.worker_id_id WHERE worker.id={0}".format(id))
            ctx = cur.fetchmany(3)
            cnx.commit()
            nombre = 'Isaac'
            print(ctx)
            print(f'La longituf es: %s' + str(len(ctx)))
            for i in ctx:
                print(i[0])
                print(i[1])
                print(type(i))
            #create_qr(id)
            #qrImage = qrcode.make(i)
            #qrImage.save("qrcodeImage.png")
            #print(nombre)
            c = canvas.Canvas('credencialpdf.pdf')
            c.drawImage('/Users/k3nsh1n/Dev/restExample/static/cred.png', x=10, y=400, width=575, height=400)
            c.setFont('Helvetica', size=10)
            c.drawString(x=47, y=450, text=nombre)
            c.showPage()
            c.save()
    except OSError as e:
        raise e
    response = HttpResponse('Credencial Generada', 'application/json')
    return response


