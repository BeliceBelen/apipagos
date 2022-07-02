#from django.http import HttpResponse
import re
from django.db import DatabaseError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from.models import Cliente, Cobro, Ciudad, Pago
from.models import FichaInscripcion, DetallePago
import json

# Create your views here.
#def inicio(request):
  #  return HttpResponse("Holaaaa bienvenidos →")

class ClienteView(View):
#despachar o enviar datos con el metodo decorador
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#vamos a listar
    def get(self,request,id=0):
        if(id>0):
            clientes=list(Cliente.objects.filter(id=id).values())
            if len(clientes) > 0:
                cliente=clientes[0]
                datos={'message':"Exitos",'clientes':cliente}
            else:
                datos = {'message': "Cliente no encontrado..."}
            return JsonResponse(datos)  
        else:    
            clientes=list(Cliente.objects.values())
            if len(clientes)>0:
                datos={'message':"Success",'clientes':clientes}
            else:
                datos={'message': "Cliente no encontrado..."}
            return JsonResponse(datos)   

#creacion de clientes
    def post(self,request):
        jd=json.loads(request.body)
        #print(jd)
        #crear unnuevo cliente
        Cliente.objects.create(nombres=jd['nombres'],apellidos=jd['apellidos'],
        fechaNacimiento=jd['fechaNacimiento'],telefono=jd['telefono'],direccion=jd['direccion'])
        datos={'message':"Exitos"}
        return JsonResponse(datos)

#modificacion de clientes
    def put(self,request,id):
        jd=json.loads(request.body)
        clientes=list(Cliente.objects.filter(id=id).values())
        if len(clientes) > 0:
            cliente=Cliente.objects.get(id=id)
            cliente.nombres=jd['nombres']
            cliente.apellidos=jd['apellidos']
            cliente.fechaNacimiento=jd['fechaNacimiento']
            cliente.telefono=jd['telefono']
            cliente.direccion=jd['direccion']
            cliente.save()
            datos = {'message':"exitos"}
        else:
            datos = {'message':"Cliente no encontrado"}
        return JsonResponse(datos)

#eliminacion de clientes
    def delete(self,request,id):
        clientes=list(Cliente.objects.filter(id=id).values())
        if len(clientes) > 0:
            Cliente.objects.filter(id=id).delete()
            datos = {'message':"exitos"}
        else: 
            datos = {'message':"Cliente no encontrado"}
        return JsonResponse(datos)  


#--------------TABLA COBROS-------------
class CobroView(View):
#despachar o enviar datos con el metodo decorador
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#vamos a listar
    def get(self,request,id=0):
        if(id>0):
            cobros=list(Cobro.objects.filter(id=id).values())
            if len(cobros) > 0:
                cobro=cobros[0]
                datos={'message':"Exitos",'cobros':cobro}
            else:
                datos = {'message': "Cobro no encontrado..."}
            return JsonResponse(datos)  
        else:    
            cobros=list(Cobro.objects.values())
            if len(cobros)>0:
                datos={'message':"Exitos",'cobros':cobros}
            else:
                datos={'message': "Cobro no encontrado..."}
            return JsonResponse(datos)   

#creacion de cobros
    def post(self,request):
        jd=json.loads(request.body)
        #print(jd)
        #crear unnuevo cobro
        Cobro.objects.create(tipoInscripcion=jd['tipoInscripcion'],descripcion=jd['descripcion'],
        costo=jd['costo'],fechaCobro=jd['fechaCobro'])
        datos={'message':"registro con éxito"}
        return JsonResponse(datos)

#modificacion de cobros
    def put(self,request,id):
        jd=json.loads(request.body)
        cobros=list(Cobro.objects.filter(id=id).values())
        if len(cobros) > 0:
            cobro=Cobro.objects.get(id=id)
            cobro.tipoInscripcion=jd['tipoInscripcion']
            cobro.descripcion=jd['descripcion']
            cobro.costo=jd['costo']
            cobro.fechaCobro=jd['fechaCobro']
            cobro.save()
            datos = {'message':"modificado con éxito"}
        else:
            datos = {'message':"Cobro no encontrado"}
        return JsonResponse(datos)

#eliminacion de cobros
    def delete(self,request,id):
        cobros=list(Cobro.objects.filter(id=id).values())
        if len(cobros) > 0:
            Cobro.objects.filter(id=id).delete()
            datos = {'message':"exitos"}
        else: 
            datos = {'message':"Cobro no encontrado"}
        return JsonResponse(datos)       




