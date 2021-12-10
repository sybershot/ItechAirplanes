from typing import Dict, Tuple, Type


class AircraftFactory:
    _blueprints: Dict[str, Tuple[Type, Dict]] = {}
              # ^ This abomination is Type info for easing PyCharm's understanding what should be in there (type safety)

    @classmethod
    def get_available_factories(cls):
        return cls._blueprints

    @classmethod
    def register_aircraft(cls, aircraft_name: str, aircraft_type, **info):
        if aircraft_name in cls._blueprints:
            raise RuntimeError(f"Aircraft of type \"{aircraft_name}\" already registered")
        cls._blueprints[aircraft_name] = (aircraft_type, info)

    @classmethod
    def create_aircraft(cls, aircraft_name):
        if aircraft_name in cls._blueprints:
            aircraft_class, aircraft_info = cls._blueprints[aircraft_name]
            return aircraft_class(aircraft_name, **aircraft_info)
        raise RuntimeError(f"No class found for aircraft type \"{aircraft_name}\"")
