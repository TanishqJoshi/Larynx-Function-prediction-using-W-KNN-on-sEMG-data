myDir = uigetdir; %gets directory
myFiles = dir(fullfile(myDir,'*.mat')); %gets all csv files in struct

FinalData = {};

for k = 1:length(myFiles)
  baseFileName = myFiles(k).name;
  fullFileName = string(baseFileName);

  fprintf(1, 'Now Reading -  %s\sn', fullFileName);
  initial = load(fullFileName);
  len = length(initial.decomposed_Data);
  for i=1:len
      data = initial.decomposed_Data{i,1};
      data = data';
      FinalData = [FinalData;data];
  end
end

save('CoughDataControl_ch1','FinalData');


FinalData = {};

for k = 1:length(myFiles)
  baseFileName = myFiles(k).name;
  fullFileName = string(baseFileName);

  fprintf(1, 'Now Reading -  %s\sn', fullFileName);
  initial = load(fullFileName);
  len = length(initial.decomposed_Data);
  for i=1:len
      data = initial.decomposed_Data{i,2};
      data = data';
      FinalData = [FinalData;data];
  end
end

save('CoughDataControl_ch2','FinalData');

FinalData = {};

for k = 1:length(myFiles)
  baseFileName = myFiles(k).name;
  fullFileName = string(baseFileName);

  fprintf(1, 'Now Reading -  %s\sn', fullFileName);
  initial = load(fullFileName);
  len = length(initial.decomposed_Data);
  for i=1:len
      data = initial.decomposed_Data{i,3};
      data = data';
      FinalData = [FinalData;data];
  end
end

save('CoughDataControl_ch3','FinalData');
