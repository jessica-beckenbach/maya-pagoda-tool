#0008_script_Beckenbach.py
#
#Jessica Beckenbach
#SCAD VSFX 160 A01 
#May 22, 2018
#
# Creates To-ji Temple
#
# v1.1 
#
#####################################

import maya.cmds as cm


#-----------------functions that don't make geometry
    
def makeFinalCombine_MultipleStorey():
    #unites all geometry into one, for buildings with more than one storey
    if merge==True:
        cm.select( 'floor_g*' , 'roof_gr*' , 'topRoof_group' , r=True )
        cm.polyUnite( n='Temple' )
        cm.delete( ch=True )


def extrudeLowerRoofShape( faceNumber , x , y ):
    cm.polyExtrudeFacet( "balconyBottomFloor.f[" + faceNumber + "]" , ltz=1.31 * x , lty=1.05 * y )
    cm.polyExtrudeFacet( "balconyBottomFloor.f[" + faceNumber + "]" , ltz=0.7 * x , lty=0.35 * y )
    cm.polyExtrudeFacet( "balconyBottomFloor.f[" + faceNumber + "]" , ltz=0.55 * x , lty=0.16 * y )
    cm.polyExtrudeFacet( "balconyBottomFloor.f[" + faceNumber + "]" , ltz=0.6 * x , lty=0.08 * y )
    cm.polyExtrudeFacet( "balconyBottomFloor.f[" + faceNumber + "]" , ltz=1.35 * x )

