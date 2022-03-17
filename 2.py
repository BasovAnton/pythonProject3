# 2.	Считалочка
# Дано N человек, считалка из K слогов. Считалка начинает
# считать с первого человека. Когда считалка досчитывает до k-г
# о слога, человек, на котором она остановилась, вылетает. Игра п
# роисходит до тех пор, пока не останется последний человек. Для дан
# ных N и К дать номер последнего оставшегося человека.
import itertools


def counting(men, s):
    men_list = [i for i in range(1, men + 1)]
    for i in range(men-1):
        if s > len(men_list):
            men_list.pop(s % len(men_list)-1)
        elif s < len(men_list):
            men_list.pop(s)
        elif s == len(men_list):
            men_list.pop(len(men_list)-1)

    return men_list[0]
    #
    # while True:
    #     if len(men_list) == 1:
    #         print(f'Остался номер: {men_list[0]}')
    #         break
    #     else:
    #         if s > men:
    #             del_men = s - men - 1
    #
    #         else:
    #             del_men = s - 1
    #             while len(men_list) <= del_men:
    #                 del_men = del_men - len(men_list)
    #         del men_list[del_men]
    #         out_ = del_men
    #         if out_ > len(men_list):
    #             out_ = out_ - len(men_list) - 1
    #         print(men_list)





if __name__ == '__main__':
    print(counting(5, 7))

