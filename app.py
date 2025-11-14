from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from models import Dispositivo, Session

class DispositivoService(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Integer, _returns=Integer)
    def crear(ctx, tipo_dispositivo, marca, num_serie, user_id):
        session = Session()
        nueva = Dispositivo(tipo_dispositivo=tipo_dispositivo, marca=marca, num_serie=num_serie, user_id=user_id)
        session.add(nueva)
        session.commit()
        return nueva.id_dispositivo


    @rpc(Integer, _returns=Unicode)
    def leer(ctx, dispositivo_id):
        session = Session()
        dispositivo = session.get(Dispositivo, dispositivo_id)
        if not dispositivo:
            return "No encontrado"
        return f"{dispositivo.id_dispositivo}: {dispositivo.tipo_dispositivo}, {dispositivo.marca}, {dispositivo.num_serie}, User ID: {dispositivo.user_id}"


    @rpc(Integer, Unicode, Unicode, Unicode, Integer, _returns=Unicode)
    def actualizar(ctx, dispositivo_id, tipo_dispositivo, marca, num_serie, user_id):
        session = Session()
        dispositivo = session.get(Dispositivo, dispositivo_id)
        if not dispositivo:
            return "No encontrado"
        dispositivo.tipo_dispositivo = tipo_dispositivo
        dispositivo.marca = marca
        dispositivo.num_serie = num_serie
        dispositivo.user_id = user_id
        session.commit()

        return "Actualizada"


    @rpc(Integer, _returns=Unicode)
    def eliminar(ctx, dispositivo_id):
        session = Session()
        dispositivo = session.get(Dispositivo, dispositivo_id)
        if not dispositivo:
            return "No encontrado"
        session.delete(dispositivo)
        session.commit()
        return "Eliminada"


application = Application(
    [DispositivoService],
    tns="spyne.dispositivos.app",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    print("Servidor SOAP en http://localhost:8000")
    server = make_server("0.0.0.0", 8000, wsgi_app)
    server.serve_forever()
