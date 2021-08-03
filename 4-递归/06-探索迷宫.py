# -*- coding: utf-8 -*-

import turtle

# 迷宫标志
OBSTACLE = '+'  # 墙壁
DEAD_END = '-'  # 死胡同
TRIED = '.'  # 走过的格子
PART_OF_PATH = '*'  # 离开迷宫的路线
START_POS = 'S'  # 起始位置

# 迷宫数据文件
MAZE_FILE = 'maze_data.txt'

# 移动方向
MOVE_DIRECT = (
    (0, -1),  # 上
    (-1, 0),  # 左
    (0, 1),  # 下
    (1, 0),  # 右
)


class Maze:
    """迷宫"""

    def __init__(self, maze_file, screen):
        maze_list = []
        row = 0
        with open(maze_file) as f:
            for line in f:
                if line := line.strip('\n'):
                    tmp = []
                    for col in range(len(line)):
                        if (ch := line[col]) == START_POS:
                            start_row, start_col = row, col
                        tmp.append(ch)
                    maze_list.append(tmp)
                    row += 1
        self.maze_list = maze_list  # 迷宫矩阵
        self.max_row, self.max_col = len(maze_list), len(maze_list[0])  # 矩阵行数、列数
        self.start_row, self.start_col = start_row, start_col  # 小乌龟起始行列
        self.turtle = turtle.Pen()  # 小乌龟
        self.screen = screen  # 画布窗口
        self.setup()

    def setup(self):
        self.turtle.speed(0)
        self.screen.setup(width=600, height=600)
        self.screen.setworldcoordinates(
            -(self.max_col - 1) / 2 - 0.5,
            -(self.max_row - 1) / 2 - 0.5,
            (self.max_col - 1) / 2 + 0.5,
            (self.max_row - 1) / 2 + 0.5,
        )

    def translate_x(self, x):
        """转换x坐标"""
        return x - self.max_col / 2

    def translate_y(self, y):
        """转换y坐标"""
        return -y + self.max_row / 2

    def draw_center_rect(self, x, y, color):
        """根据矩形中心点位置绘制矩形"""
        left_bottom = self.translate_x(x) - 0.5, self.translate_y(y) - 0.5
        self.turtle.up()
        self.turtle.goto(left_bottom)
        self.turtle.down()
        self.turtle.setheading(90)
        self.turtle.color('black', color)
        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(1)
            self.turtle.right(90)
        self.turtle.end_fill()

    def draw_maze(self):
        """绘制迷宫"""
        self.screen.tracer(0)
        for y in range(self.max_row):
            for x in range(self.max_col):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_center_rect(x, y, 'tan')
        self.turtle.up()
        self.move_turtle(self.start_col, self.start_row)
        self.turtle.shape('turtle')
        self.turtle.color('black', 'blue')
        self.turtle.setheading(90)
        self.turtle.down()
        self.screen.tracer(1)

    def drop_breadcrumb(self, color):
        """撒面包屑"""
        self.turtle.dot(color)

    def move_turtle(self, x, y, trace=False):
        """移动小乌龟"""
        x, y = self.translate_x(x), self.translate_y(y)
        if not trace:
            self.turtle.up()
        self.turtle.setheading(self.turtle.towards(x, y))
        self.turtle.goto(x, y)
        self.turtle.down()

    def update_position(self, x, y, val=None):
        """更新位置"""
        if val is not None:
            self.maze_list[y][x] = val

        if val == PART_OF_PATH:
            self.move_turtle(x, y, trace=True)
        else:
            self.move_turtle(x, y)

        if val == DEAD_END:
            color = 'red'
        elif val == PART_OF_PATH:
            color = 'green'
        elif val == TRIED:
            color = 'black'
        else:
            color = None

        if color:
            self.drop_breadcrumb(color)

    def is_exit(self, x, y):
        """判断小乌龟是否走出迷宫"""
        return x in {0, self.max_col - 1} or y in {0, self.max_row - 1}

    def __getitem__(self, idx):
        return self.maze_list[idx]


def search_maze(maze, x=None, y=None):
    if x is None:
        x = maze.start_col
    if y is None:
        y = maze.start_row

    # 遇到墙或者死胡同
    if maze[y][x] in {OBSTACLE, DEAD_END}:
        return False
    # 遇到走过的格子
    if maze[y][x] == TRIED:
        return False
    # 找到了出口
    if maze.is_exit(x, y):
        maze.update_position(x, y)
        return True
    # 标记当前格子已经走过
    maze.update_position(x, y, TRIED)

    # 尝试向四个方向移动， 寻找任意一条能走出迷宫的路线
    found = any(
        search_maze(maze, x + dx, y + dy) for (dx, dy) in MOVE_DIRECT
    )

    if not found:
        maze.update_position(x, y, DEAD_END)
    else:
        # 乌龟从终点回到起点并标记完整的路线
        maze.update_position(x, y, PART_OF_PATH)
    return found


if __name__ == '__main__':
    screen = turtle.Screen()
    maze = Maze(MAZE_FILE, screen)
    maze.draw_maze()
    search_maze(maze)
    screen.exitonclick()
