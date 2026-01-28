from abc import ABC, abstractmethod
import random


class CommsError(Exception):
    """Base class for communication errors."""

    pass


class TemporalInterferenceError(CommsError):
    pass


class LinkTerminatedError(CommsError):
    pass


class DataCorruptedError(CommsError):
    pass


class OutOfRangeError(CommsError):
    pass


class Packet:
    def __init__(self, data, sender, receiver):
        self.data = data
        self.sender = sender
        self.receiver = receiver

    def __repr__(self):
        return f"Packet(data='{self.data}', sender='{self.sender.name}', receiver='{self.receiver.name}')"


class SpaceEntity(ABC):
    def __init__(self, name, distance_from_earth):
        self.name = name
        self.distance_from_earth = distance_from_earth

    def __repr__(self):
        return f"SpaceEntity(name='{self.name}', distance_from_earth={self.distance_from_earth})"

    @abstractmethod
    def receive_signal(self, packet: Packet):
        pass


class SpaceNetwork:
    def __init__(self, level=1, noise=0.7):
        self._broken_links = set()
        self.level = level
        self.noise = noise if level >= 2 else 0.0

    def send(self, packet: Packet):
        source_entity = packet.sender
        dest_entity = packet.receiver

        # Check for broken link
        link_key = (source_entity.name, dest_entity.name)
        if link_key in self._broken_links:
            raise LinkTerminatedError("Link has been permanently terminated")

        # Check Range
        dist = abs(source_entity.distance_from_earth - dest_entity.distance_from_earth)
        if dist > 150 and self.level > 2:
            raise OutOfRangeError(f"Distance {dist} exceeds max range of 150")

        # Simulate Noise/Errors
        if random.random() < self.noise:
            # Weighted probabilities:
            # TemporalInterferenceError: 50%
            # DataCorruptedError: 60%
            # LinkTerminatedError: 20%
            error_type = random.choices(
                [TemporalInterferenceError, DataCorruptedError, LinkTerminatedError],
                weights=[50, 60, 20],
                k=1,
            )[0]

            if error_type is LinkTerminatedError and self.level > 2:
                self._broken_links.add(link_key)
                raise LinkTerminatedError("Link has been permanently terminated")
            elif error_type is TemporalInterferenceError:
                raise TemporalInterferenceError("Temporary interference, please retry")
            else:
                raise DataCorruptedError("Data corrupted during transmission")

        print(
            f"[Network] Transmitting from {source_entity.name} to {dest_entity.name}..."
        )
        dest_entity.receive_signal(packet)
