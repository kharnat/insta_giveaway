import time
from os import listdir
from os.path import isfile, join

files = [f for f in listdir('2kk_words_400x400') if isfile(join('2kk_words_400x400', f))]


# task 1
def unique_values():
    final_array_task_1 = set()
    for index, file in enumerate(files):
        with open('2kk_words_400x400/' + file) as opened_file:
            lines = opened_file.readlines()
            lines = [line.rstrip() for line in lines]
            final_array_task_1 = final_array_task_1 | set(lines)

    print('Уникальных словосочетаний: ' + str(len(final_array_task_1)))


# task 2
def exist_in_all_files():
    final_array_task_2 = set()
    for index, file in enumerate(files):
        with open('2kk_words_400x400/' + file) as opened_file:
            lines = opened_file.readlines()
            lines = [line.rstrip() for line in lines]
            if index == 0:
                final_array_task_2 = set(lines)
            else:
                final_array_task_2 = final_array_task_2 & set(lines)

    print('Словосочетаний, которые есть во всех 20 файлах: : ' + str(len(final_array_task_2)))


# task 3
def exist_in_at_least_ten():
    counter = {}
    final_array_task_3 = set()

    for index, file in enumerate(files):
        with open('2kk_words_400x400/' + file) as opened_file:
            lines = opened_file.readlines()
            lines = [line.rstrip() for line in lines]
            unique_words = set(lines)

            for word in unique_words:
                counter_by_word = counter.get(word)
                if counter_by_word:
                    counter[word] += 1
                else:
                    counter[word] = 1
                if counter[word] >= 10:
                    final_array_task_3.add(word)

    print('Словосочетаний, которые есть, как минимум, в десяти файлах: ' + str(len(final_array_task_3)))


if __name__ == '__main__':
    start = round(time.time() * 1000)
    unique_values()             # Уникальных словосочетаний: 129240     1730 ms
    end = round(time.time() * 1000)
    exist_in_all_files()
    exist_in_at_least_ten()
    print(str(end - start) + ' ms')

