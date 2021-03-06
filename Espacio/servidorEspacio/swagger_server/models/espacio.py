# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Espacio(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cod_id: int=None, nombre: str=None, tipo: str=None, capacidad: int=None, precio_hora: int=None, facultad: str=None):
        """
        Espacio - a model defined in Swagger

        :param cod_id: The cod_id of this Espacio.
        :type cod_id: int
        :param nombre: The nombre of this Espacio.
        :type nombre: str
        :param tipo: The tipo of this Espacio.
        :type tipo: str
        :param capacidad: The capacidad of this Espacio.
        :type capacidad: int
        :param precio_hora: The precio_hora of this Espacio.
        :type precio_hora: int
        :param facultad: The facultad of this Espacio.
        :type facultad: str
        """
        self.swagger_types = {
            'cod_id': int,
            'nombre': str,
            'tipo': str,
            'capacidad': int,
            'precio_hora': int,
            'facultad': str
        }

        self.attribute_map = {
            'cod_id': 'codId',
            'nombre': 'nombre',
            'tipo': 'tipo',
            'capacidad': 'capacidad',
            'precio_hora': 'precioHora',
            'facultad': 'facultad'
        }

        self._cod_id = cod_id
        self._nombre = nombre
        self._tipo = tipo
        self._capacidad = capacidad
        self._precio_hora = precio_hora
        self._facultad = facultad

    @classmethod
    def from_dict(cls, dikt) -> 'Espacio':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Espacio of this Espacio.
        :rtype: Espacio
        """
        return deserialize_model(dikt, cls)

    @property
    def cod_id(self) -> int:
        """
        Gets the cod_id of this Espacio.

        :return: The cod_id of this Espacio.
        :rtype: int
        """
        return self._cod_id

    @cod_id.setter
    def cod_id(self, cod_id: int):
        """
        Sets the cod_id of this Espacio.

        :param cod_id: The cod_id of this Espacio.
        :type cod_id: int
        """

        self._cod_id = cod_id

    @property
    def nombre(self) -> str:
        """
        Gets the nombre of this Espacio.

        :return: The nombre of this Espacio.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Sets the nombre of this Espacio.

        :param nombre: The nombre of this Espacio.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def tipo(self) -> str:
        """
        Gets the tipo of this Espacio.

        :return: The tipo of this Espacio.
        :rtype: str
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str):
        """
        Sets the tipo of this Espacio.

        :param tipo: The tipo of this Espacio.
        :type tipo: str
        """

        self._tipo = tipo

    @property
    def capacidad(self) -> int:
        """
        Gets the capacidad of this Espacio.

        :return: The capacidad of this Espacio.
        :rtype: int
        """
        return self._capacidad

    @capacidad.setter
    def capacidad(self, capacidad: int):
        """
        Sets the capacidad of this Espacio.

        :param capacidad: The capacidad of this Espacio.
        :type capacidad: int
        """

        self._capacidad = capacidad

    @property
    def precio_hora(self) -> int:
        """
        Gets the precio_hora of this Espacio.

        :return: The precio_hora of this Espacio.
        :rtype: int
        """
        return self._precio_hora

    @precio_hora.setter
    def precio_hora(self, precio_hora: int):
        """
        Sets the precio_hora of this Espacio.

        :param precio_hora: The precio_hora of this Espacio.
        :type precio_hora: int
        """

        self._precio_hora = precio_hora

    @property
    def facultad(self) -> str:
        """
        Gets the facultad of this Espacio.

        :return: The facultad of this Espacio.
        :rtype: str
        """
        return self._facultad

    @facultad.setter
    def facultad(self, facultad: str):
        """
        Sets the facultad of this Espacio.

        :param facultad: The facultad of this Espacio.
        :type facultad: str
        """

        self._facultad = facultad

