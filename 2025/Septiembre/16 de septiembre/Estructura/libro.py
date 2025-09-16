class libro():
    
    def __init__(self, autor: str, genero: str, num_paginas: int):
        self.autor = autor
        self.genero = genero
        self.num_paginas = num_paginas
    
    @property
    def autor(self):
        return self.autor
    @property
    def genero(self):
        return self.genero
    @property
    def num_paginas(self):
        return self.num_paginas
    