from pyrosim_z.commonFunctions import Save_Whitespace

class GEOMETRY_URDF: 

    def __init__(self, shape, size_string):

        self.depth   = 3

        self.string1 = '<geometry>'

        self.string2 = '    <{} size="{}" />'.format(shape, size_string)

        self.string3 = '</geometry>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
