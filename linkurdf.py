from pyrosim_z.originurdf      import ORIGIN_URDF

from pyrosim_z.geometryurdf    import GEOMETRY_URDF

from pyrosim_z.inertialurdf    import INERTIAL_URDF

from pyrosim_z.visualurdf      import VISUAL_URDF

from pyrosim_z.collisionurdf   import COLLISION_URDF

from pyrosim_z.commonFunctions import Save_Whitespace

class LINK_URDF:

    def __init__(self,name, pos_xyz, shape, size_string, color_name, color, pos_rpy = [0, 0, 0]):

        self.name = name

        self.depth = 1

        self.origin   = ORIGIN_URDF(pos_xyz, pos_rpy)

        self.inertial  = INERTIAL_URDF(self.origin)

        self.geometry = GEOMETRY_URDF(shape, size_string)

        self.visual    = VISUAL_URDF(self.origin , self.geometry, color_name, color)

        self.collision = COLLISION_URDF(self.origin , self.geometry)

    def Save(self,f):

        self.Save_Start_Tag(f)

        self.inertial.Save(f)

        self.visual.Save(f)

        self.collision.Save(f)

        self.Save_End_Tag(f)

# ------------------- Private methods -----------------

    def Save_End_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('</link>\n')

    def Save_Start_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('<link name="' + self.name + '">\n')