def mergeCorners( vtxs , x , z ):
    cm.select( "balconyBottomFloor.vtx[" + vtxs["lvl1"]["vtx1"] + "]", "balconyBottomFloor.vtx[" + vtxs["lvl1"]["vtx2"] + "]", r=True )
    cm.move( 0, 0, 1.31 * z , r=True )
    cm.select( "balconyBottomFloor.vtx[" + vtxs["lvl1"]["vtx3"] + "]", "balconyBottomFloor.vtx[" + vtxs["lvl1"]["vtx4"] + "]", r=True )
    cm.move( 1.31 * x , 0, 0, r=True )
    cm.polyMergeVertex( "balconyBottomFloor.vtx[" + vtxs["lvl1"]["vtx2"] + "]", "balconyBottomFloor.vtx[" + vtxs["lvl1"]["vtx6"] + "]", d=0.2 )
    cm.polyMergeVertex( "balconyBottomFloor.vtx[" + vtxs["lvl1"]["vtx1"] + "]", "balconyBottomFloor.vtx[" + vtxs["lvl1"]["vtx5"] + "]", d=0.2 )
    
    cm.select( 'balconyBottomFloor.vtx[' + vtxs['lvl2']['vtx1'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl2']['vtx2'] + ']', r=True )
    cm.move( 0, 0, 2.013 * z , r=True )
    cm.select( 'balconyBottomFloor.vtx[' + vtxs['lvl2']['vtx3'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl2']['vtx4'] + ']', r=True )
    cm.move( 2.013 * x , 0, 0, r=True )
    cm.polyMergeVertex( 'balconyBottomFloor.vtx[' + vtxs['lvl2']['vtx2'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl2']['vtx6'] + ']', d=0.2 )
    cm.polyMergeVertex( 'balconyBottomFloor.vtx[' + vtxs['lvl2']['vtx1'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl2']['vtx5'] + ']', d=0.2 )
    
    cm.select( 'balconyBottomFloor.vtx[' + vtxs['lvl3']['vtx1'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl3']['vtx2'] + ']', r=True )
    cm.move( 0, 0, 2.575 * z , r=True )
    cm.select( 'balconyBottomFloor.vtx[' + vtxs['lvl3']['vtx3'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl3']['vtx4'] + ']', r=True )
    cm.move( 2.575 * x , 0, 0, r=True )
    cm.polyMergeVertex( 'balconyBottomFloor.vtx[' + vtxs['lvl3']['vtx5'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl3']['vtx6'] + ']', d=0.2 )
    cm.polyMergeVertex( 'balconyBottomFloor.vtx[' + vtxs['lvl3']['vtx7'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl3']['vtx8'] + ']', d=0.2 )
    
    cm.select( 'balconyBottomFloor.vtx[' + vtxs['lvl4']['vtx1'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl4']['vtx2'] + ']', r=True )
    cm.move( 0, 0, 3.23 * z , r=True )
    cm.select( 'balconyBottomFloor.vtx[' + vtxs['lvl4']['vtx3'] + ']',  'balconyBottomFloor.vtx[' + vtxs['lvl4']['vtx4'] + ']', r=True )
    cm.move( 3.23 * x , 0, 0, r=True )
    cm.polyMergeVertex( 'balconyBottomFloor.vtx[' + vtxs['lvl4']['vtx5'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl4']['vtx6'] + ']', d=0.2 )
    cm.polyMergeVertex( 'balconyBottomFloor.vtx[' + vtxs['lvl4']['vtx7'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl4']['vtx8'] + ']', d=0.2 )

    cm.select( 'balconyBottomFloor.vtx[' + vtxs['lvl5']['vtx1'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl5']['vtx2'] + ']', r=True )
    cm.move( 0, 0, 4.5 * z , r=True )
    cm.select( 'balconyBottomFloor.vtx[' + vtxs['lvl5']['vtx3'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl5']['vtx4'] + ']', r=True )
    cm.move( 4.5 * x , 0, 0, r=True )
    cm.polyMergeVertex( 'balconyBottomFloor.vtx[' + vtxs['lvl5']['vtx2'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl5']['vtx6'] + ']', d=0.2 )
    cm.polyMergeVertex( 'balconyBottomFloor.vtx[' + vtxs['lvl5']['vtx1'] + ']', 'balconyBottomFloor.vtx[' + vtxs['lvl5']['vtx5'] + ']', d=0.2 )


def extrudeUpperRoofShape( faceNumber , x , y ):
    cm.polyExtrudeFacet( "tr_roof.f[" + faceNumber + "]" , 
    ltz=float(width)/1.15 *x , lty=float(width)/1.1 *y )
    cm.polyExtrudeFacet( "tr_roof.f[" + faceNumber + "]" , 
    ltz=float(width)/1.5 *x, lty=float(width)/1.76 *y )
    cm.polyExtrudeFacet( "tr_roof.f[" + faceNumber + "]" , 
    ltz=float(width)/1.578 *x, lty=float(width)/2.5 *y )
    cm.polyExtrudeFacet( "tr_roof.f[" + faceNumber + "]" , 
    ltz=float(width)/1.66 *x, lty=float(width)/6 *y )
    cm.polyExtrudeFacet( "tr_roof.f[" + faceNumber + "]" , 
    ltz=float(width)/1.76 *x, lty=float(width)/10 *y )


def mergeTopCorners( vtxs , x , z ):
    cm.select( "tr_roof.vtx[" + vtxs['lvl1']['vtx1'] + "]", "tr_roof.vtx[" + vtxs['lvl1']['vtx2'] + "]", r=True )
    cm.move( 0, 0, float(width)/1.161 * z , r=True )
    cm.select( "tr_roof.vtx[" + vtxs['lvl1']['vtx3'] + "]", "tr_roof.vtx[" + vtxs['lvl1']['vtx4'] + "]", r=True )
    cm.move( float(width)/1.161 * x , 0, 0, r=True )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl1']['vtx2'] + "]", "tr_roof.vtx[" + vtxs['lvl1']['vtx6'] + "]", d=float(width)/10 )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl1']['vtx1'] + "]", "tr_roof.vtx[" + vtxs['lvl1']['vtx5'] + "]", d=float(width)/10 )
    
    cm.select( "tr_roof.vtx[" + vtxs['lvl2']['vtx1'] + "]", "tr_roof.vtx[" + vtxs['lvl2']['vtx2'] + "]", r=True )
    cm.move( 0, 0, float(width)/0.663 * z , r=True )
    cm.select( "tr_roof.vtx[" + vtxs['lvl2']['vtx3'] + "]", "tr_roof.vtx[" + vtxs['lvl2']['vtx4'] + "]", r=True )
    cm.move( float(width)/0.663 * x , 0, 0, r=True )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl2']['vtx2'] + "]", "tr_roof.vtx[" + vtxs['lvl2']['vtx6'] + "]", d=float(width)/10 )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl2']['vtx1'] + "]", "tr_roof.vtx[" + vtxs['lvl2']['vtx5'] + "]", d=float(width)/10 )
    
    cm.select( "tr_roof.vtx[" + vtxs['lvl3']['vtx1'] + "]", "tr_roof.vtx[" + vtxs['lvl3']['vtx2'] + "]", r=True )
    cm.move( 0, 0, float(width)/0.46 * z , r=True )
    cm.select( "tr_roof.vtx[" + vtxs['lvl3']['vtx3'] + "]", "tr_roof.vtx[" + vtxs['lvl3']['vtx4'] + "]", r=True )
    cm.move( float(width)/0.46 * x , 0, 0, r=True )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl3']['vtx4'] + "]", "tr_roof.vtx[" + vtxs['lvl3']['vtx6'] + "]", d=float(width)/10 )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl3']['vtx3'] + "]", "tr_roof.vtx[" + vtxs['lvl3']['vtx5'] + "]", d=float(width)/10 )
    
    cm.select( "tr_roof.vtx[" + vtxs['lvl4']['vtx1'] + "]", "tr_roof.vtx[" + vtxs['lvl4']['vtx2'] + "]", r=True )
    cm.move( 0, 0, float(width)/0.358 * z , r=True )
    cm.select( "tr_roof.vtx[" + vtxs['lvl4']['vtx3'] + "]", "tr_roof.vtx[" + vtxs['lvl4']['vtx4'] + "]", r=True )
    cm.move( float(width)/0.358 * x , 0, 0, r=True )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl4']['vtx4'] + "]", "tr_roof.vtx[" + vtxs['lvl4']['vtx6'] + "]", d=float(width)/10 )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl4']['vtx3'] + "]", "tr_roof.vtx[" + vtxs['lvl4']['vtx5'] + "]", d=float(width)/10 )

    cm.select( "tr_roof.vtx[" + vtxs['lvl5']['vtx1'] + "]", "tr_roof.vtx[" + vtxs['lvl5']['vtx2'] + "]", r=True )
    cm.move( 0, 0, float(width)/0.3 * z , r=True )
    cm.select( "tr_roof.vtx[" + vtxs['lvl5']['vtx3'] + "]", "tr_roof.vtx[" + vtxs['lvl5']['vtx4'] + "]", r=True )
    cm.move( float(width)/0.3 * x , 0, 0, r=True )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl5']['vtx2'] + "]", "tr_roof.vtx[" + vtxs['lvl5']['vtx6'] + "]", d=float(width)/10 )
    cm.polyMergeVertex( "tr_roof.vtx[" + vtxs['lvl5']['vtx1'] + "]", "tr_roof.vtx[" + vtxs['lvl5']['vtx5'] + "]", d=float(width)/10 )



def addCurvePieceEdgeLoops( weight , edges ):
    edgeLength = len(edges)
    cm.select ( "pillar_curvePiece.e[" + edges[0] + "]" , r=True )
    for i in range(1,edgeLength):
        cm.select( "pillar_curvePiece.e[" + edges[i] + "]" , tgl=True )
    cm.polySplitRing( wt= weight , sma=30, fq=True )
    

#-----------------functions that make the geometry



#makes base (long part) of pillar
def makePillarLongPart():
    #makes long part of pillar
    cm.polyCube( d=0.2, w=0.2, h=5, n="pillar_longPart" )
    cm.move( 0, 2.5, 0)
    
    #makes little cube on top of pillar
    cm.polyCube( d=0.3, w=0.3, h=0.2, n="pillar_longPartTop" )
    cm.move( 0, 5, 0 )


#makes the little straight piece
def makePillarStraightPiece():
    #create the thing
    cm.polyCube( d=0.12, w=0.12, h=0.3, n="pillar_straightPiece" ) 
    
    #extrude
    cm.polyExtrudeFacet( 'pillar_straightPiece.f[1]', ltz=0.1)
    cm.scale( 1.5, 1, 1.5 )
    cm.polyExtrudeFacet( 'pillar_straightPiece.f[1]', ltz=0.12)
    cm.select( "pillar_straightPiece", r=True )
    cm.move(0, 5.2, 0)
    
    
#makes the little curved piece
def makePillarCurvePiece():
    #makes curved piece
    cm.polyCube( d=0.5 , w=0.17 , h=0.17 , n="pillar_curvePiece" )
    cm.move ( 0, 5.06, 0.25 )
    cm.select ( "pillar_curvePiece.e[0]" , r=True )
    cm.move ( 0 , 0 , 0.05 , r=True )
    cm.select ( "pillar_curvePiece.f[0]" , r=True )
    cm.polyExtrudeFacet( 'pillar_curvePiece.f[0]', ltz=0.1)
    cm.rotate ( -25, 0, 0, r=True )
    cm.move (0, -0.11, 0.04, r=True)
    cm.polyExtrudeFacet( 'pillar_curvePiece.f[0]', ltz=0.1)
    cm.rotate ( -30, 0, 0, r=True)
    cm.move ( 0, -0.16, 0.1, r=True )
    cm.polyExtrudeFacet( 'pillar_curvePiece.f[0]', ltz=0.1)
    cm.rotate ( -20, 0, 0, r=True)
    cm.move ( 0, -0.17, 0.09, r=True )
    cm.polyExtrudeFacet( 'pillar_curvePiece.f[0]', ltz=0.07)
    cm.polyExtrudeFacet( 'pillar_curvePiece.f[0]', ltz=0.095)
    cm.scale( 1.5, 1, 1.5 )
    cm.move (0, 0, -0.2, r=True)
    cm.polyExtrudeFacet( 'pillar_curvePiece.f[0]', ltz=0.1)
    
    
    #manipulate shape of object
    cm.select( "pillar_curvePiece.e[30]", r=True )
    cm.move(0, 0, -0.005, r=True )
    cm.select( "pillar_curvePiece.e[22]", r=True )
    cm.move(0, -0.03, -0.02, r=True )
    cm.select( "pillar_curvePiece.e[0]", "pillar_curvePiece.e[3]", r=True )
    cm.move (0, 0.02, 0, r=True)
    cm.select( "pillar_curvePiece.e[14]", r=True )
    cm.move (0, 0.02, -0.004, r=True)
    cm.select( "pillar_curvePiece.e[18]", r=True )
    cm.move(0, 0, 0, r=True )
    cm.select( "pillar_curvePiece.e[26]", r=True )
    cm.move(0, -0.03, 0, r=True )

    #inserts edge loops 
    edges = [ '0', '1', '2', '3', '14', '18', '22', '26', 
    '30', '34', '38', '42', '46', '50', '54', '58' ]
    addCurvePieceEdgeLoops( 0.95 , edges )
    addCurvePieceEdgeLoops( 0.95 , edges )
    addCurvePieceEdgeLoops( 0.1  , edges )
    addCurvePieceEdgeLoops( 0.4  , edges )
       
    
    edges = [ '4', '5', '8', '9', '16', '19', '24', '27', '32', '35', '40', '43', 
    '48', '51', '56', '59', '74', '90', '106', '122', '138', '154', '170', '186' ]
    addCurvePieceEdgeLoops( 0.95 , edges )
    
    edges.extend( [ '189', '191', '193', '195', '197', '199' ] )
    addCurvePieceEdgeLoops( 0.05 , edges )
    
    edges = [ '36', '37', '39', '41', '68', '80', '100', '112', '132', '144', '164', 
    '176', '210', '230', '258', '278' ]
    addCurvePieceEdgeLoops( 0.95 , edges )
    
    edges.remove( '112' )
    edges.remove( '144' )
    edges.remove( '176' )
    edges.remove( '80'  )
    edges.remove( '278' )
    edges.remove( '230' )
    edges.extend( [ '285', '287', '291', '293', '295', '297' ] )
    addCurvePieceEdgeLoops( 0.95 , edges )
    
    edges = [ '44', '45', '47', '49', '70', '78', '102', '110', '134', '142', '166', 
    '174', '212', '228', '260', '276' ]
    addCurvePieceEdgeLoops( 0.95 , edges )

    edges.remove( '174' )
    edges.remove( '142' )
    edges.remove( '110' )
    edges.remove( '276' )
    edges.remove( '78' )
    edges.remove( '228' )
    edges.extend( [ '349', '351', '355', '357', '359', '361' ] )
    addCurvePieceEdgeLoops( 0.95 , edges )
    
    edges.remove( '349' )
    edges.remove( '351' )
    edges.remove( '355' )
    edges.remove( '357' )
    edges.remove( '359' )
    edges.remove( '361' )
    edges.extend( [ '393', '381', '383', '387', '389', '391' ] )
    addCurvePieceEdgeLoops( 0.05 , edges )

    edges = [ '381', '383', '387', '389', '391', '393', '412', '417', '427',
    '429', '431', '433', '435', '437' ]
    addCurvePieceEdgeLoops( 0.05 , edges )

    edges = [ '52', '53', '55', '57', '72', '76', '104', '108', '136',
    '140', '168', '172', '214', '226', '262', '274' ]
    addCurvePieceEdgeLoops( 0.05 , edges )
    
    edges = [ '76', '108', '140', '172', '226', '274', '476', '481', 
    '491', '493', '495', '497', '499', '501', '503', '505']
    addCurvePieceEdgeLoops( 0.05 , edges )
  
    
    #moves pivots
    cm.select( "pillar_curvePiece" , r=True )
    cm.move( 0, 0, -0.05 , "pillar_curvePiece.scalePivot","pillar_curvePiece.rotatePivot", r=True )

    

#assembles a normal pillar
def makeNormalPillar():
    #first level
    makePillarLongPart()
    makePillarStraightPiece()
    makePillarCurvePiece()
    #second level
    cm.select( "pillar_curvePiece" , r=True )
    cm.duplicate()
    cm.move( 0, 0.5, 0.66, r=True)
    cm.duplicate()
    cm.rotate(0, 90, 0, r=True)
    cm.move( 0,0, -0.18, r=True)
    cm.duplicate()
    cm.rotate(0, 180, 0, r=True)
    cm.duplicate('pillar_straightPiece')
    cm.select( "pillar_straightPiece1" , r=True )
    cm.move( 0, 0.5, 0.655, r=True)
    cm.duplicate('pillar_straightPiece')
    cm.select( "pillar_straightPiece2" , r=True )
    cm.move( 0, 0.5, 0, r=True)
    cm.select ( 'pillar_curvePiece1.f[2]' , 'pillar_curvePiece1.f[76]' ,
    'pillar_curvePiece1.f[44]' , 'pillar_curvePiece1.f[60]', 'pillar_curvePiece1.f[92]' ,
    'pillar_curvePiece1.f[95:99]' , 'pillar_curvePiece1.f[119:123]' , r=True)
    cm.move( 0, 0, -0.66, r=True)
    #third level
    cm.select ( 'pillar_curvePiece1', tgl=True )
    cm.select ( 'pillar_curvePiece2', tgl=True )
    cm.select ( 'pillar_curvePiece3', tgl=True )
    cm.duplicate()
    cm.move( 0, 0.5, 0.65, r=True)
    cm.select ( 'pillar_curvePiece4.f[2]' , 'pillar_curvePiece4.f[76]' ,
    'pillar_curvePiece4.f[44]' , 'pillar_curvePiece4.f[60]', 'pillar_curvePiece4.f[92]' ,
    'pillar_curvePiece4.f[95:99]' , 'pillar_curvePiece4.f[119:123]' , r=True) 
    cm.move( 0, 0, -0.66, r=True) 
    cm.duplicate('pillar_straightPiece2')
    cm.select( "pillar_straightPiece3" , r=True )
    cm.move( 0, 0.5, 0, r=True)
    cm.duplicate()
    cm.move( 0,0, 0.65, r=True)
    cm.duplicate()
    cm.move( 0,0, 0.67, r=True)
    
    #smooths it
    cm.polySmooth( 'pillar_curvePiece' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece1' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece2' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece3' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece4' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece5' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece6' , dv=1 )

    #combines it into single mesh
    cm.select ( 'pillar*' , r=True )
    cm.polyUnite( n='normalPillar' )
    cm.delete( ch=True )
    
        
    
#makes the corner pillar
def makeCornerPillar(): 
    #first level
    makePillarLongPart()
    makePillarStraightPiece()
    makePillarCurvePiece() 
    cm.move( 0, 0, -0.2 , "pillar_curvePiece.scalePivot","pillar_curvePiece.rotatePivot", r=True )
    cm.select( "pillar_curvePiece" , r=True )
    cm.duplicate()
    cm.rotate( 0, -90, 0 , r=True )
    cm.duplicate()                                #makes diagonal piece
    cm.rotate( 0, 45, 0 , r=True ) 
    cm.move ( -0.15 , 0 , 0.15, r=True )
    cm.select ( 'pillar_curvePiece2.f[2]' , 'pillar_curvePiece2.f[76]' ,
    'pillar_curvePiece2.f[44]' , 'pillar_curvePiece2.f[60]', 'pillar_curvePiece2.f[92]' ,
    'pillar_curvePiece2.f[95:99]' , 'pillar_curvePiece2.f[119:123]' , r=True)
    cm.move ( 0.15 , 0 , -0.15, r=True )
    
    
    #second level, make medium curve piece
    cm.duplicate( 'pillar_curvePiece' )
    cm.select( "pillar_curvePiece3" , r=True )
    cm.move( 0, 0.5, 0.65, r=True)
    cm.select ( 'pillar_curvePiece3.f[2]' , 'pillar_curvePiece3.f[76]' ,
    'pillar_curvePiece3.f[44]' , 'pillar_curvePiece3.f[60]', 'pillar_curvePiece3.f[92]' ,
    'pillar_curvePiece3.f[95:99]' , 'pillar_curvePiece3.f[119:123]' , r=True)
    cm.move ( 0 , 0 , -0.6, r=True )
    cm.move( 0, 0, -0.65 , "pillar_curvePiece3.scalePivot","pillar_curvePiece3.rotatePivot", r=True )
    
    #second level, make everything else
    cm.duplicate("pillar_curvePiece3")
    cm.select( "pillar_curvePiece4" , r=True )
    cm.rotate( 0, -90, 0, r=True)
    cm.duplicate()                                #makes diagonal piece
    cm.rotate( 0, 45, 0, r=True)
    cm.move ( -0.37, 0, 0.37, r=True )
    cm.select ( 'pillar_curvePiece5.f[2]' , 'pillar_curvePiece5.f[76]' ,
    'pillar_curvePiece5.f[44]' , 'pillar_curvePiece5.f[60]', 'pillar_curvePiece5.f[92]' ,
    'pillar_curvePiece5.f[95:99]' , 'pillar_curvePiece5.f[119:123]' , r=True)
    cm.move ( 0.4 , 0 , -0.4, r=True )
    cm.select( 'pillar_straightPiece' , r=True )
    cm.duplicate()
    cm.move(0, 0.5, 0 , r=True)
    cm.duplicate()
    cm.move(0, 0, 0.66 , r=True)
    cm.duplicate()
    cm.move(-0.66, 0, -0.66 , r=True)
    cm.duplicate()
    cm.move(0.06, 0, 0.61 , r=True)
    cm.rotate(0,45,0, r=True)
        
        
    #third level, make long curve piece, part 1
    cm.duplicate( 'pillar_curvePiece' )
    cm.select( "pillar_curvePiece6" , r=True )
    cm.move( 0, 1, 1.3, r=True)
    cm.select ( 'pillar_curvePiece6.f[2]' , 'pillar_curvePiece6.f[76]' ,
    'pillar_curvePiece6.f[44]' , 'pillar_curvePiece6.f[60]', 'pillar_curvePiece6.f[92]' ,
    'pillar_curvePiece6.f[95:99]' , 'pillar_curvePiece6.f[119:123]' , r=True)
    cm.move ( 0 , 0 , -1.3 , r=True )
    cm.move( 0, 0, -1.3 , "pillar_curvePiece6.scalePivot","pillar_curvePiece6.rotatePivot", r=True )    
    
    #third level, make middle long bit
    cm.select( "pillar_curvePiece6" , r=True )
    cm.duplicate()
    cm.rotate( 0, -45, 0, r=True)
    cm.move( -0.5 , 0 , 0.5 , r=True )
    cm.select ( 'pillar_curvePiece7.f[2]' , 'pillar_curvePiece7.f[76]' ,
    'pillar_curvePiece7.f[44]' , 'pillar_curvePiece7.f[60]', 'pillar_curvePiece7.f[92]' ,
    'pillar_curvePiece7.f[95:99]' , 'pillar_curvePiece7.f[119:123]' , r=True)
    cm.move ( 0.5 , 0 , -0.5 , r=True )
    cm.select('pillar_straightPiece1' , r=True)
    cm.duplicate()
    cm.move( 0 , 0.5 , 0 , r=True )
    cm.select('pillar_straightPiece4' , r=True)
    cm.duplicate()
    cm.move( 0 , 0.5 , 0 , r=True )
    cm.duplicate()
    cm.move( -0.68 , 0 , 0.68 , r=True )
    
    #third level, make long curve piece, part 2
    cm.select('pillar_straightPiece5' , r=True)
    cm.duplicate()
    cm.move( 0 , 0 , 0.66 , r=True )
    cm.duplicate()
    cm.move( 0 , 0 , .66 , r=True )
    cm.select( "pillar_curvePiece1" , r=True )
    cm.duplicate()
    cm.move( 0 , 1 , 1.31 , r=True )   
    cm.polySmooth( 'pillar_curvePiece6' , dv=1 )
    cm.select('pillar_curvePiece6' , 'pillar_straightPiece8' , 'pillar_straightPiece9' , r=True) 
    cm.polyUnite( n='pillar_curvePieceL' )
    cm.delete( ch=True )

    
    #third level, make other side
    cm.duplicate()
    cm.rotate(0,-90,0, r=True)
    cm.select('pillar_curvePiece' , r=True)
    cm.duplicate()
    cm.move( -1.32 , 1 , 0 , r=True )
    
    #smooth curve pieces
    cm.polySmooth( 'pillar_curvePiece' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece1' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece2' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece3' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece4' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece5' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece7' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece8' , dv=1 )
    cm.polySmooth( 'pillar_curvePiece9' , dv=1 )
    
    
    #combine corner pillar
    cm.select( 'pillar_*' , r=True )
    cm.polyUnite( n='cornerPillar' )
    cm.delete( ch=True )
    
    

#makes the part under the roof
def makeFloor(): 
    #make pillars  
    makeCornerPillar()
    for i in range(int(width)):
        makeNormalPillar()
        cm.move ( (3*i)+3 , 0, 0, r=True )    

    #make rafters   
    actualWidth = ( 3 * float(width))
    cm.polyCube( d=0.16, h=0.16, w=( actualWidth + 3) , sx=5, sy=5, sz=5, n='rafter1' )
    cm.move( (actualWidth + 3 ) * 0.5 , 4.06 , 0, r=True )
    cm.duplicate() 
    cm.move( 0, 1, 0, r=True)
    cm.duplicate()
    cm.move( 0, 0.52, 0, r=True)
    cm.duplicate()
    cm.move( 0, 0.495, 0, r=True)
    cm.duplicate()
    cm.move( 0, 0, 0.676, r=True)
    cm.duplicate()
    cm.move( 0, 0.5, -0.676, r=True)
    cm.polyCube( d=0.16, h=0.16, w=( actualWidth + 4.8) , sx=5, sy=5, sz=5, n='rafter7' )
    cm.move( (actualWidth + 2.9 ) * 0.5, 6.564 , 0.68, r=True )
    cm.polyCube( d=0.16, h=0.16, w=( actualWidth + 6.2) , sx=5, sy=5, sz=5, n='rafter8' )
    cm.move( (actualWidth + 3 ) * 0.5, 6.564 , 1.32, r=True )
    cm.polyCube( d=0.16, h=0.16, w=( actualWidth + 8) , sx=5, sy=5, sz=5, n='rafter9' )
    cm.move( (actualWidth + 3 ) * 0.5, 6.564 , 1.94, r=True )    
        
    #group them
    cm.select( 'cornerPillar', 'normalP*', 'rafter*', r=True )
    cm.group( n='pillars' )
    cm.delete( ch=True )
    
    #move and duplicate
    cm.move ( (actualWidth + 3)*-0.5 , 0, (actualWidth + 3)*0.5 , a=True )
    cm.move( 0, 0, 0 , "pillars.scalePivot","pillars.rotatePivot", a=True )
    cm.duplicate()
    cm.rotate( 0, 90, 0, r=True )
    cm.duplicate()
    cm.rotate( 0, 90, 0, r=True )
    cm.duplicate()
    cm.rotate( 0, 90, 0, r=True )
    
    #make the inside cube 
    cm.polyCube( d= actualWidth+3.1 , h=7, w= actualWidth+3.1 , n='insidecube' )
    cm.move( 0, 3.5, 0, r=True)
    
    #group
    cm.select( 'pillar*', 'insidecube', r=True )
    cm.group( n='floor_group' )


        
#make lower roof 
def makeLowerRoof():
    #--make balcony floor
    
    #create the roof group
    cm.group( em=True , n='roof_group' )
    
    #make balcony bottom floor
    balconyWidth = (3 * float(width)) + 5
    cm.polyCube( d=balconyWidth , h=0.1 , w=balconyWidth , n='balconyBottomFloor' )
    cm.move(0, 7.8, 0, r=True)
    cm.parent( 'balconyBottomFloor' , 'roof_group' )
    
    #make balcony rafter supports
    for i in range(int(width)):
        cm.polyCube( d=balconyWidth+0.8 , w=0.5 , h=0.3, n='balconySupport1' )
        cm.move(3*i,0,0, r=True)
    cm.select( 'balconySupport*' , r=True)
    cm.move( (float(width) -1)*-0.75 , 4, 0, r=True )
    cm.group( 'balconySupport*' , n='rafterGroup' , p='roof_group' )
    cm.duplicate()
    cm.rotate(0, 90, 0)
    
    #make balcony top floor
    cm.select( 'balconyBottomFloor' , r=True)
    cm.duplicate( n='balconyTopFloor' )
    cm.move( 0, 0.4, 0, r=True )
        
    
    #--make balcony railing
    
    #make horizontal railing
    cm.polyCube( d=balconyWidth+2 , h=0.25 , w=0.25 , n='balcony_horizontalRafter' )
    cm.move( balconyWidth / 2 -0.125, 8.7, 0, r=True )
    cm.move( 0, 9, 0, 'balcony_horizontalRafter.scalePivot', 
    'balcony_horizontalRafter.rotatePivot', a=True )
    cm.rotate( 0, -90, 0, r=True)
    cm.duplicate()
    cm.move(0, 0.5, 0, r=True)
    
    
    #make vertical railing
    for i in range(int(width)):
        cm.polyCube( d=0.25 , w=0.25, h=1, n='balcony_verticalRafter' )
        cm.move( 3*i , 0 , 0, r=True )
    cm.select( 'balcony_verticalRafter*' , r=True)
    cm.move( (float(width) -1)*-0.75 , 4.3, balconyWidth/4 -0.05, r=True )
    
    #group and rotate
    cm.select( 'balcony_*' , r=True )
    cm.group( n='balconyRailing' , p='roof_group' )
    cm.move( 0,9,0, 'balconyRailing.scalePivot' , 'balconyRailing.rotatePivot' , a=True )
    cm.duplicate()
    cm.rotate( 0,90,0, r=True )
    cm.duplicate()
    cm.rotate( 0,90,0, r=True )
    cm.duplicate()
    cm.rotate( 0,90,0, r=True )
    
    
    #--make roof
    
    #make basic roof shape
    
    extrudeLowerRoofShape( str(4) , 1 ,  1 )
    extrudeLowerRoofShape( str(0) , 1 , -1 )
    extrudeLowerRoofShape( str(2) , 1 ,  1 )
    extrudeLowerRoofShape( str(5) , 1 , -1 )


    #-merge corners
    
    #first corner
    vtxs = { 
    "lvl1" : { "vtx1" : "68" , "vtx2" : "71" , "vtx3" : "48" , "vtx4" : "51" , "vtx5" : "51" , "vtx6" : "48" } ,
    "lvl2" : { "vtx1" : "70" , "vtx2" : "73" , "vtx3" : "52" , "vtx4" : "55" , "vtx5" : "55" , "vtx6" : "52" } ,
    "lvl3" : { "vtx1" : "72" , "vtx2" : "75" , "vtx3" : "56" , "vtx4" : "59" , "vtx5" : "59" , "vtx6" : "72" , "vtx7" : "74" , "vtx8" : "56" } ,
    "lvl4" : { "vtx1" : "74" , "vtx2" : "77" , "vtx3" : "60" , "vtx4" : "63" , "vtx5" : "63" , "vtx6" : "74" , "vtx7" : "60" , "vtx8" : "76" } ,
    "lvl5" : { "vtx1" : "76" , "vtx2" : "79" , "vtx3" : "64" , "vtx4" : "67" , "vtx5" : "67" , "vtx6" : "64" } ,
    }
    mergeCorners( vtxs , -1 , -1 )
    
    #second corner 
    vtxs = { 
    'lvl1' : { 'vtx1' : '8'  , 'vtx2' : '10' , 'vtx3' : '49' , 'vtx4' : '50' , 'vtx5' : '49' , 'vtx6' : '49' } ,
    'lvl2' : { 'vtx1' : '12' , 'vtx2' : '14' , 'vtx3' : '51' , 'vtx4' : '52' , 'vtx5' : '51' , 'vtx6' : '51' } ,
    'lvl3' : { 'vtx1' : '16' , 'vtx2' : '18' , 'vtx3' : '53' , 'vtx4' : '54' , 'vtx5' : '53' , 'vtx6' : '18' , 'vtx7' : '53' , 'vtx8' : '16' } ,
    'lvl4' : { 'vtx1' : '20' , 'vtx2' : '22' , 'vtx3' : '55' , 'vtx4' : '56' , 'vtx5' : '22' , 'vtx6' : '55' , 'vtx7' : '20' , 'vtx8' : '55' } ,
    'lvl5' : { 'vtx1' : '24' , 'vtx2' : '26' , 'vtx3' : '57' , 'vtx4' : '58' , 'vtx5' : '57' , 'vtx6' : '57' } ,
    }
    mergeCorners( vtxs , 1 , -1 )
    
    #third
    vtxs = { 
    'lvl1' : { 'vtx1' : '9'  , 'vtx2' : '11' , 'vtx3' : '29' , 'vtx4' : '30' , 'vtx5' : '29' , 'vtx6' : '30' } ,
    'lvl2' : { 'vtx1' : '13' , 'vtx2' : '15' , 'vtx3' : '31' , 'vtx4' : '32' , 'vtx5' : '31' , 'vtx6' : '32' } ,
    'lvl3' : { 'vtx1' : '17' , 'vtx2' : '19' , 'vtx3' : '33' , 'vtx4' : '34' , 'vtx5' : '19' , 'vtx6' : '34' , 'vtx7' : '17' , 'vtx8' : '33' } ,
    'lvl4' : { 'vtx1' : '21' , 'vtx2' : '23' , 'vtx3' : '35' , 'vtx4' : '36' , 'vtx5' : '23' , 'vtx6' : '36' , 'vtx7' : '21' , 'vtx8' : '35' } ,
    'lvl5' : { 'vtx1' : '25' , 'vtx2' : '27' , 'vtx3' : '37' , 'vtx4' : '38' , 'vtx5' : '37' , 'vtx6' : '38' } ,
    }
    mergeCorners( vtxs , 1 , 1 )
    
    #fourth
    vtxs = { 
    'lvl1' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '29' , 'vtx4' : '28' , 'vtx5' : '28' , 'vtx6' : '29' } ,
    'lvl2' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '30' , 'vtx4' : '31' , 'vtx5' : '30' , 'vtx6' : '31' } ,
    'lvl3' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '32' , 'vtx4' : '33' , 'vtx5' : '49' , 'vtx6' : '33' , 'vtx7' : '48' , 'vtx8' : '32' } ,
    'lvl4' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '35' , 'vtx4' : '34' , 'vtx5' : '35' , 'vtx6' : '49' , 'vtx7' : '34' , 'vtx8' : '48' } ,
    'lvl5' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '37' , 'vtx4' : '36' , 'vtx5' : '36' , 'vtx6' : '37' } ,
    }
    mergeCorners( vtxs , -1 , 1 )

    
#makes the top roof
def makeTopRoof():
    
    #--make basic shape
    cm.polyCube( d=float(width) , w=float(width) , h=0.1, n='tr_roof' )
    
    extrudeUpperRoofShape( str(0) , 1 , -1 )
    extrudeUpperRoofShape( str(2) , 1 ,  1 )
    extrudeUpperRoofShape( str(4) , 1 ,  1 )
    extrudeUpperRoofShape( str(5) , 1 , -1 )
    
    
    #--merge edges
    
    vtxs = {             #first
    'lvl1' : { 'vtx1' : '68' , 'vtx2' : '71' , 'vtx3' : '28' , 'vtx4' : '31' , 'vtx5' : '31' , 'vtx6' : '28' } ,
    'lvl2' : { 'vtx1' : '70' , 'vtx2' : '73' , 'vtx3' : '32' , 'vtx4' : '35' , 'vtx5' : '35' , 'vtx6' : '32' } ,
    'lvl3' : { 'vtx1' : '72' , 'vtx2' : '75' , 'vtx3' : '36' , 'vtx4' : '39' , 'vtx5' : '74' , 'vtx6' : '72' } ,
    'lvl4' : { 'vtx1' : '74' , 'vtx2' : '77' , 'vtx3' : '40' , 'vtx4' : '43' , 'vtx5' : '76' , 'vtx6' : '74' } ,
    'lvl5' : { 'vtx1' : '76' , 'vtx2' : '79' , 'vtx3' : '44' , 'vtx4' : '47' , 'vtx5' : '47' , 'vtx6' : '44' } ,
    }
    mergeTopCorners( vtxs , -1 , -1 )
    
    vtxs = {             #second
    'lvl1' : { 'vtx1' : '48' , 'vtx2' : '50' , 'vtx3' : '29' , 'vtx4' : '30' , 'vtx5' : '30' , 'vtx6' : '29' } ,
    'lvl2' : { 'vtx1' : '50' , 'vtx2' : '52' , 'vtx3' : '33' , 'vtx4' : '34' , 'vtx5' : '34' , 'vtx6' : '33' } ,
    'lvl3' : { 'vtx1' : '52' , 'vtx2' : '54' , 'vtx3' : '37' , 'vtx4' : '38' , 'vtx5' : '53' , 'vtx6' : '52' } ,
    'lvl4' : { 'vtx1' : '54' , 'vtx2' : '56' , 'vtx3' : '41' , 'vtx4' : '42' , 'vtx5' : '55' , 'vtx6' : '54' } ,
    'lvl5' : { 'vtx1' : '56' , 'vtx2' : '58' , 'vtx3' : '45' , 'vtx4' : '46' , 'vtx5' : '46' , 'vtx6' : '45' } ,
    }
    mergeTopCorners( vtxs , 1 , -1 )
    
    vtxs = {             #third
    'lvl1' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '9' , 'vtx4' : '10' , 'vtx5' : '9' , 'vtx6' : '10' } ,
    'lvl2' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '13' , 'vtx4' : '14' , 'vtx5' : '13' , 'vtx6' : '14' } ,
    'lvl3' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '17' , 'vtx4' : '18' , 'vtx5' : '48' , 'vtx6' : '49' } ,
    'lvl4' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '21' , 'vtx4' : '22' , 'vtx5' : '48' , 'vtx6' : '49' } ,
    'lvl5' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '25' , 'vtx4' : '26' , 'vtx5' : '25' , 'vtx6' : '26' } ,
    }
    mergeTopCorners( vtxs , 1 , 1 )
    
    vtxs = {             #fourth
    'lvl1' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '8' , 'vtx4' : '11' , 'vtx5' : '8' , 'vtx6' : '11' } ,
    'lvl2' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '12' , 'vtx4' : '15' , 'vtx5' : '12' , 'vtx6' : '15' } ,
    'lvl3' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '16' , 'vtx4' : '19' , 'vtx5' : '48' , 'vtx6' : '49' } ,
    'lvl4' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '20' , 'vtx4' : '23' , 'vtx5' : '48' , 'vtx6' : '49' } ,
    'lvl5' : { 'vtx1' : '48' , 'vtx2' : '49' , 'vtx3' : '24' , 'vtx4' : '27' , 'vtx5' : '24' , 'vtx6' : '27' } ,
    }
    mergeTopCorners( vtxs , -1 , 1 )
    
    
    #moves into position
    cm.select( 'tr_roof' , r=True )
    cm.move( 0, float(width)*2.15, 0, r=True )
    
    #--make top of roof
    
    cm.polyExtrudeFacet( 'tr_roof.f[1]' , ltz=1 )
    
    #make first hemisphere   
    cm.polySphere( r=( float(width)/3 ) , sx=10 , sy=10 , n='tr_thingOnTopOfTopRoof' )
    cm.delete( 'tr_thingOnTopOfTopRoof.f[0:39]' , 'tr_thingOnTopOfTopRoof.f[80:89]' )
    cm.scale( 1, 0.8, 1 , r=True )
    cm.move( 0, float(width)*2.15 + 1, 0, r=True )
    
    #get the height of the first hemisphere
    what = cm.ls( sl = True )
    where = cm.xform( what , t = True , query = True )
    where[1] = where[1] + float(width)/3 * 0.8 
    
    #make the connector between the first and second hemispheres
    cm.polyCylinder( r=float(width)/10 , h=0.5, n='tr_connector1' )
    cm.move( 0, where[1] + 0.2 , 0, r=True )
    cm.delete( 'tr_connector1.f[20:21]' )
    
    
    #make flower thing            
    cm.polySphere( r=( float(width)/3 ) , n='tr_flowerThing' )
    cm.delete( 'tr_flowerThing.f[180:359]' , 'tr_flowerThing.f[380:399]' )
    
    cm.polySelect( 'tr_flowerThing', el=340, r=True )    #select every other edge loop
    for i in range( 342, 359 , 2 ):
        cm.polySelect( 'tr_flowerThing', el=i, tgl=True )
    
    cm.scale( 0.7, 0.7, 0.7, r=True )
    cm.move( 0, -0.3, 0, r=True )
    cm.polyCloseBorder( 'tr_flowerThing.e[180]' )          
    cm.polyPoke( 'tr_flowerThing.f[200]' )              
    cm.move( 0, ( float(width)/3 )/-5, 0, 'tr_flowerThing.vtx[201]' , r=True )
    
    cm.select( 'tr_flowerThing', r=True ) 
    cm.move( 0, ( float(width)/3 ) + where[1] + 0.3, 0, r=True)
    
    #make the disc thingys
    discWidth=float(width)/3
    for i in range(9):
        cm.polyCylinder( r=discWidth , h=float(width)/6 , n='tr_disc#' )
        cm.move( 0, float(width)/2.3*i + where[1] + float(width), 0, r=True )
        discWidth=discWidth*0.95
        
        
    #make spiral disk thing
    cm.polyHelix( c=11, h=float(width)/1.5, w=float(width)/2.3, r=0.03, sco=15, n='tr_spiral' )
    cm.move( 0, where[1] + float(width)*5.2 , 0, r=True )
    cm.select( 'tr_spiral.f[1320]' , r=True )
    cm.rotate( 0, -45, 0, r=True )
    cm.move( float(width)/ -6.97, 0, float(width)/ -6.97, r=True )
    cm.select( 'tr_spiral.f[1321]' , r=True )
    cm.rotate( 0, 45, 0, r=True )
    cm.move( float(width)/ -7.8, 0, float(width)/ 7.8, r=True )
    
    #make the connector between the flower thing and the disks and helix
    cm.polyCylinder( r=float(width)/ 10 , h=float(width)*5.5 , n='tr_connector2' )
    cm.move( 0, ( float(width)/3 ) + where[1] + float(width)*2.7,  0, r=True )
    cm.scale( 0.5, 1, 0.5, 'tr_connector2.f[21]', r=True )
    
    #make top cylinder
    cm.polyCylinder( r=float(width)/ 7.5 , h=float(width)/3.75, n='tr_topCylinder' )
    cm.move( 0, where[1] + float(width)*5.83, 0, r=True )
    
    #make connector between topCylinder and topSphereThing
    cm.polyCylinder( r=float(width)/ 15, h=float(width)/6, n='tr_connector3' )
    cm.move( 0, where[1] + float(width)*6, 0, r=True )
    
    #make topSphere
    cm.polySphere( r=float(width)/ 10 ,sx=10, sy=10, n='tr_topSphere' )
    cm.move( 0, where[1] + float(width)*6.15, 0, r=True )
    cm.select( 'tr_topSphere.vtx[91]' , r=True )
    cm.softSelect( sse=1, ssd=float(width)/6)
    cm.move( 0, float(width)/10, 0, r=True )
    cm.softSelect( sse=0 )
    cm.move( 0, float(width)/60, 0, r=True )
    
    #group it
    cm.select( 'tr_*' , r=True )
    cm.group( n='topRoof_group' )
    

