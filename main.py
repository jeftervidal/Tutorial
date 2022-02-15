from flask import Flask
from datetime import datetime
from azure.eventhub import EventHubConsumerClient
from azure.eventhub import TransportType


import os
import threading

app=Flask(__name__)

CONNECTION_STR = f'Endpoint=sb://iothub-ns-teste1-ih-17047609-c170a962f5.servicebus.windows.net/;SharedAccessKeyName=service;SharedAccessKey=P9K7Z52S61aYF8=;EntityPath=teste1-ih'
rasp_temp = "Nenhuma atualização ESP32"


# Define callbacks to process events
def on_event_batch(partition_context, event):
    global rasp_temp
    rasp_temp = event.body_as_str()
    print(rasp_temp)
    # for event in events:
        # print("Received event from partition: {}.".format(partition_context.partition_id))
        # print("Telemetry received: ", event.body_as_str())
        # rasp_temp = event.body_as_str();
        # print("Properties (set by device): ", event.properties)
        # print("System properties (set by IoT Hub): ", event.system_properties)
        # print()
    # partition_context.update_checkpoint()

def on_error(partition_context, error):
    # Put your code here. partition_context can be None in the on_error callback.
    if partition_context:
        print("An exception: {} occurred during receiving from Partition: {}.".format(
            partition_context.partition_id,
            error
        ))
    else:
        print("An exception: {} occurred during the load balance process.".format(error))


class TempHum():
    t = 0
    h = 0
    date_t=datetime.today()    
    date_h=datetime.today()
data = TempHum()


@app.route('/')
def Hello_fucking_world():
    return " Save save Familia do IoT -  <br>  <br> --- Together We make IT Happen --- Go Orange --- <br> <br> Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---Together We make IT Happen ---"

@app.route('/gettemp')
def gettemp():
    #return f"Sensor de temperatura - São Paulo - Casa do Jefter {data.date_t.day}/{data.date_t.month}/{data.date_t.year} - {data.date_t.hour}:{data.date_t.minute}:{data.date_t.second} <br> {data.t} Graus Celsius"
    return rasp_temp

@app.route('/settemp/<temp2>')
def settemp(temp2):
    data.t=float(temp2)
    data.date_t=datetime.today()

    return str(data.t) 

@app.route('/gethumidade')
def gethumidade():
    return f"Sensor de temperatura - São Paulo - Casa do Jefter {data.date_h.day}/{data.date_h.month}/{data.date_h.year} - {data.date_h.hour}:{data.date_h.minute}:{data.date_h.second} <br> {data.h} %"
   
@app.route('/sethumidade/<humidade2>')
def sethumidade(humidade2):
    data.h=float(humidade2)
    data.date_h=datetime.today()
    return str(data.h) 

if __name__ == "__main__":
    print("inicializando")
    client = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        consumer_group="$default",
        transport_type=TransportType.AmqpOverWebsocket  # uncomment it if you want to use web socket
        )
    try:
        propriedades = client.get_eventhub_properties()
        print(propriedades)
    except:
        print("Erro conexão com event hub")
    
    # try:
    #     with client:
    #         client.receive_batch(
    #             on_event_batch=on_event_batch,
    #             on_error=on_error
    #         )
    # except KeyboardInterrupt:
    #     print("Receiving has stopped.")
    ConsumerThread = threading.Thread(
        target=client.receive,
        kwargs={
            "on_event": on_event_batch
            # "starting_position": "-1",  # "-1" is from the beginning of the partition.
        }
    )
    ConsumerThread.start()
    app.run(host='0.0.0.0', port=8080,debug=True)
    print("Antes de client.close()")
    client.close()
    print("Após client.close()")