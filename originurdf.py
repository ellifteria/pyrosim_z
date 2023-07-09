from pyrosim_z.commonFunctions import Save_Whitespace

class ORIGIN_URDF: 

    def __init__(self, pos_xyz, pos_rpy = [0, 0, 0]):

        self.depth  = 3

        self.string = '<origin xyz="{} {} {}" rpy="{} {} {}"/>'.format(*pos_xyz, *pos_rpy)

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string + '\n' )
