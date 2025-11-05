import paho.mqtt.client as mqtt
import ssl
import mysql.connector
from datetime import datetime
import json
import os

# Parámetros
mysql_connection = mysql.connector.connect(
    host="localhost",
    port=27090,
    user="iker",
    password="pirineus",
    database="proyecto"
)
cursor = mysql_connection.cursor()

endpoint = "a119el31cwa6e4-ats.iot.us-east-1.amazonaws.com"  # Endpoint de tu AWS IoT
port = 8883
client_id = "BACKEND_EquipA_1"
suscribe_topic = "institut/registre/ESP_equipA_1" # cambiar a +
public_topic = "institut/resposta/ESP_equipA_1"

# Rutas a tus certificados
root_ca = os.path.join("D:\\Baixades\\arduinoProyectos", "AmazonRootCA1.pem")
cert_file = os.path.join("D:\\Baixades\\arduinoProyectos", "3f72580e05200aa8998d2039b8130074842cc4044cb875ebdb06985486277f0e-certificate.pem.crt")
key_file = os.path.join("D:\\Baixades\\arduinoProyectos", "3f72580e05200aa8998d2039b8130074842cc4044cb875ebdb06985486277f0e-private.pem.key")

# Callback cuando se conecta
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado correctamente a AWS IoT")
        client.subscribe(suscribe_topic)
    else:
        print("Error de conexión, código:", rc)

# Callback para mensajes recibidos
def on_message(client, userdata, msg):
    json_payload = msg.payload.decode('utf-8')
    print(f"Mensaje recibido: {msg.topic} -> {json_payload}")

    try:
        response = {
            "isAllowed": is_allowed_device(json_payload)
        }
        send_message(json.dumps(response))
    except Exception as e:
        print("Error al procesar el mensaje:", e)

def is_allowed_device(json_payload):
    try:
        data = json.loads(json_payload)
        device_id = data.get("device_id")
        if not device_id:
            raise ValueError("device_id no proporcionado en el payload")
    except Exception as e:
        print("Error al parsear JSON:", e)
        return False

    timestamp_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = """
        SELECT COUNT(*)
        FROM DISPOSITIUS d
        JOIN HORARIS h ON h.classe_id = d.classe_id
        WHERE d.device_id = %s
          AND %s BETWEEN h.timestamp_inici AND h.timestamp_fi;
    """
    cursor.execute(query, (device_id, timestamp_now))
    result = cursor.fetchall()
    return result[0][0] > 0

def send_message(message):
    client.publish(public_topic, message)
    print(f"Mensaje enviado: {public_topic} -> {message}")

# Crear cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id)
client.tls_set(ca_certs=root_ca,
               certfile=cert_file,
               keyfile=key_file,
               tls_version=ssl.PROTOCOL_TLSv1_2)
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker
client.connect(endpoint, port)
client.loop_forever()
