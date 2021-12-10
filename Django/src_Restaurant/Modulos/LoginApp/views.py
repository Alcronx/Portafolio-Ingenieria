from django.db.models.deletion import RESTRICT
from django.shortcuts import redirect, render
from Modulos.LoginApp.forms import FormularioLogin
from Modulos.LoginApp.models import Login
from Modulos.AdminApp.models import AgregarUsuarios
from django.contrib import messages

def index(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"LOGIN")
    resultadoConsulta = Login.objects.filter(username='ADMIN',passworduser='ADMIN').exists()
    if not resultadoConsulta:
        AgregarUsuarios('ADMIN','ADMIN','ADMIN')
    if(not logeado):
        #recoleta Los Mensajes del sistema
        system_messages = messages.get_messages(request)
        #Comprueba si el Metodo es POST
        if request.method=="POST":
            #Obtiene los datos del formulario
            formulario=FormularioLogin(request.POST)
            #Comprueba si el formulario es Valido
            if formulario.is_valid():
                #Obtiene La Info del formulario
                infForm = formulario.cleaned_data
                #Comprueba si el usuario existe en la base de datos, si es asi retornara link de redireccionamiento
                usuarioExiste,linkRedirect = ComprobarUsuarioDB(infForm['nombre'],infForm['contrasena'],request)
                if usuarioExiste:
                    return redirect(linkRedirect)
                #Si usuario no existe o sucede algun error se enviara mensaje de error
                else:
                    messages.error(request, "Error Al Loguearse intentelo Denuevo")
                    formularioLogin=FormularioLogin()
                    return render(request, "indexLogin.html", {"form":formularioLogin,"mensajes": system_messages})
            #En caso de que formulario no sea valido enviara mensaje de error
            else:
                messages.error(request, "Error Al Loguearse intentelo Denuevo")
                formularioLogin=FormularioLogin()
                return render(request, "indexLogin.html", {"form":formularioLogin,"mensajes": system_messages})
        #Si no es post enviara formulario vacio
        else:
            formularioLogin=FormularioLogin()
            return render(request, "indexLogin.html", {"form":formularioLogin,"mensajes": system_messages})
    else:    
        return redirect(linkredireccion)

      
#Comprueba si el usuario existe en la base de datos
def ComprobarUsuarioDB(nombre,contrasena,request):
    try:
        resultado = Login.objects.get(username=nombre,passworduser=contrasena,state=1)
        nombre = resultado.username
        id = resultado.iduser
        rol = resultado.rol
        estado = resultado.state
        if estado=='1':
            request.session['Nombre']=nombre
            request.session['ID']=id
            request.session['Rol']=rol
            redirecion = redireccionamiento(rol)
            return True,redirecion
        return False,"/"
    except:
        return False,"/"

#Funcion Que comprueba el usuario y redirecciona
def ComprobarUsuario(request,rol):
    if(UsuarioLogeado(request)):
        rolCookie = request.session.get('Rol',False)
        if(ComprobarRol(rolCookie,rol)):
            return True,True,"correcto"
        else:
            return True,False,"/"+redireccionamiento(rolCookie)
    else:
        return False,False,"/"


#Funcion Que Comprueba si usuario esta logeado
def UsuarioLogeado(request):
    if request.session.get('ID',False):
        return True
    else:
        return False
#Funcion que Comprueba si el rol es correcto
def ComprobarRol(rolCookie,rol):
    if rolCookie:
        if rol == rolCookie:
            return True
        else:
            return False
    else:
        return False     

def redireccionamiento(rol):
    return tabla_Redirecion.get(rol,"/")

def desconectar(request):
    try:
        del request.session['Nombre']
        del request.session['ID']
        del request.session['Rol']
        return redirect("/")
    except:
        return redirect("/")

tabla_Redirecion = {
        'ADMIN': 'administrador/',
        'BODEGA': 'bodega/',
        'FINANZAS': 'finanzas/',
        'COCINA': 'cocina/',
        'TOTEM': 'totem/',
    }






        

