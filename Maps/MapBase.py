class MapBase(MutableMapping)
    """Abstract Base class that includes nonpublic _Item class"""
    
    class _Item:
        """Stores Key-value pairs as map items"""
        __slots__ = '_key', '_value'
        
        def __init__(self, k, v):
            self._key = k
            self._value = v
            
        def __equals__(self, other):
            return self._key == other._key  #compes items based on their keys
        
        def__notEquals__(self, other):
            return not (self == other)      #opposite of __eq__
        
        def __compareItems__(self, other):
            return self.key <other._key     #compare items based on their keys
            
