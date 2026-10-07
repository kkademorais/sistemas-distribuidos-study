import threading
import queue
import time

def produtor(fila: queue.Queue):
    for i in range(7):
        time.sleep(1)
        mensagem = f"mensagem {i}"
        fila.put(mensagem)
        print(f"Mensagem produzida: {mensagem}")
    fila.put(None)

def consumidor(fila: queue.Queue):
    while True:
        mensagem = fila.get()
        if mensagem is None: 
            fila.task_done()
            break
        print(f"Mensagem consumida: {mensagem}")
        fila.task_done()

fila = queue.Queue()
thread_produtor = threading.Thread(target=produtor, args=[fila])
thread_consumidor = threading.Thread(target=consumidor, args=[fila])
thread_produtor.start()
thread_consumidor.start()
thread_produtor.join()
thread_consumidor.join()
print("fila finalizada..")


#thread = threading.Thread(group=None, target=print, args=["Hello World from Thread"])
#thread.run()