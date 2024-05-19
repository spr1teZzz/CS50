# Getting Started 
Download the distribution code from https://cdn.cs50.net/ai/2023/x/projects/0/tictactoe.zip and unzip it.
Once in the directory for the project, run pip3 install -r requirements.txt to install the required Python package (pygame) for this project.

# Understanding
这个项目中有两个主要文件:runner.py和tictactoe.py。tictactoe.py包含玩游戏的所有逻辑，以及做出最佳移动。runner.py已经为您实现了，它包含了运行游戏图形界面的所有代码。一旦您完成了tictactoe.py中所需的所有功能，您应该能够运行python runner.py来对抗您的AI!
让我们打开tictactoe.py来了解它提供了什么。首先，我们定义三个变量:X, O和EMPTY，来表示棋盘的可能移动。函数initial_state返回棋盘的起始状态。对于这个问题，我们选择将棋盘表示为由三个列表组成的列表(代表棋盘的三行)，其中每个内部列表包含三个值，分别是X、O或EMPTY。下面是我们留给您实现的函数!

# Specification
完成player, actions, result, winner, terminal, utility和minimax的实现。

player函数应该将棋盘状态作为输入，并返回玩家的回合(X或O)。
    在最初的游戏状态中，X先走一步。随后，player函数进行交替切换进行另外一次的移动。
    如果提供了终端棋盘作为输入(即游戏已经结束)则任何返回值都是可以接受的。

actions函数应该返回在给定的棋盘上可以采取的所有可能动作的集合。
    每个动作都应该表示为一个元组(i, j)，其中i对应移动的行(0、1或2)，j对应行中对应移动的单元格(也是0、1或2)。
    可能的移动是指棋盘上没有存在X或O的任何单元格。
    任何返回值是指可以接受如果提供了终端棋盘作为输入。

result函数以一个棋盘和一个动作作为输入，并且应该返回一个新的棋盘状态，并且不修改原来的棋盘。
    如果action不是棋盘的有效操作，您的程序应该引发异常（raise an exception）。
    返回的棋盘状态应该是由原始输入的棋盘所产生的，并让该轮到的玩家在输入动作所指示的单元格中移动。
    重要的是，原始的棋盘应该保持不变:因为Minimax最终需要在计算过程中考虑许多不同的棋盘状态。这意味着简单地更新棋盘中的单元本身并不是结果函数的正确实现。在做任何修改之前，你可能想要先对棋盘做一个深度拷贝（deep copy）。

winner函数应该接受一个棋盘作为输入，如果有赢家的话，返回这个棋盘的赢家。
    如果X玩家赢了游戏，你的函数应该返回X。如果O玩家赢了游戏，你的函数应该返回O。
    一个人可以在水平，垂直或对角线上连续移动三个动作来赢得游戏。
    你可以假设最多有一个赢家(也就是说，没有一个棋盘会同时有两个玩家，因为这是一个无效的棋盘状态)。
    如果游戏中没有赢家(因为游戏正在进行中，或者因为游戏以平局结束)，该函数应该返回None。

terminal函数应该接受一个棋盘作为输入，并返回一个布尔值，表示游戏是否结束。
    如果游戏结束，或者因为有人赢了游戏，或者因为所有单元格都被填满了并且没有人赢，这个函数应该返回True。
    否则，如果游戏仍在进行中，该函数应该返回False。

utility 函数应接受terminal棋盘作为输入，输出棋盘的效用。
    如果X赢了，效用是1。如果O赢了，效用是-1。如果游戏以平局结束，则效用为0。
    您可以假设，只有terminal(board)为True时，在棋盘上调用utility函数。

minimax函数应该将一个棋盘作为输入，并返回玩家在该棋盘上移动的最佳移动。 
    返回的移动应该是最优的动作(i, j)，这是棋盘上允许的动作之一。如果多个移动同样是最优的，那么这些移动中的任何一个都是可以接受的。 
    如果是棋盘是terminal棋盘，minimax函数应该返回None。

对于所有接受棋盘作为输入的函数，您可以假设它是一个有效的棋盘(也就是说，它是一个包含三行的列表，每一行有三个值X, O或EMPTY)。您不应该修改所提供的函数声明(每个函数的参数顺序或数量)。 
 
一旦所有功能都正确实现，您应该能够运行python runner.py并与AI进行对战。而且，因为一字棋是双方都在优化玩法的平局，所以你永远不可能打败AI(尽管如果你玩得不太好，它可能会打败你!)

# Hints
如果您想在不同的Python文件中测试您的函数，您可以使用以下行导入它们:
from tictactoe import initial_state。 
欢迎您向tictactoy.py中添加额外的辅助函数，前提是它们的名称不与模块中已有的函数或变量名称冲突。 
Alpha-beta修剪是可选的，但可能会使你的AI更有效地运行!

# Testing
如果您愿意，可以执行下面的命令(在系统上设置check50之后)来评估代码的正确性。这不是必须的;您可以简单地按照本规范末尾的步骤提交，这些测试将在我们的服务器上运行。无论哪种方式，一定要自己编译和测试它!
check50 ai50/projects/2024/x/tictactoe

# How to Submit
submit50 ai50/projects/2024/x/tictactoe