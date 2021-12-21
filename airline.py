from typing import List

from aircraft_factory import AircraftFactory
import aircrafts


class Airline:
    def __init__(self):
        self._hangar: List[aircrafts.Aircraft] = []

    def get_hangar(self):
        return self._hangar

    def add_aircraft(self, aircraft: aircrafts.Aircraft):
        self._hangar.append(aircraft)
        self._hangar.sort(key=lambda a: a.flight_range)

    def find_aircraft(self, flight_range, cargo, passengers):
        suitable = filter(lambda a: flight_range <= a.flight_range and
                                    cargo <= a.cargo_capacity and
                                    passengers <= a.passenger_capacity, self._hangar)
        _aircraft = {aircraft.calc_flight_cost(flight_range): aircraft for aircraft in suitable}
        cheapest = min(_aircraft.keys())
        return _aircraft[cheapest], cheapest
