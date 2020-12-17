# chess from scratch
#%%
import pandas as pd


# setting up the reference board with numbers and letters
board_letters = pd.DataFrame(columns=['A','B','C','D','E','F','G','H'])
board_numbers = pd.DataFrame(['1','2','3','4','5','6','7','8'])

numbers=['1','2','3','4','5','6','7','8']
letters=['A','B','C','D','E','F','G','H']
index_=[_ for _ in range(1,9)]
test=[]
board=pd.DataFrame()
cnt_let = 0
cnt_num = 0
tmp=[]
for letter in letters:
    for number in numbers:        
        pos = letter+number
        tmp.append(pos)
        cnt_num+=1
    board.insert(cnt_let,letter,tmp)
    tmp=[]   
    cnt_let+=1
board.index += 1


# setting up the pieces
pawns_w=['pawn_'+str(i) +'w' for i in range(1,9)]
pawns_b=['pawn_' +str(i)+'b' for i in range(1,9)]
others=['tower_1','knight_1','bishop_1','queen','king','bishop_2','tower_2','knight_2']
others_w=[i +'w' for i in others]
others_b=[i +'b' for i in others]

white_pieces=pawns_w+others_w
black_pieces=pawns_b+others_b




# setting up the gameboard
## first creating a copy so we can set up the pieces without changing the reference-board
game_board = board.copy()


game_board.loc[3]=None
game_board.loc[4]=None
game_board.loc[5]=None
game_board.loc[6]=None

## inserting pawns
game_board.loc[2]=pawns_w
game_board.loc[7]=pawns_b
## inserting other pieces
game_board.loc[1]=others_w
game_board.loc[8]=others_b


piece_positions=game_board.isin(white_pieces+black_pieces)



# a method for moving pieces based on type and destination
def move_piece_w(piece,location):
    piece_type = piece[:len(piece)-3]
    piece_position = decode_position(find_position(piece))  
    location_ = decode_position(location)  
    distance = calc_distance(piece,location)

    # create a dataframe where empty spaces is returned as True, in order to check wheter we can make this move.
    roadblocks=game_board.notnull()



    if piece_type == 'pawn' and distance[0]>0<=2 and distance[1]==0 and roadblocks.iloc[location_] == False:
        print("successful move")
        game_board.iloc[piece_position] = None
        game_board.iloc[location_] = piece
        
    elif piece_type == 'tower':
        if distance[0]>0 and distance[1]==0 and roadblocks.iloc[location_] ==False or distance[0]==0 and distance[1]>0 and roadblocks.iloc[location_] ==False:
            print('Tower move')
        else:
            print('illegal move!')
    else:
        print('illegal move!')




def roadblock(piece_position,location_):
    piece_position[0]







def decode_position(position):
    letters_value={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
    letter = position[:1]
    number = int(position[1:])-1
    letter_value=letters_value[letter]
    return number,letter_value
#def attack(piece,location):
        

def find_position(piece):
    try:
        pos=getIndexes(game_board,piece)
        letter=pos[1]
        number=pos[0]
        pos_=str(letter)+str(number)
        return pos_
    except:
        print('ERROR: use an actual piece name')
        pass


def getIndexes(dfObj, value):
    ''' Get index positions of value in dataframe i.e. dfObj.'''
    listOfPos = []
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj.isin([value])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos[0]



def calc_distance(piece,location):
    pos = decode_position(find_position(piece))
    loc = decode_position(location)
    cnt = 0
    # the relative distance in xy-coordinates
    distance =[]
    for item in pos:
        distance.append(loc[cnt]-pos[cnt])
        cnt+=1    
    
    return distance




# %%
