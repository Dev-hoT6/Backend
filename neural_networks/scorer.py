import torch
import numpy as np

import onnx
import onnxruntime as ort

opt = ort.SessionOptions()
opt.graph_optimization_level= ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
opt.log_severity_level=3
opt.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL

ort_session = ort.InferenceSession('/home/ubuntu/backend/neural_networks/fully_connected_classifier_123.onnx', opt)

score_dict = {
    1 : 100,
    2 : 300,
    3 : 500
}


### 모델 통해 점수화
def get_score(vector):
    vector = {'input' : vector.view(-1).numpy()}
    score = ort_session.run(None, vector)
    score = score[0].argmax()
    return int(score) + 1

def get_point(score):
    return score_dict[score]