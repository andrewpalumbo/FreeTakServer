#######################################################
# 
# ClientInformationController.py
# Python implementation of the Class ClientInformationController
# Generated by Enterprise Architect
# Created on:      19-May-2020 6:56:00 PM
# Original author: Natha Paquette
# 
#######################################################
from lxml import etree
from FreeTAKServer.controllers.model.Event import Event
from FreeTAKServer.controllers.model.ClientInformation import ClientInformation
from FreeTAKServer.controllers.BasicModelInstantiate import BasicModelInstantiate
import uuid
from logging.handlers import RotatingFileHandler
import logging
from FreeTAKServer.controllers.configuration.LoggingConstants import LoggingConstants
import sys
from FreeTAKServer.controllers.CreateLoggerController import CreateLoggerController
logger = CreateLoggerController("ClientInformationController").getLogger()
loggingConstants = LoggingConstants()

class ClientInformationController(BasicModelInstantiate):
    def __init__(self):
        pass
    '''
    connection setup is obsolete with intstantiateClientInformationModelFromController
    '''

    def intstantiateClientInformationModelFromConnection(self, rawClientInformation, queue):
        try:
            self.m_clientInformation = ClientInformation()
            argument = "initialConnection"
            self.m_clientInformation.dataQueue = queue
            self.modelObject = Event(argument)
            self.m_clientInformation.socket = rawClientInformation[0]
            self.m_clientInformation.IP = rawClientInformation[1]
            self.m_clientInformation.idData = rawClientInformation[2]
            self.m_clientInformation.alive = 1
            self.m_clientInformation.ID = uuid.uuid1().int
            super().__init__(self.m_clientInformation.idData, self.modelObject)
            self.m_clientInformation.modelObject = self.modelObject
            return self.m_clientInformation
        except Exception as e:
            logger.error('error in client information controller '+str(e))
        
        
        


    def connectionSetup(self, client, address):
        pass
        '''
        try:

            sqliteServer = sqlite3.connect(const.DATABASE)
            cursor = sqliteServer.cursor()

            first_run = 1
            #create client dictionary within main dictionary containing arrays for data and chat also other stuff for client enitial connection
            current_id = 0
            total_clients_connected = 0
            total_clients_connected += 1
            id_data = client.recv(const.STARTBUFFER)
            print(id_data)
            print('\n'+str(id_data))
            print('\n \n')
            tree = ET.fromstring(id_data)
            uid = tree.get('uid')
            if uid == self.bandaidUID:
                return 'Bandaid'
            callsign = tree[1][1].attrib['callsign']
            current_id = uuid.uuid1().int

            #add identifying information
            self.client_dict[current_id] = {'id_data': '', 'main_data': [], 'alive': 1, 'uid': '', 'client':client, 'callsign':callsign}
            self.client_dict[current_id]['id_data'] = id_data
            self.client_dict[current_id]['uid'] = uid
            cursor.execute(sql.INSERTNEWUSER,(str(current_id), str(uid), str(callsign)))
            sqliteServer.commit()
            cursor.close()
            sqliteServer.close()
            #print(self.client_dict)
            logger.info('client connected, information is as follows initial'+ '\n'+ 'connection data:'+str(id_data)+'\n'+'current id:'+ str(current_id))
            return str(first_run)+' ? '+str(total_clients_connected)+' ? '+str(id_data)+' ? '+str(current_id)
        except Exception as e:
            logger.warning('error in connection setup: ' + str(e))
            logger.warning(id_data)
            return "error"
    '''
#rawClientInformation = ['abc', 'def', b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<event version="2.0" uid="ANDROID-359975090666199" type="a-f-G-U-C" time="2020-05-25T12:23:13.288Z" start="2020-05-25T12:23:13.288Z" stale="2020-05-25T12:29:28.288Z" how="h-e"><point lat="43.855596" lon="-66.10805" hae="20.395709421887993" ce="62.1" le="9999999.0"/><detail><takv os="28" version="3.12.0-45691.45691-CIV" device="SAMSUNG SM-G950W" platform="ATAK-CIV"/><contact endpoint="*:-1:stcp" callsign="SUMMER"/><uid Droid="SUMMER"/><precisionlocation altsrc="GPS" geopointsrc="GPS"/><__group role="Sniper" name="Cyan"/><status battery="4"/><track course="191.76600028243948" speed="0.0"/></detail></event>']
#ClientInformationController().intstantiateClientInformationModelFromConnection(rawClientInformation)