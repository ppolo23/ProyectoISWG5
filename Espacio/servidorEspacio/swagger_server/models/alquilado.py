# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Alquilado(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cod_id: int=None, id_prof: int=None, fecha: str=None, hora_inicio: str=None, hora_fin: str=None):
        """
        Alquilado - a model defined in Swagger

        :param cod_id: The cod_id of this Alquilado.
        :type cod_id: int
        :param id_prof: The id_prof of this Alquilado.
        :type id_prof: int
        :param fecha: The fecha of this Alquilado.
        :type fecha: str
        :param hora_inicio: The hora_inicio of this Alquilado.
        :type hora_inicio: str
        :param hora_fin: The hora_fin of this Alquilado.
        :type hora_fin: str
        """
        self.swagger_types = {
            'cod_id': int,
            'id_prof': int,
            'fecha': str,
            'hora_inicio': str,
            'hora_fin': str
        }

        self.attribute_map = {
            'cod_id': 'codId',
            'id_prof': 'id_prof',
            'fecha': 'fecha',
            'hora_inicio': 'horaInicio',
            'hora_fin': 'horaFin'
        }

        self._cod_id = cod_id
        self._id_prof = id_prof
        self._fecha = fecha
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin

    @classmethod
    def from_dict(cls, dikt) -> 'Alquilado':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Alquilado of this Alquilado.
        :rtype: Alquilado
        """
        return deserialize_model(dikt, cls)

    @property
    def cod_id(self) -> int:
        """
        Gets the cod_id of this Alquilado.

        :return: The cod_id of this Alquilado.
        :rtype: int
        """
        return self._cod_id

    @cod_id.setter
    def cod_id(self, cod_id: int):
        """
        Sets the cod_id of this Alquilado.

        :param cod_id: The cod_id of this Alquilado.
        :type cod_id: int
        """

        self._cod_id = cod_id

    @property
    def id_prof(self) -> int:
        """
        Gets the id_prof of this Alquilado.

        :return: The id_prof of this Alquilado.
        :rtype: int
        """
        return self._id_prof

    @id_prof.setter
    def id_prof(self, id_prof: int):
        """
        Sets the id_prof of this Alquilado.

        :param id_prof: The id_prof of this Alquilado.
        :type id_prof: int
        """

        self._id_prof = id_prof

    @property
    def fecha(self) -> str:
        """
        Gets the fecha of this Alquilado.

        :return: The fecha of this Alquilado.
        :rtype: str
        """
        return self._fecha

    @fecha.setter
    def fecha(self, fecha: str):
        """
        Sets the fecha of this Alquilado.

        :param fecha: The fecha of this Alquilado.
        :type fecha: str
        """

        self._fecha = fecha

    @property
    def hora_inicio(self) -> str:
        """
        Gets the hora_inicio of this Alquilado.

        :return: The hora_inicio of this Alquilado.
        :rtype: str
        """
        return self._hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio: str):
        """
        Sets the hora_inicio of this Alquilado.

        :param hora_inicio: The hora_inicio of this Alquilado.
        :type hora_inicio: str
        """

        self._hora_inicio = hora_inicio

    @property
    def hora_fin(self) -> str:
        """
        Gets the hora_fin of this Alquilado.

        :return: The hora_fin of this Alquilado.
        :rtype: str
        """
        return self._hora_fin

    @hora_fin.setter
    def hora_fin(self, hora_fin: str):
        """
        Sets the hora_fin of this Alquilado.

        :param hora_fin: The hora_fin of this Alquilado.
        :type hora_fin: str
        """

        self._hora_fin = hora_fin

