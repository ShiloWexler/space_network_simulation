from space_network_lib import *
import time
class Satellite(SpaceEntity):
    def __init__(self, name, distance_from_earth, network):
        super().__init__(name=name, distance_from_earth= distance_from_earth)
        self.network = network
    def receive_signal(self, packet)->None:
        if isinstance(packet, RelayPacket):
            inner_packet = packet.data
            inner_packet.sender = self
            network_to_receive = self.network
            print(f"Unwrapping and forwarding to {inner_packet.receiver}")
            attempt_transmission(inner_packet, network_to_receive)
        else:
            print( f"{self.name}  Received: {packet}.")
class BrokenConnectionError(Exception):
    pass

def attempt_transmission(packet , network:SpaceNetwork):
    while True:
        try:
            network.send(packet)
            print("Transmission successful!")
            break
        except TemporalInterferenceError:
            print("Interference, waiting 2 seconds...")
            time.sleep(2)
        except DataCorruptedError:
            print("...corrupted, retrying immediately")
        except LinkTerminatedError:
            print("Link lost")
            raise BrokenConnectionError()
        except OutOfRangeError:
            print("Target out of range")
            raise BrokenConnectionError()

class RelayPacket(Packet):
    def __init__(self, packet_to_relay:Packet, sender, proxy ):
        super().__init__(sender= sender, data= packet_to_relay, receiver= proxy)
    def __repr__(self):
        return f"RelayPacket(Relaying [{self.data}] to {self.receiver} from {self.sender})"
class Planet(SpaceEntity):
    def receive_signal(self, packet: Packet):
        pass
def create_onion_path(original_packt, path_list, origin_sender):
    correct_packet = original_packt
    for satellite in reversed(path_list):
        correct_packet = RelayPacket(packet_to_relay=correct_packet, sender=origin_sender, proxy=satellite)
    return correct_packet
def smart_send_packet(original_packt:Packet, satellite_list, origin_sender):
    correct_packet = original_packt
    updated_list =[]
    for i in range(len(satellite_list)):
        if original_packt.sender.distance_from_earth < \
                satellite_list[i].distance_from_earth < original_packt.receiver.distance_from_earth:
            updated_list.append(satellite_list[i])
    for i in range(len(updated_list)):
        for j in range(len(updated_list)-1-i):
            if updated_list[j].distance_from_earth < updated_list[j+1].distance_from_earth:
                updated_list[j], updated_list[j + 1] = updated_list[j + 1], updated_list[j]
    for satellite in updated_list:
        correct_packet = RelayPacket(packet_to_relay=correct_packet, sender=origin_sender, proxy=satellite)
    return correct_packet
