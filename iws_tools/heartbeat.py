from datetime import datetime, timedelta
import socket
import time
import json
from threading import Thread, Event
from pathlib import Path
import inspect

class Heartbeat:
    def __init__(self, server_ip=None, server_port=None, host_name=None, hasSettings=False, pub_callback=None, hourOffset=None):
        self.server_ip = server_ip
        self.server_port = server_port
        self.pub_callback = pub_callback
        self.host_name = host_name
        self.hasSettings = hasSettings
        self.rc = 0
        if self.pub_callback is None:
            self.rc = 1
        self.event = Event()
        self.hourOffset = hourOffset
        directory_name = inspect.getfile(inspect.currentframe())
        ver_path = Path(directory_name).parent / 'version.txt'
        try:
            ver_file = open(ver_path, "r")
            self.version = ver_file.read().strip()
        except:
            self.version = 'unknown'

    def heartbeat_thread(self):
        ''' A thread that will publish a heartbeat every 10 seconds

        A heartbeat message contains the hosts host name, ip address, and the time
        of its last heartbeat message.

        A socket connection is made to the broker in order to determine the ip
        address of the local interface that is connected to the network that the
        broker is on. This method is used in order to deal with the situation
        where the PC has multiple network interface. We only want the ip address of
        the interface connected to the brokers network.
        '''
        
        while self.event.wait(1) is False:
            heartbeat = {}
            address = (self.server_ip, self.server_port)
            if (self.server_ip is not None) & (self.server_port is not None):
                ip_addr = None
                try:
                    with socket.create_connection(address=address, timeout=1) as con:
                        ip_addr = con.getsockname()[0]
                except:
                    ip_addr = socket.gethostbyname(self.host_name)
                heartbeat.update({'hostName': self.host_name,
                                'ipAddress': ip_addr,
                                  'hasSettings':self.hasSettings})
            if self.hourOffset is not None:
                localTime = datetime.utcnow()+ timedelta(hours=self.hourOffset)
                last_heartbeat = localTime.isoformat(sep=' ', timespec='milliseconds')
                heartbeat.update({'lastHeartbeat': last_heartbeat})
            heartbeat.update({'version': self.version})
            json_heartbeat = json.dumps(heartbeat)
            self.pub_callback(json_heartbeat)

    def stop(self):
        self.event.set()

    def start(self):
        if self.rc == 0:
            thread = Thread(target=self.heartbeat_thread, name='Heartbeat Thread')
            thread.start()
        return self.rc
    
