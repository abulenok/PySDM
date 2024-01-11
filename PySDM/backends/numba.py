"""
Multi-threaded CPU backend using LLVM-powered just-in-time compilation
"""

from PySDM.backends.impl_numba.methods.chemistry_methods import ChemistryMethods
from PySDM.backends.impl_numba.methods.collisions_methods import CollisionsMethods
from PySDM.backends.impl_numba.methods.condensation_methods import CondensationMethods
from PySDM.backends.impl_numba.methods.displacement_methods import DisplacementMethods
from PySDM.backends.impl_numba.methods.freezing_methods import FreezingMethods
from PySDM.backends.impl_numba.methods.isotope_methods import IsotopeMethods
from PySDM.backends.impl_numba.methods.moments_methods import MomentsMethods
from PySDM.backends.impl_numba.methods.physics_methods import PhysicsMethods
from PySDM.backends.impl_numba.methods.terminal_velocity_methods import (
    TerminalVelocityMethods,
)
from PySDM.formulae import Formulae
from PySDM.storages.holders.numba import NumbaStorageHolder
from PySDM.storages.numba.backend.index import IndexBackend
from PySDM.storages.numba.backend.pair import PairBackend


class Numba(  # pylint: disable=too-many-ancestors,duplicate-code
    CollisionsMethods,
    PairBackend,
    IndexBackend,
    PhysicsMethods,
    CondensationMethods,
    ChemistryMethods,
    MomentsMethods,
    FreezingMethods,
    DisplacementMethods,
    TerminalVelocityMethods,
    NumbaStorageHolder,
    IsotopeMethods,
):
    default_croupier = "local"

    # TODO #1185  https://github.com/pylint-dev/pylint/issues/9225
    # pylint: disable=super-init-not-called
    def __init__(self, formulae=None, double_precision=True):
        if not double_precision:
            raise NotImplementedError()
        self.formulae = formulae or Formulae()
        CollisionsMethods.__init__(self)
        PhysicsMethods.__init__(self)
        CondensationMethods.__init__(self)
        ChemistryMethods.__init__(self)
        MomentsMethods.__init__(self)
        FreezingMethods.__init__(self)
        DisplacementMethods.__init__(self)
        TerminalVelocityMethods.__init__(self)
