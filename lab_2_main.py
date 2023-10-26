import pandas as pd
from time import time
from ldfs import limited_deep_first_search
from rbfs import recursive_best_first_search
from puzzle import Puzzle


# --------- Функція табличного представлення поточного стану ----------
def print_state(state, state_number=None):
    if state_number is not None:
        print(f'Стан {state_number}:')
    for i in range(0, len(state), 3):
        row = state[i:i + 3]
        print(row)

state = [[1, 3, 4,
          8, 6, 2,
          7, 0, 5],

         [1, 3, 4,
          0, 6, 2,
          8, 7, 5],

         [2, 8, 1,
          0, 4, 3,
          7, 6, 5],

         [2, 1, 0,
          4, 8, 3,
          7, 6, 5],

         [2, 8, 1,
          4, 6, 3,
          0, 7, 5],

         [2, 8, 1,
          4, 0, 6,
          7, 5, 3],

         [1, 8, 4,
          6, 7, 2,
          5, 3, 0],

         [0, 1, 4,
          6, 8, 2,
          5, 7, 3],

         [1, 0, 6,
          8, 3, 5,
          7, 4, 2],

         [1, 3, 6,
          7, 8, 5,
          4, 2, 0],

         [1, 6, 2,
          7, 4, 0,
          5, 3, 8],

         [1, 6, 2,
          7, 0, 8,
          5, 4, 3],

         [8, 7, 1,
          6, 0, 3,
          2, 5, 4],

         [8, 7, 1,
          6, 3, 4,
          2, 5, 0],

         [5, 1, 3,
          2, 7, 6,
          0, 8, 4],

         [5, 1, 3,
          2, 0, 6,
          8, 7, 4],

         [4, 2, 6,
          1, 5, 0,
          8, 7, 3],

         [4, 2, 6,
          1, 0, 5,
          8, 7, 3],

         [1, 2, 3,
          5, 6, 4,
          0, 8, 7],

         [1, 2, 3,
          6, 4, 0,
          5, 8, 7]]

data = pd.DataFrame(columns=['Алгоритм', 'Час', 'Операцій', 'Пам\'ять'])

sum_memo_ldfs = 0
sum_memo_rbfs = 0
sum_lens_ldfs = 0
sum_lens_rbfs = 0
sum_time_ldfs = 0
sum_time_rbfs = 0

for i in range(0, 20):
    print('------------------------------------------')
    print('Стартовий стан', i + 1)
    print_state(state[i])


    Puzzle.num_of_instances = 0
    t0 = time()
    max_depth = 20
    ldfs = limited_deep_first_search(state[i], max_depth)
    t1 = time() - t0
    print('\nLDFS:', ldfs)
    print('Операцій:', len(ldfs))
    print('Пам\'ять:', Puzzle.num_of_instances)
    print('Час:', t1)

    sum_time_ldfs = sum_time_ldfs + t1
    sum_lens_ldfs = sum_lens_ldfs + len(ldfs)
    sum_memo_ldfs = sum_memo_ldfs + Puzzle.num_of_instances
    # data = {'Час': [t1],
    #         'Операцій': [len(ldfs)],
    #         'Пам\'ять': [Puzzle.num_of_instances]}
    new_row = pd.Series({'Алгоритм': 'LDFS', 'Час': t1, 'Операцій': len(ldfs), 'Пам\'ять': Puzzle.num_of_instances})
    data = pd.concat([data, new_row.to_frame().T], ignore_index=False)
    # my_row = pd.DataFrame([new_row])
    # data = data.append(my_row, ignore_index=True)
    # data = pd.concat([data, new_row], ignore_index=True)
    # data = data.loc(new_row)

    Puzzle.num_of_instances = 0
    t0 = time()
    rbfs = recursive_best_first_search(state[i])
    t1 = time() - t0
    print('\nRBFS:', rbfs)
    print('Операцій:', len(rbfs))
    print('Пам\'ять:', Puzzle.num_of_instances)
    print('Час:', t1)

    sum_time_rbfs = sum_time_rbfs + t1
    sum_lens_rbfs = sum_lens_rbfs + len(rbfs)
    sum_memo_rbfs = sum_memo_rbfs + Puzzle.num_of_instances
    # data = {'Час': [t1],
    #         'Операцій': [len(rbfs)],
    #         'Пам\'ять': [Puzzle.num_of_instances]}
    new_row = pd.Series({'Алгоритм': 'RBFS', 'Час': t1, 'Операцій': len(rbfs), 'Пам\'ять': Puzzle.num_of_instances})
    data = pd.concat([data, new_row.to_frame().T], ignore_index=True)
    # my_row = pd.DataFrame([new_row])
    # data = data.append(my_row, ignore_index=True)
    # data = pd.concat([data, new_row], ignore_index=True)
    # data = data.loc(new_row)

    # # Об'єднання двох таблиць
    # state_results = pd.concat([ldfs_df, rbfs_df])

print('\n-------- Порівняння алгоритмів -------- \n', data)

print('\n----------------------------------------\n')
print('--------- Середні результати алгоритмів ---------')

print('\nCереднє по пам\'яті LDFS', (sum_memo_ldfs / 20))
print('Cереднє по операціям LDFS', (sum_lens_ldfs / 20))
print('Cереднє по часу LDFS', (sum_time_ldfs / 20))

print('\nCереднє по пам\'яті RBFS', (sum_memo_rbfs / 20))
print('Cереднє по операціям RBFS', (sum_lens_rbfs / 20))
print('Cереднє по часу RBFS', (sum_time_rbfs / 20))