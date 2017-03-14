% function that will be called by Nelder-Mead algorithm to compute
% the corelation of the model with the params and the tSeries.
% It needs to return 1-correlation because Nelder-Mead minimizes
function valueToBeMinimized = pRFCorr(params,stimImage,stimX,stimY,canonical,tSeries)
 
