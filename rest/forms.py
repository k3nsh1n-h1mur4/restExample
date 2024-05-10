from django import forms


class workerForm(forms.Form):    
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
    app = forms.CharField(label='Apellido Paterno', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    apm = forms.CharField(label='Apellido Materno', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    nombres = forms.CharField(label='Nombres', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    edad = forms.CharField(label='Edad', max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    matricula = forms.CharField(label='Matrícula', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    adscripcion = forms.CharField(label='Adscripción', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    categoria = forms.CharField(label='Categoría', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    n_afil = forms.CharField(label='# Afiliación', max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    calle = forms.CharField(label='Calle', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    num = forms.CharField(label='Número Ext.', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    colonia = forms.CharField(label='Colonia', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    cp = forms.CharField(label='Código Postal', max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    mcpio = forms.CharField(label='Municipio', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tel_t = forms.CharField(label='# Trabajo', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tel_p = forms.CharField(label='# Particular', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tel_c = forms.CharField(label='# Célular', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    entRec = forms.ChoiceField(label='Entrega-Recepción', widget=forms.Select(attrs={'class': 'form-control'}), required=False, choices=ENTREC,)

    
class authPerForm(forms.Form):
    app = forms.CharField(label='Apelliod Paterno', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    apm = forms.CharField(label='Apellido Materno', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    nombre = forms.CharField(label='Nombre(s)', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    parentesco = forms.CharField(label='Parentesco', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tel = forms.CharField(label='Teléfono', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    #authPer_id = forms.ForeignKey(workerModel, on_delete=forms.CASCADE)
    #createdat = forms.DateTimeField(auto_now_add=True)

class regHForm(forms.Form):    
    app = forms.CharField(label='Apellido Paterno', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    apm = forms.CharField(label='Apellido Materno', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    nombre = forms.CharField(label='Nombre(s)', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    f_nac = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'class': 'form-control'}), required=False)
    edad = forms.FloatField(label='Edad', widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    alergias = forms.CharField(label='Alergias', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    
    
class workerUpdateForm(forms.Form):
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
    app = forms.CharField(label='Apellido Paterno', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    apm = forms.CharField(label='Apellido Materno', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    nombres = forms.CharField(label='Nombres', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    edad = forms.CharField(label='Edad', max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    matricula = forms.CharField(label='Matrícula', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    adscripcion = forms.CharField(label='Adscripción', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    categoria = forms.CharField(label='Categoría', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    n_afil = forms.CharField(label='# Afiliación', max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    calle = forms.CharField(label='Calle', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    num = forms.CharField(label='Número Ext.', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    colonia = forms.CharField(label='Colonia', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    cp = forms.CharField(label='Código Postal', max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    mcpio = forms.CharField(label='Municipio', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tel_t = forms.CharField(label='# Trabajo', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tel_p = forms.CharField(label='# Particular', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tel_c = forms.CharField(label='# Célular', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    entRec = forms.ChoiceField(label='Entrega-Recepción', widget=forms.Select(attrs={'class': 'form-control'}), required=False, choices=ENTREC,)

