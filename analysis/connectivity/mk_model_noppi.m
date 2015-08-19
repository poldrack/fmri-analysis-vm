load('DCM_truemodel.mat')
DCM.b=zeros(5,5);
DCM = rmfield(DCM,'M'); % This line is needed if the template model is already estimated
DCM = spm_dcm_estimate(DCM);
save('DCM_noppi.mat','DCM');
