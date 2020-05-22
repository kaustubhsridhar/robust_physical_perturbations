#!/bin/bash
python classify_yadav.py \
    --srcimgs /home/kaustubh-anaconda/Documents/Vision\ Research/Results/ImagesGTSRB_with_tfs_and_softmax/AdvResizedStop/ \
    --weights ./models/gtsrb_usstop/model_best_test \
    --img_rows 32 \
    --img_cols 32 \
    --nb_classes 43

python classify_yadav.py \
    --srcimgs /home/kaustubh-anaconda/Documents/Vision\ Research/Results/ImagesGTSRB_with_tfs_and_softmax/CleanResizedStop/ \
    --weights ./models/gtsrb_usstop/model_best_test \
    --img_rows 32 \
    --img_cols 32 \
    --nb_classes 43

python classify_yadav.py \
    --srcimgs /home/kaustubh-anaconda/Documents/Vision\ Research/Results/ImagesGTSRB_with_tfs_and_softmax/Clean_UWM_Box_Github/ \
    --weights ./models/gtsrb_usstop/model_best_test \
    --img_rows 32 \
    --img_cols 32 \
    --nb_classes 43

python classify_yadav.py \
    --srcimgs /home/kaustubh-anaconda/Documents/Vision\ Research/Results/ImagesGTSRB_with_tfs_and_softmax/Adv_UWM_Box/ \
    --weights ./models/gtsrb_usstop/model_best_test \
    --img_rows 32 \
    --img_cols 32 \
    --nb_classes 43
