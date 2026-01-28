from mission_utils import *
earth = Planet("earth",0)
network05 = SpaceNetwork(level=5)
sat1 = Satellite("Sat1",100,network05)
sat2 = Satellite("Sat2",200,network05)
sat3 = Satellite("sat3",300,network05)
sat4 = Satellite("sat4",400,network05)

p_final = Packet("Hello from Earth", earth ,sat4)


p_earth_path = create_onion_path(p_final,[sat1,sat2,sat3], earth)
attempt_transmission(p_earth_path,network05)
