/*****************************************************************************
 * Project: RooFit                                                           *
 *                                                                           *
  * This code was autogenerated by RooClassFactory                            * 
 *****************************************************************************/

#ifndef ROOEXPTAILPDF
#define ROOEXPTAILPDF

#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooCategoryProxy.h"
#include "RooAbsReal.h"
#include "RooAbsCategory.h"
 
class RooExpTailPdf : public RooAbsPdf {
public:
  RooExpTailPdf() {} ; 
  RooExpTailPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _s,
	      RooAbsReal& _a);
  RooExpTailPdf(const RooExpTailPdf& other, const char* name=0) ;
  virtual TObject* clone(const char* newname) const { return new RooExpTailPdf(*this,newname); }
  inline virtual ~RooExpTailPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy s ;
  RooRealProxy a ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooExpTailPdf,1) // Your description goes here...
};
 
#endif