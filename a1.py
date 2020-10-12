"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{user.name}} ({{user.id}})"
__email__ = ""
__date__ = ""


def select_word_at_random(word_select):
    '''
    从词库中随机选出一个单词
    :param word_select:
    :return:
    '''
    if word_select not in ["FIXED", "ARBITRARY"]:
        return None
    all_words = load_words(word_select)
    word = all_words[random_index(all_words)]
    return word


def create_guess_line(guess_no, word_length):
    '''
    打印输出行
    :param guess_no:
    :param word_length:
    :return:
    '''
    res = 'Guess {}|'.format(guess_no)
    start, end = GUESS_INDEX_TUPLE[word_length-6][guess_no-1]
    for i in range(word_length):
        if (i >= start) and (i <= end):
            res += ' * |'
        else:
            res += ' - |'
    return res


def display_guess_matrix(guess_no, word_length, scores):
    '''
    打印猜词过程和得分
    :param guess_no:
    :param word_length:
    :param scores:
    :return:
    '''
    title = ' '*len('Guess 4') + WALL_VERTICAL
    for i in range(word_length):
        title += ' {} '.format(i + 1) + WALL_VERTICAL
    print(title)
    print(WALL_HORIZONTAL*(33 + (word_length - 6)*4))
    for i in range(guess_no):
        item = create_guess_line(i + 1, word_length)
        try:
            score = str(scores[i])
            item += ' ' * 3 + score + ' Points'
        except Exception as e:
            # item += ' ' * 3
            pass
        print(item)
        print(WALL_HORIZONTAL * (33 + (word_length - 6) * 4))


def compute_value_for_guess(word, start_index, end_index, guess):
    '''
    返回用户的得分
    :param word:
    :param start_index:
    :param end_index:
    :param guess:
    :return:
    '''
    element = ('a', 'e', 'i', 'o', 'u')
    right_word = word[start_index:end_index+1]
    score = 0
    # 正确位置的得分
    right_element = []
    right_word_index = start_index
    for i in guess:
        if i == word[right_word_index]:
            right_element.append(i)
            if i in element:
                score += 14
            else:
                score += 12
        right_word_index = right_word_index + 1
    # 计算不正确位置的得分
    # 去重
    guess_filter = set(guess)
    for i in guess_filter:
        if (i in right_word) and (i not in right_element) :
            score += 5
    return score


def main():
    '''
    main函数
    :return:
    '''
    flag = True
    print(WELCOME)
    while flag:
        word_select = input(INPUT_ACTION)
        if word_select == 's':
            start_game()
            flag = False
        elif word_select == 'h':
            print(HELP)
            start_game()
            flag = False
        elif word_select == 'q':
            flag = False
        else:
            print(INVALID)


def start_game():
    '''
    开始游戏
    :return:
    '''
    word = None
    while word is None:
        word_select = input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
        word = select_word_at_random(word_select)
    print("Now try and guess the word, step by step!!")
    word_length = len(word)
    guess_on = 1
    score = []
    while not (guess_on == word_length):
        display_guess_matrix(guess_on, word_length, score)
        guess = ""
        start_index, end_index = GUESS_INDEX_TUPLE[word_length-6][guess_on-1]
        while len(guess) != (end_index - start_index + 1):
            guess = input("Now enter Guess {}: ".format(guess_on))
        score_item = compute_value_for_guess(word, start_index, end_index, guess)
        score.append(score_item)
        guess_on += 1
    display_guess_matrix(guess_on, word_length, score)
    guess = input("Now enter your final guess. i.e. guess the whole word: ")
    if guess == word:
        print("You have guessed the word correctly. Congratulations.")
    else:
        print("Your guess was wrong. The correct word was \"{}\"".format(word))


if __name__ == "__main__":
    # main()
    # print(create_guess_line(4, 7))
    # scores = (26, 10)
    # display_guess_matrix(3, 8, scores)
    # print(compute_value_for_guess("crushing", 1, 3, "rus"))
    main()
    # print(display_guess_matrix(1, 6, ()))
   # print(compute_value_for_guess('aecdio', 3, 4, 'dx'))
