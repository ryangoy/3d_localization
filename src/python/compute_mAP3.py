import numpy as np
import sys
import functools
from utils import nms


# Retruns precision and recall arrays of a given sccene and category
def compute_PR_curve(preds, preds_conf, labels, labels_confs, threshold=0.5):
    curr_preds = [] 
    Ps = [1.0, 0.0]
    Rs = [0.0, 1.0]
    
    confidences = []


    # Loop through all the predictions for a scene in descending order of confidence values. Calculates AP.
    for scene in range(len(preds)):
        
        for p in range(len(preds[scene])):
            pred = preds[scene][p]
            # Find a label that the prediction corresponds to if it exists.
            pred_matched = False  
            matched_labels = []
            for l in range(len(labels[scene])):

                label = labels[scene][l]
                if l in matched_labels:
                    continue

                max_LL = np.max(np.array([pred[:3], label[:3]]), axis=0)
                min_UR = np.min(np.array([pred[3:], label[3:]]), axis=0)
                intersection = np.prod(min_UR - max_LL)
                union = np.prod(pred[3:]-pred[:3]) + np.prod(label[3:]-label[:3]) - intersection
                
                # If we found a label that matches our prediction, i.e. a true positive
                if min(min_UR - max_LL) > 0 and intersection/union > threshold and labels_confs[scene][l] == 1:
                    curr_preds.append(1)
                    pred_matched = True
                    matched_labels.append(l)
                    break

            # If we couldn't find a single label to match our prediction, i.e. a false positive
            if not pred_matched:
                curr_preds.append(0)

            confidences.append(preds_conf[scene][p])

    indices = np.argsort(confidences)[::-1]
    ordered_preds = np.array(curr_preds)[indices]

    curr_ordered = []
    for op in ordered_preds:
        curr_ordered.append(op)
        precision = float(sum(curr_ordered)) / len(curr_ordered)
        recall = float(sum(curr_ordered)) / len(labels)
        Ps.append(precision)
        Rs.append(recall)

    return Ps, Rs

def compute_AP_from_PR(Ps, Rs):
    # Calculate AP for scene:
    PR_vals = []
    for recall_threshold in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        
        if len(Ps) == 0:
            PR_vals.append(0)
            continue

        i = np.argmax(Ps)

        while Rs[i] < recall_threshold:
            del Rs[i]
            del Ps[i]

            if len(Ps) == 0:
                break
            else:
                i = np.argmax(Ps)
        if len(Ps) == 0:
            PR_vals.append(0)
        else:
            PR_vals.append(Ps[i])
    assert len(PR_vals) == 11
    return PR_vals

def compute_mAP(preds, preds_conf, labels, labels_conf, hide_print=False, use_nms=True):

    APs = []
    for c in range(len(preds_conf[0][0])):


        if use_nms:
            new_preds, new_preds_conf = nms(preds_conf, preds, 0.5, c)
        else:
            new_preds, new_preds_conf = preds, preds_conf

        category_preds = []
        category_preds_conf = []
        category_labels = []
        category_labels_conf = []
        for i in range(len(new_preds_conf)):
            category_preds.append(new_preds[i])
            category_preds_conf.append(new_preds_conf[i][:, c])
            category_labels.append(np.array(labels[i]))
            category_labels_conf.append(np.array(labels_conf[i])[:, c+1])

        

        Ps, Rs = compute_PR_curve(category_preds, category_preds_conf, category_labels, category_labels_conf)
        PR_vals = compute_AP_from_PR(Ps, Rs)

        APs.append(sum(PR_vals)/11)
        

    mAP = sum(APs) / len(APs)

    if not hide_print:
        print("APs for each category are {}".format(APs))
        print("mAP is {}".format(mAP))

    return mAP

if __name__ == '__main__':
    preds = np.load(sys.argv[1])
    preds_conf = np.load(sys.argv[2])
    labels = np.load(sys.argv[3])
    labels_conf = np.load(sys.argv[4]) # tells us the category, not really the confidence
    mAP = compute_mAP(preds, preds_conf, labels, labels_conf)