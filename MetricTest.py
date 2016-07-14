import itk
def test():
    AffineTransformType = itk.AffineTransform[itk.D, 2]
    transformToFind = AffineTransformType.New()
    transformToFind.SetIdentity()
    
    del AffineTransformType
    del transformToFind
    
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
    fixedPoint[1] = 0
    fixedPoints.SetPoint(0, fixedPoint)
    movingPoints.SetPoint(0, fixedPoint)

    
    translation = TranslationType.New()
    translation.SetIdentity()
    
    metric = EuclideanDistancePointSetMetricType.New()
    metric.SetFixedPointSet(fixedPoints)
    metric.SetMovingPointSet(movingPoints)
    metric.SetMovingTransform(translation)
    metric.Initialize()
    
    print metric.GetValue()
    optP = itk.Array[itk.D]()
    optP.SetSize(2)
    optP.SetElement(0, 100)
    optP.SetElement(1, 100)
    metric.UpdateTransformParameters(optP, 1)
    print metric.GetValue()
    
    
test()
test()
