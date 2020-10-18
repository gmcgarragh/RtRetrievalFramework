# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ils_fts.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ils_fts')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ils_fts')
    _ils_fts = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ils_fts', [dirname(__file__)])
        except ImportError:
            import _ils_fts
            return _ils_fts
        try:
            _mod = imp.load_module('_ils_fts', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ils_fts = swig_import_helper()
    del swig_import_helper
else:
    import _ils_fts
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


SHARED_PTR_DISOWN = _ils_fts.SHARED_PTR_DISOWN

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

import full_physics_swig.ils
import full_physics_swig.state_vector
import full_physics_swig.generic_object
import full_physics_swig.dispersion
import full_physics_swig.level_1b
class IlsFts(full_physics_swig.ils.Ils, full_physics_swig.dispersion.ObserverDispersion):
    """

    This does an ILS convolution for FTS data.

    This wraps some old Fortran code that models and sinc + box-car. We
    may replace this at some point.

    C++ includes: ils_fts.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, Disp, Dispersion_perturb, Level_1b, Spec_index, Band_name, Hdf_band_name):
        """

        IlsFts::IlsFts(const boost::shared_ptr< DispersionPolynomial > &Disp, const
        blitz::Array< double, 2 > &Dispersion_perturb, const
        boost::shared_ptr< Level1bFts > &Level_1b, int Spec_index, const
        std::string &Band_name, const std::string &Hdf_band_name, const
        DoubleWithUnit &Ils_half_width=DoubleWithUnit((2000+1)*1e-2,
        units::inv_cm))
        Constructor. 
        """
        _ils_fts.IlsFts_swiginit(self, _ils_fts.new_IlsFts(Disp, Dispersion_perturb, Level_1b, Spec_index, Band_name, Hdf_band_name))

    def notify_update(self, *args):
        """

        virtual void FullPhysics::IlsFts::notify_update(const Dispersion &D)

        """
        return _ils_fts.IlsFts_notify_update(self, *args)


    def apply_ils(self, *args):
        """

        ArrayAd< double, 1 > IlsFts::apply_ils(const blitz::Array< double, 1 > &High_resolution_wave_number, const
        ArrayAd< double, 1 > &High_resolution_radiance, const std::vector< int
        > &Pixel_list) const

        """
        return _ils_fts.IlsFts_apply_ils(self, *args)

    __swig_destroy__ = _ils_fts.delete_IlsFts
IlsFts.notify_update = new_instancemethod(_ils_fts.IlsFts_notify_update, None, IlsFts)
IlsFts.apply_ils = new_instancemethod(_ils_fts.IlsFts_apply_ils, None, IlsFts)
IlsFts_swigregister = _ils_fts.IlsFts_swigregister
IlsFts_swigregister(IlsFts)



