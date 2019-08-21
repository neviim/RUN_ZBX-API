#import urllib3
from pyzabbix import ZabbixAPI
from Config import *
from Template import *
from Group import *
from UpdateHost import *
from Host import *
from Skel import *
from Import import *
from ITService import *
from Item import *

zapi = ZabbixAPI(url=server, user=username, password=password)
zapi.session.verify = False