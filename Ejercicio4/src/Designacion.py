

class Designacion:
    __designacion_anio = ''
    __justicia_federal_o_nacional = ''
    __cargo_tipo = ''
    __instancia_tipo = ''
    __materia = ''
    __cantidad_varones = ''
    __cantidad_mujeres = ''

    def __str__(self) -> str:
        out = ''
        out += self.__designacion_anio + '\t'
        out += self.__justicia_federal_o_nacional + '\t'
        out += self.__cargo_tipo  + '\t'
        out += self.__instancia_tipo  + '\t'
        out += self.__materia  + '\t'
        out += self.__cantidad_varones + '\t'
        out += self.__cantidad_mujeres + '\n'
        return out

    def __init__(self, designacion_anio ,justicia_federal_o_nacional ,cargo_tipo ,instancia_tipo ,materia ,cantidad_varones , cantidad_mujeres):
        self.__designacion_anio = designacion_anio
        self.__justicia_federal_o_nacional = justicia_federal_o_nacional
        self.__cargo_tipo = cargo_tipo
        self.__instancia_tipo = instancia_tipo
        self.__materia = materia
        self.__cantidad_varones = cantidad_varones
        self.__cantidad_mujeres = cantidad_mujeres

    def getCantMujeres(self):
        return self.__cantidad_mujeres

    def getAnio(self):
        return self.__designacion_anio

    def getCantHombres(self):
        return self.__cantidad_varones

    def getMateria(self):
        return self.__materia

    def getCargo(self):
        return self.__cargo_tipo
    

    
    
