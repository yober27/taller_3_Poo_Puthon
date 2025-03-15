
from Cliente import cliente
from Saludo import saludo

# ++++++++++ Codigo Principal ++++++
objCliente = cliente()
objSaludo = saludo()

#uso los datos de los objetos
objCliente.tomar_datos()
aux_mensaje = objSaludo.hacer_saludo_formal()
objCliente.hacer_saludo(aux_mensaje)

#llamo a los metodos del objeto
