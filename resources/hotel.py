from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Recife'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'João Pessoa'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'Natal'
    },
]



class Hoteis(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """

    def get(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {'Hoteis': hoteis}


class Hotel(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_

    Returns:
        _type_: _description_
    """
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')

    argumentos.add_argument('cidade')

    def find_hotel(self, hotel_id):
        """_summary_

        Args:
            hotel_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel

        return None

    def get(self, hotel_id):
        """_summary_

        Args:
            hotel_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        hotel = Hotel.find_hotel(self, hotel_id)
        return hotel if hotel else {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        """_summary_

        Args:
            hotel_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        """_summary_


        Args:
            hotel_id (_type_): _description_
        """
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)

        hotel = Hotel.find_hotel(self, hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201


    def delete(self, hotel_id):
        """_summary_

        Args:
            hotel_id (_type_): _description_
        """
        Hotel.hoteis = [hotel for hotel in Hotel.hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted'}
        