#assembles it all together
def assembleIt( width , height ):
    #if it's a one storey tower
    if height==1:
        makeFloor()
        makeLowerRoof()
        if merge==True:
            cm.select( 'floor_group' , 'roof_group' , r=True )
            cm.polyUnite( n='Temple' )
            cm.delete( ch=True )

         
    #if it's a two storey tower   
    elif height==2:
        makeFloor()
        makeLowerRoof()
        cm.select( 'floor_group' , r=True )
        cm.duplicate()
        cm.move( 0,8,0 , r=True )
        makeTopRoof()       
        if width==1:
            cm.scale( 2.2, 2.2, 2.2, r=True )
        elif width==2:
            cm.scale( 1.3, 1.3, 1.3, r=True )
        elif width>=4:
            roofWidth = ( float(width)* -0.05 + 1 )
            cm.scale( roofWidth, roofWidth, roofWidth, r=True )
        bottom = cm.xform( bb=True, q=True )
        top = cm.xform( 'floor_group1', bb=True , q=True )
        cm.move( 0, top[4] - bottom[1] - 1, 0, 'topRoof_group', r=True )
        makeFinalCombine_MultipleStorey()
    
    
    # if it has more than two storeys
    else:
        makeFloor()
        makeLowerRoof()
        for i in range( int(height) -2 ):
            cm.select( 'floor_group' , r=True )
            cm.duplicate()
            cm.move( 0,7.9*(i+1),0 , r=True )
            cm.select( 'roof_group' , r=True )
            cm.duplicate()
            cm.move( 0,7.9*(i+1),0 , r=True )
        cm.select( 'floor_group' , r=True )
        cm.duplicate()
        cm.move( 0,7.9*(height-1),0 , r=True )
        makeTopRoof()
        if width==1:
            cm.scale( 2.18, 2.18, 2.18, r=True )
        elif width==2:
            cm.scale( 1.3, 1.3, 1.3, r=True )
        elif width>=4:
            roofWidth = ( float(width)* -0.05 + 1 )
            cm.scale( roofWidth, roofWidth, roofWidth, r=True )
        bottom = cm.xform( bb=True, q=True )
        top = cm.xform( 'floor_group'+str(height-1), bb=True , q=True )
        cm.move( 0, top[4] - bottom[1] - 0.5, 0, 'topRoof_group', r=True )
        makeFinalCombine_MultipleStorey()
        


