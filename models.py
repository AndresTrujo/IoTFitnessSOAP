from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Definición del modelo
Base = declarative_base()

# Definición de la clase Dispositivo
class Dispositivo(Base):
    __tablename__ = "dispositivos"

    id_dispositivo = Column(Integer, primary_key=True, autoincrement=True)
    tipo_dispositivo = Column(String(100), nullable=False)
    marca = Column(String(100), nullable=False)
    num_serie = Column(String(100), nullable=False, unique=True)
    user_id = Column(Integer, nullable=False)

# Configuración de la base de datos
engine = create_engine("mysql+pymysql://root:tnFDznZrsuFkjODbobqazNerUpckRDeb@yamanote.proxy.rlwy.net:50372/railway")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)