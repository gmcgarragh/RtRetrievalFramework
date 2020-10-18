# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _spectral_window.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_spectral_window')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_spectral_window')
    _spectral_window = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_spectral_window', [dirname(__file__)])
        except ImportError:
            import _spectral_window
            return _spectral_window
        try:
            _mod = imp.load_module('_spectral_window', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _spectral_window = swig_import_helper()
    del swig_import_helper
else:
    import _spectral_window
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


SHARED_PTR_DISOWN = _spectral_window.SHARED_PTR_DISOWN

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

import full_physics_swig.generic_object
class SpectralWindow(full_physics_swig.generic_object.GenericObject):
    """

    This class represents a the spectral window.

    The definition of a spectral window is purposely fuzzy, we want to
    support things like excluding certain wavenumbers. So the interface
    simple takes a list of potential wavenumbers (e.g., the wavenumbers
    measured to the GOSAT oxygen A spectrometer) and returns the list of
    values that fall within the window. For example, if the window is just
    a wavenumber range, then all the wavenumbers that fall within that
    range are returned.

    Note that there are a few closely related classes, with similar
    sounding names. See spectrum_doxygen for a description of each of
    these.

    C++ includes: spectral_window.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _spectral_window.delete_SpectralWindow

    def apply(self, Grid, Spec_index):
        """

        Spectrum SpectralWindow::apply(const Spectrum &Spec, int Spec_index) const
        Apply a spectral window to a Spectrum, returning the possibly empty
        part of the spectrum that passes through the window. 
        """
        return _spectral_window.SpectralWindow_apply(self, Grid, Spec_index)


    def grid_indexes(self, Grid, Spec_index):
        """

        virtual std::vector<int> FullPhysics::SpectralWindow::grid_indexes(const SpectralDomain &Grid, int Spec_index) const =0
        Given a list of wavenumbers, this returns the indices that fall within
        the window. 
        """
        return _spectral_window.SpectralWindow_grid_indexes(self, Grid, Spec_index)


    def _v_number_spectrometer(self):
        """

        virtual int FullPhysics::SpectralWindow::number_spectrometer() const =0
        Number of spectrometers. 
        """
        return _spectral_window.SpectralWindow__v_number_spectrometer(self)


    @property
    def number_spectrometer(self):
        return self._v_number_spectrometer()


    def _v_spectral_bound(self):
        """

        virtual SpectralBound FullPhysics::SpectralWindow::spectral_bound() const =0
        Bounds of spectral window. 
        """
        return _spectral_window.SpectralWindow__v_spectral_bound(self)


    @property
    def spectral_bound(self):
        return self._v_spectral_bound()

SpectralWindow.__str__ = new_instancemethod(_spectral_window.SpectralWindow___str__, None, SpectralWindow)
SpectralWindow.apply = new_instancemethod(_spectral_window.SpectralWindow_apply, None, SpectralWindow)
SpectralWindow.grid_indexes = new_instancemethod(_spectral_window.SpectralWindow_grid_indexes, None, SpectralWindow)
SpectralWindow._v_number_spectrometer = new_instancemethod(_spectral_window.SpectralWindow__v_number_spectrometer, None, SpectralWindow)
SpectralWindow._v_spectral_bound = new_instancemethod(_spectral_window.SpectralWindow__v_spectral_bound, None, SpectralWindow)
SpectralWindow_swigregister = _spectral_window.SpectralWindow_swigregister
SpectralWindow_swigregister(SpectralWindow)



