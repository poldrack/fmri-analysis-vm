load('/home/vagrant/fmri-analysis-vm/analysis/connectivity/dcmfiles/DCM_truemodel.mat')
DCM.b=zeros(5,5);
DCM.b(3,4)=1
DCM.b(4,5)=1
DCM = rmfield(DCM,'M'); % This line is needed if the template model is already estimated
DCM = spm_dcm_estimate(DCM);
save('/home/vagrant/fmri-analysis-vm/analysis/connectivity/dcmfiles/DCM_wrongppi.mat','DCM');
