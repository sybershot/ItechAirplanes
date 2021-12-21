from aircrafts import aircraft_types, MilitaryAircraft, CivilAircraft, FreighterAircraft
from airline import Airline
from aircraft_factory import AircraftFactory


def list_blueprints(company):
    """
    Prints all available blueprints to the factory.
    """
    blueprints = AircraftFactory.get_available_blueprints()
    print('Available blueprints:')
    for _name, (aircraft_type, info) in blueprints.items():
        print(f'{_name}, {info}')


def add_blueprint(company: Airline):
    """
    Adds new aircraft blueprint to aircraft factory.
    """
    for _i, aircraft_type in enumerate(aircraft_types):
        print(f'{_i + 1}. {aircraft_type.__name__}')
    _type_choice = int(input('Choice (type "0" to go back): ')) - 1
    if _type_choice == -1: return
    if _type_choice > len(aircraft_types) - 1: print('Choice is invalid.')
    _name, flight_range, takeoff_cost, cargo_capacity, passenger_capacity = (
        input('Please enter name of the aircraft: '),
        int(input('Please, enter maximum flight range of the aircraft (NM): ')),
        int(input('Please, enter takeoff cost of the aircraft (US $): ')),
        int(input('Please, enter maximum cargo payload of the aircraft (kg): ')),
        int(input('Please, enter maximum passenger capacity: ')))
    AircraftFactory.register_aircraft(_name, aircraft_types[_type_choice], flight_range=flight_range,
                                      takeoff_cost=takeoff_cost, cargo_capacity=cargo_capacity,
                                      passenger_capacity=passenger_capacity)
    print('Successfully added aircraft to factory!')


def buy_new_aircraft(company: Airline):
    """
    Creates an instance of the selected blueprint.
    """
    blueprints = AircraftFactory.get_available_blueprints()
    _choices = []
    print('Available aircraft for adding:')
    for _i, _name in enumerate(blueprints.keys()):  # showing all available blueprints in factory
        print(f'{_i + 1}. {_name}')
        _choices.append(_name)
    _choice = int(input('Choice (type "0" to go back): ')) - 1
    if _choice == -1: return
    if _choice > len(_choices) - 1: print('Choice is invalid.')
    company.add_aircraft(AircraftFactory.create_aircraft(_choices[_choice]))
    print('Successfully added aircraft to hangar!')


def show_hangar(company: Airline):
    """
    Prints all aircraft in company's hangar.
    """
    if company.get_hangar() == 0:
        print('Hangar is empty! :(')
        return
    print('Aircraft in hangar (sorted by flight range):')
    for aircraft in company.get_hangar():
        print(f'{aircraft.name}, maximum flight range (NM): {aircraft.flight_range}')


def find_aircraft(company: Airline):
    """
    Searches aircraft in company's hangar by specific parameters.
    """
    flight_range, cargo, passengers = int(input('Please, enter minimum required flight range (NM): ')), \
                                      int(input('Please, enter cargo payload (kg): ')), \
                                      int(input('Please, enter number of passengers: '))
    found_aircraft = company.find_aircraft(flight_range, cargo, passengers)
    print(f'Found aircraft: {found_aircraft[0].name}, flight cost: {found_aircraft[1]:.2f}')


def add_test_blueprints(company: Airline):
    """
    Adds three aircraft blueprints to the aircraft factory:
    IL-2, Boeing 747-8, Cargojet B767-200
    """
    AircraftFactory.register_aircraft('IL-2', MilitaryAircraft, flight_range=8000, takeoff_cost=1500,
                                      cargo_capacity=400, passenger_capacity=1)
    AircraftFactory.register_aircraft('Boeing 747-8', CivilAircraft, flight_range=8000, takeoff_cost=1000,
                                      cargo_capacity=120000, passenger_capacity=1048)
    AircraftFactory.register_aircraft('Cargojet B767-200', FreighterAircraft, flight_range=3000, takeoff_cost=10000,
                                      cargo_capacity=45000, passenger_capacity=0)


choices = [('List available aircraft blueprints.', list_blueprints),
           ('Add new blueprint to factory.', add_blueprint),
           ('Add new aircraft to hangar.', buy_new_aircraft),
           ('Show hangar.', show_hangar),
           ('Find suitable aircraft.', find_aircraft),
           ('Add test blueprints to factory.', add_test_blueprints),
           ('Exit.', lambda a: exit(0))]

if __name__ == '__main__':
    airline = Airline()
    while True:
        print('\n\nWELCOME TO DeFault AIRLINES CONTROL CENTER\n'
              'Available options:')
        for i, (name, _) in enumerate(choices):
            print(f'{i + 1}. {name}')

        choice = int(input('Choice: ')) - 1
        if choice > len(choices) - 1:
            print('Choice is invalid.')
            continue
        choices[choice][1](airline)
