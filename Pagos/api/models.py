from tabnanny import verbose
from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    telefono=models.PositiveIntegerField()
    direccion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombres + " " + self.apellidos
    

class Cobro(models.Model):
    tipoInscripcion=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    costo=models.PositiveIntegerField()
    fechaCobro=models.DateField()
    
    def __str__(self):
        return self.tipoInscripcion 
        

class Ciudad(models.Model):
    nombre=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pago(models.Model):
    montoTotal=models.IntegerField()
    mesPagado=models.CharField(max_length=20)
    fechaPago=models.DateField()  

    def __str__(self):
        return f'{self.fechaPago}'


class FichaInscripcion(models.Model):
    fechaInscripcion=models.DateField()
    peso=models.CharField(max_length=20)
    estatura=models.CharField(max_length=20)
    cliente=models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)
    cobro=models.ForeignKey(Cobro,null=True,blank=True,on_delete=models.CASCADE)
    ciudad=models.ForeignKey(Ciudad,null=True,blank=True,on_delete=models.CASCADE)
    detallePago=models.ManyToManyField(Pago, through='DetallePago')

    def __str__(self):
        #return str(self.fechaInscripcion), self.peso
        return f'{self.fechaInscripcion} {self.peso} {self.cliente}'


class DetallePago(models.Model):
    pag=models.ForeignKey(Pago,null=True,blank=True,on_delete=models.CASCADE)
    inscripcion=models.ForeignKey(FichaInscripcion,null=True,blank=True,on_delete=models.CASCADE)
    montoDetalle=models.IntegerField()
    fechaDetalle=models.DateField()
    descripcion=models.CharField(max_length=20)


    def __str__(self):
        return f'{self.fechaDetalle}'



    


