# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _pressure_fixed_level.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pressure_fixed_level')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pressure_fixed_level')
    _pressure_fixed_level = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pressure_fixed_level', [dirname(__file__)])
        except ImportError:
            import _pressure_fixed_level
            return _pressure_fixed_level
        try:
            _mod = imp.load_module('_pressure_fixed_level', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pressure_fixed_level = swig_import_helper()
    del swig_import_helper
else:
    import _pressure_fixed_level
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


SHARED_PTR_DISOWN = _pressure_fixed_level.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.pressure_imp_base
import full_physics_swig.pressure
import full_physics_swig.state_vector
import full_physics_swig.generic_object
class PressureFixedLevel(full_physics_swig.pressure_imp_base.PressureImpBase):
    """

    This class maintains the pressure portion of the state.

    This particular implementation has a fixed set of pressure levels,
    with only the surface pressure changing. As the surface pressure
    changes, it may pass a pressure level, changing the number of levels
    that lie above the surface.

    C++ includes: pressure_fixed_level.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, Pressure_flag, Press_level, Surface_pressure):
        """

        FullPhysics::PressureFixedLevel::PressureFixedLevel(bool Pressure_flag, const boost::shared_ptr< PressureLevelInput >
        &Press_level, double Surface_pressure)

        """
        _pressure_fixed_level.PressureFixedLevel_swiginit(self, _pressure_fixed_level.new_PressureFixedLevel(Pressure_flag, Press_level, Surface_pressure))

    def _v_surface_pressure_uncertainty(self):
        """

        double FullPhysics::PressureFixedLevel::surface_pressure_uncertainty() const
        Return the current surface pressure uncertainty. This is in Pascals.

        """
        return _pressure_fixed_level.PressureFixedLevel__v_surface_pressure_uncertainty(self)


    @property
    def surface_pressure_uncertainty(self):
        return self._v_surface_pressure_uncertainty()


    def set_surface_pressure(self, Surface_pressure):
        """

        void FullPhysics::PressureFixedLevel::set_surface_pressure(const AutoDerivative< double > &Surface_pressure)
        Set the surface pressure. This is in Pascals. 
        """
        return _pressure_fixed_level.PressureFixedLevel_set_surface_pressure(self, Surface_pressure)


    def _v_number_active_level(self):
        """

        int FullPhysics::PressureFixedLevel::number_active_level() const
        Number of active levels, this is just the size of pressure_grid for
        the current surface pressure. 
        """
        return _pressure_fixed_level.PressureFixedLevel__v_number_active_level(self)


    @property
    def number_active_level(self):
        return self._v_number_active_level()


    def _v_number_active_layer(self):
        """

        int FullPhysics::PressureFixedLevel::number_active_layer() const
        Number of active layers.

        This is 1 less than the number of levels, since the levels give the
        top an bottom of a layer. 
        """
        return _pressure_fixed_level.PressureFixedLevel__v_number_active_layer(self)


    @property
    def number_active_layer(self):
        return self._v_number_active_layer()


    @property
    def max_number_level(self):
        return self._v_max_number_level()


    def _v_pressure_active_levels(self):
        """

        blitz::Array<double, 1> FullPhysics::PressureFixedLevel::pressure_active_levels() const
        Return the pressure on the fixed levels, but only include the
        "active" portion.

        This is all the pressure levels above the surface, plus the last one
        at or below the surface. This is the same size as pressure_grid, but
        differs in that the bottom level typically lies below the surface 
        """
        return _pressure_fixed_level.PressureFixedLevel__v_pressure_active_levels(self)


    @property
    def pressure_active_levels(self):
        return self._v_pressure_active_levels()

    __swig_destroy__ = _pressure_fixed_level.delete_PressureFixedLevel
PressureFixedLevel._v_surface_pressure_uncertainty = new_instancemethod(_pressure_fixed_level.PressureFixedLevel__v_surface_pressure_uncertainty, None, PressureFixedLevel)
PressureFixedLevel.set_surface_pressure = new_instancemethod(_pressure_fixed_level.PressureFixedLevel_set_surface_pressure, None, PressureFixedLevel)
PressureFixedLevel._v_number_active_level = new_instancemethod(_pressure_fixed_level.PressureFixedLevel__v_number_active_level, None, PressureFixedLevel)
PressureFixedLevel._v_number_active_layer = new_instancemethod(_pressure_fixed_level.PressureFixedLevel__v_number_active_layer, None, PressureFixedLevel)
PressureFixedLevel._v_pressure_active_levels = new_instancemethod(_pressure_fixed_level.PressureFixedLevel__v_pressure_active_levels, None, PressureFixedLevel)
PressureFixedLevel_swigregister = _pressure_fixed_level.PressureFixedLevel_swigregister
PressureFixedLevel_swigregister(PressureFixedLevel)



