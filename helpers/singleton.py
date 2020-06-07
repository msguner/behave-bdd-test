class Singleton(type):
    current_instance = None

    def __call__(cls, *args, **kwargs):
        if cls.current_instance is None:
            cls.current_instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.current_instance
