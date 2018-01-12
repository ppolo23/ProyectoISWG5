# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Profesor(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, dni: str=None, cantidad: float=None, fecha: str=None):
        """
        Profesor - a model defined in Swagger

        :param dni: The dni of this Profesor.
        :type dni: str
        :param cantidad: The cantidad of this Profesor.
        :type cantidad: float
        :param fecha: The fecha of this Profesor.
        :type fecha: str
        """
        self.swagger_types = {
            'dni': str,
            'cantidad': float,
            'fecha': str
        }

        self.attribute_map = {
            'dni': 'dni',
            'cantidad': 'cantidad',
            'fecha': 'fecha'
        }

        self._dni = dni
        self._cantidad = cantidad
        self._fecha = fecha

    @classmethod
    def from_dict(cls, dikt) -> 'Profesor':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Profesor of this Profesor.
        :rtype: Profesor
        """
        return deserialize_model(dikt, cls)

    @property
    def dni(self) -> str:
        """
        Gets the dni of this Profesor.

        :return: The dni of this Profesor.
        :rtype: str
        """
        return self._dni

    @dni.setter
    def dni(self, dni: str):
        """
        Sets the dni of this Profesor.

        :param dni: The dni of this Profesor.
        :type dni: str
        """

        self._dni = dni

    @property
    def cantidad(self) -> float:
        """
        Gets the cantidad of this Profesor.

        :return: The cantidad of this Profesor.
        :rtype: float
        """
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: float):
        """
        Sets the cantidad of this Profesor.

        :param cantidad: The cantidad of this Profesor.
        :type cantidad: float
        """

        self._cantidad = cantidad

    @property
    def fecha(self) -> str:
        """
        Gets the fecha of this Profesor.

        :return: The fecha of this Profesor.
        :rtype: str
        """
        return self._fecha

    @fecha.setter
    def fecha(self, fecha: str):
        """
        Sets the fecha of this Profesor.

        :param fecha: The fecha of this Profesor.
        :type fecha: str
        """

        self._fecha = fecha

