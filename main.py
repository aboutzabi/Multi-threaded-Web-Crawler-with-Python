import http.client
import threading
import logging
import ssl

logging.basicConfig(level=logging.INFO, format='(%(threadName)-10s) %(message)s',)

executed_crawlers = []  # Define the global variable

def save(html, file_absolute_path):
    logging.info("saving {} bytes to {}".format(len(html), file_absolute_path))
    with open(file_absolute_path, 'wb+') as file:
        file.write(html)
        file.flush()

def crawl(req):
    logging.info("executing get request for parameters: {}".format(str(req)))
    if req["scheme"] == "http":
        connection = http.client.HTTPConnection(req["host"], req["port"])
    elif req["scheme"] == "https":
        connection = http.client.HTTPSConnection(req["host"], req["port"], context=ssl._create_unverified_context())
    else:
        logging.error("Invalid scheme specified")
        return None
    
    connection.request("GET", req["path"])
    response = connection.getresponse()
    logging.info("got {} response http code".format(response.status))
    logging.debug("headers: {}".format(str(response.headers)))
    response_content = response.read()
    logging.debug("actual response: {}".format(response_content))
    return response_content

class Mycrawler(threading.Thread):
    def __init__(self, req, file_path):
        threading.Thread.__init__(self, name="Crawler-{}".format(req["host"]))
        self.req = req
        self.file_path = file_path
    
    def run(self):
        global executed_crawlers
        html = crawl(self.req)
        if html is not None:
            save(html, self.file_path)
            executed_crawlers.append(self.getName())

def __main__():
    global executed_crawlers
    continue_input = True
    threads = []
    while continue_input:
        scheme = input("scheme (http/https): ").lower()
        host = input("host: ")
        port = 80 if scheme == "http" else 443  # Default to port 443 for HTTPS
        path = "/"  
        file_path = input("output file absolute path: ")
        req = {"scheme": scheme, "host": host, "port": port, "path": path}
        threads.append(Mycrawler(req, file_path))
        continue_input = input("add another? (y/N) ").lower() == "y"
    
    for t in threads:
        t.start()
        t.join()  # Wait for each thread to finish

    print("Executed crawlers:", executed_crawlers)

__main__()
