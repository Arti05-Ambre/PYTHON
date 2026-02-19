A=Point(4,-1)
    B=Point(3,0)
    S=Segment(A,B)
    #Rotate about origin through an angle pi
    S=S.rotate(pi)
    S=S.scale(3,0)
    points=S.points
    p=points[0]
    q=points[1]
    p1=p.transform(Matrix([[0,1,0],[1,0,0],[0,0,1]]))
    q1=q.transform(Matrix([[0,1,0],[1,0,0],[0,0,1]]))
    Segment(p1,q1)
