# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Reservado(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cod_id: int=None, id_grupo: int=None, fecha_inicio: str=None, fecha_fin: str=None, hora_inicio: str=None, hora_fin: str=None, dia_semana: str=None):
        """
        Reservado - a model defined in Swagger

        :param cod_id: The cod_id of this Reservado.
        :type cod_id: int
        :param id_grupo: The id_grupo of this Reservado.
        :type id_grupo: int
        :param fecha_inicio: The fecha_inicio of this Reservado.
        :type fecha_inicio: str
        :param fecha_fin: The fecha_fin of this Reservado.
        :type fecha_fin: str
        :param hora_inicio: The hora_inicio of this Reservado.
        :type hora_inicio: str
        :param hora_fin: The hora_fin of this Reservado.
        :type hora_fin: str
        :param dia_semana: The dia_semana of this Reservado.
        :type dia_semana: str
        """
        self.swagger_types = {
            'cod_id': int,
            'id_grupo': int,
            'fecha_inicio': str,
            'fecha_fin': str,
            'hora_inicio': str,
            'hora_fin': str,
            'dia_semana': str
        }

        self.attribute_map = {
            'cod_id': 'codId',
            'id_grupo': 'id_grupo',
            'fecha_inicio': 'fechaInicio',
            'fecha_fin': 'fechaFin',
            'hora_inicio': 'horaInicio',
            'hora_fin': 'horaFin',
            'dia_semana': 'diaSemana'
        }

        self._cod_id = cod_id
        self._id_grupo = id_grupo
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin
        self._dia_semana = dia_semana

    @classmethod
    def from_dict(cls, dikt) -> 'Reservado':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Reservado of this Reservado.
        :rtype: Reservado
        """
        return deserialize_model(dikt, cls)

    @property
    def cod_id(self) -> int:
        """
        Gets the cod_id of this Reservado.

        :return: The cod_id of this Reservado.
        :rtype: int
        """
        return self._cod_id

    @cod_id.setter
    def cod_id(self, cod_id: int):
        """
        Sets the cod_id of this Reservado.

        :param cod_id: The cod_id of this Reservado.
        :type cod_id: int
        """

        self._cod_id = cod_id

    @property
    def id_grupo(self) -> int:
        """
        Gets the id_grupo of this Reservado.

        :return: The id_grupo of this Reservado.
        :rtype: int
        """
        return self._id_grupo

    @id_grupo.setter
    def id_grupo(self, id_grupo: int):
        """
        Sets the id_grupo of this Reservado.

        :param id_grupo: The id_grupo of this Reservado.
        :type id_grupo: int
        """

        self._id_grupo = id_grupo

    @property
    def fecha_inicio(self) -> str:
        """
        Gets the fecha_inicio of this Reservado.

        :return: The fecha_inicio of this Reservado.
        :rtype: str
        """
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: str):
        """
        Sets the fecha_inicio of this Reservado.

        :param fecha_inicio: The fecha_inicio of this Reservado.
        :type fecha_inicio: str
        """

        self._fecha_inicio = fecha_inicio

    @property
    def fecha_fin(self) -> str:
        """
        Gets the fecha_fin of this Reservado.

        :return: The fecha_fin of this Reservado.
        :rtype: str
        """
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, fecha_fin: str):
        """
        Sets the fecha_fin of this Reservado.

        :param fecha_fin: The fecha_fin of this Reservado.
        :type fecha_fin: str
        """

        self._fecha_fin = fecha_fin

    @property
    def hora_inicio(self) -> str:
        """
        Gets the hora_inicio of this Reservado.

        :return: The hora_inicio of this Reservado.
        :rtype: str
        """
        return self._hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio: str):
        """
        Sets the hora_inicio of this Reservado.

        :param hora_inicio: The hora_inicio of this Reservado.
        :type hora_inicio: str
        """

        self._hora_inicio = hora_inicio

    @property
    def hora_fin(self) -> str:
        """
        Gets the hora_fin of this Reservado.

        :return: The hora_fin of this Reservado.
        :rtype: str
        """
        return self._hora_fin

    @hora_fin.setter
    def hora_fin(self, hora_fin: str):
        """
        Sets the hora_fin of this Reservado.

        :param hora_fin: The hora_fin of this Reservado.
        :type hora_fin: str
        """

        self._hora_fin = hora_fin

    @property
    def dia_semana(self) -> str:
        """
        Gets the dia_semana of this Reservado.

        :return: The dia_semana of this Reservado.
        :rtype: str
        """
        return self._dia_semana

    @dia_semana.setter
    def dia_semana(self, dia_semana: str):
        """
        Sets the dia_semana of this Reservado.

        :param dia_semana: The dia_semana of this Reservado.
        :type dia_semana: str
        """

        self._dia_semana = dia_semana
