import pybullet as pblt

from pyrosim_z.nndf import NNDF

from pyrosim_z.linksdf  import LINK_SDF

from pyrosim_z.linkurdf import LINK_URDF

from pyrosim_z.model import MODEL

from pyrosim_z.sdf   import SDF

from pyrosim_z.urdf  import URDF

from pyrosim_z.joint import JOINT

SDF_FILETYPE  = 0

URDF_FILETYPE = 1

NNDF_FILETYPE   = 2

# global availableLinkIndex

# global linkNamesToIndices

def end():

    if filetype == SDF_FILETYPE:

        sdf.Save_End_Tag(f)

    elif filetype == NNDF_FILETYPE:

        nndf.Save_End_Tag(f)
    else:
        urdf.Save_End_Tag(f)

    f.close()

def End_Model():

    model.Save_End_Tag(f)

def Get_Touch_Sensor_Value_For_Link(linkName):

    touchValue = -1.0

    desiredLinkIndex = linkNamesToIndices[linkName]

    pts = None
    while pts is None:
        pts = pblt.getContactPoints()

    for pt in pts:

        linkIndex = pt[4]

        if ( linkIndex == desiredLinkIndex ):

            touchValue = 1.0

    return touchValue

def Prepare_Link_Dictionary(bodyID):

    global linkNamesToIndices

    linkNamesToIndices = {}

    for jointIndex in range( 0 , pblt.getNumJoints(bodyID) ):

        jointInfo = pblt.getJointInfo( bodyID , jointIndex )

        jointName = jointInfo[1]

        jointName = jointName.decode("utf-8")

        jointName = jointName.split("_")

        linkName = jointName[1]

        linkNamesToIndices[linkName] = jointIndex

        if jointIndex==0:

           rootLinkName = jointName[0]

           linkNamesToIndices[rootLinkName] = -1

def get_link_names_to_indices():
    global linkNamesToIndices
    return linkNamesToIndices

def Prepare_Joint_Dictionary(bodyID):

    global jointNamesToIndices

    jointNamesToIndices = {}

    for jointIndex in range( 0 , pblt.getNumJoints(bodyID) ):

        jointInfo = pblt.getJointInfo( bodyID , jointIndex )

        jointName = jointInfo[1].decode('UTF-8')

        jointNamesToIndices[jointName] = jointIndex

def get_joint_names_to_indices():
    global jointNamesToIndices
    return jointNamesToIndices

def Prepare_To_Simulate(bodyID):

    Prepare_Link_Dictionary(bodyID)

    Prepare_Joint_Dictionary(bodyID)

# [x] change to new function parameters
def send_link(name="default",pos_xyz=[0,0,0], pos_rpy = [0, 0, 0], shape = "box", size_string="1.0 1.0 1.0", color_name = "Cyan", color=[0.0, 1.0, 1.0, 1.0]):

    global availableLinkIndex

    global links

    if filetype == SDF_FILETYPE:
        raise Exception("sdf type type not yet implemented")

        Start_Model(name,pos)

        link = LINK_SDF(name,pos,size)

        links.append(link)
    else:
        link = LINK_URDF(name, pos_xyz, shape, size_string, color_name, color, pos_rpy)

        links.append(link)

    link.Save(f)

    if filetype == SDF_FILETYPE:

        End_Model()

    linkNamesToIndices[name] = availableLinkIndex

    availableLinkIndex = availableLinkIndex + 1

def send_joint(name,parent,child,type,position, axis = [0, 1, 0], limit = [0.0, -3.14159, 3.14159, 0.0]):

    joint = JOINT(name,parent,child,type,position, axis, limit)

    joint.Save(f)

def Send_Motor_Neuron(name,jointName):

    f.write('    <neuron name = "' + str(name) + '" type = "motor"  jointName = "' + jointName + '" />\n')

def Send_Sensor_Neuron(name,linkName):

    f.write('    <neuron name = "' + str(name) + '" type = "sensor" linkName = "' + linkName + '" />\n')

def Send_Synapse( sourceNeuronName , targetNeuronName , weight ):

    f.write('    <synapse sourceNeuronName = "' + str(sourceNeuronName) + '" targetNeuronName = "' + str(targetNeuronName) + '" weight = "' + str(weight) + '" />\n')

 
def Set_Motor_For_Joint(bodyIndex,jointName,controlMode,targetPosition,maxForce):

    pblt.setJointMotorControl2(

        bodyIndex      = bodyIndex,

        jointIndex     = jointNamesToIndices[jointName],

        controlMode    = controlMode,

        targetPosition = targetPosition,

        force          = maxForce)

def Start_NeuralNetwork(filename):

    global filetype

    filetype = NNDF_FILETYPE

    global f

    f = open(filename,"w")

    global nndf

    nndf = NNDF()

    nndf.Save_Start_Tag(f)

def Start_SDF(filename):

    global availableLinkIndex

    availableLinkIndex = -1

    global linkNamesToIndices

    linkNamesToIndices = {}

    global filetype

    filetype = SDF_FILETYPE

    global f
 
    f = open(filename,"w")

    global sdf

    sdf = SDF()

    sdf.Save_Start_Tag(f)

    global links

    links = []

def Start_URDF(filename):

    global availableLinkIndex

    availableLinkIndex = -1

    global linkNamesToIndices

    linkNamesToIndices = {}

    global filetype

    filetype = URDF_FILETYPE

    global f

    f = open(filename,"w")

    global urdf 

    urdf = URDF()

    urdf.Save_Start_Tag(f)

    global links

    links = []

def Start_Model(modelName,pos):

    global model 

    model = MODEL(modelName,pos)

    model.Save_Start_Tag(f)
