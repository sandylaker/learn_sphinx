class Foo:
    """Foo is a dummy class to demonstrate how to use ``autodoc`` in ``sphinx``.

    .. note::

        The age should be an positive integer.

    Args:
        name (str): personal name.
        age (int): personal age.

    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        """Get the personal name.

        Returns:
            str: the name.
        """
        return self.name

    def get_age(self):
        """Get the personal age.
        
        Returns:
            int: the age.
        """
        return self.age

    def get_name_and_age(self):
        """Get both the name and age.

        Returns:
            tuple[str, int]: 

                - name: personal name.
                - age: personal age.
        """
        return self.name, self.age
