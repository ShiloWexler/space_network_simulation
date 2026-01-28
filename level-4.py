from mission_utils import *
earth = Planet("earth",0)
network04 = SpaceNetwork(level=4)
sat1 = Satellite("Sat1",100,network04)
sat2 = Satellite("Sat2",200,network04)

p_final = Packet("Hello from Earth", earth ,sat2)
p_earth_to_sat1 = RelayPacket(p_final,earth,sat1)
attempt_transmission(p_earth_to_sat1,network04)
