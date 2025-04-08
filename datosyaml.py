import yaml

with open('/home/devasc/labs/devnet-src/python/eva1.yaml' , 'r') as archivo:
    archivo_yaml = archivo.read()


parseoyaml  = yaml.safe_load(archivo_yaml)

print("id_usuario:", parseoyaml.get("id_usuario"))
print("token_seguridad:", parseoyaml.get("token_seguridad"))
print("fecha_creacion", parseoyaml.get("fecha_creacion"))
print("estado", parseoyaml.get("estado"))
