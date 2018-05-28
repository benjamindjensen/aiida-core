# -*- coding: utf-8 -*-
from .identifier import IdentifierParamType


class CalculationParamType(IdentifierParamType):
    """
    The ParamType for identifying Calculation entities or its subclasses
    """

    name = 'Calculation'

    @property
    def orm_class_loader(self):
        """
        Return the orm entity loader class, which should be a subclass of OrmEntityLoader. This class is supposed
        to be used to load the entity for a given identifier 

        :return: the orm entity loader class for this ParamType
        """
        from aiida.orm.utils.loaders import CalculationEntityLoader
        return CalculationEntityLoader
