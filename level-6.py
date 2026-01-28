from mission_utils import *
earth = Planet("earth",0)
network06 = SpaceNetwork(level=6)
sat1 = Satellite("Sat1",100,network06)
sat2 = Satellite("Sat2",200,network06)
sat3 = Satellite("sat3",300,network06)
sat4 = Satellite("sat4",400,network06)
sat5 = Satellite("sat5",500,network06)
sat6 = Satellite("sat5",145,network06)
sat7 = Satellite("sat5",230,network06)

p_final = Packet("Hello from Earth", earth ,sat5)


p_earth_path = smart_send_packet(p_final,[sat1,sat2,sat3,sat4,sat5], earth)
attempt_transmission(p_earth_path,network06)