#---------UI stuff--------

#closes an old window if present
def closeWindow( *args ):
    cm.deleteUI( 'guiWindow' , wnd=True )
    
#function that makes the temples
def makeTemple( *args ):
    #make things global to work
    global width
    global merge
    #turn sliders and buttons into variables
    width = cm.intSliderGrp( w, q=True, v=True )
    height = cm.intSliderGrp( h, q=True, v=True )
    merge = cm.checkBox( m, q=True, v=True )
    #assemble the thing
    closeWindow()
    assembleIt( width , height )
    

#check to see if the temple builder window exists, and if it does, deletes it
if cm.window('guiWindow', exists = True):
    cm.deleteUI('guiWindow')

#creates window
cm.window( 'guiWindow', t='Temple Builder' , mnb = False , mxb = False , s=False, w=400 , h=130 )
form = cm.formLayout( nd=100, w=400 , h=130 )

#sliders
w = cm.intSliderGrp( l='Width ' , f=True , min=1 , max=20 , s=1 , v=2 )
h = cm.intSliderGrp( l='Height' , f=True , min=1 , max=20 , s=1 , v=2 )

#checkbox
m = cm.checkBox( l = 'Merge Geometry' , v=True )

#button
b = cm.button( l='Make Temple' , w=390, h=45, command=makeTemple )

#stick stuff into the window
cm.formLayout( form , edit=True, 
af=[ (w, 'left', 0), (w, 'right', 5), (w, 'top', 5), (h, 'left', 0), (h, 'right', 5), (m, 'left', 107), (b, 'left', 5) ], 
ac=[ (h, 'top', 5, w), (m, 'top', 5, h), (b, 'top', 5, m) ] )

#display the window
cm.showWindow()


