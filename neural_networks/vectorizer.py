from torch import tensor

### 모델 가져와서 벡터화
def vectorize():
    return tensor([[1, 2, 3], [5, 6, 7]])

if __name__ == '__main__':
    print(str(vectorize().tolist()))