class Giant:

    def __init__(self):
        self._name = "Tran Quang Huy"
        self._id = 'abc123'
        self._height = 123

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) > 32:
            return
        self._name = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        if len(value) > 16:
            return
        self._id = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        if value > 128:
            return
        self._height = value
