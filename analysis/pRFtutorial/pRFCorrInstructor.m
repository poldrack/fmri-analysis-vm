% function that will be called by Nelder-Mead algorithm to compute
% the corelation of the model with the params and the tSeries.
% It needs to return 1-correlation because Nelder-Mead minimizes
function valueToBeMinimized = pRFCorr(params,stimImage,stimX,stimY,canonical,tSeries)
 
% number of volumes
n = length(tSeries);
 
% unpack parameters
x = params(1);
y = params(2);
s = params(3);
 
% compute rf
rf = exp(-((stimX-x).^2 + (stimY-y).^2)/(2*s^2));
 
% compute model neural response
modelNeuralResponse = squeeze(sum(sum(stimImage .* repmat(rf,1,1,n))));
 
% compute the model bold response from the above
modelBoldResponse = conv(modelNeuralResponse,canonical);
 
% trim length
modelBoldResponse = modelBoldResponse(1:n)';
 
% normalize
modelBoldResponse = modelBoldResponse-mean(modelBoldResponse);
modelBoldResponse = modelBoldResponse/sqrt(sum(modelBoldResponse.^2));
 
% compute correlation (note the (:) which is just to make sure
% that both arrays are column vectors
r = corr(modelBoldResponse(:),tSeries(:));
 
% and return 1-r 
valueToBeMinimized = 1-r;

% display the fit - this is worthwhile to do, particularly while testing
% to see what the non-linear fit is doing (which can sometimes do some
% really weird things)
clf;
subplot(1,3,1:2);
hold on
tSeries = tSeries-mean(tSeries);
tSeries = tSeries/sqrt(sum(tSeries.^2));
plot(tSeries,'k-');
plot(modelBoldResponse,'r-');
xlabel('Time (volumes)');
ylabel('Response');
title(sprintf('[%0.3f %0.3f] std: %0.3f corr: %0.4f',x,y,s,r));
subplot(1,3,3);
imagesc(rf);
colormap(hot);
axis square
axis off
drawnow