#--------------TABLA Ciudad-------------
class CiudadView(View):
#despachar o enviar datos con el metodo decorador
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)           

        
#vamos a listar
    def get(self,request,id=0):
        if(id>0):
            ciudades=list(Ciudad.objects.filter(id=id).values())
            if len(ciudades) > 0:
                ciudad=ciudades[0]
                datos={'message':"Exitos",'ciudades':ciudad}
            else:
                datos = {'message': "Ciudad no encontrada..."}
            return JsonResponse(datos)  
        else:    
            ciudades=list(Ciudad.objects.values())
            if len(ciudades)>0:
                datos={'message':"Exitos",'ciudades':ciudades}
            else:
                datos={'message': "Ciudad no encontrada..."}
            return JsonResponse(datos)   

#creacion de ciudades
    def post(self,request):
        jd=json.loads(request.body)
        #print(jd)
        #crear una nueva ciudad
        Ciudad.objects.create(nombre=jd['nombre'],pais=jd['pais'])
        datos={'message':"registro con éxito"}
        return JsonResponse(datos)

#modificacion de ciudad
    def put(self,request,id):
        jd=json.loads(request.body)
        ciudades=list(Ciudad.objects.filter(id=id).values())
        if len(ciudades) > 0:
            ciudad=Ciudad.objects.get(id=id)
            ciudad.nombre=jd['nombre']
            ciudad.pais=jd['pais']
            ciudad.save()
            datos = {'message':"exitos"}
        else:
            datos = {'message':"Ciudad no encontrada"}
        return JsonResponse(datos)

#eliminacion de ciudad
    def delete(self,request,id):
        ciudades=list(Ciudad.objects.filter(id=id).values())
        if len(ciudades) > 0:
            Ciudad.objects.filter(id=id).delete()
            datos = {'message':"exitos"}
        else: 
            datos = {'message':"Ciudad no encontrada"}
        return JsonResponse(datos)       





#--------------TABLA FICHA-INSCRIPICION-------------
class FichaInscripcionView(View):
#despachar o enviar datos con el metodo decorador
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)           

        
#vamos a listar
    def get(self,request,id=0):
        if(id>0):
            inscripciones=list(FichaInscripcion.objects.filter(id=id).values())
            if len(inscripciones) > 0:
                inscripcion=inscripciones[0]
                datos={'message':"Exitos",'inscripciones':inscripcion}
            else:
                datos = {'message': "inscripcion no encontrada..."}
            return JsonResponse(datos)  
        else:    
            inscripciones=list(FichaInscripcion.objects.values())
            if len(inscripciones)>0:
                datos={'message':"Exitos",'inscripciones':inscripciones}
            else:
                datos={'message': "inscripcion no encontrada..."}
            return JsonResponse(datos)   

#creacion de inscripcion
    def post(self,request):
        jd=json.loads(request.body)
        #print(jd)
        #crear una nuevo
        FichaInscripcion.objects.create(fechaInscripcion=jd['fechaInscripcion'],peso=jd['peso'],estatura=jd['estatura'],
        cliente_id=jd['cliente_id'],cobro_id=jd['cobro_id'],ciudad_id=jd['ciudad_id'])
        datos={'message':"registrado con éxito"}
        return JsonResponse(datos)

#modificacion de inscripcion
    def put(self,request,id):
        jd=json.loads(request.body)
        inscripciones=list(FichaInscripcion.objects.filter(id=id).values())

        if len(inscripciones) > 0:
            inscripcion=FichaInscripcion.objects.get(id=id)
            inscripcion.fechaInscripcion=jd['fechaInscripcion']
            inscripcion.peso=jd['peso']
            inscripcion.estatura=jd['estatura']
            inscripcion.cliente_id=jd['cliente_id']
            inscripcion.cobro_id=jd['cobro_id']
            inscripcion.ciudad_id=jd['ciudad_id']
            inscripcion.save()
            datos = {'message':"exitos"}
            print(datos)
        else:
            datos = {'message':"inscripcion no encontrada"}
            print(datos)
        return JsonResponse(datos)
        

#eliminacion de inscripcion
    def delete(self,request,id):
        inscripciones=list(FichaInscripcion.objects.filter(id=id).values())
        if len(inscripciones) > 0:
            FichaInscripcion.objects.filter(id=id).delete()
            datos = {'message':"exitos"}
        else: 
            datos = {'message':"inscripcion no encontrada"}
        return JsonResponse(datos)       



