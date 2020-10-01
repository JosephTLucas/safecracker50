import numpy as np

layer1 = np.array([8, 0, 16, 0, 19, 0, 8, 0, 17, 0, 6, 0, 6, 0, 8, 0])
layer12 = np.array([17, 4, 20, 4, 14, 4, 5, 1, 14, 10, 17, 19, 5, 6, 18, 8])
layer2 = np.array([0, 11, 0, 8, 0, 12, 0, 11, 0, 3, 0, 8, 0, 10, 0, 14])
layer23 = np.array([20, 8, 19, 10, 15, 20, 12, 20, 13, 13, 0, 22, 19, 10, 0, 5])
layer3 = np.array([0, 0, 11, 0, 8, 0, 8, 0, 8, 0, 10, 0, 11, 0, 10, 0])
layer34 = np.array([12, 1, 10, 12, 22, 0, 5, 8, 5, 1, 24, 8, 10, 20, 7, 20])
layer4 = np.array([9, 0, 8, 0, 8, 0, 9, 0, 6, 0, 10, 0, 8, 0, 10, 0])
layer45 = np.array([13, 11, 13, 10, 18, 10, 10, 10, 10, 15, 7, 19, 18, 2, 9, 27])
layer5 = np.array([0, 16, 8, 4, 15, 7, 10, 1, 10, 4, 5, 3, 15, 16, 4, 7])

layers = (layer1, layer12, layer2, layer23, layer3, layer34, layer4, layer45, layer5)

columns = np.array(layers)

def integrity_check():
    for layer in layers:
        if len(layer) != 16:
            print(f"{layer} has {len(layer)} entries.  Needs 16.")
            break
    return

def rotate(i):
    columns[i] = np.roll(columns[i],1)
    return            

def check():
    if np.sum(columns, axis=0).any() != 50:
        return False
    else:
        return True

if __name__ == "__main__":
    integrity_check()
    count = 0
    options = [i for i in range(9)]
    for i in range(9):
        for k in [a for a in options if a is not i]:
            for j in range(16):
                rotate(k)
                count += 1
                print(np.sum(columns, axis=0))
                flag = check()
                if flag is True:
                    break
    if flag is False:
        print(f"Exhausted at {count}")
    print(columns)
    print(np.sum(columns, axis=0))
