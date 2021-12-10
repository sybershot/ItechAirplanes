from abc import ABC
from aircraft_factory import AircraftFactory


# region Aircraft types


class Aircraft(ABC):

    def __init__(self, name, flight_range, takeoff_cost, cargo_capacity, passenger_capacity):
        super().__init__()
        self.name = name
        self.flight_range = flight_range  # flight range is in NM (Nocturnal Mile)
        self.takeoff_cost = takeoff_cost  # cost is in US $
        self.cargo_capacity = cargo_capacity  # cargo capacity means maximum cargo capacity
        self.passenger_capacity = passenger_capacity  # passenger capacity means maximum passenger capacity

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.flight_range}, {self.takeoff_cost}, ' \
               f'{self.cargo_capacity}, {self.passenger_capacity})'

    def calc_flight_cost(self, required_range):
        raise NotImplementedError


class MilitaryAircraft(Aircraft):

    def calc_flight_cost(self, required_range):
        return (self.takeoff_cost + required_range * 0.8) / ((self.cargo_capacity / 1000) + self.passenger_capacity) * 5


class FreighterAircraft(Aircraft):

    def calc_flight_cost(self, required_range):
        return (self.takeoff_cost + required_range * 0.8) / (self.cargo_capacity / 1000)


class CivilAircraft(FreighterAircraft):

    def calc_flight_cost(self, required_range):
        return (self.takeoff_cost + required_range * 0.64) / (
                    (self.cargo_capacity / 1000) + self.passenger_capacity) * 1000


aircraft_types = [MilitaryAircraft, FreighterAircraft, CivilAircraft]

# endregion
AircraftFactory.register_aircraft('IL-2', MilitaryAircraft, flight_range=8000, takeoff_cost=1500,
                                  cargo_capacity=400, passenger_capacity=1)
AircraftFactory.register_aircraft('Boeing 747-8', CivilAircraft, flight_range=8000, takeoff_cost=1000,
                                  cargo_capacity=120000, passenger_capacity=1048)
AircraftFactory.register_aircraft('Cargojet B767-200', FreighterAircraft, flight_range=3000, takeoff_cost=10000,
                                  cargo_capacity=45000, passenger_capacity=0)
