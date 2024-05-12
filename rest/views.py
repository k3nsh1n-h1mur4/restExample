import sqlite3
from sqlite3.dbapi2 import ProgrammingError
from plyer import notification
from datetime import datetime
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer


from django.shortcuts import render, redirect
from rest.forms import workerForm, authPerForm, regHForm, workerUpdateForm
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
                    cur.execute("INSERT INTO registerH(app,apm,nombre,f_nac,edad,alergias,createdat,regp_id_id)VALUES(?,?,?,?,?,?,?,?)", \
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
            createdat = datetime.now()
            entRec = form.cleaned_data['entRec']
            try:
                with sqlite3.connect('db.sqlite3') as cnx:
                    cur = cnx.cursor()
                    cur.execute("UPDATE worker SET app=?,apm=?,nombres=?,edad=?,adscripcion=?,categoria=?,n_afil=?,calle=?,num=?,colonia=?,\
                                cp=?,mcpio=?,tel_t=?,tel_p=?,tel_c=?,createdat=?,entRec=?", (app,apm,nombres,edad,adscripcion,categoria,n_afil,calle,num,\
                                colonia,cp,mcpio,tel_p,tel_p,tel_c,createdat,entRec))
            except sqlite3.ProgrammingError as e:
                raise e
    return render(request, 'index.html', {'title': title}) 
