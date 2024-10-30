board=[["0","1","3"],
       ["4","5","6"],
       ["6","7","8"]]
def print_board():
  for row in board:
    print(row)
def check_mark(mark):
  for i in range(3):
    if(board[i][0]==mark and board[i][1]==mark and board[i][2]==mark):
      return True
  for i in range(3):
    if(board[0][i]==mark and board[1][i]==mark and board[2][i]==mark):
      return True
  if(board[0][0]==mark and board[1][1]==mark and board[2][2]==mark):
    return True
  if(board[0][2]==mark and board[1][1]==mark and board[2][0]==mark):
    return True
  return False

def play_tic():
  current_player="1"
  moves=0
  mark="X"
  while moves<9:
    print("Player "+ current_player+"'s move")
    cell=int(input("Enter the cell no. : "))
    row=cell//3
    col=cell%3
    if board[row][col]!="X" and board[row][col]!="O":
      board[row][col]=mark
      moves+=1
      print_board()
      result=check_mark(mark)
    else:
      print("This cell is already occupied. Try Again")
      continue
    if result==True:
      print("The winner is ",current_player)
      break
    if moves==9:
      print("Its a DRAW")
    if moves%2==0:
      current_player="1"
      mark="X"
    elif moves%2!=0:
      current_player="2"
      mark="O"

play_tic()
