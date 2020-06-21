#######################################################
# 
# sendClientData.py
# Python implementation of the Class sendClientData
# Generated by Enterprise Architect
# Created on:      19-May-2020 7:37:17 PM
# Original author: Natha Paquette
# 
#######################################################

from logging.handlers import RotatingFileHandler
import logging
from FreeTAKServer.controllers.configuration.LoggingConstants import LoggingConstants
import sys
from FreeTAKServer.controllers.CreateLoggerController import CreateLoggerController
logger = CreateLoggerController("SendClientData").getLogger()

loggingConstants = LoggingConstants()

class SendClientData:
    def __init__(self):
        pass
    def SendDataInQueue(self,  dataQueue, clientQueue):
        logger.info(loggingConstants.SENDCLIENTDATASENDDATAINQUEUEINFO)
        while True:
            tempQueue = clientQueue
            tempArray = []
            if dataQueue.empty() == False:
                while tempQueue.empty() == False:
                   tempArray.append(tempQueue.get())
                data = dataQueue.get()
                sender = data.clientInformation
                for client in tempArray:
                    clientInformation = client.clientInformation
                    if clientInformation != sender:
                        sock = client.clientInformation.socket
                        
                        sock.send(data.xmlString)
                    else:
                        pass
            else:
                pass
    
    def HelloWorld(self):
        print('hello world')
        '''
        killSwitch = 0
        try:
            while killSwitch == 0:
                time.sleep(const.DELAY)
                if killSwitch == 1:
                    break
                if len(self.emergencyDict)>0:
                        for x in self.emergencyDict:
                            client.send(self.emergencyDict[x])
                        logger.debug('emergency activated')
                else:
                    pass

                if len(self.client_dict[current_id]['main_data'])>0:

                    for x in self.client_dict[current_id]['main_data']:
                        logger.debug(self.client_dict[current_id]['main_data'])
                        client.send(x)
                        print('\n'+'sent '+ str(x)+' to '+ str(address) + '\n')
                        self.client_dict[current_id]['main_data'].remove(x)

                else:
                    client.send(Serializer().serializerRoot(RequestCOTController().ping(eventuid = uuid.uuid1())).encode())
            client.shutdown()
            client.close()
        except Exception as e:
            logger.warning('error in send info '+str(e))
            client.shutdown()
            client.close()
            return 1
        '''