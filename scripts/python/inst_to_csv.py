# author  = Emmanuel Mouillet
# email   = emmanuel@fantome.in
# version = 1.0.0

#----------------------------------------------------------------------------
# Export houdini instance point info to a .csv table
#----------------------------------------------------------------------------

import hou

def exportInstToCsv(current):
    path_geo = current.parm('points_inst').eval()
    path_csv = current.parm('csv_export').eval()

    geo    = hou.node(path_geo).geometry()
    points = geo.points()

    title  = ',px,py,pz'
    field  = ''

    for point in points:
        ptnum = point.number()
        field += str(ptnum)
        
        p     = point.attribValue('P')
        sp    = ','+str(p[0])+','+str(p[2])+','+str(p[1])
        field += sp     
        
        if geo.findPointAttrib('rotE') != None:
            if ptnum == 0:
                title += ',rx,ry,rz'
            r     = point.attribValue('rotE')
            sr    = ','+str(r[0])+','+str(r[2])+','+str(r[1])
            field += sr
     
        if geo.findPointAttrib('scale') != None:
            if ptnum == 0:
                title += ',sx,sy,sz'
            s     = point.attribValue('scale')
            ss    = ','+str(s[0])+','+str(s[2])+','+str(s[1])
            field += ss
            
        field += '\n'

    liste = title+'\n'+field 
    file  = open(path_csv, 'w')
    file.write(liste)
    file.close()
