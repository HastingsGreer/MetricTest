import itk


def test():
    PointSetType = itk.PointSet[itk.UI, 2, itk.DefaultStaticMeshTraits[itk.UI, 
                                    2, 2, itk.F, itk.F, itk.UI]]

    PointType = itk.Point[itk.F, 2]
    
    TranslationType = itk.TranslationTransform[itk.D, 2]
    EuclideanDistancePointSetMetricType = itk.EuclideanDistancePointSetToPointSetMetricv4[PointSetType]
    
    fixedPoints = PointSetType.New()
    fixedPoints.Initialize()
    movingPoints = PointSetType.New()
    movingPoints.Initialize()


    fixedPoint = PointType()
    fixedPoint[0] = 0
    fixedPoint[1] = 1
    fixedPoints.SetPoint(0, fixedPoint)
    movingPoints.SetPoint(0, fixedPoint)

    
    translation = TranslationType.New()
    translation.SetIdentity()
    
    metric = EuclideanDistancePointSetMetricType.New()
    metric.SetFixedPointSet(fixedPoints)
    metric.SetMovingPointSet(movingPoints)
    metric.SetMovingTransform(translation)
    metric.Initialize()

    print "Before transform changes:"
    print metric.GetValue()
    
    print metric.GetFixedPointSet().GetPoint(0)
    #print metric.GetTransformedFixedPointSet().GetPoint(0)
    print metric.GetMovingPointSet().GetPoint(0)
    print metric.GetModifiableFixedTransformedPointSet().GetPoint(0)
    print metric.GetTransform()
    optP = itk.Array[itk.D]()
    optP.SetSize(2)
    optP.SetElement(0, 100)
    
    optP.SetElement(1, 100)
    print metric
    metric.UpdateTransformParameters(optP, 2)
    print "After metric changes:"
    print metric
    
    print metric.GetValue()
    
    print metric.GetFixedPointSet().GetPoint(0)
    #print metric.GetTransformedFixedPointSet().GetPoint(0)
    print metric.GetMovingPointSet().GetPoint(0)
    print metric.GetModifiableFixedTransformedPointSet().GetPoint(0)
    print metric.GetTransform()

    
    
test()
test()
