# coding=utf-8
# 前三名
def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    sort_list = sorted(input_list, reverse=True)
    return sort_list[:3]


# 中位数
def median(numbers):
    num = len(numbers)
    numbers.sort()  # The sort method sorts a list directly, rather than returning a new sorted list
    if num % 2 == 0:
        return (numbers[int(num / 2) - 1] + numbers[int(num / 2)]) / 2
    else:
        middle_index = int(len(numbers) / 2)
        return numbers[middle_index]


def list_sum(input_list):
    """求列表总和
    :param input_list:
    :return:
    """
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for input in input_list:
        sum += input
    return sum


def tag_count(input_list):
    """
    编写一个函数 tag_count，其参数以字符串列表的形式列出。该函数应该返回字符串中有多少个 XML 标签。XML 是类似于 HTML 的数据语言。
    你可以通过一个字符串是否是以左尖括号 "<" 开始，以右尖括号 ">" 结尾来判断该字符串是否为 XML 标签
    :param input_list:
    :return:
    """
    count = 0
    for input in input_list:
        if '<' in input and '>' in input:
            count += 1
    return count


def html_list(list):
    """
    编写 html_list 函数。该函数需要一个参数，一个字符串列表，并返回一个 HTML 列表的单个字符串。例如，如果为函数提供列表 ['first string', 'second string']，则该函数可产生以下字符串。

<ul>
<li>first string</li>
<li>second string</li>
</ul>
    :param list:
    :return:
    """
    str = "<ul>\n"

    for li in list:
        str += "<li>" + li + "</li>\n"

    str += "</ul>"
    return str;


def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box

    # print sides of box
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*")
    print("*" * width) #print bottom edge of box


def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    with open(filename) as f:
    # use the for loop syntax to process each line
    # and add the actor name to cast_list
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list