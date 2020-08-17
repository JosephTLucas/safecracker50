import numpy as np

layer1 = (8, 0, 16, 0, 19, 0, 8, 0, 17, 0, 6, 0, 6, 0, 8, 0)
layer12 = (17, 4, 20, 4, 14, 4, 5, 1, 14, 10, 17, 19, 5, 6, 18, 8)
layer2 = (0, 11, 0, 8, 0, 12, 0, 11, 0, 3, 0, 8, 0, 10, 0, 14)
layer23 = (20, 8, 19, 10, 15, 20, 12, 20, 13, 13, 0, 22, 19, 10, 0, 5)
layer3 = (0, 0, 11, 0, 8, 0, 8, 0, 8, 0, 10, 0, 11, 0, 10, 0)
layer34 = (12, 1, 10, 12, 22, 0, 5, 8, 5, 1, 24, 8, 10, 20, 7, 20)
layer4 = (9, 0, 8, 0, 8, 0, 9, 0, 6, 0, 10, 0, 8, 0, 10, 0)
layer45 = (13, 11, 13, 10, 18, 10, 10, 10, 10, 15, 7, 19, 18, 2, 9, 27)
layer5 = (0, 16, 8, 4, 15, 7, 10, 1, 10, 4, 5, 3, 15, 16, 4, 7)

layers = (layer1, layer12, layer2, layer23, layer3, layer34, layer4, layer45, layer5)

columns = np.zeros((5,16))

def integrity_check():
    for layer in layers:
        if len(layer) != 16:
            print(f"{layer} has {len(layer)} entries.  Needs 16.")

if __name__ == "__main__":
    integrity_check()
    print(np.sum(columns, axis=0))
    
