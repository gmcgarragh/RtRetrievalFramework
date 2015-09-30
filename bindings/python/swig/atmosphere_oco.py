# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _atmosphere_oco.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_atmosphere_oco', [dirname(__file__)])
        except ImportError:
            import _atmosphere_oco
            return _atmosphere_oco
        if fp is not None:
            try:
                _mod = imp.load_module('_atmosphere_oco', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _atmosphere_oco = swig_import_helper()
    del swig_import_helper
else:
    import _atmosphere_oco
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


SHARED_PTR_DISOWN = _atmosphere_oco.SHARED_PTR_DISOWN
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

import full_physics_swig.rt_atmosphere
import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
import full_physics_swig.aerosol
import full_physics_swig.aerosol_extinction
import full_physics_swig.aerosol_property
class ObserverAtmosphereOco(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        _atmosphere_oco.ObserverAtmosphereOco_swiginit(self,_atmosphere_oco.new_ObserverAtmosphereOco())
    __swig_destroy__ = _atmosphere_oco.delete_ObserverAtmosphereOco
ObserverAtmosphereOco.notify_update = new_instancemethod(_atmosphere_oco.ObserverAtmosphereOco_notify_update,None,ObserverAtmosphereOco)
ObserverAtmosphereOco.notify_add = new_instancemethod(_atmosphere_oco.ObserverAtmosphereOco_notify_add,None,ObserverAtmosphereOco)
ObserverAtmosphereOco.notify_remove = new_instancemethod(_atmosphere_oco.ObserverAtmosphereOco_notify_remove,None,ObserverAtmosphereOco)
ObserverAtmosphereOco_swigregister = _atmosphere_oco.ObserverAtmosphereOco_swigregister
ObserverAtmosphereOco_swigregister(ObserverAtmosphereOco)

class AtmosphereOco(full_physics_swig.rt_atmosphere.RtAtmosphere,full_physics_swig.aerosol.ObserverAerosol):
    """
    This class maintains the atmosphere portion of the state, and uses
    this to set up the atmosphere and ground information needed to run the
    Radiative transfer code.

    This particular implementation forwards most of the work to other
    classes such as Absorber and Aerosol. This class then coordinates
    these other classes, and provides the calculations needed to set up
    the RT code.

    For some set ups, aerosol_ptr and/or ground_ptr may be null. For a
    Rayleigh only atmosphere, we don't have any aerosol to include. For up
    looking (e.g., TCCON FTS), there is no ground portion included in the
    radiative transfer.

    C++ includes: atmosphere_oco.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        AtmosphereOco::AtmosphereOco(const boost::shared_ptr< Absorber > &absorberv, const
        boost::shared_ptr< Pressure > &pressurev, const boost::shared_ptr<
        Temperature > &temperaturev, const std::vector< boost::shared_ptr<
        Altitude > > &altv, const boost::shared_ptr< Constant > &C)

        """
        _atmosphere_oco.AtmosphereOco_swiginit(self,_atmosphere_oco.new_AtmosphereOco(*args))
    def optical_depth_wrt_iv(self, *args):
        """
        virtual ArrayAd<double, 1> FullPhysics::AtmosphereOco::optical_depth_wrt_iv(double wn, int spec_index, const ArrayAd< double, 2 > &iv) const

        """
        return _atmosphere_oco.AtmosphereOco_optical_depth_wrt_iv(self, *args)

    def single_scattering_albedo_wrt_iv(self, *args):
        """
        virtual ArrayAd<double, 1> FullPhysics::AtmosphereOco::single_scattering_albedo_wrt_iv(double wn, int spec_index, const ArrayAd< double, 2 > &iv) const

        """
        return _atmosphere_oco.AtmosphereOco_single_scattering_albedo_wrt_iv(self, *args)

    def scattering_moment_wrt_iv(self, *args):
        """
        virtual ArrayAd<double, 3> FullPhysics::AtmosphereOco::scattering_moment_wrt_iv(double wn, int spec_index, const ArrayAd< double, 2 > &iv, int
        nummom=-1, int numscat=-1) const

        """
        return _atmosphere_oco.AtmosphereOco_scattering_moment_wrt_iv(self, *args)

    def notify_update(self, *args):
        """
        virtual void FullPhysics::AtmosphereOco::notify_update(const Pressure &P)

        """
        return _atmosphere_oco.AtmosphereOco_notify_update(self, *args)

    def _v_timer_info(self):
        """
        std::string AtmosphereOco::timer_info() const

        """
        return _atmosphere_oco.AtmosphereOco__v_timer_info(self)

    def _v_pressure(self):
        """
        const boost::shared_ptr<Pressure>& FullPhysics::AtmosphereOco::pressure_ptr() const

        """
        return _atmosphere_oco.AtmosphereOco__v_pressure(self)

    @property
    def pressure(self):
        return self._v_pressure()

    def _v_absorber(self):
        """
        const boost::shared_ptr<Absorber>& FullPhysics::AtmosphereOco::absorber_ptr() const

        """
        return _atmosphere_oco.AtmosphereOco__v_absorber(self)

    @property
    def absorber(self):
        return self._v_absorber()

    def _v_aerosol(self):
        """
        const boost::shared_ptr<Aerosol>& FullPhysics::AtmosphereOco::aerosol_ptr() const

        """
        return _atmosphere_oco.AtmosphereOco__v_aerosol(self)

    @property
    def aerosol(self):
        return self._v_aerosol()

    def _v_temperature(self):
        """
        const boost::shared_ptr<Temperature>& FullPhysics::AtmosphereOco::temperature_ptr() const

        """
        return _atmosphere_oco.AtmosphereOco__v_temperature(self)

    @property
    def temperature(self):
        return self._v_temperature()

    def _v_constant(self):
        """
        const boost::shared_ptr<Constant>& FullPhysics::AtmosphereOco::constant_ptr() const

        """
        return _atmosphere_oco.AtmosphereOco__v_constant(self)

    @property
    def constant(self):
        return self._v_constant()

    def _v_rayleigh(self):
        """
        const boost::shared_ptr<Rayleigh>& FullPhysics::AtmosphereOco::rayleigh_ptr() const

        """
        return _atmosphere_oco.AtmosphereOco__v_rayleigh(self)

    @property
    def rayleigh(self):
        return self._v_rayleigh()

    def _v_altitude_obj(self):
        """
        const boost::shared_ptr<Altitude>& FullPhysics::AtmosphereOco::altitude_ptr(int Spec_index) const

        """
        return _atmosphere_oco.AtmosphereOco__v_altitude_obj(self)

    @property
    def altitude_obj(self):
        return self._v_altitude_obj()

    def clone(self):
        """
        boost::shared_ptr< AtmosphereOco > AtmosphereOco::clone() const
        This clones a Atmosphere object.

        This is a deep copy, all of the objects that are part of this are
        cloned also (e.g., Pressure, Temperature).

        This cloned copy will not be attached to any StateVector, nor will any
        Observer<Atmosphere> objects be attached (although the original object
        is unchanged). You can attach the clone to any objects you wish to.

        This property is particularly useful to "freeze" the state. For
        example, if the StateVector was set the apriori state and the
        Atmosphere attached to the StateVector is cloned, then the cloned
        version will continue to be the "Apriori atmosphere", even if the
        StateVector is subsequently changed thus updating the original object.

        """
        return _atmosphere_oco.AtmosphereOco_clone(self)

    def _v_rayleigh_only_atmosphere(self):
        """
        bool FullPhysics::AtmosphereOco::rayleigh_only_atmosphere() const
        Indicate we have rayleigh only atmosphere, i.e., we don't have any
        aerosol content. 
        """
        return _atmosphere_oco.AtmosphereOco__v_rayleigh_only_atmosphere(self)

    @property
    def rayleigh_only_atmosphere(self):
        return self._v_rayleigh_only_atmosphere()

    def set_surface_pressure_for_testing(self, *args):
        """
        void AtmosphereOco::set_surface_pressure_for_testing(double x)
        For unit test purposes, it is useful to be able to directly change the
        surface pressure.

        This is intended just for testing purposes. This only works if the
        Pressure is a PressureFixedLevel, otherwise it will fail. 
        """
        return _atmosphere_oco.AtmosphereOco_set_surface_pressure_for_testing(self, *args)

    __swig_destroy__ = _atmosphere_oco.delete_AtmosphereOco
AtmosphereOco.optical_depth_wrt_iv = new_instancemethod(_atmosphere_oco.AtmosphereOco_optical_depth_wrt_iv,None,AtmosphereOco)
AtmosphereOco.single_scattering_albedo_wrt_iv = new_instancemethod(_atmosphere_oco.AtmosphereOco_single_scattering_albedo_wrt_iv,None,AtmosphereOco)
AtmosphereOco.scattering_moment_wrt_iv = new_instancemethod(_atmosphere_oco.AtmosphereOco_scattering_moment_wrt_iv,None,AtmosphereOco)
AtmosphereOco.notify_update = new_instancemethod(_atmosphere_oco.AtmosphereOco_notify_update,None,AtmosphereOco)
AtmosphereOco._v_timer_info = new_instancemethod(_atmosphere_oco.AtmosphereOco__v_timer_info,None,AtmosphereOco)
AtmosphereOco._v_pressure = new_instancemethod(_atmosphere_oco.AtmosphereOco__v_pressure,None,AtmosphereOco)
AtmosphereOco._v_absorber = new_instancemethod(_atmosphere_oco.AtmosphereOco__v_absorber,None,AtmosphereOco)
AtmosphereOco._v_aerosol = new_instancemethod(_atmosphere_oco.AtmosphereOco__v_aerosol,None,AtmosphereOco)
AtmosphereOco._v_temperature = new_instancemethod(_atmosphere_oco.AtmosphereOco__v_temperature,None,AtmosphereOco)
AtmosphereOco._v_constant = new_instancemethod(_atmosphere_oco.AtmosphereOco__v_constant,None,AtmosphereOco)
AtmosphereOco._v_rayleigh = new_instancemethod(_atmosphere_oco.AtmosphereOco__v_rayleigh,None,AtmosphereOco)
AtmosphereOco._v_altitude_obj = new_instancemethod(_atmosphere_oco.AtmosphereOco__v_altitude_obj,None,AtmosphereOco)
AtmosphereOco.clone = new_instancemethod(_atmosphere_oco.AtmosphereOco_clone,None,AtmosphereOco)
AtmosphereOco._v_rayleigh_only_atmosphere = new_instancemethod(_atmosphere_oco.AtmosphereOco__v_rayleigh_only_atmosphere,None,AtmosphereOco)
AtmosphereOco.set_surface_pressure_for_testing = new_instancemethod(_atmosphere_oco.AtmosphereOco_set_surface_pressure_for_testing,None,AtmosphereOco)
AtmosphereOco_swigregister = _atmosphere_oco.AtmosphereOco_swigregister
AtmosphereOco_swigregister(AtmosphereOco)



