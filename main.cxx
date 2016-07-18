#include "itkEuclideanDistancePointSetToPointSetMetricv4.h"
#include "itkTransform.h"
#include "itkTranslationTransform.h"

#include <fstream>


int itkEuclideanDistancePointSetMetricTestRun()
{
  const int Dimension = 2;
  typedef itk::PointSet<unsigned char, Dimension> PointSetType;

  typedef typename PointSetType::PointType PointType;

  typename PointSetType::Pointer fixedPoints = PointSetType::New();
  fixedPoints->Initialize();

  typename PointSetType::Pointer movingPoints = PointSetType::New();
  movingPoints->Initialize();

  
  PointType fixedPoint;
  fixedPoint[0] = 0;
  fixedPoint[1] = 0;
  fixedPoints->SetPoint( 0, fixedPoint );

  movingPoints->SetPoint( 0, fixedPoint );

  // Simple translation transform for moving point set
  //
  typedef itk::TranslationTransform<double, Dimension> TranslationTransformType;
  typename TranslationTransformType::Pointer translationTransform = TranslationTransformType::New();
  translationTransform->SetIdentity();

  // Instantiate the metric
  typedef itk::EuclideanDistancePointSetToPointSetMetricv4<PointSetType> PointSetMetricType;
  typename PointSetMetricType::Pointer metric = PointSetMetricType::New();
  metric->SetFixedPointSet( fixedPoints );
  metric->SetMovingPointSet( movingPoints );
  metric->SetMovingTransform( translationTransform );
  metric->Initialize();

  typename PointSetMetricType::MeasureType value = metric->GetValue();

  std::cout << "value: " << value << std::endl;
  
  
  typedef typename PointSetMetricType::DerivativeType Params;
  
  Params optP;
  optP.SetSize(2);
  optP.SetElement(0, 100);
  optP.SetElement(1, 100);
  std::cout << metric << std::endl;
  metric->UpdateTransformParameters(optP, 1);
  std::cout << metric << std::endl;
  value = metric->GetValue();
  std::cout << "value: " << value << std::endl;
  
  return 0;
}

int main( int, char* [] )
{
  itkEuclideanDistancePointSetMetricTestRun();
  return 0;
}
