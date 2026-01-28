from mission_utils import *
network01 = SpaceNetwork(level=1)
sat1 = Satellite("Sat1",100,network01)
sat2 = Satellite("Sat2",200,network01)

new_message = Packet("Landed safely", sat1 , sat2)
network01.send(new_message)