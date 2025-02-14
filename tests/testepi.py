import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', 
        port=5672, 
        virtual_host='/',
        credentials=pika.PlainCredentials('anthony', 'anthony321')
    ))
    print("Conexão com RabbitMQ bem-sucedida!")
    connection.close()
except Exception as e:
    print(f"Erro ao conectar ao RabbitMQ: {e}")
