from aircrafts import aircraft_types
from airline import Airline
from aircraft_factory import AircraftFactory


def list_blueprints(company):
    blueprints = AircraftFactory.get_available_factories()
    print('Available blueprints:')
    for _name, (aircraft_type, info) in blueprints.items():
        print(f'{_name}, {info}')


def add_blueprint(company: Airline):
    for _i, aircraft_type in enumerate(aircraft_types):  # showing all available blueprints in factory
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
    blueprints = AircraftFactory.get_available_factories()
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
    if company.get_hangar() == 0:
        print('Hangar is empty! :(')
        return
    print('Aircraft in hangar (sorted by flight range):')
    for aircraft in company.get_hangar():
        print(f'{aircraft.name}, maximum flight range (NM): {aircraft.flight_range}')


def find_aircraft(company: Airline):
    flight_range, cargo, passengers = int(input('Please, enter minimum required flight range (NM): ')), \
                                      int(input('Please, enter cargo payload (kg): ')), \
                                      int(input('Please, enter number of passengers: '))
    found_aircraft = company.find_aircraft(flight_range, cargo, passengers)
    print(f'Found aircraft: {found_aircraft[0].name}, flight cost: {found_aircraft[1]:.2f}')


choices = [('List available aircraft blueprints.', list_blueprints),
           ('Add new blueprint to factory.', add_blueprint),
           ('Add new aircraft to hangar.', buy_new_aircraft),
           ('Show hangar.', show_hangar),
           ('Find suitable aircraft.', find_aircraft),
           ('Exit.', lambda a: exit(0))]

if __name__ == '__main__':
    airline = Airline()
    while True:
        print('\n\nWELCUM TO POOTIS AIRLINES CONTROL CENTER\n'
              'Available options:')
        for i, (name, _) in enumerate(choices):
            print(f'{i + 1}. {name}')

        choice = int(input('Choice: ')) - 1
        if choice > len(choices) - 1:
            print('Choice is invalid.')
            continue
        choices[choice][1](airline)
