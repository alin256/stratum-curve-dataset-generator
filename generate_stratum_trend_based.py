import math
import random
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing

random.seed(51)

delta_x = 10.
scale_from_ft = 2.
x_scaling = 3e-3

# added some trend function
x_positions = np.arange(0., 3000., delta_x)
x = (x_positions - x_positions[math.floor(len(x_positions) *0.36)]) * x_scaling

# a = random.random() - 0.5
# b = random.random() - 0.4
# c = random.random() - 0.2
a = 0.
b = 0.
c = 0.
y_positions = a * x ** 3 + b * x ** 2 + c * x
y_dirivatives = (3 * a * x ** 2 + 2 * b * x + c) * x_scaling
y_positions -= y_positions[0]

np.savez('trend.mpz', x_pos=x_positions, y_pos=y_positions)

plt.plot(x_positions / delta_x, y_positions)
# plt.figure()
# plt.plot(x_positions, y_dirivatives)
# plt.show()


def cot(angle):
    return math.cos(angle) / math.sin(angle)


class SubsurfaceState:
    def __init__(self, angle=math.pi/2, position=0, thl=0):
        self.angle = angle
        self.position = position
        self.thl = thl
        # self.data = data
        self._fault_through_max = 10
        self._max_angle_change = 0.035
        # state angle
        # state position

    def to_numpy(self):
        return np.array([self.angle, self.position, self.thl])

    @staticmethod
    def numpy_len():
        return 3

    @staticmethod
    def from_numpy(np_array):
        return SubsurfaceState(np_array[0], np_array[1], np_array[2])

    def get_next_state(self, distance=delta_x):
        new_position = self.position + distance * cot(self.angle)
        new_state = SubsurfaceState(angle=self.angle, position=new_position, thl=self.thl + distance)
        return new_state

    def get_next_state_random(self, distance=delta_x):
        new_thl = self.thl + distance
        # check if we are close to the trend
        new_angle = self.angle + (random.random() - 0.5) * 0.01
        expected_cot = np.interp(new_thl, x_positions, y_dirivatives)
        new_cot = cot(new_angle)
        delta_angle = 0
        if (0.5 + random.random())*0.03 < abs(expected_cot - new_cot)\
                and random.random() > 0.2:
            # approx
            sign = -np.sign(expected_cot - new_cot)
            magnitude = abs(expected_cot - new_cot) * (1.0 + (random.random() - 0.5) * 0.8)
            delta_angle = sign * min(self._max_angle_change, magnitude)

        new_angle += delta_angle
        new_cot = cot(new_angle)

        new_position = self.position + distance * cot(new_angle)
        expected_position = np.interp(new_thl, x_positions, y_positions)

        delta = 0
        if (0.5 + random.random())*7 < abs(expected_position - new_position)\
                and random.random() > 0.8:
            sign = np.sign(expected_position - new_position)
            magnitude = abs(expected_position - new_position) * (1.0 + (random.random() - 0.5))
            delta = sign * min(self._fault_through_max, magnitude)
        # if self._fault_through_max + random.random() < abs(expected_position - new_position):
        #     delta = random.random() * (expected_position - new_position)

        new_position += delta

        new_state = SubsurfaceState(angle=new_angle, position=new_position, thl=new_thl)
        return new_state
        # new_angle


def plot_states_single(states_single):
    ys = []
    if isinstance(states_single,(np.ndarray)):
        for j in range(len(states_single)):
            ys.append(states_single[j][1])
    else:
        for state in states_single:
            ys.append(state.position)
    plt.plot(x_positions/delta_x, np.array(ys)*scale_from_ft)


def plot_states(states):
    for states_single in states:
        plot_states_single(states_single)


def generate_one_trajectory(shape):
    states_single = np.zeros((shape[1], shape[2]))
    state = SubsurfaceState()
    states_single[0] = state.to_numpy()
    for j in range(len(x_positions) - 1):
        state = state.get_next_state_random()
        states_single[j + 1] = state.to_numpy()
    return states_single


if __name__ == "__main__":

    num_realizations = 100
    plot_first_n = 20
    all_states = np.zeros((num_realizations, len(x_positions), SubsurfaceState.numpy_len()))
    shape = all_states.shape
    # all_states = []

    with multiprocessing.Pool(20) as pool:
        results = pool.map(generate_one_trajectory, [shape] * num_realizations)

    # results = map(generate_one_trajectory, [shape] * num_realizations)

    print('done')
    result_list = list(results)
    # print(result_list)

    for i, res in enumerate(result_list):
        if i < plot_first_n:
            plot_states_single(res)
            # print(res)
        all_states[i] = res

    print(all_states.shape)

    # training dataset
    np.savez('train_data_trend.npz', data=all_states)

    num_realizations = num_realizations // 50
    random.seed(101)
    with multiprocessing.Pool(20) as pool:
        results = pool.map(generate_one_trajectory, [shape] * num_realizations)

    result_list = list(results)

    all_states = np.zeros((num_realizations, len(x_positions), SubsurfaceState.numpy_len()))
    for i, res in enumerate(result_list):
        all_states[i] = res

    print(all_states.shape)

    # testing dataset
    np.savez('test_data_trend.npz', data=all_states)

    # plt.axis('equal')
    plt.title('Examples of the generated SVD curves from the dataset')
    plt.xlabel('Vertical section, ft')
    plt.ylabel('Stratigraphic Vertical Depth, ft')
    plt.savefig('trajcetories.png')
    plt.show()


