from mission_utils import *
network02 = SpaceNetwork(level=2)
sat1 = Satellite("Sat1",100,network02)
sat2 = Satellite("Sat2",200,network02)

new_message = Packet("Landed safely", sat1 , sat2)
attempt_transmission(new_message,network02)
