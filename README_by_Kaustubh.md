Original : https://github.com/evtimovi/robust_physical_perturbations
Paper : https://arxiv.org/pdf/1707.08945.pdf
Goal : 
save list of probabilities/softmax outputs given by lisa-cnn for every 32x32 image in <folder>
Or
save list of probabilities/softmax outputs given by gtsrb-cnn for every any-size image in <folder>

Modified : 
lisa_cnn_attack>manyclassify.py
gtsrb_cnn_attack>classify_yadav.py

 Added :
isa_cnn_attack>produce_softmax_outputs.sh
gtsrb_cnn_attack>produce_softmax_outputs.sh

Method : 
1. conda activate vision_env_py2

2. cd Documents/Vision\ Research/Results/<Outer-Folder-of-<folder>>/robust_physical_perturbations/lisa-cnn-attack/
Or
2. cd Documents/Vision\ Research/Results/<Outer-Folder-of-<folder>>/robust_physical_perturbations/gtsrb-cnn-attack/

(Note : Specify <folder>’s in below bash)

3. bash produce_softmax_outputs.sh

Result : 
name of image and corresponding softmax outputs in predictions.csv in <folder>


