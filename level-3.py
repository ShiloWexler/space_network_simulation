from mission_utils import *
network03 = SpaceNetwork(level=3)
sat1 = Satellite("Sat1",100,network03)
sat2 = Satellite("Sat2",200,network03)

new_message = Packet("Landed safely", sat1 , sat2)
try:
    attempt_transmission(new_message,network03)
except BrokenConnectionError:
    print("Transmission failed")