#--------------TABLA DETALLEPAGO-------------
class DetallePagoView(View):
#despachar o enviar datos con el metodo decorador
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)           

        
#vamos a listar
    def get(self,request,id=0):
        if(id>0):
            detalles=list(DetallePago.objects.filter(id=id).values())
            if len(detalles) > 0:
                detalle=detalles[0]
                datos={'message':"Exitos",'detalles':detalle}
            else:
                datos = {'message': "detalle no encontrado..."}
            return JsonResponse(datos)  
        else:    
            detalles=list(DetallePago.objects.values())
            if len(detalles)>0:
                datos={'message':"Exitos",'detalles':detalles}
            else:
                datos={'message': "detalle no encontrado..."}
            return JsonResponse(datos)   

#creacion de Detallepago
    def post(self,request):
        jd=json.loads(request.body)
        #print(jd)
        #crear una nueva ciudad
        DetallePago.objects.create(pag_id=jd['pag_id'],inscripcion_id=jd['inscripcion_id'],montoDetalle=jd['montoDetalle'],fechaDetalle=jd['fechaDetalle'],
        descripcion=jd['descripcion'])
        datos={'message':"registrado con éxito"}
        return JsonResponse(datos)

#modificacion de Detallepago
    def put(self,request,id):
        jd=json.loads(request.body)
        detalles=list(Pago.objects.filter(id=id).values())

        if len(detalles) > 0:
            detalle=DetallePago.objects.get(id=id)
            detalle.pag_id=jd['pag_id']
            detalle.inscripcion_id=jd['inscripcion_id']
            detalle.montoDetalle=jd['montoDetalle']
            detalle.fechaDetalle=jd['fechaDetalle']
            detalle.descripcion=jd['descripcion']
            detalle.save()
            datos = {'message':"exitos"}
            print(datos)
        else:
            datos = {'message':"detalle no encontrado"}
            print(datos)
        return JsonResponse(datos)
        

#eliminacion de Detallepago
    def delete(self,request,id):
        detalles=list(DetallePago.objects.filter(id=id).values())
        if len(detalles) > 0:
            Pago.objects.filter(id=id).delete()
            datos = {'message':"exitos"}
        else: 
            datos = {'message':"detalle no encontrado"}
        return JsonResponse(datos)       




#--------------TABLA pago-------------
class PagoView(View):
#despachar o enviar datos con el metodo decorador
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)           

        
#vamos a listar
    def get(self,request,id=0):
        if(id>0):
            pagos=list(Pago.objects.filter(id=id).values())
            if len(pagos) > 0:
                pago=pagos[0]
                datos={'message':"Exitos",'pagos':pago}
            else:
                datos = {'message': "inscripcion no encontrada..."}
            return JsonResponse(datos)  
        else:    
            pagos=list(Pago.objects.values())
            if len(pagos)>0:
                datos={'message':"Exitos",'pagos':pagos}
            else:
                datos={'message': "pago no encontrado..."}
            return JsonResponse(datos)   

#creacion de pago
    def post(self,request):
        jd=json.loads(request.body)
        #print(jd)
        #crear un nuevo
        Pago.objects.create(montoTotal=jd['montoTotal'],mesPagado=jd['mesPagado'],fechaPago=jd['fechaPago'])
        datos={'message':"registrado con éxito"}
        return JsonResponse(datos)

#modificacion de pago
    def put(self,request,id):
        jd=json.loads(request.body)
        pagos=list(Pago.objects.filter(id=id).values())

        if len(pagos) > 0:
            pago=Pago.objects.get(id=id)
            pago.montoTotal=jd['montoTotal']
            pago.mesPagado=jd['mesPagado']
            pago.fechaPago=jd['fechaPago']
            pago.save()
            datos = {'message':"exitos"}
            print(datos)
        else:
            datos = {'message':"pago no encontrado"}
            print(datos)
        return JsonResponse(datos)
        

#eliminacion de pago
    def delete(self,request,id):
        pagos=list(Pago.objects.filter(id=id).values())
        if len(pagos) > 0:
            Pago.objects.filter(id=id).delete()
            datos = {'message':"exitos"}
        else: 
            datos = {'message':"pago no encontrado"}
        return JsonResponse(datos)     







# #funiones
#         def factura(self,request,id):
#             datospagos=list(Cliente.objects.filter(id=id).values())

#             return JsonResponse(datospagos)