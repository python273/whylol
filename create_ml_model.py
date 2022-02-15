import random

target1 = b'''"expr": "CMP quord ptr (R12 + RAX*0x8] , 0x0",\n'''
target2 = b'''"expr": "CMP qword ptr [RBX + 0x10],R14"     ,\n'''
target3 = b'''"expr": "CMP qword ptr [RSP + 0x8],0x0"      ,\n'''

assert len(target1) == len(target2) == len(target3)

with open('image.png', 'rb') as f:
    data1 = f.read()

with open('test_image_1.png', 'rb') as f:
    data2 = f.read()

with open('test_image_2.png', 'rb') as f:
    data3 = f.read()

print(f'Taget len: {len(target1)}')

num_neurons = 150

inputs = [data1, data2, data3]
targets = [target1, target2, target3]

def execute_neuron(input, weights):
    return sum(a*b for a, b in zip(input, weights)) % 256


def create_nn():
    all_weights = []

    print('starting')

    for i in range(len(targets[0])):
        print('neuron', i)
        weights = [random.randint(0, 255) for _ in range(num_neurons)]

        while True:
            weights[random.randint(0, len(weights) - 1)] = random.randint(0, 255)

            if all(
                execute_neuron(inp, weights) == tar[i]
                for inp, tar in zip(inputs, targets)
            ):
                break

        all_weights.extend(weights)

    print(all_weights)

    with open('neural_network_weights.bin', 'wb') as f:
        f.write(bytes(all_weights))

create_nn()
