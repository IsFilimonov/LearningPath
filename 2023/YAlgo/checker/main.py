import os
import sys
import filecmp
import glob

def start():  

    # TODO: len != 4 --- ненадежно, тк запуск может быть из разных мест
    if len(sys.argv) != 4:
        raise("Должно быть введено 3 параметра: День, Задача, Тест")
        exit

    day, task = sys.argv[1:3]
    dir_task = os.path.join("checker", "day_{}".format(day),"task_{}".format(task))
    
    if sys.argv[3].isnumeric():
        examples = [sys.argv[3]]
    elif sys.argv[3] == "+":
        files = sorted(glob.glob("in_*.txt", root_dir=dir_task))
        examples = [el.removeprefix("in_").removesuffix(".txt") for el in files]
    else:
        exit

    for example in examples:

        f_code = os.path.join(dir_task, "solution.py")
        f_input = os.path.join(dir_task, "in_{}.txt".format(example))
        f_answer = os.path.join(dir_task, "ans_{}.txt".format(example))
        f_output = os.path.join(dir_task, "out_{}.txt".format(example))
        
        cmd1 = "python3.10 {} < {} > {}".format(
            f_code,
            f_input,
            f_answer
        )

        os.system(cmd1)

        result = filecmp.cmp(f_answer, f_output)
        
        print(
            "Day: " + day +
            " Task: " + task +
            " Example: " + example +
            " ~~~> " + str(result)
            )


if __name__ == "__main__":
    start()
