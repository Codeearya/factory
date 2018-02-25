from xml_json_factory.connector_factory import *

def main():

    sqlite_factory = connect_to('xml_json_factory/data/person.sq3')

    print()

    xml_factory = connect_to('xml_json_factory/data/person.xml')

    xml_data = xml_factory.parsed_data

    liars = xml_data.findall(".//{}[{}='{}']".format('person','lastName', 'Liar'))

    print('found: {} persons'.format(len(liars)))

    for liar in liars:


        print('first name: {}'.format(liar.find('firstName').text))

        print('last name: {}'.format(liar.find('lastName').text))

        [print('phone number ({}):'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]

    print()

    json_factory = connect_to('xml_json_factory/data/donut.json')

    json_data = json_factory.parsed_data

    print('found: {} donuts'.format(len(json_data)))

    for donut in json_data:

     print('name: {}'.format(donut['name']))

     print('price: ${}'.format(donut['ppu']))

     [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]

if __name__ == '__main__':

    main()