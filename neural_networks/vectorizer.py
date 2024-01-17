import torch
import numpy as np

import onnxruntime as ort

from transformers import AutoTokenizer

MODEL_NAME = "snunlp/KR-SBERT-V40K-klueNLI-augSTS"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


opt = ort.SessionOptions()
opt.graph_optimization_level= ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
opt.log_severity_level=3
opt.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL

ort_session = ort.InferenceSession('/home/ubuntu/backend/neural_networks/S_Transformer-onnx.onnx', opt)

### pooling 함수
def mean_pooling(model_output, attention_mask):
    token_embeddings = torch.tensor(model_output[0]) #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.shape).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

### 모델 가져와서 벡터화
def encode(text):
    encoded_input = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    return encoded_input

def vectorize(encoded_input):
    encoded_input_np = {name : np.atleast_2d(value) for name, value in encoded_input.items()}
    vc = ort_session.run(None, encoded_input_np)
    se = mean_pooling(vc, encoded_input['attention_mask'])
    return se

def sbert(text):
    '''
    In: 텍스트
    Out: 벡터(torch.tensor)
    '''
    result = encode(text)
    result = vectorize(result)
    return result

if __name__ == '__main__':
    text_sample = ['상의', '리뷰리뷰리뷰리뷰']
    print(sbert(text_sample))